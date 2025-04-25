# Flake8: noqa
from app.performace_tests.test_sql import test_sql_read_complex
from app.performace_tests.test_mongo import test_mongo_read_complex
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_read_complex = test_sql_read_complex()
    mongo_times_read_complex = test_mongo_read_complex()
    if not sql_times_read_complex or not mongo_times_read_complex:
        print("No se pudieron obtener los tiempos de lectura compleja para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_complex, mongo_times_read_complex, "SQL Read Complex", "MongoDB Read Complex", "Comparativa de Lectura Compleja")