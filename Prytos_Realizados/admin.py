from django.contrib import admin
from .models import Uso_Edif, Prytos_Realizados

class Uso_Edif_Admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
class Prytos_Realizados_Admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# REGISTROS:
admin.site.register(Uso_Edif, Uso_Edif_Admin)
admin.site.register(Prytos_Realizados, Prytos_Realizados_Admin)