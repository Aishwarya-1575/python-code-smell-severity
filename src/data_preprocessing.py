import pandas as pd
from pathlib import Path

# 1. Load raw dataset
raw_path = Path("data/raw/dataset.csv")
df = pd.read_csv(raw_path)

print(f"📄 Raw dataset: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Check if 'Severity' already exists
if 'Severity' not in df.columns:
    print("⚠️ 'Severity' column not found. Generating severity scores...")

    # Example rule-based severity calculation
    # Change 'LinesOfCode' and 'Complexity' to match your dataset's column names
    if 'LinesOfCode' in df.columns and 'Complexity' in df.columns:
        df['SeverityScore'] = df['LinesOfCode'] * 0.6 + df['Complexity'] * 0.4

        # Convert numeric score into categories
        def map_severity(score):
            if score < 50:
                return 0  # Low
            elif score < 100:
                return 1  # Medium
            else:
                return 2  # High

        df['Severity'] = df['SeverityScore'].apply(map_severity)
        df.drop(columns=['SeverityScore'], inplace=True)
    else:
        raise ValueError("Dataset missing required columns for severity calculation.")
else:
    print("✅ Using existing 'Severity' column from dataset.")

# 3. Save processed data
processed_path = Path("data/processed/dataset.csv")
processed_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_path, index=False)

print(f"💾 Processed dataset saved to {processed_path}")
