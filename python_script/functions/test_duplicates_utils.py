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

def test_number_of_duplicates_invalid(bad_input):
    with pytest.raises(TypeError):
        number_of_duplicates(bad_input)


#################################################
from duplicates_utils import normalize_id

@pytest.mark.parametrize(
    "input_data, key_column, id_column, replace_text, expected_output, expected_mapping",
    [
        # Basic test
        (
            pd.DataFrame({"key": ["A", "B", "A"], "id": [3, 2, 1]}),
            "key",
            "id",
            "Unknown",
            pd.DataFrame({"key": ["A", "B"], "id": [1, 2]}),
            {3: 1, 2: 2, 1: 1},
        ),
        # Missing values in key_column
        (
            pd.DataFrame({"key": [None, "B", "A"], "id": [3, 2, 1]}),
            "key",
            "id",
            "Unknown",
            pd.DataFrame({"key": ["Unknown", "B", "A"], "id": [3, 2, 1]}),
            {3: 3, 2: 2, 1: 1},
        ),
        # Duplicates id values
        (
            pd.DataFrame({"key": ["A", "A", "A"], "id": [5, 3, 1]}),
            "key",
            "id",
            "Unknown",
            pd.DataFrame({"key": ["A"], "id": [1]}),
            {5: 1, 3: 1, 1: 1},
        ),
        # Empty dataframe
        (
            pd.DataFrame(columns=["key", "id"]),
            "key",
            "id",
            "Unknown",
            pd.DataFrame(columns=["key", "id"]),
            {},
        ),
    ]
)
def test_normalize_id(input_data, key_column, id_column, replace_text, expected_output, expected_mapping):
    result_df, result_mapping = normalize_id(input_data, key_column, id_column, replace_text)
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_output.reset_index(drop=True))
    assert result_mapping == expected_mapping


@pytest.mark.parametrize(
    "input_data, key_column, id_column, expected_exception, expected_message",
    [
        ("not a dataframe", "key", "id", TypeError, "Input must be a pandas DataFrame"),
        (pd.DataFrame({"key": ["A", "B"], "id": [1, 2]}), "wrong_key", "id", ValueError, "Missing required columns: {'wrong_key'}"),
        (pd.DataFrame({"key": ["A", "B"], "extra": [1, 2]}), "key", "id", ValueError, "Missing required columns: {'id'}"),
        (pd.DataFrame({"key": ["A", "B"], "id": [1, 2], "extra": [3, 4]}), "key", "id", ValueError, "DataFrame contains extra columns: {'extra'}"),
    ]
)
def test_normalize_id_exceptions(input_data, key_column, id_column, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        normalize_id(input_data, key_column, id_column)