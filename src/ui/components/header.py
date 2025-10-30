import flet as ft
from typing import Callable

def create_header(file_button: Callable):
    return ft.AppBar(
        leading=ft.Container(
            content=file_button,
            alignment=ft.alignment.center,
            margin=ft.margin.only(left=10, top=4, bottom=4)
        ),
        leading_width=190,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        toolbar_height=45
    )