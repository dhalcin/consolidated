import flet as ft

def main_content():

    example_data = [
        'L01',
        'L02',
        'L03',
        'L04',
        'L05'
    ]

    data = []

    for lt in example_data:
        data.append(ft.DropdownOption(
            key=lt,
            content=ft.Text(lt, color=ft.Colors.BLACK)
        ))

    return ft.Column(
        [
            ft.ResponsiveRow(
                [
                    ft.Container(
                        content=ft.Dropdown(
                            label=ft.Text('# Lote', color='black'),
                            editable=True,
                            options=data,
                            expand=True,
                            bgcolor=ft.Colors.WHITE,
                        ),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Dropdown(
                            label=ft.Text('# Lote', color='black'),
                            editable=True,
                            options=data,
                            expand=True,
                            bgcolor=ft.Colors.WHITE
                        ),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Dropdown(
                            label=ft.Text('# Lote', color='black'),
                            editable=True,
                            options=data,
                            expand=True,
                            bgcolor=ft.Colors.WHITE
                        ),
                        col={'sm': 6}
                    ),
                    ft.Container(
                        content=ft.Dropdown(
                            label=ft.Text('# Lote', color='black'),
                            editable=True,
                            options=data,
                            expand=True,
                            bgcolor=ft.Colors.WHITE
                        ),
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
                [ft.Text(value='Datos Generales', color='red')],
                alignment=ft.MainAxisAlignment.START,
                expand=True
            ),
            #! main content
            main_content()
        ],
        expand=True
    )