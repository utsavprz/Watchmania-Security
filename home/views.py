from random import random
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from product.models import Category, Products, featuredProduct

# Create your views here.


def index(request):
    current_user = request.user
    featuredProducts = featuredProduct.objects.all()

    allcategory = Category.objects.all()
    context={
        'current_user':current_user,
        'featuredProducts':featuredProducts,
        'allcategory':allcategory,
    }
    return render(request,'home.html',context)