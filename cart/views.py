from django.shortcuts import render, redirect, reverse, HttpResponse

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

def adjust_cart(request, item_id):
    """ A view to allow the cart items to be adjusted. """

    qauntity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if qauntity > 0:
        cart[item_id] = qauntity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))

def remove_from_cart(request, item_id):
    """ A view to allow the cart items to be removed. """

    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
