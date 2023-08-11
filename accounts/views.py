from datetime import timezone
from platform import python_version_tuple
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.models import LoginAttempts, User_Address
from accounts.models import user_details as userDetailModel
from cart.models import Order

from .forms import CreateUserForm, LoginForm

from django.utils import timezone 


from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout


from captcha.fields import CaptchaField

import logging

audit_logger = logging.getLogger('audit_logger')
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
    max_attempts = 3
    show_captcha = False

    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Check if the username and password are provided
        if not form.has_error('username') and not form.has_error('password'):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            # If the user is valid, log them in
            if user is not None:
                try:
                    login_attempt = LoginAttempts.objects.get(user__username=username)      
                    if login_attempt.attempts >= max_attempts:
                        messages.error(request, f'Your account is locked due to too many false login attempts. Enter the CAPTCHA to unlock.')
                        audit_logger.info(f'{timezone.now()} - LoginAttempt - {username} - Failed')
                        show_captcha = True

                        systemCaptcha = request.POST.get('captcha_0')
                        print(f'systemCaptcha:{systemCaptcha}')
                        print(form.fields)
                        userEnteredCaptcha = form.cleaned_data.get('captcha')
                        print(f'userEnteredCaptcha:{userEnteredCaptcha}')

                        if systemCaptcha != None and userEnteredCaptcha != None:
                            if(systemCaptcha == userEnteredCaptcha[0]):
                                auth_login(request, user)
                                # Reset login attempts and last_attempt_time upon successful login
                                LoginAttempts.objects.filter(user=user).delete()
                                audit_logger.info(f'{timezone.now()} - LoginAttempt - {username} - Success')
                                return redirect('index') 
                    else:
                        if not form.has_error('username') and not form.has_error('password'):
                            auth_login(request, user)
                            # Reset login attempts and last_attempt_time upon successful login
                            LoginAttempts.objects.filter(user=user).delete()
                            audit_logger.info(f'{timezone.now()} - LoginAttempt - {username} - Success')
                            return redirect('index')
                except LoginAttempts.DoesNotExist:
                     
                     if not form.has_error('username') and not form.has_error('password'):
                            auth_login(request, user)
                            # Reset login attempts and last_attempt_time upon successful login
                            LoginAttempts.objects.filter(user=user).delete()
                            audit_logger.info(f'{timezone.now()} - LoginAttempt - {username} - Success')
                            return redirect('index')
            else:
                try:
                    login_attempt = LoginAttempts.objects.get(user__username=username)
                    if login_attempt.attempts < max_attempts:
                        login_attempt.attempts += 1
                        login_attempt.last_attempt_time = timezone.now()
                        login_attempt.save()
                        if max_attempts - login_attempt.attempts != 0:
                            messages.error(request, f'Your credentials are incorrect, you have {max_attempts - login_attempt.attempts} attempts left.')
                            audit_logger.info(f'{timezone.now()} - LoginAttempt - {username}, Failed attempt {login_attempt.attempts}')
                        else:
                            messages.error(request, f'Your credentials are wrong\nYour account is locked due to too many false login attempts. Enter the CAPTCHA to unlock.')
                            audit_logger.info(f'{timezone.now()} - LoginAttempt - {username}, Failed attempt. Account Blocked')
                            show_captcha = True
                        # Check if the user has reached the maximum login attempts (e.g., 3 attempts)
                        if login_attempt.attempts >= max_attempts:
                            # Implement your account lockout logic here
                            # For example, you can disable the user's account or show a CAPTCHA
                            show_captcha = True
                    else:
                        messages.error(request, f'Your account is locked due to too many false login attempts. Enter the CAPTCHA to unlock.')
                        show_captcha = True

                except LoginAttempts.DoesNotExist:
                    # If this is the first login attempt, create a new instance
                    login_attempt = LoginAttempts.objects.create(user=User.objects.get(username=username), attempts=1)
        else:
            # Form is invalid, no need to manually add errors to the form
            # The errors will be displayed using messages.error
            pass
    else:
        form = LoginForm()

    # Add the captcha field to the form if needed
    if show_captcha:
        form.fields['captcha'] = CaptchaField()

    # Convert messages to a list
    message_list = list(messages.get_messages(request))

    return render(request, 'login.html', {'form': form, 'show_captcha': show_captcha, 'messages': message_list})




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
