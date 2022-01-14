from unicodedata import category
from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    available = models.BooleanField()
    image = models.CharField(max_length=300)
