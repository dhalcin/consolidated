import flet as ft
from src.ui.components import create_sidebar
from src.ui.components import create_header
from src.ui.components import create_file_pick_button
from src.data_logic import open_excel

def main_app(page: ft.Page):
    page.title = 'Consolidado'

    select_file_text = ft.Text(value='', size=14, color=ft.Colors.BLACK)

    def handle_file_pick(e: ft.FilePickerResultEvent, on_file_selected: callable):
        global manage_file
        if e.files:
            file_name = e.files[0].name
            file_path = e.files[0].path
            select_file_text.value = f'Selected file : {file_name}'
            on_file_selected(file_path)
            page.update()

    def on_file_selected(path):
        file_path = open_excel(path)
        print(file_path)

    file_picker_dialog = ft.FilePicker(
        on_result=lambda e: handle_file_pick(e, on_file_selected)
    )
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