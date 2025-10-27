import flet as ft
from src.ui.components import create_sidebar

def main_app(page: ft.Page):
    page.title = 'Consilidado'

    page.add(
        ft.Row(
            controls=[create_sidebar()],
            expand=True
        )
    )

ft.app(main_app)