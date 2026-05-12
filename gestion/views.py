from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistroForm, ClienteForm, EmpleadoForm

# Create your views here.
from .forms import RegistroForm, ClienteForm, EmpleadoForm, MesaForm, PlatoForm, OrdenForm
from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura


@login_required
def inicio(request):
    context = {
        'total_clientes': Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas': Mesa.objects.count(),
        'total_platos': Plato.objects.count(),
        'total_ordenes': Orden.objects.count(),
        'total_facturas': Factura.objects.count(),
    }
    return render(request, 'gestion/inicio.html', context)


@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})


@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})


@login_required
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})


@login_required
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})


@login_required
def lista_ordenes(request):
    ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})


@login_required
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})

def registro(request):

    if request.method == 'POST':

        form = RegistroForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('/')

    else:

        form = RegistroForm()

    return render(request, 'gestion/registro.html', {
        'form': form
    })

@login_required
def crear_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/clientes/')

    else:

        form = ClienteForm()

    return render(request, 'gestion/crear_cliente.html', {
        'form': form
    })

@login_required
def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':

        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():

            form.save()

            return redirect('/clientes/')

    else:

        form = ClienteForm(instance=cliente)

    return render(request, 'gestion/editar_cliente.html', {
        'form': form
    })


@login_required
def eliminar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    cliente.delete()

    return redirect('/clientes/')

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')
    else:
        form = EmpleadoForm()
    return render(request, 'gestion/crear_empleado.html', {'form': form})

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('/empleados/')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'gestion/editar_empleado.html', {'form': form})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('/empleados/')
    return render(request, 'gestion/eliminar_empleado.html', {'empleado': empleado})


def crear_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mesas/')
    else:
        form = MesaForm()
    return render(request, 'gestion/crear_mesa.html', {'form': form})

def editar_mesa(request, id):
    mesa = get_object_or_404(Mesa, id=id)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('/mesas/')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'gestion/editar_mesa.html', {'form': form})

def eliminar_mesa(request, id):
    mesa = get_object_or_404(Mesa, id=id)
    if request.method == 'POST':
        mesa.delete()
        return redirect('/mesas/')
    return render(request, 'gestion/eliminar_mesa.html', {'mesa': mesa})

def crear_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/platos/')
    else:
        form = PlatoForm()
    return render(request, 'gestion/crear_plato.html', {'form': form})

def editar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('/platos/')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'gestion/editar_plato.html', {'form': form})

def eliminar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    if request.method == 'POST':
        plato.delete()
        return redirect('/platos/')
    return render(request, 'gestion/eliminar_plato.html', {'plato': plato})

def crear_orden(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ordenes/')
    else:
        form = OrdenForm()
    return render(request, 'gestion/crear_orden.html', {'form': form})

def editar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('/ordenes/')
    else:
        form = OrdenForm(instance=orden)
    return render(request, 'gestion/editar_orden.html', {'form': form})

def eliminar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == 'POST':
        orden.delete()
        return redirect('/ordenes/')
    return render(request, 'gestion/eliminar_orden.html', {'orden': orden})

