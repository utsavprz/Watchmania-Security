from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.adminpanelLogin, name="adminpanelLogin"),
    path("admin-dashboard", views.adminpanel, name="admindashboard"),
    path("logoutAdmin", views.logoutAdmin, name="logoutAdmin")
]
