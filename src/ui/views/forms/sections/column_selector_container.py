import flet as ft

def main_content():
    return ft.Row(
        [
            ft.Text(value='Select Column', color='red')
        ],
        expand=True
    )

def build_column_selector_container():
    return ft.Column(   # Column is used to occupy the entire size of the parent Container that is in forms_container
                        # a case that does not work with Row
        [
            ft.Text(value='Selecionar Columnas', color='red'),
            main_content()
        ],
        expand=True
    )