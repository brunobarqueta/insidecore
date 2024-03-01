from django.db import models
from abstracts import EntityCommonAbstract
from models.tenant import Tenant 
from models.formula import Formula

class ServiceItem(EntityCommonAbstract):
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=50, blank=False)
    rubric = models.CharField(max_length=4000, blank=False)
    application = models.CharField(max_length=4000, blank=False)
    tenant = models.ManyToManyField(Tenant)
    formula_lcl = models.ManyToManyField(Formula)
    formula_fcl =models.ManyToManyField(Formula)