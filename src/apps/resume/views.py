from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def view(request: HttpRequest) -> HttpResponse:
    return render(request,"resume/Resume.html")