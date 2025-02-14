import pandas as pd

def number_of_duplicates(input_dataframe):
    if not isinstance(input_dataframe, (pd.DataFrame, pd.Series)):
        raise TypeError("Input must be a pandas DataFrame or Series")
    
    df_new = input_dataframe.drop_duplicates()

    new_rows = len(df_new)
    old_rows = len(input_dataframe)
    return(old_rows-new_rows)

