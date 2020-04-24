from os import urandom

# import delorean
from django.test import TestCase

from apps.resume.models.firm import Firm
from apps.resume.models.project import Project
from apps.resume.models.technology import Technology


class Test(TestCase):
    def test_project(self):
        placeholder = urandom(4).hex()

        fi = Firm(name=placeholder)

        kw = {
            "name": placeholder,
            "firm": fi,
            # "started_at": start,
        }

        prj = Project(**kw)
        self.assertEqual(prj.name, placeholder)
        self.assertEqual(str(prj), f"#{prj.pk} {placeholder} -> {placeholder!r}")

        prj = Project(achievements="a\nb\nc\n", **kw)
        self.assertSetEqual(set(prj.achievemen), set("abc"))

        prj = Project(responsibilities="a\nb\nc\n", **kw)
        self.assertSetEqual(set(prj.responsibil), set("abc"))

    def test_firm(self):
        placeholder = urandom(4).hex()

        fi = Firm(name=placeholder)
        self.assertEqual(str(fi), f"{fi.pk}: {placeholder}")

    def test_technology(self):
        placeholder = urandom(4).hex()

        framework = Technology(name=placeholder, pk=None)
        self.assertEqual(str(framework), f"#None {placeholder!r} : ")

        framework = Technology(name=placeholder, version="1.0.0", pk=None)
        self.assertEqual(str(framework), f"#None {placeholder!r} :  1.0.0")
