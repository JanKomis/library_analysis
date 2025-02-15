import pandas as pd
import pytest
from lang_utils import contain_lang

@pytest.mark.parametrize("valid_input, expected", [
    (pd.Series(["en", "fr", "xyz", None, "de"]), 
     pd.Series([True, True, False, False, True], dtype=bool)),  
    (pd.Series(["crp", "en", "zh", "xyz"]), 
     pd.Series([True, True, True, False], dtype=bool))
])

def test_contain_lang_valid_input(valid_input,expected):
    #data = pd.Series(["en", "fr", "xyz", None, "de"])
    #expected = pd.Series([True, True, False, False, True])
    result = contain_lang(valid_input)
    pd.testing.assert_series_equal(result, expected)

@pytest.mark.parametrize("invalid_input", [
    "not a series", 
    123, 
    12.34, 
    None, 
    ["en", "fr"], 
    {"key": "9783161484100"}
])

def test_contain_lang_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        contain_lang(invalid_input)