# 📄 README — Part C

## Data Analysis & Machine Learning (Oil & Gas)

**Folder:** `Part C – Data Analysis & Machine Learning (Oil & Gas)`

### Project Structure

```
Part C – Data Analysis & Machine Learning (Oil & Gas)/
│
├─ oil_gas_ml-py/
│   ├─ analysis.py
│   ├─ crude_oil.csv
│   ├─ Task clarification.txt
│
├─ oil_gas_ml-js/
│   ├─ analysis.js
│   ├─ crude_oil.csv
├─ README.md
```

---

### Overview

This task analyzes historical crude oil prices to detect unusual price changes
between consecutive years.

The solution uses **simple statistical analysis**, not heavy machine learning.

---

### Dataset

- CSV file containing yearly crude oil prices
- Columns include:
  - Entity
  - Code
  - Year
  - Oil price

---

### Approach

1. Read price data from CSV
2. Calculate year-to-year price changes
3. Calculate:
   - Average price change
   - Standard deviation

4. Use **Z-score** to detect anomalies

A year is considered anomalous if its price change is far from the normal range.

---

### Why This Approach

- Easy to understand and explain
- Suitable for time-series data
- Avoids unnecessary ML complexity
- Focuses on logic instead of libraries

---

### Python Version

- Implemented using plain Python
- Uses built-in statistics functions

### JavaScript Version

- Implemented using Node.js
- All calculations are written manually
- No external data science libraries

---

### How to Run

**Python version**

```bash
python analysis.py
```

**JavaScript version**

```bash
node analysis.js
```

---

### Notes

- This task focuses on data understanding, not model training
- Results from both versions are consistent
