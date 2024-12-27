from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "legenda", "descricao"]
    empty_value_display = "-???-"
    list_display_links = ["id", "nome"]
    search_fields = ["nome"]
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)