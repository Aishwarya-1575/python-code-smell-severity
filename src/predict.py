# src/predict.py

import pickle
import pandas as pd
import re
import sys
import os

# Load trained model
MODEL_PATH = os.path.join("models", "code_smell_model.pkl")
VECTORIZER_PATH = os.path.join("models", "vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

def clean_code(code):
    """Remove comments and extra spaces from code for preprocessing"""
    code = re.sub(r"#.*", "", code)   # remove single line comments
    code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)  # remove docstrings
    code = re.sub(r"\s+", " ", code)  # collapse spaces
    return code.strip()

def predict_severity(code_snippet: str):
    """Predict the severity of a given code snippet"""
    cleaned_code = clean_code(code_snippet)
    features = vectorizer.transform([cleaned_code])
    prediction = model.predict(features)[0]
    return prediction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠ Usage: python src/predict.py '<your_code_here>'")
    else:
        code_input = sys.argv[1]
        result = predict_severity(code_input)
        print(f"Predicted Severity: {result}")
