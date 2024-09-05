from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review, Comments
from .forms import ProductForm, ReviewForm, CommentForm

import random

# Create your views here.


def all_products(request):
    """ A view to show all the products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product details """

    product = get_object_or_404(Product, pk=product_id)
    # To get all reviews for the specific product.
    reviews = Review.objects.filter(product=product)

    # Get 4 random products from the same category as product.id
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    random_related_products = random.sample(list(related_products), min(len(related_products), 4))

    review_form = ReviewForm()
    comment_form = CommentForm()

    context = {
        'product': product,
        'reviews': reviews,
        'random_related_products': random_related_products,
        'review_form': review_form,
        'comment_form': comment_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def review(request, product_id):
    """ A view to leave a review. """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            product.update_rating()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add review, please check your form is valid.')
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html, context')


@login_required
def delete_review(request, review_id):
    """ Delete a review if user is review.reviewer. """
    review = get_object_or_404(Review, id=review_id, reviewer=request.user)
    product = review.product

    if request.method == 'POST':
        review.delete()
        product.update_rating()
        messages.success(request, 'You have successfully delete your review.')
        return redirect(reverse('product_detail', args=[product.id]))

    context = {
        'review': review,
    }

    return render(request, 'products/delete_review.html', context)


@login_required
def edit_review(request, review_id):
    """ Edit a review if user is review.reviewer. """
    review = get_object_or_404(Review, id=review_id, reviewer=request.user)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
             request,
             'Your review has been updated successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ReviewForm(instance=review)

    context = {
        'review': review,
        'product': product,
        'form': form,
    }

    return render(request, 'products/edit_review.html', context)


@login_required
def add_comment(request, review_id):
    """ A view to allow users to add a comment to a review. """
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.commenter = request.user
            comment.save()

            # Send email to the reviewer
            subject = render_to_string(
                'products/comment_emails/comment_email_subject.txt',
                {'review': review})
            body = render_to_string(
                'products/comment_emails/comment_email_body.txt',
                {'review': review})
            customer_email = review.reviewer.email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [customer_email])

            messages.success(request, 'Comment added successfully!')
            return redirect(
                reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(
                request,
                'Failed to add comment. Please ensure the form is valid.')
    else:
        comment_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'review': review,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment if user is comment.commenter. """
    comment = get_object_or_404(
        Comments,
        id=comment_id,
        commenter=request.user)
    review = comment.review
    product = review.product

    if request.method == 'POST':
        comment.delete()
        messages.success(
            request,
            'You have successfully deleted your comment.')
        return redirect(reverse('product_detail', args=[product.id]))

    context = {
        'comment': comment,
    }

    return render(request, 'products/delete_comment.html', context)


@login_required
def edit_comment(request, comment_id):
    """ Edit comment if user is comment.commenter. """
    comment = get_object_or_404(
        Comments,
        id=comment_id,
        commenter=request.user)
    review = comment.review
    product = review.product

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your comment has been updated successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = CommentForm(instance=comment)

    context = {
        'comment': comment,
        'review': review,
        'product': product,
        'form': form,
    }

    return render(request, 'products/edit_comment.html', context)


@login_required
def add_product(request):
    """ Add a product to the store. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but only the store owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product to store!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add produc, please check the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product already existing on the store. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but only the store owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                f'Attempt to edit {product.name} has failed, please ensure the form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are about to edit {product.name}.')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product already existing on the store. """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, but only the store owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Successfully deleted {product.name}!')
    return redirect(reverse('products'))
