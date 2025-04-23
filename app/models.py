from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_registro = models.DateField()
    activo = models.BooleanField(default=True)
    etiquetas = models.JSONField(default=list)
