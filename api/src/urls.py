from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token

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
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    url('api/swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('api/swagger/$', schema_view.with_ui('swagger',
                                             cache_timeout=0), name='schema-swagger-ui'),
    url('api/redoc/$', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
    path('api/auth/login', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
