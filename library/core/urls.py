from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, MembersViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'members', MembersViewSet)
