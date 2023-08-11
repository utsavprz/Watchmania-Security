from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class User_Address(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

class user_details(models.Model):
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    phone_verified = models.BooleanField(default=False,blank=True)
    dob = models.DateField()
    age = models.IntegerField(null=True,blank=True)
    default_User_Address = models.ForeignKey(User_Address,null=True,blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.user_info.id}'
class LoginAttempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attempts = models.PositiveIntegerField(default=0)
    last_attempt_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - Attempts: {self.attempts}"