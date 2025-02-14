import pandas as pd

def strip_data(series):    
    if not isinstance(series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    
    strip_column = series.str.replace(r'^[\d_,;.\-/# ]+|[\d_,;.\-/# ]+$', '', regex=True)
    return(strip_column)
