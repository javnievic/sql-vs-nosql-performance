# Flake8: noqa
from app.performace_tests.test_sql import test_sql_delete_all
from app.performace_tests.test_mongo import test_mongo_delete_all
from app.utils.plot_utils import grafica_barras_comparativa_sin_iteraciones


def run():
    sql_times_delete_all = test_sql_delete_all()
    mongo_times_delete_all = test_mongo_delete_all()
    if not sql_times_delete_all or not mongo_times_delete_all:
        print("No se pudieron obtener los tiempos de eliminación total para SQL o MongoDB.")
        return
    grafica_barras_comparativa_sin_iteraciones(sql_times_delete_all, mongo_times_delete_all, "SQL Delete All", "MongoDB Delete All", "Comparativa de Eliminación Total")