# Flake8: noqa
from app.performace_tests.test_sql import test_sql_update_single
from app.performace_tests.test_mongo import test_mongo_update_single
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_update_single = test_sql_update_single()
    mongo_times_update_single = test_mongo_update_single()
    if not sql_times_update_single or not mongo_times_update_single:
        print("No se pudieron obtener los tiempos de actualización simple para MySQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_single, mongo_times_update_single, "MySQL Update Single", "MongoDB Update Single", "Comparativa de Actualización Simple")