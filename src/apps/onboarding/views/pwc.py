from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PwcView(PasswordChangeView):  # no cover
    template_name = "onboarding/pwc_form.html"
    success_url = reverse_lazy("onboarding:pwc_done")
    extra_context = {
        "File": ["index", "Profile", "onboarding:index"],
        "file5": ["resume:index", "Resume"],
        "file2": ["thoughts:index", "Thoughts"],
        "file4": ["blog:blog", "Blog"],
        "file3": ["index:index", "Home"],
    }
