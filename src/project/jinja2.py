from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import ModuleLoader

# Compile template
# Environment(loader=FileSystemLoader('foopkg/templates'))\
#   .compile_templates("foopkg/compiled/foopkg.zip")

# Environment
# env = Environment(loader=ModuleLoader("foopkg/compiled/foopkg.zip"))


def environment(**options):

    Environment(**options).compile_templates("src/project/target.zip")
    env = Environment(loader=ModuleLoader("src/project/target.zip"))
    env.globals.update(
        {"static": static, "url": reverse,}
    )
    return env
