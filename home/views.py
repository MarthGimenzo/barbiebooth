from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')


def about(request):
    """A view to return the about page"""

    return render(request, 'home/about.html')


def contact(request):
    """A view to return the contact page"""

    return render(request, 'home/contact.html')


def faqs(request):
    """A view to return the faqs page"""

    return render(request, 'home/faqs.html')


def privacy_policy(request):
    """A view to return the privacy policy page"""

    return render(request, 'home/privacy_policy.html')


def terms_conditions(request):
    """A view to return the terms&conditions page"""

    return render(request, 'home/terms_conditions.html')
