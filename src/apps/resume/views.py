from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


from apps.resume.models import Project


class IndexView(TemplateView):
   def get_context_data(self, **kwargs):
       ctx = super().get_context_data()

       projects = Project.objects.all()
       ctx["projects"]=projects
       return ctx

# Create your views here.
# def view(request: HttpRequest) -> HttpResponse:
#  return render(request,"resume/index.html")
# class IndexView(View):
#   def get(self,request):
#      return render(request, "resume/index.html")
