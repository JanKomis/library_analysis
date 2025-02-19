import pandas as pd

def number_of_duplicates(input_dataframe):
    if not isinstance(input_dataframe, (pd.DataFrame, pd.Series)):
        raise TypeError("Input must be a pandas DataFrame or Series")
    
    df_new = input_dataframe.drop_duplicates()

    new_rows = len(df_new)
    old_rows = len(input_dataframe)
    return(old_rows-new_rows)


def normalize_id(input_dataframe, key_column, id_column, replace_text = 'Unknown'):
    if not isinstance(input_dataframe, (pd.DataFrame)):
        raise TypeError("Input must be a pandas DataFrame")
    
    required_columns = {key_column, id_column}
    if not required_columns.issubset(input_dataframe.columns):
        missing = required_columns - set(input_dataframe.columns)
        raise ValueError(f"Missing required columns: {missing}")
    
    if set(input_dataframe.columns) != required_columns:
        extra_columns = set(input_dataframe.columns) - required_columns
        raise ValueError(f"DataFrame contains extra columns: {extra_columns}")
    
    df = input_dataframe.copy()
    df[key_column] = df[key_column].replace(['', None, 'Null'], replace_text)

    min_ids = df.groupby(key_column, as_index=False)[id_column].min()
    df = df.merge(min_ids, on=key_column, suffixes=('', '_min'))
    
    id_mapping = dict(zip(df[id_column], df[f'{id_column}_min']))
    df[id_column] = df[f'{id_column}_min']
    df.drop(columns=[f'{id_column}_min'], inplace=True)
    df_unique = df.drop_duplicates(subset=[key_column])
    
    return df_unique, id_mapping

