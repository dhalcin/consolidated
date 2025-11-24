import flet as ft

def main_content():
    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Text(value='Apellido Materno', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='Apellido Paterno', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='Nombres', color='red'),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Text(value='DNI', color='red')
                    ),
                    ft.Container(
                        content=ft.Text(value='Edad', color='red')
                    ),
                    ft.Container(
                        content=ft.Text(value='Genero', color='red')
                    )
                ]
            )
        ]
    )


def build_professional_data_container():
    return ft.Column(   # Column is used to occupy the entire size of the parent Container that is in forms_container
                        # a case that does not work with Row
        [
            ft.Row(
                [ft.Text(value='Datos del Paciente', color='red')],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            main_content()
        ],
        expand=True
    )