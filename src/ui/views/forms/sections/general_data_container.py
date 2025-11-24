import flet as ft

def main_content():
    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Text(value='N° de Lote', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='N° de Hoja', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='N° de Registro', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='Fecha', color='red'),
                        col={'sm': 6}
                    )
                ]
            )
        ]
    )


def build_general_data_container():
    return ft.Column(
        [
            #! title Data Generales
            ft.Row(
                [ft.Text(value='Datos Generales', color='red')],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            #! main content
            main_content()
        ],
        expand=True
    )