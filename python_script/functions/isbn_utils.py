import isbnlib
import pandas as pd

def contain_isbn13(pandas_series):
    if not isinstance(pandas_series, pd.Series):
        raise TypeError("Input must be a pandas Series")
    
    return pandas_series.apply(lambda isbn: False 
                               if pd.isna(isbn) 
                               else isbnlib.is_isbn13(str(isbn))).astype(bool)


