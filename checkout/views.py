from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django import template

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.info(request, "You have nothing in your cart.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHAuEG3qcBkdHCUH1uSZ4xDCvoKtxOCGw3wAN0TNn8HNAoJk3FfPWuiUfLiRoEOZniVxkIwDLmlLhVyDLcHkJPH00C1BNhlEI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
