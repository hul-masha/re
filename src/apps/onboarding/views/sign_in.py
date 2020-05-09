from django.contrib.auth.views import LoginView


class SignInView(LoginView):
    template_name = "onboarding/sign_in.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
