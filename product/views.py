from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from cart.models import Order

from product.models import Category, Products

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

def display(request):
    
    category = request.GET.get('category')
    current_user = request.user
    category_name = Category.objects.get(id=category)
    allcategory = Category.objects.all()
   
    filteredProd = Products.objects.all()

    if category != None:
        filteredProd = Products.objects.filter(category = category)

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

def detail(request,item_id):
    allProducts = Products.objects.get(pk=item_id)
    allcategory = Category.objects.all()
    current_user = request.user

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
    }
    return render(request,'productDetail.html',context)