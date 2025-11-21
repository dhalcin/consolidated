import flet as ft
from src.ui.views.settings import build_theme_container

def main(page: ft.Page):

    page.add(
        ft.Column(
            [ 
                ft.Container(
                    content=build_theme_container()
                    # border=ft.border.all(1, ft.Colors.AMBER)
                )
            ],
            expand=True
        )
    )