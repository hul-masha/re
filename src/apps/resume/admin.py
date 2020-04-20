from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Technology, Project


@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    ...

@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    ...
