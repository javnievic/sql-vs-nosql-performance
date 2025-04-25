# Flake8: noqa
from app.performace_tests.test_sql import test_sql_read_simple
from app.performace_tests.test_mongo import test_mongo_read_simple
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_read_simple = test_sql_read_simple()
    mongo_times_read_simple = test_mongo_read_simple()
    if not sql_times_read_simple or not mongo_times_read_simple:
        print("No se pudieron obtener los tiempos de lectura simple para MySQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_simple, mongo_times_read_simple, "MySQL Read Simple", "MongoDB Read Simple", "Comparativa de Lectura Simple")