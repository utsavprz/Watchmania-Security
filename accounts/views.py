from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CreateUserForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            print(request.POST)
            print("Got data")
            form = CreateUserForm(request.POST)
            if form.is_valid():
                print("form valid")
                form.save()
                print("form saved")
                return redirect('login')
            else:
                messages.error(request, "Error")

    context ={
        'form':form
    }
    return render(request, 'register.html',context)

def login(request): 
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    auth_login(request,user)
                    return redirect('index')
                else:
                    messages.info(request, "*Username or password is incorrect")
            else:
                messages.info(request, "*Enter username and password")

    return render(request, 'login.html')