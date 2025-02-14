import pytest
import pandas as pd
from duplicates_utils import number_of_duplicates


@pytest.mark.parametrize("dataframe, expected", [
    (pd.DataFrame({"A": [1, 2, 2, 3]}), 1),  
    (pd.DataFrame({"A": [1, 2, 3, 4]}), 0), 
    (pd.DataFrame({"A": [1, 1, 1, 1], "B": [2, 2, 2, 2]}), 3), 
    (pd.DataFrame(), 0),  
])
def test_number_of_duplicates_valid(dataframe, expected):
    assert number_of_duplicates(dataframe) == expected


def test_number_of_duplicates_series():
    series = pd.Series([1, 2, 2, 3])
    assert number_of_duplicates(series) == 1  

@pytest.mark.parametrize("bad_input", [
    123,  
    "Hello",  
    12.34,  
    None,  
    [1, 2, 3],  
    {"key": "value"},  
    (1, 2, 3),  
    {1, 2, 3}  
])

def test_number_of_duplicates_invalid_input(bad_input):
    with pytest.raises(TypeError):
        number_of_duplicates(bad_input)