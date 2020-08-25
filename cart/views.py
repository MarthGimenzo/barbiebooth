from django.shortcuts import render, redirect

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
    print(request.session['cart'])
    return redirect(redirect_url)