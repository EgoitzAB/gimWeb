from django.db import models
from PIL import Image
import os
import pillow_avif

# Create your models here.
class Seccion(models.Model):
    titulo = models.CharField(max_length=300)
    contenido = models.TextField()
    orden = models.PositiveIntegerField()
    publicado = models.BooleanField(default=False)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.titulo


class ImagenSeccion(models.Model):
    seccion = models.ForeignKey(Seccion, related_name="imagenes", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagen_seccion/")
    titulo = models.CharField(max_length=150, blank=True, null=True)
    pie_foto = models.CharField(max_length=150, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.imagen:
            self.convert_image_to_avif()
    
    def convert_image_to_avif(self):
        ruta_original_imagen = self.imagen.path
        avif_imagen_path = os.path.splitext(ruta_original_imagen)[0] + ".avif"

        with Image.open(ruta_original_imagen) as img:
            img = img.convert("RGB")
            img.save(avif_imagen_path, format="AVIF", exif=None)
        
        self.imagen.name = os.path.splitext(self.imagen.name)[0] + ".avif"
        super().save()

class Horario(models.Model):
    DIA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]
    
    dia = models.CharField(max_length=10, choices=DIA_CHOICES)
    actividad = models.CharField(max_length=100)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.dia} - {self.actividad} ({self.hora_inicio} - {self.hora_fin})"
