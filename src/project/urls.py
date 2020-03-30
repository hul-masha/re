from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
here = Path(__file__).parent.resolve()
def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())
def resume(r):
    index = here.parent.parent / "Resume.html"
    with index.open() as f:
        return HttpResponse(f.read())
def thoughts(r):
    index = here.parent.parent / "Thoughts.html"
    with index.open() as f:
        return HttpResponse(f.read())
def img(rb):
    index=here.parent.parent / "gBAs.jpg"
    with index.open("rb") as f:
        return  HttpResponse(f.read())
def bootstrap(r):
    index=here.parent.parent / "css/bootstrap.min.css"
    with index.open() as f:
        return HttpResponse(f.read())
def hero(r):
    index=here.parent.parent / "css/hero-slider-style.css"
    with index.open() as f:
        return HttpResponse(f.read())
def magn(r):
    index=here.parent.parent / "css/magnific-popup.css"
    with index.open() as f:
        return HttpResponse(f.read())
def toop(r):
    index=here.parent.parent / "css/tooplate-style.css"
    with index.open() as f:
        return HttpResponse(f.read())
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('Resume.html',resume),
    path('Thoughts.html', thoughts),
    path('bootstrap.css', bootstrap),
    path('hero-slider-style.css', hero),
    path('magnific-popup.css', magn),
    path('tooplate-style.css', toop)
]