from django.views.generic import TemplateView


class SignUpConfirmedView(TemplateView):
    template_name = "onboarding/sign_up_confirmed.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
