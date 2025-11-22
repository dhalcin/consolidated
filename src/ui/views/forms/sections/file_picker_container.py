import flet as ft

def build_file_picker_container():
    return ft.Container(
        ft.ElevatedButton(
            text='Pick files',
            icon=ft.Icons.UPLOAD_FILE,
            bgcolor=ft.Colors.BLUE_400,
            color=ft.Colors.WHITE,
        ),
    )