from django.db import models

class Tipo(models.Model):
    GRUPOS = [
        ('PP', 'Pastas y Panificados'),
        ('AL', 'Alimentos Lácteos y/o Vegetales'),
        ('HU', 'Huevos'),
        ('PC', 'Productos Congelados'),
        ('OT', 'Otros'),
    ]
    
    grupo = models.CharField(max_length=2, choices=GRUPOS, verbose_name="Grupo")
    subgrupo = models.CharField(max_length=255, verbose_name="Subgrupo")
    dias_retiro = models.PositiveIntegerField(verbose_name="Días para retiro")

    def __str__(self):
        return f"{self.get_grupo_display()} - {self.subgrupo}"


class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre del producto")
    scanning = models.CharField(max_length=255, verbose_name="Código de scanning")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return self.nombre


class Fecha(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="fechas")
    fecha = models.DateField(verbose_name="Fecha de vencimiento")

    def __str__(self):
        return f"{self.producto} - {self.fecha}"