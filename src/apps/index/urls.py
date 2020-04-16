from django.urls import path
from apps.index.apps import IndexConfig
#from apps.index.views import view
#from apps.index.views import IndexView
from django.views.generic import TemplateView

app_name=IndexConfig.label

urlpatterns = [
    path('', TemplateView.as_view(template_name='index/index.html',
                                  extra_context={"File":["index","GUL MARIA","index:index"],
                                                 "file2":["resume:index","Resume"],
                                                 "file3":["thoughts:index", "Thoughts"],
                                                 }), name='index'),
]