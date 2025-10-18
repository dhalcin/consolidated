#!/usr/bin/env python3
from src import get_data
from src import find_excel_file
from src import open_excel, remove_columns, search_information
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

    user_selection = get_data(
        'Wath do you wish to perform:\n1. Perfom search \n2. Remove columns\n>'
    )

    if user_selection == '1':
        print('Perfom search')
        document = get_data('Document Number')
        search_information(document)


    elif user_selection == '2':
        print('Remove colummns')
        remove_columns()

    else:
        print('Invalid Option')


if __name__ == '__main__':
    main()
