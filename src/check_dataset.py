import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\Aishwarya\OneDrive\Desktop\severity-code-smell\data\processed\dataset.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

# Display dataset info (types + missing values)
print("\nDataset Info:")
print(df.info())

# Display numeric statistics
print("\nNumeric statistics:")
print(df.describe())

# Display category distribution for 'Data set'
print("\nCategory distribution for 'Data set':")
print(df['Data set'].value_counts())


