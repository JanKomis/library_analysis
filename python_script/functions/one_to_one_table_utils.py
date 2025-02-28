import pandas as pd
import ast

import ast

def validate_value(value):
    if value is None or isinstance(value, (int, float, bool, str)):
        return True

    raise ValueError(f"Invalid value: {value}")

def create_one_to_one_table(input_df, column_name):
    if not isinstance(input_df, (pd.DataFrame)):
        raise TypeError("Input must be a pandas DataFrame")
    
    required_columns = {column_name}
    if not required_columns.issubset(input_df.columns):
        missing = required_columns - set(input_df.columns)
        raise ValueError(f"Missing required columns: {missing}")
    

    df = input_df.copy()
    df[column_name].apply(validate_value)
    
    df[column_name] = df[column_name].astype(str).str.strip()
    
    
    unique_values = pd.DataFrame({'id': range(1, len(df[column_name].unique()) + 1), 
                                  column_name: df[column_name].unique()})
    
    unique_values[column_name] = unique_values[column_name].astype(input_df[column_name].dtype)
    
    value_mapping = dict(zip(unique_values[column_name], unique_values['id']))
    
    return unique_values, value_mapping