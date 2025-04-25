# Flake8: noqa
from app.performace_tests.test_sql import test_sql_update_complex
from app.performace_tests.test_mongo import test_mongo_update_complex
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_update_complex = test_sql_update_complex()
    mongo_times_update_complex = test_mongo_update_complex()
    if not sql_times_update_complex or not mongo_times_update_complex:
        print("No se pudieron obtener los tiempos de actualización compleja para MySQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_complex, mongo_times_update_complex, "MySQL Update Complex", "MongoDB Update Complex", "Comparativa de Actualización Compleja")