from django.contrib import admin
from clientes.models import clientes

@admin.register(clientes)
class clienteAdmin(admin.ModelAdmin):
    list_display = ['nome','contactado','foi_contactado']

# Register your models here.
