# Flake8: noqa
from app.performace_tests.test_sql import test_sql_read_filter
from app.performace_tests.test_mongo import test_mongo_read_filter
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_read_filter = test_sql_read_filter()
    mongo_times_read_filter = test_mongo_read_filter()
    if not sql_times_read_filter or not mongo_times_read_filter:
        print("No se pudieron obtener los tiempos de lectura con filtros para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_filter, mongo_times_read_filter, "SQL Read Filter", "MongoDB Read Filter", "Comparativa de Lectura con Filtros")