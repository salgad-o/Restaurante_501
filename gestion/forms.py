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


from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cargo', 'telefono', 'correo']


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero_mesa', 'capacidad', 'estado_mesa']
        widgets = {
            'numero_mesa': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'capacidad': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'estado_mesa': forms.Select(attrs={'class': 'input-estilo'}),
        }

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio', 'categoria', 'disponible']
        widgets = {
            'nombre_plato': forms.TextInput(attrs={'class': 'input-estilo'}),
            'descripcion': forms.Textarea(attrs={'class': 'input-estilo', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'categoria': forms.TextInput(attrs={'class': 'input-estilo'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'checkbox-estilo'}),
        }

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'empleado', 'mesa', 'estado_orden']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'input-estilo'}),
            'empleado': forms.Select(attrs={'class': 'input-estilo'}),
            'mesa': forms.Select(attrs={'class': 'input-estilo'}),
            'estado_orden': forms.Select(attrs={'class': 'input-estilo'}),
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['orden', 'subtotal', 'impuesto', 'total_factura', 'metodo_pago']
        widgets = {
            'orden': forms.Select(attrs={'class': 'input-estilo'}),
            'subtotal': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'impuesto': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'total_factura': forms.NumberInput(attrs={'class': 'input-estilo'}),
            'metodo_pago': forms.Select(attrs={'class': 'input-estilo'}),
        }