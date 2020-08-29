"""Opzet models.py """"

from django.db import models

class Product(models.Model):
    slug = models.CharField(max_length=500, blank=False, null=False)
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.slug


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    comment = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=500, blank=False, null=False)
    user_mail = models.CharField(max_length=500, blank=False, null=False)
    user_ip = models.CharField(max_length=15, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product

STATUS = (
    ('not_paid', 'not paid'),
    ('paid', 'paid'),
)

class Order(models.Model):
    status = models.CharField(max_length=20, default='not_paid', choices=STATUS)
    user_name = models.CharField(max_length=500, blank=False, null=False)
    user_mail = models.CharField(max_length=500, blank=False, null=False)
    user_address = models.CharField(max_length=500, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    price = models.IntegerField(default=0)                               # prijzen altijd in centen doen
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id


""" In admin.py het volgende:"""

from .models import Product, Comment

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = (
        'slug',
        'title',
        'launch_year',
        'price',
        'created_date',
        'edited_date',
    )
    list_filter = (
        'published',
    )
    search_fields = (
        'title',
        'description',
    )
    ordering = ('-edited_date',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = (
        'product',
        'comment',
        'user_name',
        'user_mail',
        'created_date',
        'edited_date',
    )
    search_fields = (
        'comment',
    )
    ordering = ('-created_date',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)






from django.db import models

class Product(models.Model):
    slug = models.CharField(max_length=500, blank=False, null=False)
    title = models.CharField(max_length=500, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(max_length=500, null=True, blank=True)
    price = models.IntegerField(default=0)
    launch_year = models.CharField(max_length=4, blank=False, null=False)       # jaar waarop de barbie was gelanceerd
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.slug

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    comment = models.TextField(blank=True, null=True)
    user_name = models.CharField(max_length=500, blank=False, null=False)
    user_mail = models.CharField(max_length=500, blank=False, null=False)
    user_ip = models.CharField(max_length=15, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product

STATUS = (
    ('not_paid', 'not paid'),
    ('paid', 'paid'),
)

class Order(models.Model):
    status = models.CharField(max_length=20, default='not_paid', choices=STATUS)
    user_name = models.CharField(max_length=500, blank=False, null=False)
    user_mail = models.CharField(max_length=500, blank=False, null=False)
    user_address = models.CharField(max_length=500, blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    price = models.IntegerField(default=0)                               # prijzen altijd in centen doen
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.id

Han
verzonden
4 uur geleden
iets aangepaste versie
Han
verzonden
4 uur geleden
vergeet niet je app te registeren, en je makemigrations en migrate te draaien
Han
verzonden
4 uur geleden
sorry, ik wilde je nog wel even helpen, maar ik was vandaag druk... eventueel kunnen we morgen (zaterdag) nog wel even bellen
