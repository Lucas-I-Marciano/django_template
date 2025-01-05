from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "legenda", "descricao", "publicado"]
    empty_value_display = "-???-"
    list_display_links = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["categoria"]
    list_per_page = 10
    list_editable = ["publicado"]

admin.site.register(Fotografia, FotografiaAdmin)