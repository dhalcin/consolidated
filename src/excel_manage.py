import pandas as pd

file_name = None
df = None

def open_excel(filename, sheet):
    global file_name, df
    file_name = filename
    df = pd.read_excel(filename, sheet)

drop_columns = [
    'column_one',
    'column_two',
    'column_three',
    'column_four',
    'column_five'
]

def remove_columns():
    df.drop(columns=drop_columns, inplace=True)
    print(df)

def search_information(document):
    patient = df.loc[df['label'] == document]
    print(patient)