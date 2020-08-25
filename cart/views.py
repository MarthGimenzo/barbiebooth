from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents"""

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """Add a a product to the cart"""

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in list(cart.keys()):
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the cart"""
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart

        return HttpResponse(status=200)

    except Exception as e:
        print('Got here')
        return HttpResponse(status=500)