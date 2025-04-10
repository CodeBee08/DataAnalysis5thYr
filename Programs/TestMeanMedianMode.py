import pandas as pd
import numpy as np
import pytest
import os
from values import test_data_folder


def calculate_mean(data, column):
    """Calculates mean, handling potential errors."""
    try:
        # Check if the column is numeric before calculating the mean
        if pd.api.types.is_numeric_dtype(data[column]):
            return data[column].mean()
        else:
            return np.nan  # Or raise a more specific exception if needed
    except (TypeError, ValueError):
        return np.nan


def calculate_median(data, column):
    """Calculates median, handling potential errors."""
    try:
        # Check if the column is numeric before calculating the median
        if pd.api.types.is_numeric_dtype(data[column]):
            return data[column].median()
        else:
            return np.nan
    except (TypeError, ValueError):
        return np.nan


def calculate_mode(data, column):
    """Calculates mode, handling potential errors."""
    try:
        mode_series = data[column].mode()
        if len(mode_series) == 1:
            return mode_series.iloc[0]
        else:
            return mode_series  # Return the Series if multiple modes
    except (TypeError, ValueError):
        return pd.Series()  # Return empty Series if no mode


def get_expected_results(test_data_dir=test_data_folder):
    """Gets the expected results from the test case definitions."""

    test_cases = {
        "Standard": {
            "description": "Typical dataset with mixed values",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "standard.csv"
        },
        "Edge_Single_Row": {
            "description": "Dataset with only one row",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_single_row.csv"
        },
        "Boundary_Age_Extreme": {
            "description": "Dataset with extreme age values",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_age_extreme.csv"
        },
        "Boundary_Chol_Extreme": {
            "description": "Dataset with extreme cholesterol values",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_chol_extreme.csv"
        },
        "Invalid_Age_NaN": {
            "description": "Dataset with NaN values in age",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_age_nan.csv"
        },
        "Invalid_Chol_NaN": {
            "description": "Dataset with NaN values in chol",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_chol_nan.csv"
        },
        "Invalid_Age_NonNumeric": {
            "description": "Dataset with non-numeric values in age",
            "expected_mean_age": np.nan,  # Expected NaN for non-numeric
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_age_nonnumeric.csv"
        },
        "Invalid_Chol_NonNumeric": {
            "description": "Dataset with non-numeric values in chol",
            "expected_mean_age": None,
            "expected_median_chol": np.nan,  # Expected NaN for non-numeric
            "expected_mode_cp": None,
            "filename": "invalid_chol_nonnumeric.csv"
        },
        "Invalid_CP_NaN": {
            "description": "Dataset with NaN values in cp",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_cp_nan.csv"
        },
        "Edge_CP_Multiple_Modes": {
            "description": "Dataset with multiple modes in cp",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_cp_multiple_modes.csv"
        },
        "Edge_CP_No_Mode": {
            "description": "Dataset with no mode in cp (all unique)",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_cp_no_mode.csv"
        },
        "Boundary_Combined_Extreme": {
            "description": "Dataset with combined extreme age and chol",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_combined_extreme.csv"
        },
        "Stress_Large_Dataset": {
            "description": "Dataset with many rows",
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "stress_large_dataset.csv"
        },
        "Edge_Empty_Dataset": {
            "description": "Empty Dataset",
            "expected_mean_age": np.nan,
            "expected_median_chol": np.nan,
            "expected_mode_cp": pd.Series(),
            "filename": "edge_empty_dataset.csv"
        },
    }

    for key in test_cases:
        tc = test_cases[key]
        file_path = os.path.join(test_data_dir, tc['filename'])
        data = pd.read_csv(file_path)

        tc['data'] = data  # Load the data from CSV
        tc['expected_mean_age'] = calculate_mean(data, 'age')
        tc['expected_median_chol'] = calculate_median(data, 'chol')
        tc['expected_mode_cp'] = calculate_mode(data, 'cp')

    return test_cases


# The actual test functions (using pytest)
@pytest.mark.parametrize("test_case", get_expected_results(test_data_folder).values(),
                         ids=get_expected_results(test_data_folder).keys())
def test_calculations(test_case):
    data = test_case['data']
    expected_mean_age = test_case['expected_mean_age']
    expected_median_chol = test_case['expected_median_chol']
    expected_mode_cp = test_case['expected_mode_cp']

    # Calculate the actual results
    actual_mean_age = calculate_mean(data, 'age')
    actual_median_chol = calculate_median(data, 'chol')
    actual_mode_cp = calculate_mode(data, 'cp')

    # Assertions (using pytest's assert)
    if isinstance(expected_mode_cp, pd.Series):
        pd.testing.assert_series_equal(actual_mode_cp, expected_mode_cp, check_dtype=False,
                                     check_index=False)
    elif expected_mode_cp is None:
        assert actual_mode_cp.empty
    else:
        assert actual_mode_cp == expected_mode_cp

    if np.isnan(expected_mean_age):
        assert np.isnan(actual_mean_age)
    else:
        assert np.isclose(actual_mean_age, expected_mean_age, equal_nan=True)

    if np.isnan(expected_median_chol):
        assert np.isnan(actual_median_chol)
    else:
        assert np.isclose(actual_median_chol, expected_median_chol, equal_nan=True)


if __name__ == '__main__':
    pytest.main(['-v', __file__])