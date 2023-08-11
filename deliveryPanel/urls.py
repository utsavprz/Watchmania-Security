from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.deliverypanelLogin, name="deliverypanelLogin"),
    path("dashboard", views.deliverypanel, name="dashboard"),
    path("logoutDeliveryGuy", views.logoutDelivery, name="logoutDeliveryGuy")
    
]
