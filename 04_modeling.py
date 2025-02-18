import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load cleaned dataset
df = pd.read_csv("outputs/cleaned_data.csv")

# Define features and target
X = df.drop(columns=["status"])
y = df["status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Ensure output directory exists
os.makedirs("outputs", exist_ok=True)

# Save results
with open("outputs/model_performance.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}\n")
    f.write(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "outputs/placement_model.pkl")
