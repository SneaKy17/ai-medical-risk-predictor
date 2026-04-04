from flask import Flask, request, jsonify
import numpy as np
import pickle
import os
import shap

app = Flask(__name__)

# Load model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "model", "model.pkl")

print("Model path:", model_path)

if not os.path.exists(model_path):
    raise Exception("❌ model.pkl not found. Run train.py first!")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "✅ Backend Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = np.array([[
            data["pregnancies"],
            data["glucose"],
            data["blood_pressure"],
            data["bmi"],
            data["age"]
        ]])

        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]

        return jsonify({
            "risk": "High" if prediction == 1 else "Low",
            "confidence": round(float(prob)*100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = np.array([[
            data["pregnancies"],
            data["glucose"],
            data["blood_pressure"],
            data["bmi"],
            data["age"]
        ]])

        prediction = model.predict(features)[0]

        return jsonify({
            "risk": "High Risk ⚠️" if prediction == 1 else "Low Risk ✅"
        })

    except Exception as e:
        return jsonify({"error": str(e)})