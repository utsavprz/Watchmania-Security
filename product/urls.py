from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("productView", views.display, name="display"),
    path("productDetail/<int:item_id>", views.detail, name="detail"),
]
