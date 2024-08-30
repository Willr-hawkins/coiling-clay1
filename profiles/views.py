from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist, WishlistItem
from .forms import UserProfileForm, CreateWishlistForm

from products.models import Product

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Attempt to update profile failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f'This is a past confirmation for order number {order_number}.'
                            'A confirmation email was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

@login_required
def user_wishlists(request):
    """ 
    Display a list of wishlists created if,
    wishlist.user is the logged in user.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    wishlists = Wishlist.objects.filter(user=user_profile)
    wishlist_form = CreateWishlistForm()

    template = 'profiles/wishlists.html'
    context = {
        'wishlists': wishlists,
        'wishlist_form': wishlist_form,
    }

    return render(request, template, context)

@login_required
def create_wishlist(request):
    """ Display a form to create a wishlist. """

    if request.method == 'POST':
        wishlist_form = CreateWishlistForm(request.POST)
        if wishlist_form.is_valid():
            wishlist = wishlist_form.save(commit=False)
            wishlist.user = request.user.userprofile
            wishlist.save()
            messages.success(request, 'Successfully created wishlist!')
            return redirect(reverse('wishlists'))
    else:
        form = CreateWishlistForm()

    template = 'profiles/wishlists.html'
    context = {
        'wishlist_form': wishlist_form,
    }

    return render(request, template, context)

@login_required
def delete_wishlist(request, wishlist_id):
    """ 
    Allow user to delete a wishlist if user
    is wishlist.user
    """
    user_profile = request.user.userprofile
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id, user=user_profile)

    if request.method == 'POST':
        wishlist.delete()
        messages.success(request, f'You have successfully deleted your {wishlist.wishlist_name} wishlist.')
        return redirect(reverse('wishlists'))

    template = 'profiles/delete_wishlist.html'
    context = {
        'user_profile': user_profile,
        'wishlist': wishlist,
    }

    return render(request, template, context)

@login_required
def wishlist_details(request, wishlist_id):
    """ 
    Display a list of products that have been added to
    a users wishlist. 
    """
    user_profile = request.user.userprofile
    wishlist = get_object_or_404(Wishlist, id=wishlist_id, user=user_profile)
    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)

    template = 'profiles/wishlist_details.html'
    context = {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
        'user_profile': user_profile,
    }

    return render(request, template, context)

@login_required
def add_to_wishlist(request, product_id, wishlist_id):
    """ Add a product to a specific wishlist. """
    user_profile = request.user.userprofile
    product = get_object_or_404(Product, pk=product_id)
    wishlist_id = request.POST.get('wishlist_id')
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id, user=user_profile)

    wishlist_item, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)

    if created:
        messages.success(request, f'{product.name} was successfully added to {wishlist.wishlist_name}!')
    else:
        messages.info(request, f'{product.name} is already saved to {wishlist.wishlist_name}!')

    return redirect('product_detail', product_id=product.id)

@login_required
def remove_from_wishlist(request, product_id, wishlist_id):
    """ Remove a product from a specific wishlist. """
    user_profile = request.user.userprofile
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id, user=user_profile)
    product = get_object_or_404(Product, pk=product_id)

    wishlist_item = get_object_or_404(WishlistItem, wishlist=wishlist, product=product)
    wishlist_item.delete()

    messages.success(request, f'{product.name} was successfully removed from your {wishlist.wishlist_name} wishlist!')

    return redirect('wishlist_details', wishlist_id=wishlist_id)