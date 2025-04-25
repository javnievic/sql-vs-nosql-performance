# Flake8: noqa
import matplotlib.pyplot as plt


def graficar_comparativa(tiempos_sql, tiempos_mongo, sql_label, mongo_label, title):
    plt.figure(figsize=(10, 6))
    plt.plot(tiempos_sql, label=sql_label, marker='o')
    plt.plot(tiempos_mongo, label=mongo_label, marker='s', color='green')
    plt.xlabel("Repetición")
    plt.ylabel("Tiempo (s)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafica_barras_comparativa_sin_iteraciones(tiempo_sql, tiempo_mongo, sql_label, mongo_label, title):
    plt.figure(figsize=(10, 6))
    plt.bar(sql_label, tiempo_sql, label=sql_label)
    plt.bar(mongo_label, tiempo_mongo, label=mongo_label)
    plt.xlabel("Base de Datos")
    plt.ylabel("Tiempo (s)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_cpu(sql_cpu, mongo_cpu, sql_label, mongo_label, title):
    grafica_barras_comparativa_sin_iteraciones(sql_cpu, mongo_cpu, sql_label, mongo_label, title)

