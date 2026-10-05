from django.contrib import admin
from .models import Piloto

@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'escuderia', 'edad', 'anio_debut', 'nacionalidad', 'usuario')
    list_filter = ('categoria', 'escuderia', 'nacionalidad')
    search_fields = ('nombre', 'escuderia', 'nacionalidad')
