from os import urandom

from django.test import Client
from django.test import TestCase

from apps.blog.models import Post
from apps.blog.views import BlogPostView
from project.utils.xtest import ResponseTestMixin
from project.utils.xtest import UserTestMixin


class Test(TestCase, ResponseTestMixin, UserTestMixin):
    def test_get_absent(self):
        self.validate_response(
            url="/blog/post/1/",
            expected_status_code=404,
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
            content_filters=(lambda _c: b"Not Found" in _c,),
        )

    def test_get_existing_anon(self):
        placeholder = urandom(4).hex()
        post = Post(title=f"t_{placeholder}", content=f"c_{placeholder}")
        post.save()

        self.validate_response(
            url=f"/blog/post/{post.pk}/",
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
            content_filters=(
                lambda _c: f"t_{placeholder}".encode() in _c,
                lambda _c: f"c_{placeholder}".encode() in _c,
                lambda _c: b"<form" not in _c,
            ),
        )

    def test_get_existing_authed(self):
        placeholder = urandom(4).hex()
        user = self.create_user(placeholder)
        client = Client()
        client.login(username=user.username, password=placeholder)

        post = Post(title=f"t_{placeholder}", content=f"c_{placeholder}")
        post.save()

        self.validate_response(
            client=client,
            url=f"/blog/post/{post.pk}/",
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
            content_filters=(
                lambda _c: f"t_{placeholder}".encode() in _c,
                lambda _c: f"c_{placeholder}".encode() in _c,
                lambda _c: b"<form" in _c,
            ),
        )

    def test_post(self):
        post = Post()
        post.save()

        self.validate_response(
            method="post",
            url=f"/blog/post/{post.pk}/",
            expected_status_code=405,
            expected_view=BlogPostView,
            expected_template="blog/post.html",
            expected_view_name="blog:post",
            content_filters=(lambda _c: _c == b"",),
        )
