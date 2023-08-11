from django.contrib import admin
from accounts.models import User_Address

from accounts.models import user_details

# Register your models here.
admin.site.register(User_Address)

admin.site.register(user_details)

