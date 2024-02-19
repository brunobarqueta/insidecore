from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)

    def __str__(self):
        self.user.username