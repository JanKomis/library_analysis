import pandas as pd
import pytest
from clean_data_utils import strip_data

@pytest.mark.parametrize("input_series, expected_series", [
    (pd.Series(["  123abc456  "]), pd.Series(["abc"])), 
    (pd.Series(["_#Hello World!#_"]), pd.Series(["Hello World!"])),  
    (pd.Series(["...test..."]), pd.Series(["test"])), 
    (pd.Series(["###test###"]), pd.Series(["test"])),  
    (pd.Series(["no_change"]), pd.Series(["no_change"])),
    (pd.Series(["123"]), pd.Series([""])),  
    (pd.Series(["  "]), pd.Series([""])),  
    (pd.Series(["-"]), pd.Series([""])),  
    (pd.Series(["Hello, world!"]), pd.Series(["Hello, world!"])),  
    (pd.Series([None]), pd.Series([None])),  
    (pd.Series([pd.NA]), pd.Series([pd.NA])),  
])


def test_strip_data(input_series, expected_series):
    pd.testing.assert_series_equal(strip_data(input_series), expected_series)

@pytest.mark.parametrize("bad_input", [
    123,  
    "Hello",  
    12.34,  
    pd.DataFrame({"col": ["Hello", "World"]}), 
    None,
    [1, 2, 3],  
    {"key": "value"},  
    (1, 2, 3),  
    {1, 2, 3} 
])

def test_bad_type(bad_input):
    with pytest.raises(TypeError):
        strip_data(bad_input)
