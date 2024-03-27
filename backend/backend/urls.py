from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver, URLPattern
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.generators import OpenAPISchemaGenerator

schema_view = get_schema_view(
   openapi.Info(
      title='App Sim Alfa',
      default_version='v1',
      description="Application for management and simulations of services.",
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/', include("logins.deprecated.urls")),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/api/v1/', include("logins.urls")),
    path('simalfa/api/v1/', include("simalfa.urls")),
    path('simulation/api/v1/', include("simulation.urls")),
]