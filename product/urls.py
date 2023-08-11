from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("productView", views.display, name="display"),
    path("productDetail/<int:item_id>", views.detail, name="detail"),
    path('review/<int:item_id>/', views.add_review, name='add_review'),
    path("category/<int:cat_id>", views.categoryDisplay, name="category"),
    path("wishlist", views.wishlistView, name="wishlist"),
    
]
