from django.db import models

# Create your models here.

class Auditoria(models.Model):
    """
    Description: Model Auditoria
    """
    operacion = models.CharField(max_length=50)
    fechahora = models.DateTimeField()
    usuario = models.CharField(max_length=50)
    