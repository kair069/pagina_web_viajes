# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario Personalizado
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Evitar conflictos de related_name con los grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Cambiar el related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Cambiar el related_name
        blank=True
    )

    def __str__(self):
        return self.username


# Modelo de Perfil de Usuario
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
