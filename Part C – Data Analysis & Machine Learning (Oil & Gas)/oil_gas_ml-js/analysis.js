const fs = require("fs");

// -----------------------------------
// STEP 1: read data from csv file
// -----------------------------------

const fileContent = fs.readFileSync("crude_oil.csv", "utf-8");
const lines = fileContent.split("\n");

const years = [];
const prices = [];

for (let i = 1; i < lines.length; i++) {
  if (!lines[i]) continue;

  const cols = lines[i].split(",");

  // Expected format:
  // Entity, Code, Year, Price
  if (cols.length < 4) continue;

  const year = Number(cols[2]);
  const price = Number(cols[3]);

  if (isNaN(year) || isNaN(price)) continue;

  years.push(year);
  prices.push(price);
}

// safety check
if (prices.length < 2) {
  console.log("Not enough valid data to analyze.");
  process.exit(1);
}

// -----------------------------------
// STEP 2: calculate price change
// -----------------------------------

const priceChanges = [];

for (let i = 1; i < prices.length; i++) {
  priceChanges.push(prices[i] - prices[i - 1]);
}

// -----------------------------------
// STEP 3: average & standard deviation
// -----------------------------------

function mean(values) {
  let sum = 0;
  for (let v of values) sum += v;
  return sum / values.length;
}

function standardDeviation(values) {
  const avg = mean(values);
  let squareSum = 0;

  for (let v of values) {
    squareSum += Math.pow(v - avg, 2);
  }

  return Math.sqrt(squareSum / (values.length - 1));
}

const averageChange = mean(priceChanges);
const standardDeviationValue = standardDeviation(priceChanges);

const Z_THRESHOLD = 3;

console.log("MODEL VALUES");
console.log("Average yearly change:", averageChange);
console.log("Standard deviation:", standardDeviationValue);
console.log("-".repeat(60));

// -----------------------------------
// STEP 4: detect anomalies
// -----------------------------------

const anomalies = [];

for (let i = 0; i < priceChanges.length; i++) {
  const change = priceChanges[i];
  const zScore = Math.abs((change - averageChange) / standardDeviationValue);

  if (zScore > Z_THRESHOLD) {
    anomalies.push({
      year: years[i + 1],
      price: prices[i + 1],
      change,
      zScore,
    });
  }
}

// -----------------------------------
// STEP 5: print result
// -----------------------------------

console.log("UNUSUAL OIL PRICE CHANGES");
console.log("-".repeat(60));

for (let item of anomalies) {
  console.log(
    "Year:",
    item.year,
    "| Price:",
    item.price.toFixed(2),
    "| Change:",
    item.change.toFixed(2),
    "| Score:",
    item.zScore.toFixed(2),
  );
}

console.log("-".repeat(60));
console.log("Total anomalies found:", anomalies.length);
