from operator import truediv
from django.db import models
from django.conf import settings

from cart.models import Order

# Create your models here.
class ShippingAddress(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,blank=True,null=True)
    email = models.CharField(max_length=150,blank=True,null=True)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address