from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from apps.resume.models.project import Project


class IndexView(ListView):  # TemplateView
    template_name = "resume/index.html"
    extra_context = {
        "File": ["resume", "RESUME", "resume:index"],
        "file2": ["thoughts:index", "Thoughts"],
        "file3": ["index:index", "Home"],
    }
    model = Project  ##queryset = Project.objects.filter(is_hidden=False)

    """def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        projects = Project.objects.all()
        ctx["projects"] = projects
        return ctx"""


# queryset = Project.objects.filter(firm__stertswith="T")lte
"""class IndexView(TemplateView):
   def get_context_data(self, **kwargs):
       ctx = super().get_context_data()

       projects = Project.objects.all()
       ctx["projects"]=projects
       return ctx"""

# Create your views here.
# def view(request: HttpRequest) -> HttpResponse:
#  return render(request,"resume/index.html")
# class IndexView(View):
#   def get(self,request):
#      return render(request, "resume/index.html")
