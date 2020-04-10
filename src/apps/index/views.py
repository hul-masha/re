from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def view(request: HttpRequest) -> HttpResponse: # это хтнты, валидация типов (то есть их соответствие типов)
    return render(request, "index/index.html")        # питон приводит значение к типу прямо на месте тк динамич язык