from django.urls import reverse
from itertools import product
import json
from multiprocessing import context
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from cart.models import Order

from product.models import Category, Products, Review
from django.contrib.auth.decorators import login_required

# Create your views here.
def searchResult(request):
    allproducts = Products.objects.all()
    current_user = request.user
    allcategory = Category.objects.all()


    item_name = request.GET.get('item_name')
    if item_name!= "" and item_name is not None:
        allproducts = allproducts.filter(search_tags__icontains=item_name)
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    context={
        'allproducts':allproducts,
        'item_name':item_name,
        'current_user':current_user,
        'allcategory':allcategory,
        'order':order,

    }
    return render(request,'searchResult.html',context)

def categoryDisplay(request,cat_id):
    current_user = request.user
    category_name = Category.objects.get(id=cat_id)

    allcategory = Category.objects.all()
   
    filteredProd = Products.objects.all()

    if category != None:
        filteredProd = Products.objects.filter(category = cat_id)


    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    context = {
        'filteredProd':filteredProd,
        'category_name': category_name,
        'allcategory':allcategory,
        'order':order,
    }  

    return render (request, 'display.html',context)

def display(request):
    current_user = request.user

    allcategory = Category.objects.all()
   
    filteredProd = Products.objects.all()

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    context = {
        'filteredProd':filteredProd,
        'allcategory':allcategory,
        'order':order,
    }     
    return render (request, 'display.html',context)

def detail(request,item_id):
    allProducts = get_object_or_404(Products, pk=item_id)
    allcategory = Category.objects.all()
    current_user = request.user

    productDet = get_object_or_404(Products,id=item_id)
    total_fav= productDet.total_favorite()

    favorite_status=False
    if productDet.favorite.filter(id=request.user.id).exists():
        favorite_status=True




    similar = Products.objects.filter(category = allProducts.category)

    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }
    context={
        'allProducts':allProducts,
        'similar':similar,
        'allcategory':allcategory,
        'order':order,
        'total_fav':total_fav,
        'favorite_status':favorite_status,
    }
    return render(request,'productDetail.html',context)



def favoritethis(request,p_id):
    product = get_object_or_404(Products, id=request.POST.get('allProducts.id'))
    if product.favorite.filter(id=request.user.id).exists():
        product.favorite.remove(request.user)

    else:
        product.favorite.add(request.user)

    return HttpResponseRedirect(reverse('wishlist'))

def wishlistView(request):
    current_user = request.user

    allcategory = Category.objects.all()
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
    else:
        order = {
            'get_cart_total':0,
            'get_cart_items':0
        }

    wishList = Products.objects.filter(favorite = current_user)
    countWishlist = Products.objects.filter(favorite = current_user).count()
    context={
        'order':order,
        'allcategory':allcategory,
        'wishList':wishList,
        'countWishlist':countWishlist
    }
    return render(request,'wishlist.html',context)





@login_required
def add_review(request, item_id):
    current_user = request.user
    product = get_object_or_404(Products, pk=item_id)
    
    # Check if the user has placed an order for the given product
    order = Order.objects.filter(user_info=current_user, complete=True, orderitem__product=product).first()
    
    if order is None:
        # If the user hasn't purchased the product, redirect to a page with an error message
        return render(request, 'review_error.html')

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        # Create a new review object
        review = Review.objects.create(product=product, user=current_user, rating=rating, comment=comment)
        review.save()

        # Redirect to the product detail page
        return HttpResponseRedirect(reverse('detail', args=(item_id,)))

    return render(request, 'add_review.html')
