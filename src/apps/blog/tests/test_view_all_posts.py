from unittest import skip

from django.test import TestCase

from apps.blog.views import AllBlogPostView
from project.utils.xtest import ResponseTestMixin


class Test(TestCase, ResponseTestMixin):
    def test_get(self):
        self.validate_response(
            url="/blog/",
            expected_view=AllBlogPostView,
            expected_template="blog/blog.html",
            expected_view_name="blog:blog",
            content_filters=(lambda _c: b"blog" in _c,),
        )

    def test_post(self):
        self.validate_response(
            method="post",
            url="/blog/",
            expected_status_code=405,
            expected_view=AllBlogPostView,
            expected_template="blog/blog.html",
            expected_view_name="blog:blog",
            content_filters=(lambda _c: _c == b"",),
        )
