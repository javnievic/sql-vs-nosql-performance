# Flake8: noqa
from app.performace_tests.test_sql import test_sql_delete_multiple
from app.performace_tests.test_mongo import test_mongo_delete_multiple
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_delete_multiple = test_sql_delete_multiple()
    mongo_times_delete_multiple = test_mongo_delete_multiple()
    if not sql_times_delete_multiple or not mongo_times_delete_multiple:
        print("No se pudieron obtener los tiempos de eliminación múltiple para MySQL o MongoDB.")
        return
    graficar_comparativa(sql_times_delete_multiple, mongo_times_delete_multiple, "MySQL Delete Multiple", "MongoDB Delete Multiple", "Comparativa de Eliminación Múltiple")