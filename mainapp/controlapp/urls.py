from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_fechas, name='index_fechas'),
    path('scanning', views.scanning, name='scanning'),
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('vencimientos', views.vencimientos, name='vencimientos'),
    path('agregar_fecha/<int:id_producto>', views.agregar_fecha, name='agregar_fecha'),
    path('modificar_producto/<int:id_producto>', views.modificar_producto, name='modificar_producto'),
    path('listado_productos', views.listado_productos, name='listado_productos'),
    path('elimimar_fecha/<int:id_fecha>', views.eliminar_fecha, name='eliminar_fecha'),
    path('eliminar_producto/<int:id_producto>', views.eliminar_producto, name='eliminar_producto'),
]