import pandas as pd

file_name = None
df = None

def open_excel(filename, sheet):
    global file_name, df
    file_name = filename
    df = pd.read_excel(filename, sheet)

def get_columns():
    all_columns = (df.columns.values).tolist()
    return all_columns

def load_and_clean_excel(columns):
    for column_name in columns:
        # Ensure that the 'label' column is a string and clean values such as '.0'
        if df[column_name].dtype != 'object':
            df[column_name] = df[column_name].astype(str)

        df[column_name] = df[column_name].str.replace('.0', '', regex=False)

def remove_columns(drop_columns):
    df.drop(columns=drop_columns, inplace=True)
    print(df)

def search_information(label, value):
    # Select rows where 'label' matchs the document
    patient = df.loc[df[label] == value] 
    print(patient)