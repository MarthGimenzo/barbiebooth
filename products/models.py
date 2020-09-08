from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


AVAILABILITY = (
    ('sold', 'Sold'),
    # ('option', 'optie'),
    ('available', 'Available'),
)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, 
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    views = models.IntegerField(default=0)
    year = models.CharField(max_length=5, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    availabilty = models.CharField(max_length=50, default='available', choices=AVAILABILITY)

    # created_date = models.DateTimeField(auto_now_add=True)
    # edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# class ProductImage(models.Model):
#     product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
#     image_url = models.URLField(max_length=1024, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     edited_date = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.image


class Comment(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
