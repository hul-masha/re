from django.test import Client
from django.test import TestCase

from apps.thoughts.views import IndexView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/thoughts/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 0)  # значит что исп не джанга шаблоны
        self.assertEqual(len(resp.template_name), 1)  # значит что список содержит только имя самого файла
        self.assertEqual(
            [_t for _t in resp.template_name], ["thoughts/index.html"]  # , "base.html"]
        )
       # self.assertEqual(len(resp.templates), 2)
       # self.assertEqual(
        #    [_t.name for _t in resp.templates], ["thoughts/index.html", "base.html"]
        #)
        self.assertEqual(resp.resolver_match.func.__name__, IndexView.as_view().__name__)