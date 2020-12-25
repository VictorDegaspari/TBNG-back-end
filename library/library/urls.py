from core.views import GroupViewSet, MembersViewSet, UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'members', MembersViewSet, basename="Members")


def get_url_scheme():
    if settings.DEBUG:
        return 'http://localhost:8000/api/'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
