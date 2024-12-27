from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ["nome", "legenda", "descricao"]
    empty_value_display = "-???-"

admin.site.register(Fotografia, FotografiaAdmin)