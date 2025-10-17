#!/usr/bin/env python3
from src import get_data
import time

def main():
    file = get_data('File name')

    time.sleep(1.5)

    print(f'\nFile "{file}" found and ready to use.\n')

    user_selection = get_data(
        'Wath do you wish to perform:\n1. Perfom search \n2. Remove columns\n>'
    )

    if user_selection == '1':
        print('Perfom search')
    
    elif user_selection == '2':
        print('Remove colummns')

    else:
        print('Invalid Option')


if __name__ == '__main__':
    main()
