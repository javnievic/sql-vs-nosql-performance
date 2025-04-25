# Flake8: noqa
from app.scripts import run_comparativa_insert, run_comparativa_read_simple, run_comparativa_read_filter, run_comparativa_read_complex, run_comparativa_update_single, run_comparativa_update_multiple, run_comparativa_update_complex, run_comparativa_delete_simple, run_comparativa_delete_multiple

insert = run_comparativa_insert
read_simple = run_comparativa_read_simple
read_filter = run_comparativa_read_filter
read_complex = run_comparativa_read_complex
update_single = run_comparativa_update_single
update_multiple = run_comparativa_update_multiple
update_complex = run_comparativa_update_complex
delete_simple = run_comparativa_delete_simple
delete_multiple = run_comparativa_delete_multiple

def run():
    insert.run()
    read_simple.run()
    read_filter.run()
    read_complex.run()
    update_single.run()
    update_multiple.run()
    update_complex.run()
    delete_simple.run()
    delete_multiple.run()