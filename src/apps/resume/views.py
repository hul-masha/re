from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
#def view(request: HttpRequest) -> HttpResponse:
  #  return render(request,"resume/index.html")
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "resume/index.html"
#class IndexView(View):
 #   def get(self,request):
  #      return render(request, "resume/index.html")
