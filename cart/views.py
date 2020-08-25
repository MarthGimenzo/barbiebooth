from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents"""

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a a product to the cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in list(cart.keys()):
        messages.success(request, f'You put {product.name} into your cart!')
        cart[item_id] = quantity

    else:
        messages.warning(request, f'You already have {product.name} in your cart!')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        messages.warning(request, f'You removed {product.name} from your cart!')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Removing {product.name} from your cart didn't work!")
        return HttpResponse(status=500)