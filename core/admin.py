from django.contrib import admin
from .models import Seccion, ImagenSeccion

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
