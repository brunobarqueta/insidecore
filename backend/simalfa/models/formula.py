from django.db import models
from tenant import Tenant
from abstracts import EntityCommonAbstract

class Formula(EntityCommonAbstract):
    description = models.CharField(max_length=255, blank=False)
    expression = models.CharField(max_length=4000, blank=False)
    tenant = models.ManyToManyField(Tenant)