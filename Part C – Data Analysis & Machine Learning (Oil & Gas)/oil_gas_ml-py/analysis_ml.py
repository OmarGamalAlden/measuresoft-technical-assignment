import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest

# -----------------------------------
# STEP 1: load dataset
# -----------------------------------

data = pd.read_csv("crude_oil.csv")

# we just need year and price
data = data[["Year", "Oil price - Crude prices since 1861 (current US$)"]]
data = data.dropna()

# -----------------------------------
# STEP 2: feature engineering
# -----------------------------------

# calculate year-to-year price change
data["price_change"] = data[
    "Oil price - Crude prices since 1861 (current US$)"
].diff()

# first row will be NaN after diff
data = data.dropna()

# model input (must be 2D array)
X = data[["price_change"]]

# -----------------------------------
# STEP 3: train anomaly detection model
# -----------------------------------

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# -----------------------------------
# STEP 4: save trained model
# -----------------------------------

joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")

# -----------------------------------
# STEP 5: quick sanity check
# -----------------------------------

data["prediction"] = model.predict(X)

# -1 means anomaly, 1 means normal
anomalies = data[data["prediction"] == -1]

print("Total records:", len(data))
print("Detected anomalies:", len(anomalies))
