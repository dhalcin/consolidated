import flet as ft

def build_file_picker_container():
    button_style = ft.ButtonStyle(
        bgcolor={
            ft.ControlState.DEFAULT: '#36B7E2',
            ft.ControlState.HOVERED: ft.Colors.GREEN_ACCENT_400
        },
        color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
        shape={ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=9)}
    )
    
    button = ft.ElevatedButton(
       text='Open File',
       icon=ft.Icons.UPLOAD_FILE,
        style=button_style
    )

    return ft.Column([button])
