from django.views.generic import DetailView
from django.views.generic import ListView

from apps.blog.models import BlogPost


class AllBlogPostView(ListView):
    template_name = "blog/blog.html"
    model = BlogPost


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = BlogPost
