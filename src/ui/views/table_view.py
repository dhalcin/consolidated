import flet as ft

def iterate_columns(columns):
    col = []
    for column in columns:
        col.append(ft.DataColumn(ft.Text(column)))
    return col
    
def create_table_view(all_columns):
    data = ft.DataTable(
        columns=iterate_columns(all_columns)
    )

    return data