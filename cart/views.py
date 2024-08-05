from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that render the cart page content. """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ A view to add a qauntity of the specified product to the shopping cart. """

    product = get_object_or_404(Product, pk=item_id)
    qauntity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += qauntity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}.')
    else:
        cart[item_id] = qauntity
        messages.success(request, f'Added {product.name} to your cart.')
    
    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """ A view to allow the cart items to be adjusted. """

    product = get_object_or_404(Product, pk=item_id)
    qauntity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if qauntity > 0:
        cart[item_id] = qauntity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}.')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart.')

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def remove_from_cart(request, item_id):
    """ A view to allow the cart items to be removed. """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag.')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"We're sorry an error occured when removing item {e} from your cart.")
        return HttpResponse(status=500)
