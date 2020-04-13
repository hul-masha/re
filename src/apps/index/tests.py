from django.test import Client
from django.test import TestCase

#from apps.index.views import IndexView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 2)
        self.assertEqual(
            [_t.name for _t in resp.templates], ["index/index.html", "base.html"]
        )
        from django.views.generic import TemplateView
        self.assertEqual(resp.resolver_match.func.__name__, TemplateView.as_view().__name__)# не фурыч тк мы сравн саму ф-ку
        # и ее рез работы и они ссыл на раз ячейки памяти