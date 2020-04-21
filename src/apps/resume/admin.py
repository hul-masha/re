from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models import Project
from apps.resume.models import Responsibility
from apps.resume.models import Technology


"""def gen_noraml_form(_models,_fields):
    class _AdminForm(forms.ModelForm):
        class Meta:
            model = _models
            _fields ="__all__"
            widgets = {
                _f: 
            }"""
# class TechnologyAdminModelForm(forms.ModelForm):
#   ...
@admin.register(Technology)
class TechnologyAdminModel(ModelAdmin):
    ...


@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    ...


@admin.register(Responsibility)
class ResponsibilityAdminModel(ModelAdmin):
    ...
