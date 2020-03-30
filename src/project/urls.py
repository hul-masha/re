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
        return  HttpResponse(f.read(), content_type="image/jpg")
def bootstrap(r):
    index=here.parent.parent / "css/bootstrap.min.css"
    with index.open() as f:
        return HttpResponse(f.read(),content_type= "text/css")
def hero(r):
    index=here.parent.parent / "css/hero-slider-style.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
def magn(r):
    index=here.parent.parent / "css/magnific-popup.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
def toop(r):
    index=here.parent.parent / "css/tooplate-style.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
def jsbootstrap(r):
    index=here.parent.parent / "js/bootstrap.min.js"
    with index.open() as f:
        return HttpResponse(f.read(),content_type="text/javascript")
def jshero(r):
    index=here.parent.parent / "js/hero-slider-main.js"
    with index.open() as f:
        return HttpResponse(f.read(),content_type="text/javascript")
def jsmag(r):
    index=here.parent.parent / "js/jquery.magnific-popup.min.js"
    with index.open() as f:
        return HttpResponse(f.read(),content_type="text/javascript")
def jsjquery(r):
    index=here.parent.parent / "js/jquery-1.11.3.min.js"
    with index.open() as f:
        return HttpResponse(f.read(),content_type="text/javascript")
def awesome(r):
    index=here.parent.parent / "font-awesome-4.5.0/css/font-awesome.min.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
def svg(r):
    index=here.parent.parent / "font-awesome-4.5.0/fonts/fontawesome-webfont.svg"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="image/svg")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html', view),
    path('Resume.html',resume),
    path('Thoughts.html', thoughts),
    path('bootstrap.css', bootstrap),
    path('hero-slider-style.css', hero),
    path('magnific-popup.css', magn),
    path('tooplate-style.css', toop),
    path('bootstrap.min.js', jsbootstrap),
    path('hero-slider-main.js',jshero),
    path('jquery.magnific-popup.min.js',jsmag),
    path('jquery-1.11.3.min.js',jsjquery),
    path('font-awesome.min.css',awesome),
    path('fontawesome-webfont.svg',svg)
]