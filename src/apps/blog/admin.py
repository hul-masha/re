from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.blog.models import Comment, Photo
from apps.blog.models import Post
from project.utils.xforms import gen_textinput_admin_form


@admin.register(Post)
class UserInfoAdminModel(ModelAdmin):
    # form = gen_textinput_admin_form(UserInfo, [UserInfo.name, UserInfo.greeting])
    ...

@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    ...

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    ...
