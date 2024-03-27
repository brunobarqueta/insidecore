from django.urls import path
from simulation.views import GetServicesItemsForTypeView, GenerateView, GetView

urlpatterns = [
    path('service-items', GetServicesItemsForTypeView.as_view(), name='service-items-for-type-get'),
    path('generate', GenerateView.as_view(), name='simulation-generate'),
    path('get/<str:email>/', GetView.as_view(), name='simulation-get'),
]