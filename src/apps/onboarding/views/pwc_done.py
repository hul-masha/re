from django.contrib.auth.views import PasswordChangeDoneView


class PwcDoneView(PasswordChangeDoneView):  # no cover
    template_name = "onboarding/pwc_done.html"
    extra_context = {
        "File": ["index", "Profile", "onboarding:index"],
        "file5": ["resume:index", "Resume"],
        "file2": ["thoughts:index", "Thoughts"],
        "file4": ["blog:blog", "Blog"],
        "file3": ["index:index", "Home"],
    }
