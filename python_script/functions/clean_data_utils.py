import pandas as pd

def strip_data(series):
    strip_column = series.str.replace(r'^[\d_,;.\-/# ]+|[\d_,;.\-/# ]+$', '', regex=True)
    return(strip_column)
