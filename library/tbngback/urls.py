from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('members.urls')),
]
