from django.contrib import admin
from .models import Servicios

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# REGISTROS:
admin.site.register(Servicios, ServicioAdmin)
