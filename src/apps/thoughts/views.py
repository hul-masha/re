from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from apps.thoughts.models import FeedbackInfo

# Create your views here.
# def view(request: HttpRequest) -> HttpResponse:
#   return render(request,"thoughts/index.html")


class IndexView(TemplateView):
    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data()
        info = FeedbackInfo.objects.first()
        ctx = {"number": info.number, "message": info.message}
        ctx.update(parent_ctx)
        return ctx


# class IndexView(View):
#   def get(self,request):
#      return render(request, "thoughts/index.html")
