from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.onboarding.forms.sign_up import SignUpForm
from apps.onboarding.utils.verification import start_verification


class SignUpView(FormView):
    template_name = "onboarding/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("onboarding:sign_up_confirmed")
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }

    @transaction.atomic()
    def form_valid(self, form):
        user = form.save()
        start_verification(self.request, user)
        return super().form_valid(form)
