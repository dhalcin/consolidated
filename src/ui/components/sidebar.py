import flet as ft

def create_sidebar():
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.DELETE,
                selected_icon=ft.Icon(
                    ft.Icons.DELETE_OUTLINE,
                    color=ft.Colors.RED_700
                ),
                label='Delete Columns'
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS,
                selected_icon=ft.Icon(
                    ft.Icons.SETTINGS_OUTLINED,
                    color=ft.Colors.GREEN_700
                ),
                label='Settings'
            )
        ]

    )

