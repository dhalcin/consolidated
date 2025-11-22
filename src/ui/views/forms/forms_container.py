import flet as ft
from src.ui.views.forms.sections import build_file_picker_container

def build_forms_container():
    return ft.Row(
        [
            build_file_picker_container()
        ],
        expand=True
    )