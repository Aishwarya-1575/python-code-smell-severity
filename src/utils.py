# src/utils.py

import re
import pickle
import os

# Paths for model and vectorizer
MODEL_PATH = os.path.join("models", "code_smell_model.pkl")
VECTORIZER_PATH = os.path.join("models", "vectorizer.pkl")


def load_model():
    """Load trained model and vectorizer from disk"""
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


def clean_code(code: str) -> str:
    """Preprocess code by removing comments, docstrings, and extra spaces"""
    code = re.sub(r"#.*", "", code)  # Remove single-line comments
    code = re.sub(r'""".*?"""', "", code, flags=re.DOTALL)  # Remove multi-line docstrings
    code = re.sub(r"\s+", " ", code)  # Collapse multiple spaces
    return code.strip()


def predict_code_severity(code_snippet: str, model, vectorizer) -> str:
    """Predict severity of code snippet"""
    cleaned_code = clean_code(code_snippet)
    features = vectorizer.transform([cleaned_code])
    prediction = model.predict(features)[0]
    return prediction
