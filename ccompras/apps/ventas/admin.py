from django.contrib import admin
from ccompras.apps.ventas.models import cliente,producto
# Register your models here.
admin.site.register(cliente)
admin.site.register(producto)