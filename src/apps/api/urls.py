from django.conf import settings
from django.urls import include
from django.urls import path
from django.urls import re_path
#from drf_yasg import openapi
#from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

from apps.api.views import ObtainAuthToken

'''# TODO: move to views
schema_view = get_schema_view(
    openapi.Info(
        title="Obliviscor API",
        default_version="v1",
        description="The API is the API",
        terms_of_service="TBD",
        contact=openapi.Contact(email=settings.EMAIL_FROM),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)'''

urlpatterns = [
    path("", include("apps.api.impl.urls")),
    path("obtain_auth_token/", ObtainAuthToken.as_view(), name="obtain_auth_token"),

]