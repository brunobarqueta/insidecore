from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):       
    username = models.CharField(("username"),max_length=150, blank=True)
    email = models.EmailField(("email address"), unique=True,
                help_text=("Obrigatório. 50 caracteres ou menos. Somente letras, dígitos e @/./+/-/_."))
    fullname = models.CharField(max_length=255, help_text=("Obrigatório."))
    cpf = models.CharField(max_length=14, help_text=('Obrigatório. Informe o cpf no seguinte formato: XXX.XXX.XXX-XX'))
    phone = models.CharField(max_length=20, help_text=("Obrigatório."))
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    8
    def __str__(self):
        return self.fullname