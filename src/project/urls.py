from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
here = Path(__file__).parent.resolve()
def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())
def view2(r):
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
    index=here.parent.parent / "css/font-awesome.min.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")
def woff2(r):
    index=here.parent.parent / "fonts/fontawesome-webfont.woff2"
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type="font/woff2")
def ttf(r):
    index=here.parent.parent / "fonts/fontawesome-webfont.ttf"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="font/ttf")
def woff(r):
    index=here.parent.parent / "fonts/fontawesome-webfont.woff"
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type="font/woff")
def svg(r):
    index=here.parent.parent / "fonts/fontawesome-webfont.svg"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="image/svg+xml")
def eot(r):
    index=here.parent.parent / "fonts/fontawesome-webfont.eot"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="application/vnd.ms-fontobject")
def otf(r):
    index=here.parent.parent / "fonts/FontAwesome.otf"
    with index.open("rb") as f:
        return HttpResponse(f.read(), content_type="font/otf")
def ico(r):
    index=here.parent.parent / "favicon.ico"
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type="image/x-icon")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('Resume.html',resume),
    path('Thoughts.html', thoughts),
    path('css/bootstrap.min.css', bootstrap),
    path('css/hero-slider-style.css', hero),
    path('css/magnific-popup.css', magn),
    path('css/tooplate-style.css', toop),
    path('gBAs.jpg',img),
    path('favicon.ico',ico),
    path('js/bootstrap.min.js', jsbootstrap),
    path('js/hero-slider-main.js',jshero),
    path('js/jquery.magnific-popup.min.js',jsmag),
    path('js/jquery-1.11.3.min.js',jsjquery),
    path('css/font-awesome.min.css',awesome),
    path('fontawesome-webfont.svg',svg),
    path('fonts/fontawesome-webfont.woff2',woff2),
    path('fonts/fontawesome-webfont.woff',woff),
    path('fonts/fontawesome-webfont.ttf',ttf),
    path('fonts/fontawesome-webfont.eot',eot),
    path('fonts/FontAwesome.otf',otf),
    path('index.html', view2)
]