import flet as ft

def build_forms_container():
    container = ft.Container (
        content=ft.Text(value='Esto es un container', color='red'),
        bgcolor=ft.Colors.AMBER_100,
        expand=True
    )

    return ft.Row(
        [
            container
        ],
        expand=True
    )