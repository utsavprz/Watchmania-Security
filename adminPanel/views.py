from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, Group
from django.contrib import messages

from myorder.models import MyOrder

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
                return redirect('Admin/adminpanelLogin')
    return render(request,'adminLogin.html')

@login_required(login_url='adminpanelLogin')
def adminpanel(request):

    getOrders = MyOrder.objects.all()

    context={
        'getOrders':getOrders,
    }

    return render(request,'Admin/adminpanel.html',context)

def logoutAdmin(request):
    logout(request)
    return redirect('adminpanelLogin')