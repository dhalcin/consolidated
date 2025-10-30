import flet as ft

def create_header(file_button: ft.Control, file_label: ft.Control):
    return ft.AppBar(
        leading=ft.Row(
            [
                ft.Container(
                    content=file_button,
                    margin=ft.margin.only(left=30, top=4, bottom=4),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=file_label,
                    alignment=ft.alignment.center_left,
                    margin=ft.margin.only(left=10)
                )  
            ],
            spacing=10
        ),
        leading_width=190,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        toolbar_height=45
    )