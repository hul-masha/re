from django.views.generic import TemplateView


class SignUpConfirmedView(TemplateView):
    template_name = "onboarding/sign_up_confirmed.html"
    extra_context = {
        "File": ["index", "Profile", "onboarding:index"],
        "file5": ["resume:index", "Resume"],
        "file2": ["thoughts:index", "Thoughts"],
        "file4": ["blog:blog", "Blog"],
        "file3": ["index:index", "Home"],
    }
