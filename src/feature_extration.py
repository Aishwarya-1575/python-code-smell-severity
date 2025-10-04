# src/feature_extration.py

import pandas as pd
import os

def extract_features(input_csv, output_csv):
    """
    Reads the raw dataset, performs basic feature extraction,
    and saves the processed features to a new CSV.
    """

    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Dataset not found: {input_csv}")

    # Load raw dataset
    df = pd.read_csv(input_csv)

    # ---- Example Feature Extraction for Python Code Smell Dataset ----
    # Assuming dataset has 'code', 'smell_type', 'severity' columns
    if 'code' in df.columns:
        # Feature 1: Length of the code snippet
        df['code_length'] = df['code'].apply(lambda x: len(str(x)))

        # Feature 2: Number of lines
        df['num_lines'] = df['code'].apply(lambda x: str(x).count("\n") + 1)

        # Feature 3: Average line length
        df['avg_line_length'] = df.apply(
            lambda row: row['code_length'] / row['num_lines'] if row['num_lines'] > 0 else 0,
            axis=1
        )

        # Feature 4: Number of functions defined
        df['num_functions'] = df['code'].apply(lambda x: str(x).count("def "))

        # Feature 5: Number of classes defined
        df['num_classes'] = df['code'].apply(lambda x: str(x).count("class "))

    else:
        print("⚠ Warning: 'code' column not found, skipping code-based features.")

    # Save processed features
    df.to_csv(output_csv, index=False)
    print(f"✅ Features extracted and saved to: {output_csv}")


if __name__ == "__main__":
    raw_data_path = os.path.join("data", "raw", "raw_dataset.csv")
    processed_data_path = os.path.join("data", "processed", "processed_dataset.csv")

    extract_features(raw_data_path, processed_data_path)
