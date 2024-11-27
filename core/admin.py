from django.contrib import admin
from .models import *

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'numero', 'nombre']
    search_fields = ['id', 'numero', 'nombre']
    list_per_page = 10

class ComunaAdmin(admin.ModelAdmin):
    list_display = ['id', 'region', 'nombre']
    search_fields = ['id', 'region', 'nombre']
    list_per_page = 10

class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'comuna', 'nombre']
    search_fields = ['id', 'comuna', 'nombre']
    list_per_page = 10

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'supermercado', 'nombre', 'marca', 'precio', 'descripcion', 'fecha_actualizacion']
    search_fields = ['id', 'supermercado', 'nombre', 'marca', 'precio', 'descripcion', 'fecha_actualizacion']
    list_per_page = 10

class RolAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['id', 'nombre']
    list_per_page = 10

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'calificacion', 'usuario', 'producto']
    search_fields = ['titulo', 'texto', 'calificacion', 'usuario', 'producto']
    list_per_page = 10

class FavoritoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario', 'producto']
    search_fields = ['id','usuario', 'producto']
    list_per_page = 10

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Supermercado, SupermercadoAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Favorito, FavoritoAdmin)
