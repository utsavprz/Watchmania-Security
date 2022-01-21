from django.contrib import admin

from checkout.models import ShippingAddress, ShippingContactInfo

# Register your models here.

admin.site.register(ShippingContactInfo)
admin.site.register(ShippingAddress)