from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.blog.models import BlogPost
from project.utils.xforms import gen_textinput_admin_form


@admin.register(BlogPost)
class UserInfoAdminModel(ModelAdmin):
    # form = gen_textinput_admin_form(UserInfo, [UserInfo.name, UserInfo.greeting])
    ...
