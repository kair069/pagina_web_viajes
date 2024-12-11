# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

# # Formulario de Registro
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_number = forms.CharField(max_length=15, required=False)
#     address = forms.CharField(widget=forms.Textarea, required=False)

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'validate'}))
    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

    # Opcional: Validaciones adicionales de campos
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email