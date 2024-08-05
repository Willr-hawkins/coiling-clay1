from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        shipping = Decimal(settings.STANDARD_SHIPPING_PRICE)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        shipping = 0
        free_shipping_delta = 0
    
    grand_total = shipping + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'shipping': shipping,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
    }

    # Adds grand_total to the context only when there are items in the cart,
    # so that the cart displays as £0.00 when empty. 
    if cart_items:
        context['grand_total'] = grand_total

    return context