from random import random
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from cart.models import Order
from product.models import Category, Products, featuredProduct

# Create your views here.


def index(request):
    current_user = request.user
    featuredProducts = featuredProduct.objects.all()

    allcategory = Category.objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    context={
        'current_user':current_user,
        'featuredProducts':featuredProducts,
        'allcategory':allcategory,
        'order':order,
    }
    return render(request,'home.html',context)