# Flake8: noqa
import time
import random
from app.models import Cliente, Producto, Pedido, PedidoProducto
import matplotlib.pyplot as plt


def test_sql_insert(num=300, repeticiones=5):
    print(f"Prueba de inserción en SQL para {num}"
          "clientes, productos y pedidos")
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

    return tiempos


def test_sql_read_simple(num=300, repeticiones=5):
    tiempos = []

    poblar_sql(num)

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(Cliente.objects.all())
        read_productos = list(Producto.objects.all())
        read_pedidos = list(Pedido.objects.all())
        read_pedidos_productos = list(PedidoProducto.objects.all())

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura simple: {end - start:.2f} s")

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Read Simple")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de lectura simple en MySQL")
    plt.legend()
    plt.show()


def test_sql_read_filter(num=300, repeticiones=5):
    tiempos = []

    poblar_sql(num)

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(Cliente.objects.filter(activo=True))
        read_productos = list(Producto.objects.filter(precio__gt=500))
        read_pedidos = list(Pedido.objects.filter(estado="pendiente"))
        read_pedidos_productos = list(PedidoProducto.objects.filter(cantidad__gt=2))

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura con filtro: {end - start:.2f} s")

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Read Filter")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de lectura con filtros en MySQL")
    plt.legend()
    plt.show()


def test_sql_read_complex(num=300, repeticiones=5):
    tiempos = []

    poblar_sql(num)

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

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Read Complex")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de lectura compleja en MySQL")
    plt.legend()
    plt.show()


def test_sql_update_single(num=300, repeticiones=5):
    tiempos = []

    poblar_sql(num)

    for i in range(repeticiones):
        start = time.time()

        first_cliente = Cliente.objects.first().id
        cliente = Cliente.objects.get(id=first_cliente + i)
        cliente.nombre = "Cliente Actualizado"
        cliente.save()

        first_producto = Producto.objects.first().id
        producto = Producto.objects.get(id=first_producto + i)
        producto.precio = 100
        producto.save()

        first_pedido = Pedido.objects.first().id
        pedido = Pedido.objects.get(id=first_pedido + i)
        pedido.estado = "completado"
        pedido.save()

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de actualización simple: {end - start:.2f} s")

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Update Single")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de actualización simple en MySQL")
    plt.legend()
    plt.show()


def test_sql_update_multiple(num=300, repeticiones=5, numero_actualizaciones=5):
    tiempos = []

    poblar_sql(num)

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

    # Mostrar gráfica
    plt.plot(tiempos, label="SQL Update Multiple")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de actualización múltiple en MySQL")
    plt.legend()
    plt.show()


def poblar_sql(num):
    Cliente.objects.all().delete()  # Limpieza
    Producto.objects.all().delete()  # Limpieza
    Pedido.objects.all().delete()  # Limpieza

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
