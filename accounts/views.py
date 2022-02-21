from platform import python_version_tuple
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.models import User_Address
from accounts.models import user_details as userDetailModel
from cart.models import Order

from .forms import CreateUserForm
from .forms import user_details


from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout

# Create your views here.

def register(request):
    current_user = request.user
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
            'form':form,
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

def logoutUser(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    current_user = request.user

    if request.user.is_authenticated:
        profileData = userDetailModel.objects.filter(user_info = current_user.id)

        if(len(profileData) <1):
            profileData = False
        else:
            profileData = userDetailModel.objects.filter(user_info = current_user.id)
        addressExists = False
        if (User_Address.objects.filter(user_info = current_user.id).exists()):
            addressData = User_Address.objects.filter(user_info = current_user.id)[0]
            addressExists=True
        else:
            addressData = []
            addressExists=False
        

        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(user_info = current_user, complete=False)
        else:
            order = {
            'get_cart_total':0,
            'get_cart_items':0
            }   

    context={
        'profileData': profileData,
        'current_user': current_user,
        'addressExists':addressExists,
        'addressData':addressData,
        'order':order,

    }
    return render(request,'profile.html',context)

def profile_update(request):
    current_user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            profileData = userDetailModel.objects.filter(user_info = current_user.id)

            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            dob = request.POST.get('dob')


            for i in profileData:
                if dob =="":
                    dob=i.dob
            
            
            if (userDetailModel.objects.filter(user_info = current_user.id).exists()):
                User.objects.filter(id = current_user.id).update(first_name = first_name, last_name=last_name, email=email)
                userDetailModel.objects.filter(user_info = current_user.id).update(dob=dob, phone=phone)
            else:
                User.objects.filter(id = current_user.id).update(first_name = first_name, last_name=last_name, email=email)
                saveData = userDetailModel(user_info = current_user, dob=dob, phone=phone)
                saveData.save()
        

            return redirect('profile')

def addAddress(request):
    current_user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            city = request.POST.get('city')
            address = request.POST.get('address')
            street = request.POST.get('street')
            postalcode = request.POST.get('postalcode')
            description = request.POST.get('description')

            saveData= User_Address(user_info=current_user, city=city,address=address,street=street,postalcode=postalcode,description=description)
            saveData.save()

            if (User_Address.objects.filter(user_info = current_user.id).exists()):
                getUsrAddress = User_Address.objects.filter(user_info = current_user.id)[0]

                if (userDetailModel.objects.filter(user_info = current_user.id).exists()):
                    userDetailModel.objects.filter(user_info = current_user.id).update(default_User_Address=getUsrAddress.id)

            return redirect('profile')

def updateAddress(request):
    current_user = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            city = request.POST.get('city')
            address = request.POST.get('address')
            street = request.POST.get('street')
            postalcode = request.POST.get('postalcode')
            description = request.POST.get('description')


            if (User_Address.objects.filter(user_info = current_user.id).update(city=city,address=address,street=street,postalcode=postalcode,description=description)):
                getUsrAddress = User_Address.objects.filter(user_info = current_user.id)[0]
                if (userDetailModel.objects.filter(user_info = current_user.id).exists()):
                    userDetailModel.objects.filter(user_info = current_user.id).update(default_User_Address=getUsrAddress.id)

            return redirect('profile')
