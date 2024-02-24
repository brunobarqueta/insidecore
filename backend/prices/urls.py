from django.urls import path
from prices import views

urlpatterns = [
    path('', views.PriceListCreateView.as_view(), name='price-list-create'),
    path('<int:pk>/', views.PriceGetPutDeleteView.as_view(), name='price-get-put-delete')
]