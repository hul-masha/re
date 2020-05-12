from django.urls import path
from django.views.generic import TemplateView

from apps.thoughts.apps import ThoughtsConfig

# from apps.thoughts.views import IndexView

app_name = ThoughtsConfig.label

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="thoughts/index.html",
            extra_context={
                "File": ["index", "Thoughts", "thoughts:index"],
                "file2": ["resume:index", "Resume"],
                "file3": ["index:index", "Home"],
                "file4": ["blog:blog", "Blog"],
                "file5": ["onboarding:index", "Profile"],
            },
        ),
        name="index",
    ),
]
