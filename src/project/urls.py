from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
here = Path(__file__).parent.resolve()
def glob_view(file="Resume.html", type="text/html"):
    index=here.parent.parent / file
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type=type)
def view(r):
    return glob_view(file="index.html")

def resume(r):
    return glob_view()

def thoughts(r):
    return glob_view("Thoughts.html")

def img(rb):
    return glob_view("gBAs.jpg","image/jpg")

def ico(r):
    return glob_view("favicon.ico", "image/x-icon")

def bootstrap(r):
    return glob_view("css/bootstrap.min.css","text/css")

def hero(r):
    return glob_view("css/hero-slider-style.css", "text/css")

def magn(r):
    return glob_view("css/magnific-popup.css", "text/css")

def toop(r):
    return glob_view("css/tooplate-style.css", "text/css")

def awesome(r):
    return glob_view("css/font-awesome.min.css", "text/css")

def woff2(r):
    return glob_view("fonts/fontawesome-webfont.woff2","font/woff2")

def ttf(r):
    return glob_view("fonts/fontawesome-webfont.ttf","font/ttf")

def woff(r):
    return glob_view("fonts/fontawesome-webfont.woff","font/woff")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('Resume.html',resume),
    path('Thoughts.html',thoughts),
    path('index.html', view),
    path('css/bootstrap.min.css', bootstrap),
    path('css/hero-slider-style.css', hero),
    path('css/magnific-popup.css', magn),
    path('css/tooplate-style.css', toop),
    path('css/font-awesome.min.css', awesome),
    path('gBAs.jpg',img),
    path('favicon.ico',ico),
    path('fonts/fontawesome-webfont.woff2', woff2),
    path('fonts/fontawesome-webfont.woff', woff),
    path('fonts/fontawesome-webfont.ttf', ttf),
    #path('js/bootstrap.min.js', jsbootstrap),
    #path('js/hero-slider-main.js',jshero),
    #path('js/jquery.magnific-popup.min.js',jsmag),
    #path('js/jquery-1.11.3.min.js',jsjquery),
    #path('fontawesome-webfont.svg',svg),
    #path('fonts/fontawesome-webfont.eot',eot),
    #path('fonts/FontAwesome.otf',otf),
]