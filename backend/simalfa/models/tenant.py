from django.db import models
from abstracts import ActiveBaseAbstract

class Tenant(ActiveBaseAbstract):
    code = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=765, blank=False)