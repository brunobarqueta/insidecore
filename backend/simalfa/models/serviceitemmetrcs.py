from django.db import models
from models.abstracts import EntityCommonAbstract
from models.metrics import Metrics
from backend.simalfa.models.serviceitem import ServiceItem
from models.tenant import Tenant

class ServiceItemMetrics(EntityCommonAbstract):
    value = models.DecimalField(max_digits=25, decimal_places=5)
    service_item = models.ManyToManyField(ServiceItem, null=False)
    metrics = models.ManyToManyField(Metrics, null=False)
    tenant = models.ManyToManyField(Tenant)