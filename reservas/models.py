from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_disponible = models.DateField()
    duracion_dias = models.PositiveIntegerField()  # Duración en días

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text="Número en formato internacional. Ejemplo: +51987654321"
    )

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="reservas")
    fecha_reserva = models.DateTimeField(default=now)
    estado = models.CharField(
        max_length=20,
        choices=[("pendiente", "Pendiente"), ("confirmada", "Confirmada"), ("cancelada", "Cancelada")],
        default="pendiente"
    )

    def __str__(self):
        return f"Reserva de {self.cliente} para {self.destino}"


class Boleta(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, related_name="boleta")
    fecha_emision = models.DateTimeField(default=now)

    @property
    def total(self):
        return self.reserva.destino.precio

    def __str__(self):
        return f"Boleta #{self.id} - {self.reserva.cliente}"
