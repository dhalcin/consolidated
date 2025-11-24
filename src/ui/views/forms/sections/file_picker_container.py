import flet as ft

def build_file_picker_container():
    button = ft.ElevatedButton(
        text='Pick Files',
        icon=ft.Icons.UPLOAD_FILE,
        bgcolor='#36B7E2',
        color=ft.Colors.WHITE,
    )

    return ft.Column(
        [
            button
        ]
    )