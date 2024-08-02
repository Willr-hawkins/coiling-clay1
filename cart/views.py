from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that render the cart page content. """

    return render(request, 'cart/cart.html')