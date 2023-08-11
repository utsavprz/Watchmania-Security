from django.conf import settings
from django.db import models

from cart.models import Delivery, Order
from checkout.models import ShippingAddress

# Create your models here.
class MyOrder(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    o_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{str(self.o_id)} - {str(self.user_info)}'