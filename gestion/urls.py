from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [

    path(
        'login/',
        LoginView.as_view(
            template_name='gestion/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'registro/',
        views.registro,
        name='registro'
    ),

    path('', views.inicio, name='inicio'),

    path(
        'clientes/crear/',
        views.crear_cliente,
        name='crear_cliente'
    ),

    path(
        'clientes/editar/<int:id>/',
        views.editar_cliente,
        name='editar_cliente'
    ),

    path(
        'clientes/eliminar/<int:id>/',
        views.eliminar_cliente,
        name='eliminar_cliente'
    ),

    path(
        'clientes/',
        views.lista_clientes,
        name='lista_clientes'
    ),

    path(
        'empleados/',
        views.lista_empleados,
        name='lista_empleados'
    ),

    path(
        'mesas/',
        views.lista_mesas,
        name='lista_mesas'
    ),

    path(
        'platos/',
        views.lista_platos,
        name='lista_platos'
    ),

    path(
        'ordenes/',
        views.lista_ordenes,
        name='lista_ordenes'
    ),

    path(
        'facturas/',
        views.lista_facturas,
        name='lista_facturas'
    ),

    path(
        'empleados/crear/',
        views.crear_empleado,
        name='crear_empleado'
    ),
    
    path(
        'empleados/editar/<int:id>/',
        views.editar_empleado,
        name='editar_empleado'
    ),

    path(
        'empleados/eliminar/<int:id>/',
        views.eliminar_empleado,
        name='eliminar_empleado'
    ),

    path(
        'mesas/crear/', 
        views.crear_mesa, 
        name='crear_mesa'
    ),

    path(
        'mesas/editar/<int:id>/',
        views.editar_mesa, 
        name='editar_mesa'
    ),

    path(
        'mesas/eliminar/<int:id>/', 
        views.eliminar_mesa, 
        name='eliminar_mesa'
    ),

    path(
        'platos/crear/',
        views.crear_plato, 
        name='crear_plato'
    ),

    path(
        'platos/editar/<int:id>/', 
        views.editar_plato, 
        name='editar_plato'
    ),

    path(
        'platos/eliminar/<int:id>/',
        views.eliminar_plato, 
        name='eliminar_plato'
    ),

    path(
        'ordenes/crear/', 
        views.crear_orden, 
        name='crear_orden'
    ),

    path(
        'ordenes/editar/<int:id>/', 
        views.editar_orden, 
        name='editar_orden'
    ),

    path(
        'ordenes/eliminar/<int:id>/', 
        views.eliminar_orden, 
        name='eliminar_orden'
    ),

]