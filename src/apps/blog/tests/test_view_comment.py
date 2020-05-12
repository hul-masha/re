from os import urandom

from django.test import Client
from django.test import TestCase

from apps.blog.models import Post
from apps.blog.views import BlogPostView
from apps.onboarding.views import SignInView
from project.utils.xtest import ResponseTestMixin
from project.utils.xtest import UserTestMixin


class Test(TestCase, ResponseTestMixin, UserTestMixin):
    def test_anon(self):
        placeholder = urandom(4).hex()
        post = Post(title=f"t_{placeholder}", content=f"c_{placeholder}")
        post.save()

        self.assertEqual(0, post.comments.count())

        self.validate_response(
            method="post",
            url=f"/blog/post/{post.pk}/comment/",
            expected_view=SignInView,
            expected_view_name="onboarding:sign_in",
            content_filters=(
                lambda _c: f"t_{placeholder}".encode() not in _c,
                lambda _c: f"c_{placeholder}".encode() not in _c,
            ),
        )

        self.assertEqual(0, post.comments.count())

    def test_post(self):
        placeholder = urandom(4).hex()

        user = self.create_user(placeholder)
        client = Client()
        client.login(username=user.username, password=user.username)

        post = Post(title=f"t_{placeholder}", content=f"c_{placeholder}")
        post.save()

        self.assertEqual(0, post.comments.count())

        self.validate_response(
            client=client,
            method="post",
            url=f"/blog/post/{post.pk}/comment/",
            form_data={
                "message": f"m_{placeholder}",
                "author": user.pk,
                "post": post.pk,
            },
            expected_view=BlogPostView,
            expected_view_name="blog:post",
            content_filters=(
                lambda _c: b"<form" in _c,
                lambda _c: f"c_{placeholder}".encode() in _c,
                lambda _c: f"m_{placeholder}".encode() in _c,
                lambda _c: f"t_{placeholder}".encode() in _c,
            ),
        )

        self.assertEqual(1, post.comments.count())
        comment = post.comments.first()
        self.assertEqual(user, comment.author)
        self.assertEqual(post, comment.post)
        self.assertEqual(f"m_{placeholder}", comment.message)

    def test_get(self):
        post = Post()
        post.save()

        user = self.create_user()
        client = Client()
        client.login(username=user.username, password=user.username)

        self.validate_response(
            client=client,
            url=f"/blog/post/{post.pk}/comment/",
            expected_status_code=405,
            expected_view=BlogPostView,
            expected_view_name="blog:post",  # не проверяет тк код 405
            content_filters=(lambda _c: _c == b"",),
        )
