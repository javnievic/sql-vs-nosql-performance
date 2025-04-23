from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_registro = models.DateField()
    activo = models.BooleanField(default=True)
    etiquetas = models.JSONField(default=list)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    inventario = models.PositiveIntegerField(default=0)
    imagen = models.URLField()


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50)  # pendiente, procesado, enviado
    productos = models.ManyToManyField(Producto, through='PedidoProducto')


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
