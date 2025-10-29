import flet as ft

def create_header():
    return ft.AppBar(
        leading=ft.Icon(ft.Icons.UPLOAD_FILE),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
    )