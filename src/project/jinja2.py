from django.conf import settings
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
    # import pdb; pdb.set_trace()
    Environment(**options).compile_templates("src/project/target.zip")
    env = Environment(loader=ModuleLoader("src/project/target.zip"))
    env.globals.update({"static": static, "url": reverse, "debug": settings.DEBUG})
    # template = env.get_template("index/index.html")
    # return template.render()
    return env
