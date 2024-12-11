from django.db import models

class Viajes(models.Model):
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.URLField(max_length=300, blank=True, null=True, help_text="URL de una imagen representativa")
    
    def __str__(self):
        return f"{self.destino} ({self.fecha_salida} - {self.fecha_regreso})"
##··············································ultima modificacion
# models.py de la app 'viajes'
from django.db import models
from users.models import CustomUser  # Importa CustomUser correctamente desde la app 'users'
from .models import Viajes  # Importa Viajes como antes

class Reserva(models.Model):
    viaje = models.ForeignKey(Viajes, on_delete=models.CASCADE, related_name="reservas")
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reservas")
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')], default='pendiente')
    precio_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f"Reserva para {self.viaje.destino} por {self.usuario.username} ({self.estado})"
    
    def pagar_reserva(self, cantidad):
        if self.estado == 'pendiente' and cantidad >= self.viaje.precio:
            self.estado = 'pagado'
            self.precio_pagado = cantidad
            self.save()
            return True
        return False
