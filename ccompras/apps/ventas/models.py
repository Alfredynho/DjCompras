from __future__ import unicode_literals

from django.db import models

# Create your models here.
class cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	status = models.BooleanField(default=True)


class producto(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status = models.BooleanField(default=True)