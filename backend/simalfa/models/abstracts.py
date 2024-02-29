from django.db import models

class ActiveBaseAbstract(models.Model):
    active = models.BooleanField(default=True)
    
class EntityCommonAbstract(ActiveBaseAbstract):
    id = models.AutoField(primary_key=True)