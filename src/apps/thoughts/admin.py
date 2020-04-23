from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.thoughts.models import Comment
from apps.thoughts.models import Feedback
from apps.thoughts.models import User


@admin.register(Feedback)
class InfoAdminModel(ModelAdmin):
    ...


@admin.register(Comment)
class CommentAdminModel(ModelAdmin):
    ...


@admin.register(User)
class UserAdminModel(ModelAdmin):
    ...
