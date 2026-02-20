from django.contrib import admin
from .models import Boi
from django.utils.html import format_html

@admin.register(Boi)
class BoiAdmin(admin.ModelAdmin):
    list_display = ('brinco', 'raca', 'peso_kg', 'ver_qrcode')
    search_fields = ('brinco', 'nome')
    list_filter = ('raca', 'sexo')
    readonly_fields = ('ver_qrcode_grande',)

    # Mostra uma miniatura na lista
    def ver_qrcode(self, obj):
        if obj.qrcode_img:
            return format_html('<img src="{}" width="50" height="50" />', obj.qrcode_img.url)
        return "-"
    ver_qrcode.short_description = "QR Code"

    # Mostra grande dentro do cadastro
    def ver_qrcode_grande(self, obj):
        if obj.qrcode_img:
            return format_html('<img src="{}" width="200" height="200" />', obj.qrcode_img.url)
        return "-"
    ver_qrcode_grande.short_description = "Visualização do QR Code"