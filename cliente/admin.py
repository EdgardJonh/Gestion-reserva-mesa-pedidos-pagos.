from django.contrib import admin
from .models import Cliente
# Register your models here.
# Configuración de Cliente
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'direccion')
    search_fields = ('nombre', 'correo')
    list_filter = ('nombre',)