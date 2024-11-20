from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Seccion, Horario, Noticia
from core.utils import generar_horario


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Secciones ya existentes
        context['secciones'] = Seccion.objects.all()

        # Generar el horario y agregarlo al contexto
        horarios = Horario.objects.all().order_by('dia', 'hora_inicio')
        horarios_data = generar_horario(horarios)
        context.update(horarios_data)
        
        return context


def mostrar_horarios(request):
    horarios = Horario.objects.all().order_by('dia', 'hora_inicio')
    context = generar_horario(horarios)  # Reutilizamos la lógica
    return render(request, 'core/horarios.html', context)

def instalaciones(request):
    # Información estática de la instalación
    instalacion = {
        'nombre': 'Gimnasio Santa Mónica',
        'descripcion': 'Un espacio dedicado al bienestar físico y mental, con equipos de última generación.',
        'direccion': 'Calle Ficticia, 123, Ciudad, País',
        'imagen': 'instalacion_gimnasio.jpg',  # Reemplaza con el nombre de la imagen
    }

    # Obtener todas las noticias
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')

    # Pasamos los datos a la plantilla
    return render(request, 'core/instalaciones.html', {'instalacion': instalacion, 'noticias': noticias})
