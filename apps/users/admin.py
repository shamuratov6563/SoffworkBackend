from django.contrib import admin

from apps.users import models
from .models import User, UserProfile

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = ('id', 'username', 'auth_type', 'auth_status', 'auth_role')

admin.site.register(UserProfile)

