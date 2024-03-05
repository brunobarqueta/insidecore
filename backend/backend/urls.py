# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver, URLPattern
from rest_framework.decorators import api_view
from rest_framework.response import Response

url = 'http://127.0.0.1:8000'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("logins.deprecated.urls")),
    path('login/api/v1/', include("logins.urls")),
    path('simalfa/api/v1/', include("simalfa.urls"))
]

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

@api_view(['GET'])
def get_routes(request):
    return Response(routes)

@api_view(['GET'])
def get_routes_depreciated(request):
    return Response(routes_depreciated)
            
urlpatterns.append(path('', get_routes))
urlpatterns.append(path('depreciated/', get_routes_depreciated))