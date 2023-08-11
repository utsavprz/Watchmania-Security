from django.contrib import admin

from myorder.views import myOrder
from .models import *
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(Delivery)