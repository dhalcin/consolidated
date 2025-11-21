from src.ui.components import create_sidebar
from src.ui.components import create_header
from src.ui.components import create_file_pick_button
from src.data_logic import open_excel, get_columns, get_rows, load_and_clean_excel
from src.ui.views import create_table_view
import flet as ft 
import asyncio

async def main_app(page: ft.Page):
    page.title = 'Consolidado'
    
    select_file_text = ft.Text(value='', size=14, color=ft.Colors.BLACK)
    async def handle_file_pick(e: ft.FilePickerResultEvent):
        if e.files:
            file_name = e.files[0].name
            file_path = e.files[0].path
            select_file_text.value = f'Selected file : {file_name}'
            page.update()
            await on_file_selected(file_path)

    view_columns_container = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
        scroll=ft.ScrollMode.ALWAYS
    )

    loader_overlay = ft.Container(
        content=ft.ProgressBar(width=400),
        alignment=ft.alignment.center,
        expand=True,
        visible=False
    )

    table_stactk = ft.Stack(
        [
            ft.Container(
                content=view_columns_container,
                alignment=ft.alignment.top_left
            ),
            loader_overlay
        ],
        expand=True
    )

    async def on_file_selected(file_path):
        loader_overlay.visible = True
        page.update()

        await asyncio.sleep(0.1)

        df = await asyncio.to_thread(open_excel, file_path)
        columns = await asyncio.to_thread(get_columns, df)
        rows = await asyncio.to_thread(get_rows, df)
        await asyncio.to_thread(load_and_clean_excel, df, columns)

        limited_rows = rows[:100]
        table_view_widget = await asyncio.to_thread(create_table_view, columns, limited_rows)
        view_columns_container.controls = [table_view_widget]
        loader_overlay.visible = False
        page.update()

    file_picker_dialog = ft.FilePicker(on_result=handle_file_pick)
    page.overlay.append(file_picker_dialog)

    select_file_button = create_file_pick_button(
        file_picker_dialog.pick_files,
        'Choose files ...'
    )

    page.appbar = create_header(select_file_button, select_file_text)

    page.add(
        ft.Row(
            [
                create_sidebar(),
                ft.VerticalDivider(width=1),
                table_stactk
            ],
            expand=True
        )
    )