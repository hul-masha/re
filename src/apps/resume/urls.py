from django.urls import path
from django.views.generic import TemplateView

from apps.resume.apps import ResumeConfig
from apps.resume.views import IndexView

app_name = ResumeConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index",),
]
