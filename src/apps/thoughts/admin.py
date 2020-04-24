from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.thoughts.models import Comment
from apps.thoughts.models import Post
from apps.thoughts.models import User
from project.utils.xforms import gen_textinput_admin_form


@admin.register(Post)
class InfoAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(Post, [Post.tema, Post.post_text],)


@admin.register(Comment)
class CommentAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(Comment, [Comment.message,],)


@admin.register(User)
class UserAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(User, [User.name,],)
