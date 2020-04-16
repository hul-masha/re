from django.test import Client
from django.test import TestCase

# from apps.index.views import IndexView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/")
        self.assertEqual(resp.status_code, 200)

        """This attribute is only populated
        when using the DjangoTemplates backend.
        If you’re using another template engine, 
        template_name may be a suitable alternative 
        if you only need the name of the template used for rendering. so this == 0 (not 2)"""
        self.assertEqual(len(resp.templates), 0)  # значит что исп не джанга шаблоны
        self.assertEqual(
            len(resp.template_name), 1
        )  # значит что список содержит только имя самого файла
        self.assertEqual(resp.resolver_match.app_name, "index")
        self.assertEqual(resp.resolver_match.url_name, "index")
        self.assertEqual(resp.resolver_match.view_name, "index:index")
        self.assertEqual(
            [_t for _t in resp.template_name], ["index/index.html"]  # , "base.html"]
        )
        from django.views.generic import TemplateView

        self.assertEqual(
            resp.resolver_match.func.__name__, TemplateView.as_view().__name__
        )
