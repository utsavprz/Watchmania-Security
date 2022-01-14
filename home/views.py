from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from product.models import Products

# Create your views here.


def index(request):
    current_user = request.user
    allproducts = Products.objects.all()

    # item_name = request.GET.get('item_name')
    # if item_name!= "" and item_name is not None:
    #     allproducts = allproducts.filter(name__icontains=item_name)
    context={
        'current_user':current_user,
        'allproducts':allproducts,
    }
    return render(request,'home.html',context)