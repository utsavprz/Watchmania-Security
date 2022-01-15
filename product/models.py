
from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name}'   

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.ForeignKey(Category,null=True,blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,null=True,blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    search_tags = models.TextField(blank=True,null=True)
    available = models.BooleanField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return f'({self.name} - {self.category})'