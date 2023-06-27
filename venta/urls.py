from django.urls import path
from . import views




urlpatterns =[

    path('',views.inicio, name='index'),
    #VISTAS DE INDEX
    path('reclamos', views.reclamoss, name='reclamos'),
    path('carrito', views.carrito, name='carrito'),
    path('cascos', views.cascoss, name='cascos'),
    path('home',views.home, name='home'),
    path('bicicletass', views.bicicletass, name='bicicletass'),
    path('login', views.login, name='login'),
    path('repuesto', views.repuesto, name='repuesto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('json', views.json, name='json'),
    
    #DJANGO
    path('generos',views.lista_genero, name='genero'),
    path('lista_clientes',views.lista_clientes, name='lista_clientes'),
    path('agregar_clientes',views.agregar_clientes, name='clientesAdd'),
    path('clienteindex', views.clienteindex, name='clienteindex'),
    path('eliminar_cliente/<str:pk>',views.eliminar_cliente, name='clientes_del'),
    path('buscar_cliente/<str:pk>',views.buscar_cliente, name='clientes_findEdit'),
    path('actualizar_cliente',views.modificar_cliente, name='clienteUpdate'),

]

