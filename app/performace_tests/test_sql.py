# Flake8: noqa
import time
import random
from app.models import Cliente, Producto, Pedido, PedidoProducto
from datetime import date

def test_sql_insert(num=10000, repeticiones=5):
    print(f"Prueba de inserción en MySQL para {num} "
        f"clientes, productos y pedidos en {repeticiones} repeticiones\n")
    tiempos = []
    for _ in range(repeticiones):
        Cliente.objects.all().delete()  # Limpieza
        Producto.objects.all().delete()  # Limpieza
        Pedido.objects.all().delete()  # Limpieza

        start = time.time()
        fecha_actual = date.today()

        # Insertar Clientes
        clientes = [Cliente(
            nombre=f"Usuario {i}",
            email=f"user{i}@test.com",
            fecha_registro=fecha_actual,
            activo=random.choice([True, False])
        ) for i in range(num)]
        clientes_creados = Cliente.objects.bulk_create(clientes)

        # Insertar Productos
        productos = [Producto(
            nombre=f"Producto {i}",
            descripcion=f"Descripción {i}",
            precio=random.uniform(10, 1000),
            categoria=random.choice(["Categoria A", "Categoria B", "Categoria C"]),
            inventario=random.randint(1, 100),
            imagen="http://example.com/product.jpg"
        ) for i in range(num)]
        productos_creados = Producto.objects.bulk_create(productos)

        # Insertar Pedidos

        pedidos = [
                Pedido(
                    cliente=cliente,
                    fecha_pedido=fecha_actual,
                    estado=random.choice(["pendiente", "completado"])
                ) for cliente in clientes_creados
            ]
        pedidos_creados = Pedido.objects.bulk_create(pedidos)

        # Insertar productos en pedidos
        pedido_productos = []
        for pedido in pedidos_creados:
            productos_random = random.sample(
                    productos_creados,
                    k=random.randint(1, 10)
                )
            for producto in productos_random:
                pedido_productos.append(PedidoProducto(
                    pedido=pedido,
                    producto=producto,
                    cantidad=random.randint(1, 5),
                    precio_unitario=producto.precio
                ))

        PedidoProducto.objects.bulk_create(pedido_productos)

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de inserción: {end - start:.2f} s")

    return tiempos

def test_sql_read_simple(repeticiones=20):
    print(f"Prueba de lectura simple en MySQL para {repeticiones} repeticiones\n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(Cliente.objects.all())
        read_productos = list(Producto.objects.all())
        read_pedidos = list(Pedido.objects.all())
        read_pedidos_productos = list(PedidoProducto.objects.all())

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura simple: {end - start:.2f} s")

    return tiempos

def test_sql_read_filter(repeticiones=20):
    print(f"Prueba de lectura con filtro en MySQL para {repeticiones} repeticiones\n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(Cliente.objects.filter(activo=True))
        read_productos = list(Producto.objects.filter(precio__gt=500))
        read_pedidos = list(Pedido.objects.filter(estado="pendiente"))

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura con filtro: {end - start:.2f} s")

    return tiempos


def test_sql_read_complex(repeticiones=20):
    print(f"Prueba de lectura compleja en MySQL para {repeticiones} repeticiones\n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        pedidos_con_clientes = list(
            Pedido.objects.select_related('cliente')
            .prefetch_related('pedidoproducto_set__producto')
            .all()
        )

        for pedido in pedidos_con_clientes:
            cliente = pedido.cliente
            productos = list(pedido.pedidoproducto_set.all())

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura compleja: {end - start:.2f} s")

    return tiempos


def test_sql_update_multiple(repeticiones=20, numero_actualizaciones=5):
    print(f"Prueba de actualización múltiple en MySQL para {repeticiones} repeticiones "
          f"y {numero_actualizaciones} actualizaciones por repetición\n")

    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        clientes = Cliente.objects.all()[i*numero_actualizaciones:(i+1)*numero_actualizaciones]
        for cliente in clientes:
            cliente.nombre = "Cliente Actualizado"
            cliente.save()

        productos = Producto.objects.all()[i*numero_actualizaciones:(i+1)*numero_actualizaciones]
        for producto in productos:
            producto.precio = 100
            producto.save()

        pedidos = Pedido.objects.all()[i*numero_actualizaciones:(i+1)*numero_actualizaciones]
        for pedido in pedidos:
            pedido.estado = "completado"
            pedido.save()

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de actualización múltiple: {end - start:.2f} s")

    return tiempos

def test_sql_update_complex(repeticiones=20):
    print(f"Prueba de actualización compleja en MySQL para {repeticiones} repeticiones\n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        productos_menos_50 = Producto.objects.filter(inventario__lt=50).update(
            precio= 10 * i
        )

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de actualización compleja: {end - start:.2f} s")

    return tiempos

def test_sql_delete_multiple(repeticiones=20, numero_eliminaciones=5):
    print(f"Prueba de eliminación múltiple en MySQL para {repeticiones} repeticiones "
          f"y {numero_eliminaciones} eliminaciones por repetición\n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        clientes = Cliente.objects.all()[i*numero_eliminaciones:(i+1)*numero_eliminaciones]
        for cliente in clientes:
            cliente.delete()

        productos = Producto.objects.all()[i*numero_eliminaciones:(i+1)*numero_eliminaciones]
        for producto in productos:
            producto.delete()

        pedidos = Pedido.objects.all()[i*numero_eliminaciones:(i+1)*numero_eliminaciones]
        for pedido in pedidos:
            pedido.delete()

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de eliminación múltiple: {end - start:.2f} s")

    return tiempos


def test_sql_delete_all():
    print("Prueba de eliminación total en MySQL \n")
    
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("MySQL: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return

    start = time.time()

    Cliente.objects.all().delete()
    Producto.objects.all().delete()
    Pedido.objects.all().delete()

    end = time.time()
    print(f"Tiempo de eliminación total: {end - start:.2f} s")

    return end - start