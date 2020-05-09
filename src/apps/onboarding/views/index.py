from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "onboarding/index.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
