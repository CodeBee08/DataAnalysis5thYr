import pandas as pd
import numpy as np
import os
from values import cleaned_csv_file

# Load the base dataset
df = pd.read_csv(cleaned_csv_file)  # Make sure this path is correct


def generate_test_data_csvs(output_dir='test_data'):
    """Generates test data CSV files."""

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    test_cases = {
        "Standard": {
            "description": "Typical dataset with mixed values",
            "data": df.copy(),
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "standard.csv"
        },
        "Edge_Single_Row": {
            "description": "Dataset with only one row",
            "data": df.iloc[[0]].copy(),
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_single_row.csv"
        },
        "Boundary_Age_Extreme": {
            "description": "Dataset with extreme age values",
            "data": df.copy(),
            "modifications": [('age', 0, df['age'].min() - 10), ('age', 1, df['age'].max() + 10)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_age_extreme.csv"
        },
        "Boundary_Chol_Extreme": {
            "description": "Dataset with extreme cholesterol values",
            "data": df.copy(),
            "modifications": [('chol', 2, 0), ('chol', 3, df['chol'].max() * 2)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_chol_extreme.csv"
        },
        "Invalid_Age_NaN": {
            "description": "Dataset with NaN values in age",
            "data": df.copy(),
            "modifications": [('age', 4, np.nan), ('age', 5, np.nan)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_age_nan.csv"
        },
        "Invalid_Chol_NaN": {
            "description": "Dataset with NaN values in chol",
            "data": df.copy(),
            "modifications": [('chol', 6, np.nan), ('chol', 7, np.nan)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_chol_nan.csv"
        },
        "Invalid_Age_NonNumeric": {
            "description": "Dataset with non-numeric values in age",
            "data": df.copy(),
            "modifications": [('age', 8, 'abc'), ('age', 9, 'def')],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "cast_age_to_object": True,
            "filename": "invalid_age_nonnumeric.csv"
        },
        "Invalid_Chol_NonNumeric": {
            "description": "Dataset with non-numeric values in chol",
            "data": df.copy(),
            "modifications": [('chol', 10, 'ghi'), ('chol', 11, 'jkl')],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "cast_chol_to_object": True,
            "filename": "invalid_chol_nonnumeric.csv"
        },
        "Invalid_CP_NaN": {
            "description": "Dataset with NaN values in cp",
            "data": df.copy(),
            "modifications": [('cp', 12, np.nan), ('cp', 13, np.nan)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "invalid_cp_nan.csv"
        },
        "Edge_CP_Multiple_Modes": {
            "description": "Dataset with multiple modes in cp",
            "data": df.copy(),
            "modifications": [('cp', 14, 0), ('cp', 15, 0), ('cp', 16, 1), ('cp', 17, 1)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_cp_multiple_modes.csv"
        },
        "Edge_CP_No_Mode": {
            "description": "Dataset with no mode in cp (all unique)",
            "data": df.copy().iloc[:10].copy(),
            "modifications": [('cp', i, i) for i in range(10)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_cp_no_mode.csv"
        },
        "Boundary_Combined_Extreme": {
            "description": "Dataset with combined extreme age and chol",
            "data": df.copy(),
            "modifications": [('age', 0, df['age'].min() - 10), ('age', 1, df['age'].max() + 10),
                              ('chol', 2, 0), ('chol', 3, df['chol'].max() * 2)],
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "boundary_combined_extreme.csv"
        },
        "Stress_Large_Dataset": {
            "description": "Dataset with many rows",
            "data": pd.concat([df.copy()] * 100, ignore_index=True),
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "stress_large_dataset.csv"
        },
        "Edge_Empty_Dataset": {
            "description": "Empty Dataset",
            "data": pd.DataFrame(columns=df.columns),
            "expected_mean_age": None,
            "expected_median_chol": None,
            "expected_mode_cp": None,
            "filename": "edge_empty_dataset.csv"
        },
    }

    for key in test_cases:
        tc = test_cases[key]
        if 'cast_age_to_object' in tc and tc['cast_age_to_object']:
            tc['data']['age'] = tc['data']['age'].astype(object)
        if 'cast_chol_to_object' in tc and tc['cast_chol_to_object']:
            tc['data']['chol'] = tc['data']['chol'].astype(object)

        if 'modifications' in tc:
            for col, index, value in tc['modifications']:
                tc['data'].loc[index, col] = value
            tc['data'] = tc['data'].reset_index(drop=True)

        # Calculate expected values *before* saving to CSV
        if tc['expected_mean_age'] is None:
            try:
                tc['expected_mean_age'] = tc['data']['age'].mean()
            except TypeError:
                tc['expected_mean_age'] = np.nan
        if tc['expected_median_chol'] is None:
            try:
                tc['expected_median_chol'] = tc['data']['chol'].median()
            except TypeError:
                tc['expected_median_chol'] = np.nan

        if tc['expected_mode_cp'] is None:
            try:
                tc['expected_mode_cp'] = tc['data']['cp'].mode()
                if isinstance(tc['expected_mode_cp'], pd.Series) and len(tc['expected_mode_cp']) == 1:
                    tc['expected_mode_cp'] = tc['expected_mode_cp'].iloc[0]
            except TypeError:
                tc['expected_mode_cp'] = pd.Series()

        # Save the DataFrame to a CSV file
        tc['data'].to_csv(os.path.join(output_dir, tc['filename']), index=False)


if __name__ == '__main__':
    generate_test_data_csvs()