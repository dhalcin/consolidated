import flet as ft

def main_content():
    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Text(value='Microred', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='Establecimiento', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='UPS-Servicio', color='red'),
                        col={'sm': 6}
                    )
                ]
            )
        ]
    )

def build_establishment_container():
    return ft.Column(
        [
            ft.Row(
                [ft.Text(value='Datos del Establecimiento', color='red')],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            main_content()
        ],
        expand=True
    )