from django.contrib.auth.views import PasswordChangeDoneView


class PwcDoneView(PasswordChangeDoneView):  # no cover
    template_name = "onboarding/pwc_done.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
