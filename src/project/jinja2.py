from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from jinja2 import ModuleLoader

# Compile template
# Environment(loader=FileSystemLoader('foopkg/templates'))\
#   .compile_templates("foopkg/compiled/foopkg.zip")

# Environment
# env = Environment(loader=ModuleLoader("foopkg/compiled/foopkg.zip"))


def environment(**options):
    # env = Environment(**options)
    # import pdb; pdb.set_trace()
    # раскоментить когда меняю содержимое шаблона или создаю новый
    # Environment(**options).compile_templates("src/project/target.zip")
    env = Environment(loader=ModuleLoader("src/project/target.zip"))
    env.globals.update({"static": static, "url": reverse, "debug": settings.DEBUG})
    return env
