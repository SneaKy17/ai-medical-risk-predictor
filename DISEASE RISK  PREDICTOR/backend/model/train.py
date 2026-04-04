import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "diabetes.csv")

df = pd.read_csv(data_path)

# IMPORTANT: check data
print(df["Outcome"].value_counts())

X = df[["Pregnancies", "Glucose", "BloodPressure", "BMI", "Age"]]
y = df["Outcome"]

# 🔥 IMPORTANT FIX → stratify
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained correctly")