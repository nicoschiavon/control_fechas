from django.shortcuts import render, redirect
from .models import Producto, Fecha, Tipo
from .forms import ProductoForm, FechaForm
from datetime import datetime

# Create your views here.

def index_fechas(request):
    productos = Producto.objects.all()
    fechas = Fecha.objects.all().order_by('fecha')
    today = datetime.now().date()
    fechas_dias = [
        {
            'producto': fecha.producto,
            'fecha': fecha.fecha,
            'id' : fecha.id,
            'dias': ((fecha.fecha - today).days) - fecha.producto.tipo.dias_retiro,
            'retirar': ((fecha.fecha - today).days) - fecha.producto.tipo.dias_retiro <= 0,
            'precio': ((fecha.fecha - today).days) - fecha.producto.tipo.dias_retiro <= 5,
         }
        for fecha in fechas
    ]

    return render(request, 'index.html', {
        'fechas_dias': fechas_dias,
    })


# Se ingresa un scanning si no se encuentra se agrega el producto a la base de datos.
# si ya se encuentra, trae el resto de datos del producto y se pide ingresar la fecha de vencimiento para guardar en el modelo de Fecha

def scanning(request):
    if request.method == 'POST':
        scanning = request.POST.get('scanning')
        producto = Producto.objects.filter(scanning=scanning)
        if producto.exists():
            producto = producto.first()
            return render(request, 'scanning.html', {'producto': producto})
        else:
            return render(request, 'scanning.html', {'scanning': scanning})
    return render(request, 'scanning.html')

def agregar_producto(request):
    if request.method == 'POST':
        form_producto = ProductoForm(request.POST)
        if form_producto.is_valid():
            producto = form_producto.save()
            producto.save()
            return redirect('listado_productos')
    else:
        form_producto = ProductoForm()
    return render(request, 'agregar_producto.html', {'form_producto': form_producto})


def vencimientos(request):
    productos = Producto.objects.all()
    fechas = Fecha.objects.all()
    return render(request, 'vencimientos.html', {'productos': productos, 'fechas': fechas})


#Agregar nueva fecha de vencimiento:
# usando el FormFecha
def agregar_fecha(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        form_fecha = FechaForm(request.POST)
        if form_fecha.is_valid():
            fecha = form_fecha.save(commit=False)
            fecha.producto = producto
            fecha.save()
            return redirect('listado_productos')
    else:
        form_fecha = FechaForm()
    return render(request, 'agregar_fecha.html', {'form_fecha': form_fecha, 'producto': producto})


# vista para modificar los productos
def modificar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        form_producto = ProductoForm(request.POST, instance=producto)
        if form_producto.is_valid():
            form_producto.save()
            return redirect('index_fechas')
    else:
        form_producto = ProductoForm(instance=producto)
    return render(request, 'agregar_producto.html', {'form_producto': form_producto, 'producto': producto})


# listado de producltos:
def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listado_productos.html', {'productos': productos})

# Eliminar Producto:
def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    return redirect('index_fechas')

# Eliminar vencimiento:
def eliminar_fecha(request, id_fecha):
    fecha = Fecha.objects.get(id=id_fecha)
    fecha.delete()
    return redirect('index_fechas')

