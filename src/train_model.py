# src/train_model.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os

# 1. Load processed data
data_path = r"data/processed/dataset.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Processed dataset not found at {data_path}")

df = pd.read_csv(data_path)
print(f"📄 Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

# 2. Ensure 'Severity' column exists
if 'Severity' not in df.columns:
    print("⚠️ 'Severity' column not found in dataset. Creating placeholder labels...")
    df['Severity'] = 0  # placeholder — replace with actual severity labels later

# 3. Features (X) and Target (y)
X = df.drop(columns=['Severity'])
y = df['Severity']

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate model
accuracy = model.score(X_test, y_test)
print(f"✅ Model trained successfully!")
print(f"📊 Accuracy: {accuracy:.2f}")

# 7. Save the trained model
import joblib
os.makedirs("models", exist_ok=True)
model_path = "models/code_smell_model.pkl"
joblib.dump(model, model_path)
print(f"💾 Model saved to {model_path}")
