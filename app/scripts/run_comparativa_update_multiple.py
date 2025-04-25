# Flake8: noqa
from app.performace_tests.test_sql import test_sql_update_multiple
from app.performace_tests.test_mongo import  test_mongo_update_multiple
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_update_multiple = test_sql_update_multiple()
    mongo_times_update_multiple = test_mongo_update_multiple()
    if not sql_times_update_multiple or not mongo_times_update_multiple:
        print("No se pudieron obtener los tiempos de actualización múltiple para MySQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_multiple, mongo_times_update_multiple, "MySQL Update Multiple", "MongoDB Update Multiple", "Comparativa de Actualización Múltiple")