import time
import random
import matplotlib.pyplot as plt
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["comparativa"]
clientes_collection = db["clientes"]
productos_collection = db["productos"]
pedidos_collection = db["pedidos"]


def test_mongo_insert(num=10000, repeticiones=5):
    print("Conectando a MongoDB...")
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
            "activo": True
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
                "estado": "pendiente",
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

    # Mostrar gráfica
    plt.plot(tiempos, label="Mongo Insert", color="green")
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Tiempo de inserción en MongoDB")
    plt.legend()
    plt.show()


test_mongo_insert(10000, 5)
