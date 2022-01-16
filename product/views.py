from multiprocessing import context
from unicodedata import category
from django.shortcuts import render

from product.models import Category, Products

# Create your views here.
def searchResult(request):
    allproducts = Products.objects.all()
    current_user = request.user

    item_name = request.GET.get('item_name')
    if item_name!= "" and item_name is not None:
        allproducts = allproducts.filter(search_tags__icontains=item_name)

    context={
        'allproducts':allproducts,
        'item_name':item_name,
        'current_user':current_user
    }
    return render(request,'searchResult.html',context)

def display(request):
    
    category = request.GET.get('category')

    category_name = Category.objects.get(id=category)

    filteredProd = Products.objects.all()

    if category != None:
        filteredProd = Products.objects.filter(category = category)


    context = {
        'filteredProd':filteredProd,
        'category_name': category_name,
    }     
    return render (request, 'display.html',context)

def detail(request,item_id):
    allProducts = Products.objects.get(pk=item_id)

    similar = Products.objects.filter(category = allProducts.category)
    
    print(similar)
    context={
        'allProducts':allProducts,
        'similar':similar
    }
    return render(request,'productDetail.html',context)