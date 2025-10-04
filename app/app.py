from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Dummy function for now (replace with your ML model later)
def predict_severity(code_text):
    if "import" in code_text and len(code_text) > 100:
        return "High"
    elif len(code_text) > 50:
        return "Medium"
    else:
        return "Low"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    code_text = ""

    # If code is pasted in textarea
    if "code" in request.form and request.form["code"].strip() != "":
        code_text = request.form["code"]

    # If file is uploaded
    elif "file" in request.files:
        file = request.files["file"]
        if file and file.filename.endswith(".py"):
            code_text = file.read().decode("utf-8")

    # If no code provided
    if code_text.strip() == "":
        return "⚠ No code provided. Please paste code or upload a .py file."

    # Call ML model (right now dummy function)
    severity = predict_severity(code_text)

    return render_template("result.html", code=code_text, severity=severity)

if __name__ == "__main__":
    app.run(debug=True)
