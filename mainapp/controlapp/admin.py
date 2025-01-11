from django.contrib import admin
from .models import Producto, Tipo, Fecha

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'subgrupo', 'dias_retiro')
    list_filter = ('grupo',)
    search_fields = ('subgrupo',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'scanning', 'tipo')
    list_filter = ('tipo__grupo',)
    search_fields = ('nombre', 'scanning')

@admin.register(Fecha)
class FechaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'fecha')
    list_filter = ('producto__tipo__grupo',)
    search_fields = ('producto__nombre', 'fecha')