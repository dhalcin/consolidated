#!/usr/bin/env python3
from src import get_data
from src import find_excel_file
from src import open_excel, get_columns, load_and_clean_excel, remove_columns, search_information
import time

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

    user_selection = get_data(
        'Wath do you wish to perform:\n1. Remove columns \n2. Perfom search\n>'
    )

    if user_selection == '1':
        print('Select the column to delete')
        time.sleep(1.5)
        for column, index in enumerate(columns):
            print(f'{index}. {column}')

        drop_columns = []
        while True:
            select_columns= get_data(
                'Column to be deleted\n'
                'Cancel\n'
            )

            if select_columns == 'cancel':
                break

            for column in select_columns.split():
                drop_columns.append(columns[int(column)])
        
        if len(drop_columns) > 0:
            print('\nRemoving columns ...\n')
            time.sleep(1)
            remove_columns(drop_columns)

    if user_selection == '2':
        print('Perfom search')
        label = get_data('\nName of the label to be selected')

        if label == 'Patient_Document_Number':
            dni = get_data('\nDocument')
            search_information(label, dni)
  
    else:
        print('Invalid Option')


if __name__ == '__main__':
    main()
