from django.test import Client
from django.test import TestCase
from django.views.generic import TemplateView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/resume/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 0)  # значит что исп не джанга шаблоны
        self.assertEqual(
            len(resp.template_name), 1
        )  # значит что список содержит только имя самого файла
        self.assertEqual(resp.resolver_match.app_name, "resume")
        self.assertEqual(resp.resolver_match.url_name, "index")
        self.assertEqual(resp.resolver_match.view_name, "resume:index")
        self.assertEqual(
            [_t for _t in resp.template_name], ["resume/index.html"]  # , "base.html"]
        )
        # self.assertEqual(len(resp.templates), 2)
        # self.assertEqual(
        #   [_t.name for _t in resp.templates], ["resume/index.html", "base.html"]
        # )
        self.assertEqual(
            resp.resolver_match.func.__name__, TemplateView.as_view().__name__
        )
