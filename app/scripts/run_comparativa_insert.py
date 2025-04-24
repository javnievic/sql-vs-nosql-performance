# Flake8: noqa
from app.performace_tests.test_sql import test_sql_insert, test_sql_read_simple, test_sql_read_filter, test_sql_read_complex, test_sql_update_single, test_sql_update_multiple, test_sql_update_complex
from app.performace_tests.test_mongo import test_mongo_insert, test_mongo_read_simple, test_mongo_read_filter, test_mongo_read_complex, test_mongo_update_single, test_mongo_update_multiple, test_mongo_update_complex
from app.utils.plot_utils import graficar_comparativa


def run():
    run_comparativa_insert()
    run_comparativa_read_simple()
    run_comparativa_read_filter()
    run_comparativa_read_complex()
    run_comparativa_update_single()
    run_comparativa_update_multiple()
    run_comparativa_update_complex()
    
def run_comparativa_insert():
    sql_times_insert = test_sql_insert()
    mongo_times_insert = test_mongo_insert()
    graficar_comparativa(sql_times_insert, mongo_times_insert, "SQL Insert", "MongoDB Insert", "Comparativa de Inserción")

def run_comparativa_read_simple():
    sql_times_read_simple = test_sql_read_simple()
    mongo_times_read_simple = test_mongo_read_simple()
    if not sql_times_read_simple or not mongo_times_read_simple:
        print("No se pudieron obtener los tiempos de lectura simple para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_simple, mongo_times_read_simple, "SQL Read Simple", "MongoDB Read Simple", "Comparativa de Lectura Simple")

def run_comparativa_read_filter():
    sql_times_read_filter = test_sql_read_filter()
    mongo_times_read_filter = test_mongo_read_filter()
    if not sql_times_read_filter or not mongo_times_read_filter:
        print("No se pudieron obtener los tiempos de lectura con filtros para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_filter, mongo_times_read_filter, "SQL Read Filter", "MongoDB Read Filter", "Comparativa de Lectura con Filtros")

def run_comparativa_read_complex():
    sql_times_read_complex = test_sql_read_complex()
    mongo_times_read_complex = test_mongo_read_complex()
    if not sql_times_read_complex or not mongo_times_read_complex:
        print("No se pudieron obtener los tiempos de lectura compleja para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_read_complex, mongo_times_read_complex, "SQL Read Complex", "MongoDB Read Complex", "Comparativa de Lectura Compleja")

def run_comparativa_update_single():
    sql_times_update_single = test_sql_update_single()
    mongo_times_update_single = test_mongo_update_single()
    if not sql_times_update_single or not mongo_times_update_single:
        print("No se pudieron obtener los tiempos de actualización simple para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_single, mongo_times_update_single, "SQL Update Single", "MongoDB Update Single", "Comparativa de Actualización Simple")

def run_comparativa_update_multiple():
    sql_times_update_multiple = test_sql_update_multiple()
    mongo_times_update_multiple = test_mongo_update_multiple()
    if not sql_times_update_multiple or not mongo_times_update_multiple:
        print("No se pudieron obtener los tiempos de actualización múltiple para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_multiple, mongo_times_update_multiple, "SQL Update Multiple", "MongoDB Update Multiple", "Comparativa de Actualización Múltiple")

def run_comparativa_update_complex():
    sql_times_update_complex = test_sql_update_complex()
    mongo_times_update_complex = test_mongo_update_complex()
    if not sql_times_update_complex or not mongo_times_update_complex:
        print("No se pudieron obtener los tiempos de actualización compleja para SQL o MongoDB.")
        return
    graficar_comparativa(sql_times_update_complex, mongo_times_update_complex, "SQL Update Complex", "MongoDB Update Complex", "Comparativa de Actualización Compleja")