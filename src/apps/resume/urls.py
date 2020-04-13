from django.urls import path

from apps.resume.apps import ResumeConfig
#from apps.resume.views import view
from apps.resume.views import IndexView

app_name=ResumeConfig.name

urlpatterns = [
    path('', IndexView.as_view(extra_context={"File":["resume","RESUME","resume:index"],
                                              "file2":["thoughts:index","Thoughts"],
                                              "file3":["index:index","Home"],
                                              }),name='index'),
]