import pandas as pd

def number_of_duplicates(dataframe):
    df_new = dataframe.drop_duplicates()

    new_rows = len(df_new)
    old_rows = len(dataframe)
    return(old_rows-new_rows)

