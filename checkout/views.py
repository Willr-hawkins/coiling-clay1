from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There appears to be nothing in your cart.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PkpAbKpfpWYCRbRn9Vai5CZsKujaJfv5ZZa9FYHqYxYvphQzfotmTCS3Bd5yqMZzv98a1fbruDxllHnRX00Uok400I0rd0TyL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)