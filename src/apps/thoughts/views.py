from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.thoughts.models import Feedback

# Create your views here.
# def view(request: HttpRequest) -> HttpResponse:
#   return render(request,"thoughts/index.html")


class IndexView(ListView):
    model = Feedback

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data()
        info = Feedback.objects.all()
        ctx["info"] = info
        return ctx


# class IndexView(View):
#   def get(self,request):
#      return render(request, "thoughts/index.html")
