from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect ('home:index')
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
    return render(request, 'login.html')