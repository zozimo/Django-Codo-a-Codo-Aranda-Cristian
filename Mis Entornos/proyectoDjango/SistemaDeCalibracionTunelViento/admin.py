from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clientes, Articulos, Pedidos

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","direccion","telefono",)
    search_fields=("nombre","telefono",)
    list_filter=("nombre",)

admin.site.register(Clientes, ClienteAdmin)

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre","seccion","precio")
    search_fields=("seccion",)
    list_filter=("nombre","seccion","precio")
admin.site.register(Articulos, ArticuloAdmin)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero","fecha","entregado")
    list_filter=("fecha",)

admin.site.register(Pedidos, PedidosAdmin)
