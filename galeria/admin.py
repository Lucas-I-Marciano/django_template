from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.

class FotografiaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fotografia, FotografiaAdmin)