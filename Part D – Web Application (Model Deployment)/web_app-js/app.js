const express = require("express");
const path = require("path");

const app = express();

// ------------------------------
// CONFIG
// ------------------------------
app.use(express.urlencoded({ extended: true }));
app.use(express.static("static"));

// ------------------------------
// MODEL VALUES (from data analysis)
// ------------------------------
const averageChange = 3.939133713043478;
const standardDeviation = 49.01342953750396;
const Z_THRESHOLD = 3;

// ------------------------------
// ROUTES
// ------------------------------
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/", (req, res) => {
  const previousPrice = Number(req.body.prev_price);
  const currentPrice = Number(req.body.curr_price);

  const change = currentPrice - previousPrice;
  const zScore = Math.abs((change - averageChange) / standardDeviation);

  let result;
  if (zScore > Z_THRESHOLD) {
    result = "Anomaly detected";
  } else {
    result = "Normal price movement";
  }

  res.send(`
    <html>
      <head>
        <title>Oil Price Detection</title>
        <link rel="stylesheet" href="/css/bootstrap.min.css">
        <link rel="stylesheet" href="/css/style.css">
      </head>
      <body class="bg-dark text-white">
        <div class="container mt-5 text-center">
          <h2>${result}</h2>
          <p>Price Change: ${change.toFixed(2)}</p>
          <p>Z-score: ${zScore.toFixed(2)}</p>
          <a href="/" class="btn btn-info mt-3">Try Again</a>
        </div>
      </body>
    </html>
  `);
});

// ------------------------------
// SERVER
// ------------------------------
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
