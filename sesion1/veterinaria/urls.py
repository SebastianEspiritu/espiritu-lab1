from django.urls import path
from . import views

app_name = 'veterinaria'

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
]