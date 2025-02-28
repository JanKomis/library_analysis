import pytest
import pandas as pd
import ast
import re
from one_to_one_table_utils import (validate_value, 
                                    create_one_to_one_table)


@pytest.mark.parametrize("value, expected", [
    ("123", True),
    ("3.14", True),
    ("True", True),
    ("'string'", True),
    ("[1, 2, 3]", True), 
    ("{'key': 'value'}", True),
    ("('hello','good afternoon')", True),
    (123, True),
    (3.14, True),
    (True, True),
    (None, True),  
    ([], False),  
    ({}, False), 
    (('hello','good afternoon'),False), 
])

def test_validate_value(value, expected):
    if expected:
        assert validate_value(value) is True
    else:
        with pytest.raises(ValueError):
            validate_value(value)


##########################################################
@pytest.mark.parametrize(
    "input_data, column_name, expected_unique_values, expected_mapping",
    [
        (
            pd.DataFrame({"category": ["A", "B", "C", "A", "B"]}),
            "category",
            pd.DataFrame({"id": [1, 2, 3], "category": ["A", "B", "C"]}),
            {"A": 1, "B": 2, "C": 3}
        ),
        (
            pd.DataFrame({"number": [1, 2, 2, 3, 1]}),
            "number",
            pd.DataFrame({"id": [1, 2, 3], "number": [1, 2, 3]}),
            {1: 1, 2: 2, 3: 3}
        ),
        (
            pd.DataFrame({"values": ["True", "False", "True", "False"]}),
            "values",
            pd.DataFrame({"id": [1, 2], "values": ["True", "False"]}),
            {"True": 1, "False": 2}
        ),
    ]
)

def test_create_one_to_one_table(input_data, column_name, expected_unique_values, expected_mapping):
    unique_values, value_mapping = create_one_to_one_table(input_data, column_name)
    
    pd.testing.assert_frame_equal(unique_values.sort_values(by="id").reset_index(drop=True), 
                                  expected_unique_values.sort_values(by="id").reset_index(drop=True))
    assert value_mapping == expected_mapping


@pytest.mark.parametrize(
    "input_data, column_name, expected_exception, expected_message",
    [
        ([], "category", TypeError, "Input must be a pandas DataFrame"),
        (pd.DataFrame({}), "category", ValueError, "Missing required columns: {'category'}"),
        (pd.DataFrame({"category": [[1, 2], [3, 4]]}), "category", ValueError, "Invalid value: [1, 2]")
    ]
)
def test_create_one_to_one_table_invalid(input_data, column_name, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=re.escape(expected_message)):
        create_one_to_one_table(input_data, column_name)
        