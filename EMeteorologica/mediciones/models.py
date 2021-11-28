from django.db import models
from django.conf import settings

# Create your models here.

class Medicion(models.Model):
    Temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    Luz = models.IntegerField()
    Humedad = models.IntegerField()
    Fecha = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

