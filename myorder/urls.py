from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.myOrder,name="myOrder"),
    path('orderedProducts/<int:order_id>',views.orderedItems,name="orderedProducts"),
]
