from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django import http as h
from django.views import View


#def view(request: HttpRequest) -> HttpResponse: # это хтнты, валидация типов (то есть их соответствие типов)
    #if request.method!="GET":
     # not work   return HttpResponse("xxx",status=405)
 #    if request.method=="GET":
  #       return render(request, "index/index.html") # питон приводит значение к типу прямо на месте тк динамич язык


#from django.views.generic import TemplateView
#class IndexView(TemplateView):
#    template_name = "index/index.html"

    #def get(self,request):
    #    return render(request, "index/index.html")
