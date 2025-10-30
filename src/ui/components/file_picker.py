import flet as ft
from typing import Callable

def create_file_pick_button(pick_action: Callable, text: str):
    return ft.ElevatedButton(
        text,
        icon=ft.Icons.UPLOAD_FILE,
        on_click=lambda e: pick_action(),
        bgcolor=ft.Colors.BLUE_400,
        color=ft.Colors.WHITE,
        height=32, 
        width=170,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=16),
            padding=ft.padding.symmetric(horizontal=10, vertical=0),
            elevation=1
        )
    )