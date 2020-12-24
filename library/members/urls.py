from django.conf import settings, urls
from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import obtain_auth_token

from members import views


def get_url_scheme():
    if settings.DEBUG:
        return 'http://localhost:8000/api/'


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test descricao",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vdegaspari.vm@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    url=get_url_scheme(),
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()

router.register(r'member', views.MembersViewSet)
