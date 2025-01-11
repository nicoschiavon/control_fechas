from .models import Producto, Tipo, Fecha
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'scanning', 'tipo']
        labels = {
            'nombre': 'Nombre del Producto',
            'scanning': 'Código de Barras',
            'tipo': 'Tipo de Producto'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'scanning': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el código de barras del producto'
                }
            ),
            'tipo': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            )
        }


#Formulario de fecha

class FechaForm(forms.ModelForm):
    class Meta:
        model = Fecha
        fields = ['fecha']
        labels = {
            'fecha': 'Fecha de Vencimiento'
        }
        widgets = {
            'fecha': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date'
                }
            )
        }