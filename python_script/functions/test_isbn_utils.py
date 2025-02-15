import pandas as pd
import pytest
from isbn_utils import contain_isbn13


def test_contain_isbn13_valid_input():
    data = pd.Series(["9783161484100", "9781234567897", "invalid", None, "9780306406157"])
    expected = pd.Series([True, True, False, False, True])
    result = contain_isbn13(data)
    pd.testing.assert_series_equal(result, expected)

@pytest.mark.parametrize("invalid_input", [
    "not a series", 
    123, 
    12.34, 
    None, 
    ["9783161484100", "9781234567897"], 
    {"key": "9783161484100"}
])
def test_contain_isbn13_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        contain_isbn13(invalid_input)