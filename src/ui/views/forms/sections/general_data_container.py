import flet as ft

def create_options(list_options):
    options = []

    for op in list_options: # The list_options list is just an example list 
        options.append(ft.DropdownOption(
            key=op,
            content=ft.Text(op, color=ft.Colors.BLACK)
        ))

    return options

def content_label(label):
    return ft.Text(value=label, color=ft.Colors.BLACK)

def dropdown(label, options):
    return ft.Dropdown(
        label=content_label(label),
        editable=True,
        options=create_options(options),
        expand=True,
        bgcolor=ft.Colors.WHITE
    ) 

def create_container(label, options):
    return ft.Container(
        content=dropdown(label, options),
        col={'sm': 6}
    )

def main_content():
    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    create_container('# Batch', ['L01', 'L02', 'L03']),
                    create_container('# Sheet', ['1', '2', '3']),
                    create_container('# Reg', ['1', '2', '3']),
                    create_container('Date', ['11', '22', '30'])
                ]
            )
        ]
    )

def build_general_data_container():
    return ft.Column(
        [
            #! title Data Generales
            ft.Row(
                [ft.Text(value='General Information', color='red')],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            #! main content
            main_content()
        ],
        expand=True
    )