import flet as ft
from src.ui.views.forms.sections import build_file_picker_container
from src.ui.views.forms.sections import build_general_data_container
from src.ui.views.forms.sections import build_establishment_container

def build_forms_container():
    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=build_file_picker_container(),
                        bgcolor='#FAFAFA',
                        padding=5,
                        col={'sm': 3, 'xl':2},
                        border=ft.border.all(1, '#36B7E2'),
                        border_radius=ft.border_radius.all(10)
                    ),
                    ft.Container(
                        content=build_general_data_container(),
                        padding=5,
                        col={"sm": 5, 'xl': 3},
                        border=ft.border.all(1, '#36B7E2'),
                        border_radius=ft.border_radius.all(10)
                    ),
                    ft.Container(
                        content=build_establishment_container(),
                        padding=5,
                        col={"sm": 4, 'xl': 3},
                        border=ft.border.all(1, '#36B7E2'),
                        border_radius=ft.border_radius.all(10)
                    )
                ]
            )
        ],
        expand=True
    )