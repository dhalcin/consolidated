import flet as ft
from src.ui.components import create_sidebar
from src.ui.components import create_header

def main_app(page: ft.Page):
    page.title = 'Consilidado'

    main_content = ft.Column(
        [
            ft.Text('DataTable')
        ]
    )

    page.appbar = create_header()

    page.add(
        ft.Row(
            [
                create_sidebar(),
                ft.VerticalDivider(width=1),
                main_content
            ],
            expand=True
        )
    )

ft.app(main_app)