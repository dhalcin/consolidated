import flet as ft

def iterate_columns(columns):
    col = [ft.DataColumn(ft.Text(column)) for column in columns]
    return col

def iterate_rows(rows):
    data_rows = []
    for row in rows:
        cells = [ft.DataCell(ft.Text(str(rw))) for rw in row]
        data_rows.append(ft.DataRow(cells=cells))
    return data_rows
        

def create_table_view(columns, rows):
    data = ft.DataTable(
        columns=iterate_columns(columns),
        rows=iterate_rows(rows)
    )

    return data