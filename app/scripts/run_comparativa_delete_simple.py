# Flake8: noqa
from app.performace_tests.test_sql import test_sql_delete_simple
from app.performace_tests.test_mongo import test_mongo_delete_simple
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_delete_simple = test_sql_delete_simple()
    mongo_times_delete_simple = test_mongo_delete_simple()
    if not sql_times_delete_simple or not mongo_times_delete_simple:
        print("No se pudieron obtener los tiempos de eliminación simple para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_delete_simple, mongo_times_delete_simple, "SQL Delete Simple", "MongoDB Delete Simple", "Comparativa de Eliminación Simple")