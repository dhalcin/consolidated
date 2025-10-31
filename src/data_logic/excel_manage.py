import pandas as pd

def open_excel(file_path):
    df = pd.read_excel(file_path, 'Consolidado')
    return df

def get_columns(df):
    all_columns = (df.columns.values).tolist()
    return all_columns