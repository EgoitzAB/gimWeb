# GimWeb - Web del Gimnasio

Este proyecto es una aplicación web basada en Django para la web de un gimnasio. Las imágenes subidas son convertidas al formato `.avif` para optimizar su almacenamiento y se les eliminan los metadatos EXIF.

## Requisitos

- Python 3.x
- Django 4.x
- Pillow (con soporte para AVIF)
- [pillow-avif-plugin](https://github.com/c0re100/pillow-avif-plugin) para habilitar el soporte de AVIF en Pillow

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone <url_del_repositorio>
    cd gimweb
    ```

2. **Crear y activar un entorno virtual**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa venv\Scripts\activate
    ```

3. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Instalar el soporte para AVIF**:
    ```bash
    pip install pillow-avif-plugin
    ```

5. **Migrar la base de datos**:
    ```bash
    python manage.py migrate
    ```

## Funcionalidades

### Secciones del gimnasio
El proyecto permite gestionar `Seccion` que pueden tener un título, contenido y un orden específico. Las secciones están ordenadas de acuerdo al campo `orden`.

### Imágenes de las secciones
Cada `Seccion` puede tener varias imágenes asociadas (`ImagenSeccion`). Las imágenes subidas son automáticamente convertidas al formato `.avif` para optimizar su tamaño y mejorar el rendimiento del sitio.

### Eliminación de metadatos EXIF
Las imágenes subidas tienen sus metadatos EXIF eliminados para proteger la privacidad de los usuarios y reducir el tamaño de las imágenes.

## Ejecución de Pruebas

Para ejecutar los tests unitarios de Django:

1. **Ejecutar las pruebas**:
    ```bash
    python manage.py test
    ```

## Tests Realizados

- **Creación y orden de secciones**: Se verifica que las secciones se ordenen correctamente en la base de datos.
- **Conversión de imágenes a AVIF**: Se asegura de que las imágenes subidas sean convertidas al formato `.avif`.
- **Eliminación de metadatos EXIF**: Se comprueba que los metadatos EXIF de las imágenes sean eliminados correctamente durante la conversión.

## Documentación adicional

Para más detalles sobre el soporte AVIF y la instalación de dependencias, puedes consultar:

- [pillow-avif-plugin](https://github.com/c0re100/pillow-avif-plugin)
- [Pillow](https://pillow.readthedocs.io/)

## Licencia

Este proyecto está bajo la Licencia GPVL3. Consulta el archivo `LICENSE` para más detalles.
