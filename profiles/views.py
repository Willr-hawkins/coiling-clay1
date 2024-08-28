from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Wishlist
from .forms import UserProfileForm, CreateWishlistForm

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