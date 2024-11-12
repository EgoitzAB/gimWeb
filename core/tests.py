from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Seccion, ImagenSeccion
from PIL import Image
import io
import os
import re


class SeccionModelTest(TestCase):
    def test_seccion_creation_and_ordering(self):
        # Crear instancias de `Seccion`
        seccion1 = Seccion.objects.create(titulo="Primera Sección", contenido="Contenido 1", orden=1)
        seccion2 = Seccion.objects.create(titulo="Segunda Sección", contenido="Contenido 2", orden=2)
        
        # Verificar el orden de las secciones
        secciones = Seccion.objects.all()
        self.assertEqual(secciones[0], seccion1)
        self.assertEqual(secciones[1], seccion2)

    def test_seccion_str_method(self):
        seccion = Seccion.objects.create(titulo="Título de Prueba", contenido="Contenido de prueba", orden=1)
        self.assertEqual(str(seccion), "Título de Prueba")

class ImagenSeccionModelTest(TestCase):
    def setUp(self):
        # Crear una instancia de `Seccion` para asociar con `ImagenSeccion`
        self.seccion = Seccion.objects.create(titulo="Sección de Prueba", contenido="Contenido", orden=1)

    def create_image_file(self):
        # Crear una imagen en memoria para subirla
        image = Image.new('RGB', (100, 100), color='red')
        image_file = io.BytesIO()
        image.save(image_file, format='JPEG')
        image_file.seek(0)
        return SimpleUploadedFile("test_image.jpg", image_file.read(), content_type="image/jpeg")

    def test_image_conversion_to_avif(self):
        # Crear una imagen de prueba en memoria
        imagen_seccion = ImagenSeccion.objects.create(
            seccion=self.seccion,
            imagen=self.create_image_file(),
            titulo="Imagen de Prueba",
            pie_foto="Pie de foto de prueba"
        )

        # Verificar que la imagen fue convertida a `.avif`
        self.assertTrue(imagen_seccion.imagen.name.endswith('.avif'))

        # Verificar que el archivo .avif existe en el sistema de archivos
        avif_image_path = imagen_seccion.imagen.path
        self.assertTrue(avif_image_path.endswith('.avif'))

        # Limpiar archivos temporales
        os.remove(avif_image_path)

    def test_image_metadata_removal(self):
        # Crear una imagen con metadatos EXIF
        exif_data = b"Exif\x00\x00" + b"\x00" * 100
        image = Image.new('RGB', (100, 100), color='blue')
        image.info['exif'] = exif_data

        image_file = io.BytesIO()
        image.save(image_file, format='JPEG')
        image_file.seek(0)

        imagen_seccion = ImagenSeccion.objects.create(
            seccion=self.seccion,
            imagen=SimpleUploadedFile("test_image_with_exif.jpg", image_file.read(), content_type="image/jpeg")
        )

        # Verificar que la imagen fue convertida a .avif
        avif_image_path = imagen_seccion.imagen.path
        self.assertTrue(avif_image_path.endswith('.avif'))

        # Cargar la imagen .avif y verificar que no contiene datos EXIF
        with Image.open(avif_image_path) as avif_img:
            exif_data = avif_img.getexif()
            # Aceptamos tanto None como un diccionario vacío {}
            self.assertTrue(exif_data is None or exif_data == {})

        # Limpiar archivos temporales
        os.remove(avif_image_path)

    def tearDown(self):
        # Opcionalmente, puedes realizar limpieza manual si es necesario
        # Aunque Django maneja la limpieza de los objetos automáticamente.
        pass


class BaseHtmlTest(TestCase):
    def test_base_html_structure(self):
        # Asegurarse de que la página principal cargue correctamente
        response = self.client.get(reverse('home'))

        # Verificar que los elementos clave existan en la plantilla base
        self.assertContains(response, '<header>')
        
        # Ajustar la expresión regular para coincidir con <nav> y cualquier clase que contenga 'navbar'
        self.assertRegex(response.content.decode(), r'<nav[^>]*class="[^"]*navbar[^"]*"[^>]*>')

        self.assertContains(response, '<footer>')



class NavbarTest(TestCase):
    def test_navbar_links(self):
        # Verificar que el enlace a la página de inicio está en el navbar
        response = self.client.get(reverse('home'))  # Ajusta 'home' al nombre de tu URL
        
        # Asegúrate de que el enlace de 'Inicio' está presente
        self.assertContains(response, 'href="/"')
        
        # Si tienes otros enlaces en la barra de navegación, comprueba si están presentes
        self.assertContains(response, 'href="/quienes-somos/"')
        self.assertContains(response, 'href="/contacto/"')
        self.assertContains(response, 'href="/actividades/"')
        self.assertContains(response, 'href="/instalaciones/"')
        self.assertContains(response, 'href="/horarios/"')


class FooterTest(TestCase):
    def test_footer(self):
        # Verificar que el pie de página se muestre correctamente
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<footer>')
        self.assertContains(response, '© 2024')  # Ajusta este texto a tu pie de página

class ImageLoadTest(TestCase):
    def test_images_in_navbar(self):
        # Verifica que el logo o imagen de la barra de navegación se cargue correctamente
        response = self.client.get(reverse('home'))  # Ajusta 'home' al nombre de tu URL
        self.assertContains(response, 'src="/static/images/logo.png"')  # Cambia la ruta según tu configuración

class TemplateTest(TestCase):
    def test_base_template_inclusion(self):
        # Verifica que la plantilla base está siendo utilizada
        response = self.client.get(reverse('home'))  # Ajusta 'home' al nombre de tu URL
        self.assertTemplateUsed(response, 'pages/base.html')

    def test_navbar_template_inclusion(self):
        # Verifica que el navbar está siendo incluido correctamente
        response = self.client.get(reverse('home'))
        
        # Expresión regular para coincidir con <nav> y clase 'navbar'
        self.assertRegex(response.content.decode(), r'<nav[^>]*class="[^"]*navbar[^"]*"[^>]*>')


class BrokenLinkTest(TestCase):
    def test_broken_links(self):
        response = self.client.get(reverse('home'))
        # Verifica que no haya enlaces rotos en la página
        self.assertNotContains(response, '404 Not Found')


class FooterViewTests(TestCase):
    
    def test_footer_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
        # Verifica que el footer tiene la sección de contacto
        self.assertContains(response, "Dónde nos puedes encontrar")
        self.assertContains(response, "Calle Rodríguez Fabrés, 23 bajo")
        self.assertContains(response, "Telefono: 923241535 - 652928976")
        
        # Verifica que el footer tiene los enlaces de navegación
        self.assertContains(response, "Principal")
        self.assertContains(response, "Actividades")
        self.assertContains(response, "Horarios")
        self.assertContains(response, "Equipo")
        
        # Verifica que el footer tiene el enlace a la política de privacidad
        self.assertContains(response, "Condiciones de privacidad")


    def test_footer_links(self):
        response = self.client.get(reverse('home'))
        
        # Enlace de formulario de contacto
        self.assertContains(response, 'href="https://gimnasiosantamonica.com/contacto/"')
        
        # Enlace a la política de privacidad
        self.assertContains(response, 'href="https://gimnasiosantamonica.com/politica-privacidad"')
        
        # Enlaces de navegación
        self.assertContains(response, 'href="https://gimnasiosantamonica.com/actividades/"')
        self.assertContains(response, 'href="https://gimnasiosantamonica.com/horarios/"')
        self.assertContains(response, 'href="https://gimnasiosantamonica.com/equipo/"')
