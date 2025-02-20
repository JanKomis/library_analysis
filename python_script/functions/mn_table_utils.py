import pandas as pd
import ast


def parse_value(value):
    if isinstance(value, str):  # Pouze pokud je to string
        value = value.strip()  # Odstraníme mezery
        if value.startswith("[") and value.endswith("]"):  # Ujistíme se, že jde o seznamový formát
            return value[1:-1].split(",")  # Rozdělíme podle čárek
        else:
            return [value]  # Pokud je to jen jediná hodnota (bez závorek), vrátíme ji jako seznam
    elif isinstance(value, list):  # Pokud už je to list, vrátíme jej beze změny
        return value
    else:
        raise ValueError(f"Neplatný formát: {value}")

"""
def parse_value(value):
    if isinstance(value, str):  # Pokud je string, pokusíme se jej převést
        try:
            parsed_value = ast.literal_eval(value)
            if not isinstance(parsed_value, list):  # Kontrola, zda je výsledek list
                raise ValueError(f"Invalid format in column: {value} (not a list)")
            return parsed_value
        except (ValueError, SyntaxError):
            raise ValueError(f"Invalid format in column: {value} (not a valid list string)")
    elif isinstance(value, list):  
        return value
    else:
        raise TypeError("Column must contain only lists or valid list strings.")
"""
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
    exploded_df.insert(0, 'unique_id', range(1, len(exploded_df) + 1))

    final_df = exploded_df[['unique_id', id_column, key_column]].rename(
    columns={'unique_id': 'id', id_column: 'main_id', key_column: f'{key_column}_id'})

    return final_df