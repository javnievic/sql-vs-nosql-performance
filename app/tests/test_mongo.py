import time
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())  # Verifica la conexión
db = client["comparativa"]
collection = db["clientes"]


def test_mongo_insert(num=100000, repeticiones=10):
    print("Conectando a MongoDB...")
    tiempos = []
    for _ in range(repeticiones):
        collection.delete_many({})  # Limpieza
        start = time.time()
        docs = [{
            "nombre": f"Usuario {i}",
            "email": f"user{i}@test.com",
            "fecha_registro": "2025-04-22",
            "activo": True
        } for i in range(num)]
        collection.insert_many(docs)
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


test_mongo_insert(100000, 10)
