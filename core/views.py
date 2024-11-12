from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Seccion

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['secciones'] = Seccion.objects.all()
        return context
