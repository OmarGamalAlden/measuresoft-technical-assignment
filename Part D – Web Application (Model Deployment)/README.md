---

# 📄 README — Part D

## Web Application (Model Deployment)

**Folder:** `Part D – Web Application (Model Deployment)`

### Project Structure

```
Part D – Web Application (Model Deployment)/
│
├─ web_app-py/
│   ├─ app.py
│   ├─ templates/
│   │   └─ index.html
│   ├─ static/
│   │   └─ css/
│   │   └─ js/
│
├─ web_app-js/
│   ├─ app.js
│   ├─ index.html
│   ├─ static/
│   │   └─ css/
│   │   └─ js/
├─ README.md
```

---

### Overview

This task is a small web application that allows the user
to test whether a price change is normal or anomalous.

It uses statistical values calculated previously during data analysis **Task - C**.

---

### How It Works

1. User enters:
   - Previous year price
   - Current year price

2. The application calculates:
   - Price difference
   - Z-score

3. The result is displayed as:
   - Normal price movement
   - Or anomaly detected

---

### Python Version

- Built using Flask
- Handles form submission and calculation on the backend

### JavaScript Version

- Built using Node.js and Express
- Same logic rewritten in JavaScript

---

### How to Run

**Python version**

```bash
python app.py
```

**JavaScript version**

```bash
npm install
node app.js
```

Then open:

```
http://localhost:3000
```

---

### Notes

- This task focuses on simple deployment logic
- No heavy ML frameworks were used
- Backend logic is intentionally simple

---

---
