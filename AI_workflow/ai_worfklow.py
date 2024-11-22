import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Data Collection: Mock Data
print("Step 1: Data Collection - Gathering raw data")
data = {
    "age": [25, 45, 35, 50, 23, 40, 65, 30],
    "bmi": [22.0, 28.5, 24.5, 30.1, 21.7, 26.4, 29.9, 23.2],
    "smoking": [0, 1, 0, 1, 0, 1, 1, 0],
    "exercise_frequency": [3, 0, 2, 0, 5, 1, 0, 4],
    "disease_risk": [0, 1, 0, 1, 0, 1, 1, 0],  # Target: 0 = Low Risk, 1 = High Risk
}
df = pd.DataFrame(data)
print(df)

# 2. Data Preprocessing
print("\nStep 2: Data Preprocessing - Cleaning and normalizing data")
X = df.drop("disease_risk", axis=1)
y = df["disease_risk"]

# Handling missing data (if any)
X.fillna(X.mean(), inplace=True)

# Normalizing the features
X_normalized = (X - X.mean()) / X.std()
print("Data normalized:\n", X_normalized)

# 3. Model Selection: Random Forest
print("\nStep 3: Model Selection - Using Random Forest Classifier")
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. Training and Validation
print("\nStep 4: Training the model and validating with test data")
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.3, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluation
print("\nStep 5: Evaluating model performance")
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Deployment: Save the trained model
print("\nStep 6: Deploying model - Saving the model for future use")
joblib.dump(model, "disease_risk_model.pkl")
print("Model saved as 'disease_risk_model.pkl'.")

# 7. Monitoring: Example prediction
print("\nStep 7: Monitoring - Predicting risk for a new patient")
new_data = pd.DataFrame({
    "age": [34],
    "bmi": [25.6],
    "smoking": [0],
    "exercise_frequency": [3]
})

# Preprocess new data
new_data_normalized = (new_data - X.mean()) / X.std()
print("New data normalized:\n", new_data_normalized)

# Load and predict
loaded_model = joblib.load("disease_risk_model.pkl")
prediction = loaded_model.predict(new_data_normalized)
risk_level = "High Risk" if prediction[0] == 1 else "Low Risk"
print(f"Predicted Disease Risk: {risk_level}")
