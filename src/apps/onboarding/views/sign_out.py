from django.contrib.auth.views import LogoutView


class SignOutView(LogoutView):  # no cover
    template_name = "onboarding/signed_out.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
