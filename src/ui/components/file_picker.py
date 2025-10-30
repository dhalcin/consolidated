import flet as ft
from typing import Callable

def create_file_pick_button(pick_action: Callable, text: str):
    return ft.ElevatedButton(
        text,
        icon=ft.Icons.UPLOAD_FILE,
        on_click=lambda e: pick_action()
    )