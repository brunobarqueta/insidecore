from django.urls import path
from simulation.views import GetServicesItemsForType

urlpatterns = [
    path('service-items', GetServicesItemsForType.as_view(), name='service-items-for-type-get'),
]