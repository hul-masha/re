from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.thoughts.models import FeedbackInfo


@admin.register(FeedbackInfo)
class InfoAdminModel(ModelAdmin):
    ...
