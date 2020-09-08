from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Comment
from .forms import CommentForm

# Create your views here.


def all_products(request):
    """A view to show all Dolls and Accessories,
    including the sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    available = True

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(request, "Please enter some search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view for the details of the product"""
    product = get_object_or_404(Product, pk=product_id)

    form = CommentForm()
    if request.POST:
        comment = Comment()
        comment.product = product
        comment.name = request.POST['name']     # user.friendlyname
        comment.description = request.POST['description']
        comment.save()
        messages.info(request, 'Your comment has been posted.')
        return redirect(reverse('product_detail',
                                args=[product.pk]))

    else:
        product.views += 1
        product.save()


    if product:
        comments = Comment.objects.filter(product=product).order_by('created_date')
    else:
        comments = None

    context = {
        'product': product,
        'comments': comments,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)







# "urls.py" definieer je je waar de gebruiker heen kan
# daarvoor moet in je "views.py" een functie bestaan
# in je models.py definieer je je model welke je in de admin.py 'aanzet', zodat je deze kan bewerken




# Object Orientated Programming
# MVC - Model View Control



# Model zijn je modellen (product, comment)
# View is je views.py waarin je de betreffende data ophaalt
# Control zijn je templates waarin je met je modellen kan interacteren (plaats nieuw comment)




# def tel_1_erbij_op(getal):
#     return getal + 1

# nieuw_getal = tel_1_erbij_op(3)
# >> 4


# class Getal:
#     int getal = X

#     def plus1():
#         return getal + 1
    
#     def min1():
#         return getal -1


# henk = Getal(3)
# henk.plus1()
# henk.plus1()
# henk.plus1()
# henk.min1()
