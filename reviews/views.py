from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ReviewForm
from .models import Review

def submit_review(request):
    """ A view to render successful reviews. """

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review, please check your form is valid.')
    else:
        form = ReviewForm()

    template = 'products/product_detail'
    context = {
        'form': form,
    }

    return render(request, template, context)
