from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# REGISTROS:
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)