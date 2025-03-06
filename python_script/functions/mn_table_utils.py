import pandas as pd
import ast


def parse_value(value):
    if isinstance(value, str):  
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):  
            return value[1:-1].split(",") 
        else:
            return [value] 
    elif isinstance(value, list):  
        return value
    else:
        raise ValueError(f"Neplatný formát: {value}")

def create_mn_table(input_df, id_column, key_column):
    if not isinstance(input_df, (pd.DataFrame)):
        raise TypeError("Input must be a pandas DataFrame")
    
    required_columns = {key_column, id_column}
    if not required_columns.issubset(input_df.columns):
        missing = required_columns - set(input_df.columns)
        raise ValueError(f"Missing required columns: {missing}")
    
    df = input_df.copy()
    df[key_column] = df[key_column].apply(parse_value)

    exploded_df = df.explode(key_column)

    exploded_df.reset_index(drop=True, inplace=True)

    final_df = exploded_df[[id_column, key_column]].rename(
        columns={id_column: 'main_id', 
                 key_column: f'{key_column}_id'})

    return final_df