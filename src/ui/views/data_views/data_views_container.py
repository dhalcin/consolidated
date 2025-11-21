import flet as ft

def build_data_view_container():
    container = ft.Container(
        content=ft.Text(value='Table', color='red'),
        bgcolor=ft.Colors.WHITE10,
        expand=True
    )

    return ft.Row(
        [
            container
        ],
        expand=True
    )