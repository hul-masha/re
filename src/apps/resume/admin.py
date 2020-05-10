from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.resume.models.firm import Firm
from apps.resume.models.project import Project
from apps.resume.models.technology import Technology
from project.utils.xforms import gen_textinput_admin_form


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
    form = gen_textinput_admin_form(Technology, (Technology.name, Technology.version),)


@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(Project, [Project.name, Project.summary])


@admin.register(Firm)
class FirmAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(Project, ("name",))  # (Firm.name,))
