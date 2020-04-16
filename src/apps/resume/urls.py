from django.urls import path
from django.views.generic import TemplateView

from apps.resume.apps import ResumeConfig

# from apps.resume.views import view
# from apps.resume.views import IndexView

app_name = ResumeConfig.label

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="resume/index.html",
            extra_context={
                "File": ["resume", "RESUME", "resume:index"],
                "file2": ["thoughts:index", "Thoughts"],
                "file3": ["index:index", "Home"],
            },
        ),
        name="index",
    ),
]
