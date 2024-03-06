# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver, URLPattern
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/', include("logins.deprecated.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('login/api/v1/', include("logins.urls")),
    path('simalfa/api/v1/', include("simalfa.urls"))
]

url = 'http://127.0.0.1:8000'
def get_routes_api(url_patterns, prefix='', routes:list = [], is_depreciated = False, routes_depreciate:list = []):
    for pattern in url_patterns:
        if isinstance(pattern, URLResolver):
            if pattern.pattern._route == 'admin/':
                continue
            is_depreciated = pattern.urlconf_module.__name__.__contains__('deprecated')
            get_routes_api(pattern.url_patterns, prefix + pattern.pattern._route, routes, is_depreciated, routes_depreciate)
        elif isinstance(pattern, URLPattern):
            path = f'/{prefix}{pattern.pattern._route}'
            if is_depreciated:
                routes_depreciate.append(url+path)
            else:
                routes.append(url+path)
    routes.sort(key=str.lower)
    routes_depreciate.sort(key=str.lower)
    return (routes, routes_depreciate)

(routes, routes_depreciated) = get_routes_api(urlpatterns)
routes.insert(0, f'{url}/depreciated')

@swagger_auto_schema(auto_schema=None, method='GET')
@api_view(['GET'])
def get_routes(request):
    return Response(routes)
@swagger_auto_schema(auto_schema=None, method='GET')
@api_view(['GET'])
def get_routes_depreciated(request):
    return Response(routes_depreciated)
            
urlpatterns.append(path('', get_routes))
urlpatterns.append(path('depreciated/', get_routes_depreciated))