from django.contrib import admin
from django.contrib.auth import get_user_model

from applications.account.models import CustomUser

User = get_user_model()  # User=CustomUser
# Register your models here.
admin.site.register(User)
