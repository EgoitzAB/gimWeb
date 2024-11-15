from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('horarios/', views.mostrar_horarios, name='mostrar_horarios'),
]