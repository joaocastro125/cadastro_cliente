from django.db import models

# Create your models here.

class clientes(models.Model):


  nome = models.CharField(max_length=64)
  contactado = models.DateTimeField(auto_now=True)
  foi_contactado = models.BooleanField(default=False)
