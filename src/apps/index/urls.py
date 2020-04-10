from django.urls import path
from apps.index.apps import IndexConfig
from apps.index.views import view

app_name=IndexConfig.name

urlpatterns = [
    path('', view,name='index'),
]