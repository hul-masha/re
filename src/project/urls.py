from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.http import HttpRequest
from django.urls import path
from django.conf import settings
from django.shortcuts import render

STATIC_DIR = settings.PROJECT_DIR / "static"
CSS_PATH_BOOTS = STATIC_DIR / "css" / "bootstrap.min.css"
RESUME_PATH= settings.PROJECT_DIR / "templates" / "Resume.html"
#here = Path(__file__).parent.resolve()
def static_re(file="Resume.html", type="text/html"):
    index=file#here.parent.parent / file
    with index.open("rb") as f:
        return HttpResponse(f.read(),content_type=type)

def view(request: HttpRequest) -> HttpResponse: # это хтнты, валидация типов (то есть их соответствие типов)
    return render(request, "index.html")        # питон приводит значение к типу прямо на месте тк динамич язык

def resume(r):
    return render(r,RESUME_PATH)

def thoughts(r):
    return render(r,"Thoughts.html")


#def img(rb):
 #   jpg_path= STATIC_DIR / "gBAs.jpg"
  #  return static_re(jpg_path,"image/jpg")

#def ico(r):
 #   ico_path=STATIC_DIR / "favicon.ico"
  #  return static_re(ico_path, "image/x-icon")

#def bootstrap(r):
 #   return static_re(CSS_PATH_BOOTS,"text/css")

#def hero(r):
 #   css_path = STATIC_DIR / "css" / "hero-slider-style.css"
  #  return static_re(css_path, "text/css")

#def magn(r):
 #   css_path = STATIC_DIR / "css" / "magnific-popup.css"
  #  return static_re(css_path, "text/css")

#def toop(r):
 #   css_path = STATIC_DIR / "css" / "tooplate-style.css"
  #  return static_re(css_path, "text/css")

#def awesome(r):
 #   css_path = STATIC_DIR / "css" / "font-awesome.min.css"
  #  return static_re(css_path, "text/css")

#def woff2(r):
 #   woff2_path=STATIC_DIR / "fonts" / "fontawesome-webfont.woff2"
  #  return static_re(woff2_path,"font/woff2")

#def ttf(r):
 #   ttf_path = STATIC_DIR / "fonts" / "fontawesome-webfont.ttf"
  #  return static_re(ttf_path,"font/ttf")

#def woff(r):
 #   woff_path = STATIC_DIR / "fonts" / "fontawesome-webfont.woff"
  #  return static_re(woff_path,"font/woff")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path('Resume.html', resume),
    path('Thoughts.html',thoughts),
    path('index.html', view),
   # path('css/bootstrap.min.css', bootstrap),
   # path('css/hero-slider-style.css', hero),
   # path('css/magnific-popup.css', magn),
   # path('css/tooplate-style.css', toop),
   # path('css/font-awesome.min.css', awesome),
   # path('assets/gBAs.jpg',img),
    #path('favicon.ico',ico),
    #path('fonts/fontawesome-webfont.woff2', woff2),
    #path('fonts/fontawesome-webfont.woff', woff),
    #path('fonts/fontawesome-webfont.ttf', ttf),
    #path('js/bootstrap.min.js', jsbootstrap),
    #path('js/hero-slider-main.js',jshero),
    #path('js/jquery.magnific-popup.min.js',jsmag),
    #path('js/jquery-1.11.3.min.js',jsjquery),
    #path('fontawesome-webfont.svg',svg),
    #path('fonts/fontawesome-webfont.eot',eot),
    #path('fonts/FontAwesome.otf',otf),
]



#def view(r, f=static_re):
 #   return f(file="index.html")#так код работает быстрее тут не тратиться время на поиск имени функ при ее вызове
#но эт все равно копейки (связь с именем установ при синтак дереве поэтому не тратиться время на  ее поиск )
     #render(r,"index.html")