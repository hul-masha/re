from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.http import HttpRequest
from django.urls import path
from django.conf import  settings
from django.shortcuts import render
here = Path(__file__).parent.resolve()
def static_re(file="Resume.html", type="text/html"):
    index=here.parent.parent / file
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type=type)

def view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

#def view(r, f=static_re):
 #   return f(file="index.html")#так код работает быстрее тут не тратиться время на поиск имени функ при ее вызове
#но эт все равно копейки (связь с именем установ при синтак дереве поэтому не тратиться время на  ее поиск )
     #render(r,"index.html")
def resume(r):
    return render(r,"Resume.html")#static_re()

def thoughts(r):
    #print(r.Get())
    return render(r,"Thoughts.html")#static_re("Thoughts.html")

def img(rb):
    return static_re("gBAs.jpg","image/jpg") #render
    #return render("gBAs.jpg",content_type="image/jpg")

def ico(r):
    return static_re("favicon.ico", "image/x-icon")

def bootstrap(r):
    return static_re("css/bootstrap.min.css","text/css")

def hero(r):
    return static_re("css/hero-slider-style.css", "text/css")

def magn(r):
    return static_re("css/magnific-popup.css", "text/css")

def toop(r):
    return static_re("css/tooplate-style.css", "text/css")

def awesome(r):
    return static_re("css/font-awesome.min.css", "text/css")

def woff2(r):
    return static_re("fonts/fontawesome-webfont.woff2","font/woff2")

def ttf(r):
    return static_re("fonts/fontawesome-webfont.ttf","font/ttf")

def woff(r):
    return static_re("fonts/fontawesome-webfont.woff","font/woff")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('Resume.html', resume),
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