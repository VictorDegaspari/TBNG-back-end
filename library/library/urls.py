from core.views import GroupViewSet, MembersViewSet, UserViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'members', MembersViewSet, basename="Members")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
