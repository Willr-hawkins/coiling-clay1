from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that render the cart page content. """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ A view to add a qauntity of the specified product to the shopping cart. """

    qauntity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += qauntity
    else:
        cart[item_id] = qauntity
    
    request.session['cart'] = cart
    return redirect(redirect_url)