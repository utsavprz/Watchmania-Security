from django.urls import path
from django.urls.conf import include

from checkout import views

urlpatterns = [
    path('',views.checkout,name="checkout"),
    path('khalti-verify',views.KhaltiVerifyView,name="khaltiverify"),
]
