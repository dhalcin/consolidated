import os

def find_excel_file(filename, search_path):
    for root, dir, files, in os.walk(search_path):
        if filename in files:
            result = os.path.join(root, filename)
            return result
    