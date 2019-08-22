from django.contrib import admin
from .models import Producto, Favorito, Tipo, Oferta, UserProfile, Contacto

class AdministrarModelo(admin.ModelAdmin):
    list_display = ('nombre', 'createdat')
    search_fields = ('nombre', 'createdat')
    date_hierarchy = 'createdat'
    list_filter = ('nombre', 'createdat')

class AdministrarOferta(admin.ModelAdmin):
    list_display = ('porcentajeInt', 'createdat')
    search_fields = ('porcentajeInt', 'createdat')
    date_hierarchy = 'createdat'
    list_filter = ('porcentajeInt', 'createdat')

class AdministrarProducto(admin.ModelAdmin):
    list_display = ('nombre', 'tipo','createdat')
    search_fields = ('nombre', 'tipo','createdat')
    date_hierarchy = 'createdat'
    list_filter = ('nombre', 'tipo','createdat')

class AdministrarFavorito(admin.ModelAdmin):
    list_display = ('user','createdat')
    search_fields = ('user','createdat')
    date_hierarchy = 'createdat'
    list_filter = ('user','createdat')

class AdministrarUserProfile(admin.ModelAdmin):
    list_display = ('pp','user')


class AdministrarContacto(admin.ModelAdmin):
    list_display = ('nombre','correo','telefono','asunto','mensaje','createdat')
    search_fields = ('nombre','createdat')
    date_hierarchy = 'createdat'
    list_filter = ('nombre','createdat')

admin.site.register(Tipo, AdministrarModelo)
admin.site.register(Producto, AdministrarProducto)
admin.site.register(Favorito, AdministrarFavorito)
admin.site.register(Oferta, AdministrarOferta)
admin.site.register(UserProfile, AdministrarUserProfile)
admin.site.register(Contacto, AdministrarContacto)