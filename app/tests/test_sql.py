import time
import random
import matplotlib.pyplot as plt
from app.models import Cliente, Producto, Pedido, PedidoProducto


def test_sql_insert(num=300, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        Cliente.objects.all().delete()  # Limpieza
        Producto.objects.all().delete()  # Limpieza
        Pedido.objects.all().delete()  # Limpieza

        start = time.time()

        # Insertar Clientes
        clientes = [Cliente(
            nombre=f"Usuario {i}",
            email=f"user{i}@test.com",
            fecha_registro="2025-04-22",
            activo=True
        ) for i in range(num)]
        Cliente.objects.bulk_create(clientes)

        # Insertar Productos
        productos = [Producto(
            nombre=f"Producto {i}",
            descripcion=f"Descripción {i}",
            precio=random.uniform(10, 1000),
            categoria="Categoria A",
            inventario=random.randint(1, 100),
            imagen="http://example.com/product.jpg"
        ) for i in range(num)]
        Producto.objects.bulk_create(productos)

        # Insertar Pedidos
        for cliente in Cliente.objects.all():
            pedido = Pedido.objects.create(
                    cliente=cliente,
                    fecha_pedido="2025-04-22",
                    estado="pendiente"
                )
            productos_random = random.sample(
                    list(Producto.objects.all()),
                    k=random.randint(1, 10)
                )
            for producto in productos_random:
                PedidoProducto.objects.create(
                    pedido=pedido,
                    producto=producto,
                    cantidad=random.randint(1, 5),
                    precio_unitario=producto.precio
                )
        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de inserción: {end - start:.2f} s")

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Insert")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de inserción en MySQL")
    plt.legend()
    plt.show()
