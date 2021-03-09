from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from apps.core import views

router = routers.DefaultRouter()

router.register(r'members', views.MembersViewSet, basename="Members")


urlpatterns = [
    path('', include(router.urls)),
]
