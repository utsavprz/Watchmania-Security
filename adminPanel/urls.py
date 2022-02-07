from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.adminpanelLogin, name="adminpanelLogin"),
    path("admin-dashboard", views.adminHome, name="admindashboard"),
    path("admin-products", views.adminProducts, name="adminproducts"),
    path("productEdit/<int:prodId>", views.productEdit, name="prodEdit") ,
    path("logoutAdmin", views.logoutAdmin, name="logoutAdmin")
]
