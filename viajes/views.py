from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Viajes
from .forms import ViajesForm

from django.views.generic import ListView
from django.db.models import Q

class ViajesListView(ListView):
    model = Viajes
    template_name = 'viajes/viajes_list.html'
    context_object_name = 'viajes'
    paginate_by = 6  # Mostrará 6 tarjetas por página

    def get_queryset(self):
        # Filtrar por destino o descripción
        query = self.request.GET.get('q', '')
        object_list = Viajes.objects.filter(
            Q(destino__icontains=query) | Q(descripcion__icontains=query)
        ) if query else Viajes.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')  # Incluye el término de búsqueda
        return context


# Crear un nuevo viaje (CREATE)
class ViajesCreateView(CreateView):
    model = Viajes
    form_class = ViajesForm
    template_name = 'viajes/viajes_form.html'
    success_url = reverse_lazy('viajes_list')

# Actualizar un viaje existente (UPDATE)
class ViajesUpdateView(UpdateView):
    model = Viajes
    form_class = ViajesForm
    template_name = 'viajes/viajes_form.html'
    success_url = reverse_lazy('viajes_list')

# Eliminar un viaje (DELETE)
class ViajesDeleteView(DeleteView):
    model = Viajes
    template_name = 'viajes/viajes_confirm_delete.html'
    success_url = reverse_lazy('viajes_list')




####### reservas

# views.py de la app 'viajes'
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Reserva, Viajes
from .forms import ReservaForm, PagoReservaForm

# Vista para crear una nueva reserva
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Viajes, Reserva
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required
@login_required
def crear_reserva(request, viaje_id):
    viaje = get_object_or_404(Viajes, id=viaje_id)

    # Verificar si el usuario ya tiene una reserva para este viaje
    if Reserva.objects.filter(viaje=viaje, usuario=request.user, estado='pendiente').exists():
        messages.error(request, "Ya tienes una reserva pendiente para este viaje.")
        return redirect('viajes_list')  # Redirigir a la lista de viajes si ya hay una reserva pendiente
    
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user  # Asignar el usuario logueado como el propietario de la reserva
            reserva.save()
            messages.success(request, f"Reserva creada con éxito para el viaje a {viaje.destino}!")
            return redirect('viajes_list')  # Redirigir a la lista de viajes o a la página de detalles de la reserva
    else:
        form = ReservaForm(initial={'viaje': viaje})

    return render(request, 'viajes/crear_reserva.html', {'form': form, 'viaje': viaje})


# Vista para pagar una reserva
@login_required
def pagar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    
    if reserva.estado == 'pagado':
        return HttpResponse("La reserva ya ha sido pagada", status=400)
    
    if request.method == 'POST':
        form = PagoReservaForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            if reserva.pagar_reserva(cantidad):
                return redirect('viajes_list')  # Redirigir al listado de viajes tras el pago
            else:
                return HttpResponse("La cantidad es insuficiente para pagar la reserva", status=400)
    else:
        form = PagoReservaForm()

    return render(request, 'viajes/pagar_reserva.html', {'form': form, 'reserva': reserva})

# Vista para eliminar una reserva
@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    
    if request.method == 'POST':
        reserva.delete()
        return redirect('viajes_list')  # Redirigir a la lista de viajes después de eliminar la reserva

    return render(request, 'viajes/eliminar_reserva.html', {'reserva': reserva})

