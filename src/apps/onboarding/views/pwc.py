from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class PwcView(PasswordChangeView):  # no cover
    template_name = "onboarding/pwc_form.html"
    success_url = reverse_lazy("onboarding:pwc_done")
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
