import pandas as pd

def open_excel(file_path):
    df = pd.read_excel(file_path, 'Consolidado')
    return df

def get_columns(df):
    all_columns = (df.columns.values).tolist()
    return all_columns

def get_rows(df):
    return df.values.tolist()

def load_and_clean_excel(df, columns):
    for column_name in columns:
        # Ensure that the 'label' column is a string and clean values such as '.0'
        if df[column_name].dtype != 'object':
            df[column_name] = df[column_name].astype(str)

        df[column_name] = df[column_name].str.replace('.0', '', regex=False)