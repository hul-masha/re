from django import http as h
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from apps.index.models import UserInfo

# def view(request: HttpRequest) -> HttpResponse: # это хтнты, валидация типов (то есть их соответствие типов)
# if request.method!="GET":
# not work   return HttpResponse("xxx",status=405)
#    if request.method=="GET":
#       return render(request, "index/index.html") # питон приводит значение к типу прямо на месте тк динамич язык


class IndexView(TemplateView):
    template_name = "index/index.html"
    extra_context = {
        "File": ["index", "GUL MARIA", "index:index"],
        "file2": ["resume:index", "Resume"],
        "file3": ["thoughts:index", "Thoughts"],
    }

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data()
        info = UserInfo.objects.first()
        ctx = {"name": info.name, "greeting": info.greeting}
        ctx.update(parent_ctx)
        return ctx


# def get(self,request):
#    return render(request, "index/index.html")
