from django.db import models
from django.contrib.auth.models import User
from product.models import Products
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.conf import settings
# Create your models here.


METHOD =(
    ("Cash on Delivery","Cash on Delivery"),
    ("Khalti","Khalti")
)
class Order(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20,choices=METHOD, default="Cash on Delivery")
    complete = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
        

    @property
    def get_cart_items(self):
        orderitems =self.orderitem_set.all().count()
        total = orderitems
        return total

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.id)

