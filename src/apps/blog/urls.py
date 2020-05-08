from django.urls import path
from django.views.generic import TemplateView

from apps.blog.apps import BlogConfig
from apps.blog.views import AllBlogPostView
from apps.blog.views import BlogPostView
from apps.blog.views import CommentView

app_name = BlogConfig.label

urlpatterns = [
    path("", AllBlogPostView.as_view(), name="blog",),
    path("post/<int:pk>/", BlogPostView.as_view(), name="post",),
    path("posts/<int:pk>/comment/", CommentView.as_view(), name="comment"),
]
