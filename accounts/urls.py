from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    
    path('register',views.register,name="register"),
    path("logout", views.logoutUser, name="logout"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path('profile_update',views.profile_update,name="profile_update"),
    path('addAddress',views.addAddress,name="addAddress"),
    path('updateAddress',views.updateAddress,name="updateAddress"),
]
