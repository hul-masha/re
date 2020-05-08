from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.blog.forms import CommentForm
from apps.blog.models import Post


class AllBlogPostView(ListView):
    template_name = "blog/blog.html"
    model = Post
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = Post
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["form"] = CommentForm(
                initial={"post": self.object, "author": self.request.user}
            )

        return ctx


class CommentView(LoginRequiredMixin, CreateView):
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }
    form_class = CommentForm
    http_method_names = ["post"]

    def get_success_url(self):
        url = reverse_lazy("blog:post", kwargs={"pk": self.kwargs["pk"]})

        return url
