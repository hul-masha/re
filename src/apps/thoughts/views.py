from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
#def view(request: HttpRequest) -> HttpResponse:
 #   return render(request,"thoughts/index.html")
from django.views import View
#from django.views.generic import TemplateView


#class IndexView(TemplateView):
 #   template_name = "thoughts/index.html"
  #  extra_context = {"File": ["thoughts", "THOUGHTS", "thoughts:index"],
   #                  "file2":["resume:index","Resume"],
    #                 "file3":["index:index","Home"],
     #                }

#class IndexView(View):
 #   def get(self,request):
  #      return render(request, "thoughts/index.html")