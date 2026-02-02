# 📄 README — Part D

## Web Application (Model Deployment)

**Folder:**
`Part D – Web Application (Model Deployment)/web_app-py`

---

## Overview

This task demonstrates **deploying a trained machine learning model** using a web application.

The application:

- Loads a trained ML model
- Accepts user input
- Performs prediction
- Displays the result in the browser

---

## How It Works

1. User enters:
   - Previous year oil price
   - Current year oil price

2. The application calculates the price change
3. The trained model predicts whether the change is:
   - Normal
   - Or an anomaly

---

## Project Structure

```
web_app-py/
│
├─ app.py
├─ model.pkl
├─ templates/
│   └─ index.html
├─ static/
│   └─ css/
│   └─ js/
├─ venv/
```

---

## Required File

⚠️ **Important**

Before running this application:

- Copy `model.pkl` from **Part C**
- Paste it into this folder (`web_app-py/`)

Without this file, the application will not run.

---

## Environment Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate virtual environment

```bash
venv\Scripts\activate
```

---

## Install Dependencies

The model was trained using `scikit-learn`, so it must be installed here as well.

```bash
python -m pip install flask scikit-learn joblib numpy
```

---

## Run the Web Application

```bash
python app.py
```

---

## Open in Browser

```
http://127.0.0.1:5000
```

---

## Notes

- The model is loaded using `joblib.load`
- The same feature used during training is used during prediction
- This represents a complete and valid **model deployment**
