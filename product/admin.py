from django.contrib import admin
from product.models import Category,Products,Brand,featuredProduct
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(featuredProduct)