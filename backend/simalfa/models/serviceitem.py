from django.db import models
from abstracts import EntityCommonAbstract
from models.tenant import Tenant 

class ServiceItem(EntityCommonAbstract):
    code = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=765, blank=False)
    process = models.CharField(max_length=1, blank=False) #Definir enum ou valor
    rubric = models.CharField(max_length=4000, blank=False)
    application = models.CharField(max_length=4000, blank=False)
    tenant = models.ManyToManyField(Tenant)
    #formula_lcl bigint NOT NULL,  verificar como funcionar
    #formula_fcl bigint NOT NULL,  verificar como funcionar