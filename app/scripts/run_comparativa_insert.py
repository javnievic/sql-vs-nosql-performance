# Flake8: noqa
from app.performace_tests.test_sql import test_sql_insert
from app.performace_tests.test_mongo import test_mongo_insert
from app.utils.plot_utils import graficar_comparativa


def run():
    sql_times_insert = test_sql_insert()
    mongo_times_insert = test_mongo_insert()
    graficar_comparativa(sql_times_insert, mongo_times_insert, "MySQL Insert", "MongoDB Insert", "Comparativa de Inserción")