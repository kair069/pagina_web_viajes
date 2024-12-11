# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# views.py

# Vista de Registro
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirige a la página 'home' (asegúrate de que 'home' esté en las URLs)
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Iniciar sesión con el usuario autenticado
            return redirect('viajes_list')  # Redirige a la página de lista de viajes
        else:
            # Si el formulario no es válido, mostramos los errores
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})



# Vista para la página de inicio (home)
def home(request):
    return render(request, 'home.html')