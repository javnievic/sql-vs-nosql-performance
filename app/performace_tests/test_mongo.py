# Flake8: noqa
import time
import random
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["comparativa"]
clientes_collection = db["clientes"]
productos_collection = db["productos"]
pedidos_collection = db["pedidos"]


def test_mongo_insert(num=10000, repeticiones=5):
    print(f"Prueba de inserción en MongoDB para {num} "
          f"clientes, productos y pedidos en {repeticiones} repeticiones\n")
    tiempos = []
    for _ in range(repeticiones):
        clientes_collection.delete_many({})  # Limpieza
        productos_collection.delete_many({})  # Limpieza
        pedidos_collection.delete_many({})  # Limpieza

        start = time.time()

        # Insertar Clientes
        clientes_docs = [{
            "nombre": f"Usuario {i}",
            "email": f"user{i}@test.com",
            "fecha_registro": "2025-04-22",
            "activo": random.choice([True, False])
        } for i in range(num)]
        clientes_collection.insert_many(clientes_docs)

        # Insertar Productos
        productos_docs = [{
            "nombre": f"Producto {i}",
            "descripcion": f"Descripción {i}",
            "precio": random.uniform(10, 1000),
            "categoria": "Categoria A",
            "inventario": random.randint(1, 100),
            "imagen": "http://example.com/product.jpg"
        } for i in range(num)]
        productos_collection.insert_many(productos_docs)

        # Insertar Pedidos
        for cliente in clientes_docs:
            pedido = {
                "cliente_id": cliente["_id"],
                "fecha_pedido": "2025-04-22",
                "estado": random.choice(["pendiente", "completado"]),
                "productos": [{
                    "producto_id": random.choice(productos_docs)["_id"],
                    "cantidad": random.randint(1, 5),
                    "precio_unitario": random.uniform(10, 1000)
                } for _ in range(random.randint(1, 10))]
            }
            pedidos_collection.insert_one(pedido)

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de inserción: {end - start:.2f} s")

    return tiempos


def test_mongo_read_simple(repeticiones=20):
    print(f"Prueba de lectura simple en MongoDB para {repeticiones} repeticiones\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(clientes_collection.find())
        read_productos = list(productos_collection.find())
        read_pedidos = list(pedidos_collection.find())

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura simple: {end - start:.2f} s")

    return tiempos


def test_mongo_read_filter(repeticiones=20):
    print(f"Prueba de lectura con filtro en MongoDB para {repeticiones} repeticiones\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        read_clientes = list(clientes_collection.find({"activo": True}))
        read_productos = list(productos_collection.find({"precio": {"$gt": 500}}))
        read_pedidos = list(pedidos_collection.find({"estado": "pendiente"}))

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura con filtro: {end - start:.2f} s")

    return tiempos


def test_mongo_read_complex(repeticiones=20):
    print(f"Prueba de lectura compleja en MongoDB para {repeticiones} repeticiones\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for _ in range(repeticiones):
        start = time.time()

        pipeline = [
            {
                "$lookup": {
                    "from": "clientes",
                    "localField": "cliente_id",
                    "foreignField": "_id",
                    "as": "clientes_info"
                }
            },
            {
                "$unwind": "$clientes_info"
            }
        ]
        pedidos_con_clientes = list(pedidos_collection.aggregate(pipeline))

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de lectura compleja: {end - start:.2f} s")

    return tiempos


def test_mongo_update_multiple(repeticiones=20, numero_actualizaciones=5):
    print(f"Prueba de actualización múltiple en MongoDB para {repeticiones} repeticiones " 
          f"y {numero_actualizaciones} actualizaciones por repetición\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        for cliente in random.sample(list(clientes_collection.find()), min(numero_actualizaciones, clientes_collection.count_documents({}))):
            clientes_collection.update_one(
                {"_id": cliente["_id"]},
                {"$set": {"nombre": f"Usuario Actualizado {i}"}}
            )

        for producto in random.sample(list(productos_collection.find()), min(numero_actualizaciones, productos_collection.count_documents({}))):
            productos_collection.update_one(
                {"_id": producto["_id"]},
                {"$set": {"precio": 100 + i}}
            )

        for pedido in random.sample(list(pedidos_collection.find()), min(numero_actualizaciones, pedidos_collection.count_documents({}))):
            pedidos_collection.update_one(
                {"_id": pedido["_id"]},
                {"$set": {"estado": "completado"}}
            )

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de actualización múltiple: {end - start:.2f} s")

    return tiempos


def test_mongo_update_complex(repeticiones=20):
    print(f"Prueba de actualización compleja en MongoDB para {repeticiones} repeticiones\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        productos_collection.update_many(
            {"inventario": {"$lt": 20 * (i+1)}},
            {"$set": {"precio": 10 * i}}
        )

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de actualización compleja: {end - start:.2f} s")

    return tiempos


def test_mongo_delete_multiple(repeticiones=20, numero_eliminaciones=5):
    print(f"Prueba de eliminación múltiple en MongoDB para {repeticiones} repeticiones "
          f"y {numero_eliminaciones} eliminaciones por repetición\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    tiempos = []

    for i in range(repeticiones):
        start = time.time()

        for cliente in random.sample(list(clientes_collection.find()), min(numero_eliminaciones, clientes_collection.count_documents({}))):
            clientes_collection.delete_one({"_id": cliente["_id"]})

        for producto in random.sample(list(productos_collection.find()), min(numero_eliminaciones, productos_collection.count_documents({}))):
            productos_collection.delete_one({"_id": producto["_id"]})

        for pedido in random.sample(list(pedidos_collection.find()), min(numero_eliminaciones, pedidos_collection.count_documents({}))):
            pedidos_collection.delete_one({"_id": pedido["_id"]})

        end = time.time()
        tiempos.append(end - start)
        print(f"Tiempo de eliminación múltiple: {end - start:.2f} s")

    return tiempos


def test_mongo_delete_all():
    print(f"Prueba de eliminación total en MongoDB\n")
    
    if clientes_collection.count_documents({}) == 0 | productos_collection.count_documents({}) == 0 | pedidos_collection.count_documents({}) == 0:
        print("MongoDB: No hay datos en la base de datos. Por favor, inserte datos primero.")
        return
    
    start = time.time()

    clientes_collection.delete_many({})
    productos_collection.delete_many({})
    pedidos_collection.delete_many({})

    end = time.time()
    print(f"Tiempo de eliminación total: {end - start:.2f} s")

    return end - start