from django.contrib.auth.views import LoginView


class SignInView(LoginView):
    template_name = "onboarding/sign_in.html"
    extra_context = {
        "File": ["index", "Profile", "onboarding:index"],
        "file5": ["resume:index", "Resume"],
        "file2": ["thoughts:index", "Thoughts"],
        "file4": ["blog:blog", "Blog"],
        "file3": ["index:index", "Home"],
    }
