#!/usr/bin/env python3
from src import get_data
from src import find_excel_file
from src import open_excel, get_columns, load_and_clean_excel, remove_columns, search_information
import time

def handle_user_input(columns):
 
    delete = None

    while True:
        user_selection = get_data(
            'Wath do you wish to perform:\n1. Remove columns \n2. Perfom search \n3. Exit\n'
        )

        if user_selection == '1':
            time.sleep(1.5)
            if not delete:
                print('Select the column to delete')
                time.sleep(1.5)
                for column, index in enumerate(columns): # All columns contained in the DataFrame
                    print(f'{index}. {column}')

            drop_columns = []

            while True:
                select_columns = get_data(
                    '1. Column to be deleted\n'
                    '2. Cancel\n'
                )

                if select_columns == 'cancel':
                    print('Canceling column deletion')
                    time.sleep(1.5)
                    break

                else:
                    print('eliminar columnas')
                    for column in select_columns.split(): # Iterate over the columns of the DataFrame and obtain the ones to be deleted
                        drop_columns.append(columns[int(column)])
                    break

            if len(drop_columns) > 0:
                print('\nRemoving columns ...\n')
                time.sleep(1)
                remove_columns(drop_columns)
                delete = True
                continue

        elif user_selection == '2':
            print('Perfom search')
            label = get_data('\nName of the label to be selected')

            if label == 'Patient_Document_Number':
                dni = get_data('\nDocument')
                search_information(label, dni)

        else:
            print('!Closing the program ...')
            return 'exit'
def main():
    file = get_data('File name')

    time.sleep(1)

    if find_excel_file(file, './'):
        print(f'\nFile "{file}", found and ready to use.\n')
        open_excel(file, 'Consolidado')
        
    else:
        print(f'\nFile "{file}", not found in system.\n')
        return 

    columns = get_columns()
    load_and_clean_excel(columns)

    user_selection = handle_user_input(columns)

    if user_selection == 'exit':
        return

if __name__ == '__main__':
    main()
