from django.shortcuts import render, redirect
from .models import CITAS_DB
from .forms import CitaForm

def lista_citas(request):
    return render(request, 'veterinaria/lista.html', {'citas': CITAS_DB})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            nueva_cita = {
                'id': len(CITAS_DB) + 1,
                'mascota': form.cleaned_data['mascota'],
                'propietario': form.cleaned_data['propietario'],
                'tipo_atencion': form.cleaned_data['tipo_atencion'],
                'fecha': str(form.cleaned_data['fecha']),
                'hora': str(form.cleaned_data['hora']),
            }
            CITAS_DB.append(nueva_cita)
            return redirect('veterinaria:lista_citas')
    else:
        form = CitaForm()
    
    return render(request, 'veterinaria/formulario.html', {'form': form})