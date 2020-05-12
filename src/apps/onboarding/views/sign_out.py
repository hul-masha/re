from django.contrib.auth.views import LogoutView


class SignOutView(LogoutView):  # no cover
    template_name = "onboarding/signed_out.html"
    extra_context = {
        "File": ["index", "Profile", "onboarding:index"],
        "file5": ["resume:index", "Resume"],
        "file2": ["thoughts:index", "Thoughts"],
        "file4": ["blog:blog", "Blog"],
        "file3": ["index:index", "Home"],
    }
