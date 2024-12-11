from django.urls import path
from .views import ViajesListView, ViajesCreateView, ViajesUpdateView, ViajesDeleteView
from . import views
urlpatterns = [
    path('', ViajesListView.as_view(), name='viajes_list'),             # Listar viajes
    path('nuevo/', ViajesCreateView.as_view(), name='viajes_create'),   # Crear viaje
    path('editar/<int:pk>/', ViajesUpdateView.as_view(), name='viajes_update'),  # Actualizar viaje
    path('eliminar/<int:pk>/', ViajesDeleteView.as_view(), name='viajes_delete'), # Eliminar viaje

    path('viaje/<int:viaje_id>/reservar/', views.crear_reserva, name='crear_reserva'),
    path('reserva/<int:reserva_id>/pagar/', views.pagar_reserva, name='pagar_reserva'),
    path('reserva/<int:reserva_id>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),
]
