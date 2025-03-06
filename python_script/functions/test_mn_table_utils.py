import pytest
import pandas as pd
from mn_table_utils import create_mn_table 

@pytest.mark.parametrize("input_data, id_column, key_column, expected_output", [
    (
        pd.DataFrame({
            'id': [],
            'keys': []
        }),
        'id',
        'keys',
        pd.DataFrame({
            'main_id': [],
            'keys_id': []
        })
    ),
    (
        pd.DataFrame({
            'id': [1],
            'keys': [['X', 'Y']]
        }),
        'id',
        'keys',
        pd.DataFrame({
            'main_id': [1, 1],
            'keys_id': ['X', 'Y']
        })
    )
])
def test_create_mn_table(input_data, id_column, key_column, expected_output):
    result = create_mn_table(input_data, id_column, key_column)
    pd.testing.assert_frame_equal(result, expected_output, check_dtype=False)

@pytest.mark.parametrize("invalid_input", [
    None, 
    "string", 
    123, 
    [1, 2, 3]
])
def test_create_mn_table_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        create_mn_table(invalid_input, 'id', 'keys')


@pytest.mark.parametrize("bad_format_df", [
    pd.DataFrame({'id': [1, 2]}),
    pd.DataFrame({'keys': ['A', 'B']}),
])
def test_create_mn_table_invalid_dataframe(bad_format_df):
    with pytest.raises(ValueError):
        create_mn_table(bad_format_df, 'id', 'keys')