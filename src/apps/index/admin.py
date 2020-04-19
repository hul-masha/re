from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from apps.index.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdminModel(ModelAdmin):
    ...
