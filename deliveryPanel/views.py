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
def deliverypanelLogin(request):

    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            print(user)
            users_in_group = Group.objects.get(name="DeliveryGuy").user_set.all()

            if user in users_in_group:

                if username and password !="":
                    if user is not None:
                        auth_login(request,user)
                        return redirect('dashboard')
                    else:
                        messages.info(request, "*Username or password is incorrect")
                else:
                    messages.info(request, "*Enter username and password")
            else:
                return redirect('deliverypanelLogin')
    return render(request,'deliveryLogin.html')

@login_required(login_url='deliverypanelLogin')
def deliverypanel(request):

    getOrders = MyOrder.objects.all()

    context={
        'getOrders':getOrders,
    }

    return render(request,'deliverypanel.html',context)

def logoutDelivery(request):
    logout(request)
    return redirect('deliverypanelLogin')