from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# def view(request: HttpRequest) -> HttpResponse:
#  return render(request,"resume/index.html")


# class IndexView(TemplateView):
#   template_name = "resume/index.html"
# class IndexView(View):
#   def get(self,request):
#      return render(request, "resume/index.html")
