from django.urls import path
from simulation.views import GetServicesItemsForTypeView, GenerateView

urlpatterns = [
    path('service-items', GetServicesItemsForTypeView.as_view(), name='service-items-for-type-get'),
    path('generate', GenerateView.as_view(), name='generate-post'),
]