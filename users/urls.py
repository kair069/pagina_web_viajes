from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),  # Aquí se crea la URL para 'home'
    
    # Agrega más rutas según sea necesario
]