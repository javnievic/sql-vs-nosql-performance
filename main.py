# Flake8: noqa
import argparse
import os
import django
import sys
import psutil
import time

def medir_cpu(func, *args, **kwargs):
    proceso = psutil.Process(os.getpid())
    cpu_inicio = proceso.cpu_percent(interval=None)
    tiempo_inicio = time.time()
    uso_cpu_total = []
    tiempos_total = func(*args, **kwargs)
    
    tiempo_fin = time.time()
    cpu_fin = proceso.cpu_percent(interval=None)

    uso_cpu = cpu_fin - cpu_inicio
    duracion = tiempo_fin - tiempo_inicio
    
    print(f"Uso de CPU estimado: {uso_cpu:.2f}%")

    uso_cpu_total.append(uso_cpu)

    return uso_cpu_total, tiempos_total



# Configura el entorno de Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configura el módulo de settings de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "comparativa.settings")

# Configura Django
django.setup()

# Ahora importa los módulos que dependen de Django
from app.performace_tests.test_sql import (
    test_sql_insert, test_sql_delete_multiple, test_sql_delete_all,
    test_sql_read_simple, test_sql_read_filter, test_sql_read_complex,
    test_sql_update_multiple, test_sql_update_complex
)
from app.performace_tests.test_mongo import (
    test_mongo_insert, test_mongo_delete_multiple, test_mongo_delete_all,
    test_mongo_read_simple, test_mongo_read_filter, test_mongo_read_complex,
    test_mongo_update_multiple, test_mongo_update_complex
)
from app.utils.plot_utils import (
    graficar_comparativa,
    grafica_barras_comparativa_sin_iteraciones,
    graficar_cpu
)
from app.models import Cliente, Producto, Pedido

def verificar_datos_mysql():
    if not Cliente.objects.exists() or not Producto.objects.exists() or not Pedido.objects.exists():
        print("No hay datos en la base de datos. Por favor, inserte datos primero.")
        print("Ejecute el siguiente comando para insertar los datos:")
        print("python main.py --test insert --num <número_de_registros> --repeticiones <número_de_repeticiones>")
        print("Los parámetros --num y --repeticiones son opcionales. Si no se especifican, se utilizarán los valores por defecto:")
        print("--num 10000 (por defecto, número de registros a insertar)")
        print("--repeticiones 5 (por defecto, número de repeticiones para la prueba)")
        return True 
    return False  

def main():
    parser = argparse.ArgumentParser(description="Comparativa de rendimiento entre MySQL y MongoDB")
    parser.add_argument("--test", required=True, choices=[
        "insert", "delete_all", "delete_multiple", "read_simple", "read_filter", "read_complex",
        "update_single", "update_multiple", "update_complex"
    ], help="Tipo de test a ejecutar")
    parser.add_argument("--num", type=int, default=None,
    help="Número de registros (para 'insert', 'delete_multiple' y 'update_multiple')")
    parser.add_argument("--repeticiones", type=int, default=None, help="Número de repeticiones")
    args = parser.parse_args()

    # Establecer el valor por defecto para repeticiones dependiendo del tipo de test
    if args.repeticiones is None:
        if args.test == "insert":
            args.repeticiones = 5  # Valor por defecto para insert
        else:
            args.repeticiones = 20  # Valor por defecto para otros tests

        # Establecer el valor por defecto para repeticiones dependiendo del tipo de test
    if args.num is None:
        if args.test == "insert":
            args.num = 10000  # Valor por defecto para insert
        else:
            args.num = 100  # Valor por defecto para actualizaciones y eliminaciones

    test = args.test

    if test == "insert":
        sql_cpu, sql_times = medir_cpu(test_sql_insert, repeticiones=args.repeticiones, num=args.num)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_insert, repeticiones=args.repeticiones, num=args.num)

        graficar_comparativa(sql_times, mongo_times, "MySQL Insert", "MongoDB Insert", "Comparativa de Inserción (Tiempo)")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Insert", "MongoDB Insert", "Comparativa de Inserción (Uso de CPU)")

    elif test == "read_simple":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_read_simple, repeticiones=args.repeticiones)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_read_simple, repeticiones=args.repeticiones)
        graficar_comparativa(sql_times, mongo_times, "MySQL Read Simple", "MongoDB Read Simple", "Comparativa de Lectura Simple")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Read Simple", "MongoDB Read Simple", "Comparativa de Lectura Simple (Uso de CPU)")

    elif test == "read_filter":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_read_filter, repeticiones=args.repeticiones)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_read_filter, repeticiones=args.repeticiones)
        graficar_comparativa(sql_times, mongo_times, "MySQL Read Filter", "MongoDB Read Filter", "Comparativa de Lectura con Filtros")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Read Filter", "MongoDB Read Filter", "Comparativa de Lectura con Filtros (Uso de CPU)")

    elif test == "read_complex":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_read_complex, repeticiones=args.repeticiones)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_read_complex, repeticiones=args.repeticiones)
        graficar_comparativa(sql_times, mongo_times, "MySQL Read Complex", "MongoDB Read Complex", "Comparativa de Lectura Compleja")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Read Complex", "MongoDB Read Complex", "Comparativa de Lectura Compleja (Uso de CPU)")

    elif test == "update_multiple":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_update_multiple, repeticiones=args.repeticiones, numero_actualizaciones=args.num)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_update_multiple, repeticiones=args.repeticiones, numero_actualizaciones=args.num)
        graficar_comparativa(sql_times, mongo_times, "MySQL Update Multiple", "MongoDB Update Multiple", "Comparativa de Actualización Múltiple")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Update Multiple", "MongoDB Update Multiple", "Comparativa de Actualización Múltiple (Uso de CPU)")

    elif test == "update_complex":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_update_complex, repeticiones=args.repeticiones)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_update_complex, repeticiones=args.repeticiones)
        graficar_comparativa(sql_times, mongo_times, "MySQL Update Complex", "MongoDB Update Complex", "Comparativa de Actualización Compleja")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Update Complex", "MongoDB Update Complex", "Comparativa de Actualización Compleja (Uso de CPU)")

    elif test == "delete_multiple":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_delete_multiple, repeticiones=args.repeticiones, numero_eliminaciones=args.num)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_delete_multiple, repeticiones=args.repeticiones, numero_eliminaciones=args.num)
        graficar_comparativa(sql_times, mongo_times, "MySQL Delete Multiple", "MongoDB Delete Multiple", "Comparativa de Eliminación Múltiple")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Delete Multiple", "MongoDB Delete Multiple", "Comparativa de Eliminación Múltiple (Uso de CPU)")

    elif test == "delete_all":
        if verificar_datos_mysql():
            return
        sql_cpu, sql_times = medir_cpu(test_sql_delete_all)
        mongo_cpu, mongo_times = medir_cpu(test_mongo_delete_all)
        grafica_barras_comparativa_sin_iteraciones(sql_times, mongo_times, "MySQL Delete All", "MongoDB Delete All", "Comparativa de Eliminación Total")
        graficar_cpu(sql_cpu, mongo_cpu, "MySQL Delete All", "MongoDB Delete All", "Comparativa de Eliminación Total (Uso de CPU)")

    else:
        print("Test no reconocido.")


if __name__ == "__main__":
    main()