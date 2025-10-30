import flet as ft
from src.ui.components import create_sidebar
from src.ui.components import create_header
from src.ui.components import create_file_pick_button

def main_app(page: ft.Page):
    page.title = 'Consilidado'

    select_file_text = ft.Text(value='', size=14, color=ft.Colors.BLACK)

    def handle_file_pick(e: ft.FilePickerResultEvent):
        if e.files:
            file_name = e.files[0].name
            select_file_text.value = f'Selected file : {file_name}'
            page.update()

    file_picker_dialog = ft.FilePicker(on_result=handle_file_pick)
    page.overlay.append(file_picker_dialog)

    
    select_file_button = create_file_pick_button(
        file_picker_dialog.pick_files,
        'Choose files ...'
    )

    main_content = ft.Column(
        [
            ft.Text('DataTable')
        ]
    )

    print(file_picker_dialog)

    page.appbar = create_header(select_file_button, select_file_text)

    page.add(
        ft.Row(
            [
                create_sidebar(),
                ft.VerticalDivider(width=1),
                main_content
            ],
            expand=True
        )
    )

ft.app(main_app)