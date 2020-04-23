from django.test import Client
from django.test import TestCase
from django.views.generic import TemplateView

from apps.resume.views import IndexView
from project.utils.xtest import ResponseTestMixin


class Test(TestCase, ResponseTestMixin):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        self.validate_response(
            url="/resume/",
            expected_view=IndexView,
            expected_view_name="resume:index",
            expected_template="resume/index.html",
        )

        """# info = UserInfo(name="xxx")
        # info.save()
        resp = self.cli.get("/resume/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 0)  # значит что исп не джанга шаблоны
        self.assertEqual(
            len(resp.template_name),
            2  # 2 при джиндже значит что вьюха наслед от ListView
            # то есть содержит шаблон по умолчанию (его бы искала если бы он не был указан явно)
            # f"{model.lower()}_list.html"
        )  # 1 значит что список содержит только имя самого файла
        self.assertEqual(resp.resolver_match.app_name, "resume")
        self.assertEqual(resp.resolver_match.url_name, "index")
        self.assertEqual(resp.resolver_match.view_name, "resume:index")
        # self.assertEqual(
        #    [_t for _t in resp.template_name], ["resume/index.html"]  # , "base.html"]
        # )
        # self.assertEqual(len(resp.templates), 2)
        # self.assertEqual(
        #   [_t.name for _t in resp.templates], ["resume/index.html", "base.html"]
        # )
        self.assertEqual(
            resp.resolver_match.func.__name__, IndexView.as_view().__name__
        )"""
