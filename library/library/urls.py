from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.core.urls')),
]
