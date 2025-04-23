import time
import matplotlib.pyplot as plt
from app.models import Cliente


def test_sql_insert(num=100000, repeticiones=10):
    tiempos = []
    for _ in range(repeticiones):
        Cliente.objects.all().delete()  # Limpieza
        start = time.time()
        Cliente.objects.bulk_create([
            Cliente(
                nombre=f"Usuario {i}",
                email=f"user{i}@test.com",
                fecha_registro="2025-04-22",
                activo=True
            ) for i in range(num)
        ])
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
