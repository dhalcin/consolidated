import flet as ft
from src.ui.views.settings import build_theme_container
from src.ui.views.forms import build_forms_container
from src.ui.views.data_views import build_data_view_container

def main(page: ft.Page):

    #page.bgcolor = '#FFFFFF'

    page.add(
        ft.Column(
            [ 
                ft.Container(
                    content=build_theme_container()
                    # border=ft.border.all(1, ft.Colors.AMBER)
                ),
                ft.Row(
                    [
                        build_forms_container()
                    ],
                    expand=True
                ),
                ft.Container(
                    content=build_data_view_container(),
                    expand=True,
                    #border=ft.border.all(0.1, ft.Colors.YELLOW_200)
                )
            ],
            expand=True
        )
    )