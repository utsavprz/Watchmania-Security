"""Brahmayeni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import urls
from django.conf import settings
from django.conf.urls.static import static


from product import views as productView
from cart import views as cartView
from checkout import views as checkoutView
from home import views as homeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('myorder/', include('myorder.urls')),
    path('checkout/', include('checkout.urls')),
    path('update_item/', cartView.updateItem,name="update_item"),
    path('searchResult',productView.searchResult,name="searched"),
    path('paymentsuccess/<int:orderID>/<int:pm>',checkoutView.paymentSuccess,name="paymentsuccess"),
    path('favoritethis/<int:p_id>', productView.favoritethis,name="favoritethis"),
    path('delivery-panel/', include('deliveryPanel.urls')),
    path('admin-panel/', include('adminPanel.urls')),
    path('session_timeout/', homeView.session_timeout, name='session_timeout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('captcha/', include('captcha.urls')),
    
    
    #  path('default/', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
