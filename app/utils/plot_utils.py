import matplotlib.pyplot as plt


def graficar_comparativa(tiempos_sql, tiempos_mongo):
    plt.figure(figsize=(10, 6))
    plt.plot(tiempos_sql, label="SQL Insert", marker='o')
    plt.plot(tiempos_mongo, label="Mongo Insert", marker='s', color='green')
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title("Comparativa de tiempos de inserción: SQL vs MongoDB")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
