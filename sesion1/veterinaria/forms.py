from django import forms

class CitaForm(forms.Form):
    TIPO_ATENCION_CHOICES = [
        ('Consulta General', 'Consulta General'),
        ('Vacunación', 'Vacunación'),
        ('Desparasitación', 'Desparasitación'),
        ('Cirugía', 'Cirugía'),
        ('Baño y Corte', 'Baño y Corte'),
    ]

    mascota = forms.CharField(
        label='Nombre de la Mascota',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Firulais'})
    )
    propietario = forms.CharField(
        label='Nombre del Propietario',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan Pérez'})
    )
    tipo_atencion = forms.ChoiceField(
        label='Tipo de Atención',
        choices=TIPO_ATENCION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    fecha = forms.DateField(
        label='Fecha de la Cita',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    hora = forms.TimeField(
        label='Hora de la Cita',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )