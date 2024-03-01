from django.db import models

class ActiveBaseAbstract(models.Model):
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True
    
class EntityCommonAbstract(ActiveBaseAbstract, models.Model):
    id = models.AutoField(primary_key=True)
    class Meta:
        abstract = True
    