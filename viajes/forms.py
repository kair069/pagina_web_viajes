from django import forms
from .models import Viajes

class ViajesForm(forms.ModelForm):
    class Meta:
        model = Viajes
        fields = ['destino', 'fecha_salida', 'fecha_regreso', 'precio', 'descripcion', 'imagen']
        widgets = {
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'fecha_regreso': forms.DateInput(attrs={'type': 'date'}),
        }


#········································

# forms.py de la app 'viajes'
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['viaje', 'usuario', 'estado', 'precio_pagado']
        widgets = {
            'viaje': forms.Select(),
            'usuario': forms.Select(),
            'estado': forms.Select(choices=Reserva._meta.get_field('estado').choices),
        }

class PagoReservaForm(forms.Form):
    cantidad = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
