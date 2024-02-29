from django.db import models
from simalfa.enums import TypeService
from tenant import Tenant
from abstracts import EntityCommonAbstract

class Metrics(EntityCommonAbstract):
    STATUS_CHOICES = [
        (TypeService.FCL, 'FCL'),
        (TypeService.LCL, 'LCL'),
        (TypeService.BOTH, 'BOTH')
    ]
    description = models.CharField(max_length=255, blank=False)
    type = models.SmallIntegerField(choices=STATUS_CHOICES) # verificar como functiona
    service = models.CharField(max_length=4000, blank=False)
    tenant = models.ManyToManyField(Tenant)