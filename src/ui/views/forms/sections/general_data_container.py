import flet as ft

def create_options(list_options):
    options = []

    for op in list_options:
        options.append(ft.DropdownOption(
            key=op,
            content=ft.Text(op, color=ft.Colors.BLACK)
        ))

    return options

def content_label(label):
    return ft.Text(label, color='black')

def dropdown(label, options):
    return ft.Dropdown(
        label=content_label(label),
        editable=True,
        options=create_options(options),
        expand=True,
        bgcolor=ft.Colors.WHITE
    ) 

def main_content():

    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container( 
                        content=dropdown('# Batch', ['L01', 'L02', 'L03']),
                        col={'sm': 6}
                    ),
                    ft.Container( 
                        content=dropdown('# Sheet', ['1', '2', '3']),
                        col={'sm': 6}
                    ),
                    ft.Container( 
                        content=dropdown('# Reg', ['1', '2', '3']),
                        col={'sm': 6}
                    ),
                    ft.Container( 
                        content=dropdown('Date', ['11', '22', '34']),
                        col={'sm': 6}
                    )
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