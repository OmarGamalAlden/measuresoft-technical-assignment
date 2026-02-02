import csv
import statistics

# -----------------------------------
# STEP 1: read data from csv file
# -----------------------------------

years = []
prices = []

PRICE_COLUMN = "Oil price - Crude prices since 1861 (current US$)"

with open("crude_oil.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        years.append(int(row["Year"]))
        prices.append(float(row[PRICE_COLUMN]))

# -----------------------------------
# STEP 2: calculate price change between each year
# -----------------------------------

priceChanges = []

for i in range(1, len(prices)):
    currentYearPrice = prices[i]
    lastYearPrice = prices[i - 1]

    change = currentYearPrice - lastYearPrice
    priceChanges.append(change)

# -----------------------------------
# STEP 3: get average and standard deviation
# (this tells us what is "normal")
# -----------------------------------

averageChange = statistics.mean(priceChanges)
standardDeviation = statistics.stdev(priceChanges)

# if change is very far from normal → anomaly
Z_THRESHOLD = 3

print("MODEL VALUES")
print("Average yearly change:", averageChange)
print("Standard deviation:", standardDeviation)
print("-" * 60)

# -----------------------------------
# STEP 4: detect unusual changes
# -----------------------------------

anomalies = []

for i in range(len(priceChanges)):
    change = priceChanges[i]

    # how far is this change from normal
    zScore = abs((change - averageChange) / standardDeviation)

    if zScore > Z_THRESHOLD:
        anomalies.append({
            "year": years[i + 1],
            "price": prices[i + 1],
            "change": change,
            "zScore": zScore
        })

# -----------------------------------
# STEP 5: print result
# -----------------------------------

print("UNUSUAL OIL PRICE CHANGES")
print("-" * 60)

for item in anomalies:
    print(
        "Year:", item["year"],
        "| Price:", round(item["price"], 2),
        "| Change:", round(item["change"], 2),
        "| Score:", round(item["zScore"], 2)
    )

print("-" * 60)
print("Total anomalies found:", len(anomalies))
