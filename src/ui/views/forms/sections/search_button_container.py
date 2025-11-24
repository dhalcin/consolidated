import flet as ft

def build_search_button_container():
    button = ft.ElevatedButton(
        text='Search',
        icon=ft.Icons.SEARCH,
        bgcolor='#36B7E2',
        color=ft.Colors.WHITE,
    )

    return ft.Column(
        [
            button
        ]
    )