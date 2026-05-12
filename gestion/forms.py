from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):

    email = forms.EmailField(
        help_text=''
    )

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        help_text=''
    )

    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        help_text=''
    )

    username = forms.CharField(
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from .models import Cliente
from .models import Empleado


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cargo', 'telefono', 'correo']