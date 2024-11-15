from django.contrib import admin
from .models import Seccion, ImagenSeccion, Horario

class ImagenSeccionInline(admin.TabularInline):
    model = ImagenSeccion
    extra = 1
    fields = ['imagen', 'titulo', 'pie_foto']
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="100" height="100" style="object-fit: cover;"/>'
        return "No Image"
    preview.allow_tags = True
    preview.short_description = "Vista previa"

class SeccionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'orden']
    inlines = [ImagenSeccionInline]

# Registrar el modelo en el admin
admin.site.register(Seccion, SeccionAdmin)

class HorarioAdmin(admin.ModelAdmin):
    list_display = ('dia', 'actividad', 'hora_inicio', 'hora_fin')
    list_filter = ('dia',)
    search_fields = ('actividad',)

admin.site.register(Horario, HorarioAdmin)

from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido']
    list_filter = ['fecha_publicacion']
