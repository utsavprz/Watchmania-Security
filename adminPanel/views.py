from importlib.resources import contents
from itertools import product
from tkinter.tix import Tree
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, Group
from django.contrib import messages
from product.forms import productForm

from product.models import Brand, Category, Products

# Create your views here.
def adminpanelLogin(request):

    if request.user.is_authenticated:
        return redirect('admindashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            print(user)

            if user.is_superuser:

                if username and password !="":
                    if user is not None:
                        auth_login(request,user)
                        return redirect('admindashboard')
                    else:
                        messages.info(request, "*Username or password is incorrect")
                else:
                    messages.info(request, "*Enter username and password")
            else:
                return redirect('adminpanelLogin')
    return render(request,'Admin/adminLogin.html')


@login_required(login_url='adminpanelLogin')
def adminHome(request):

    return render(request,'Admin/adminHome.html')

@login_required(login_url='adminpanelLogin')
def adminProducts(request):

    allProducts = Products.objects.all()

    context={
        'allProducts':allProducts,
    }

    return render(request,'Admin/adminProducts.html',context)

def logoutAdmin(request):
    logout(request)
    return redirect('adminpanelLogin')



def productEdit(request,prodId):
    prodDetail = Products.objects.get(id=prodId)

    categories = Category.objects.all()
    brands = Brand.objects.all()


    if request.method == 'GET':
        form = productForm(request.GET, request.FILES, instance=prodDetail)

        if form.is_valid():
            form.save()
            print('form save')
            return redirect('adminproducts')
    else:
        form = productForm(instance=prodDetail)

    context={
        'prodDetail':prodDetail,
        'categories':categories,
        'brands':brands,
        'form':form,
    }

    return render(request,'Admin/prodEdit.html',context)
