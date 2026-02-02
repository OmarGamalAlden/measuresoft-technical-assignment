# 📄 README — Part C

## Data Analysis & Machine Learning (Oil & Gas)

**Folder:**
`Part C – Data Analysis & Machine Learning (Oil & Gas)/oil_gas_ml-py`

---

## Overview

This task focuses on analyzing historical crude oil prices and applying a **simple machine learning approach** to detect unusual price changes (anomalies).

The goal is not advanced machine learning, but building a **clear and complete ML pipeline**:

- Data loading
- Feature engineering
- Model training
- Model saving

---

## Dataset

- File: `crude_oil.csv`
- Contains yearly crude oil prices
- Relevant columns:
  - `Year`
  - `Oil price - Crude prices since 1861 (current US$)`

---

## Approach

1. Load the dataset from CSV
2. Calculate **year-to-year price change**
3. Train an **IsolationForest** model for anomaly detection
4. Save the trained model as `model.pkl`

IsolationForest was chosen because:

- It works well for anomaly detection
- It does not require labeled data
- It is simple and suitable for this problem

---

## Project Structure

```
oil_gas_ml-py/
│
├─ analysis_ml.py
├─ crude_oil.csv
├─ model.pkl
├─ venv/
```

---

## Environment Setup (Important)

It is recommended to use a virtual environment.

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate virtual environment (Windows)

```bash
venv\Scripts\activate
```

You should see:

```
(venv)
```

---

## Install Dependencies

Always install packages using this command to avoid Windows path issues:

```bash
python -m pip install pandas scikit-learn joblib numpy
```

---

## Run the Analysis

```bash
python analysis_ml.py
```

---

## Expected Output

- Console output confirming training
- A new file created:

```
model.pkl
```

This file represents the trained machine learning model and is required for **Part D (Web Application)**.

---

## Notes

- This task uses a simple ML model intentionally
- Focus is on clarity and correctness, not complexity
- The generated `model.pkl` must be copied to Part D
