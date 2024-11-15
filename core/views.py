from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Seccion, Horario

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['secciones'] = Seccion.objects.all()
        print(context['secciones'])
        return context

def mostrar_horarios(request):
    # Obtener todos los horarios de la base de datos
    horarios = Horario.objects.all().order_by('dia', 'hora_inicio')
    
    # Organizar los horarios por días
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    horarios_por_dia = {dia: [] for dia in dias}
    
    for horario in horarios:
        horarios_por_dia[horario.dia].append(horario)
    
    # Generar la lista de horas
    horas = []
    for h in range(7, 22):  # Desde las 7 AM hasta las 10 PM
        horas.append(f"{h}:00")

    return render(request, 'core/horarios.html', {'horarios_por_dia': horarios_por_dia, 'horas': horas})