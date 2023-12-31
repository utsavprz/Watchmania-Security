from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import User_Address
from accounts.models import user_details
from captcha.fields import CaptchaField

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name','username', 'email', 'password1', 'password2']

class user_details(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = user_details
        fields = "__all__"

class User_Address(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = User_Address
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    captcha = CaptchaField()
