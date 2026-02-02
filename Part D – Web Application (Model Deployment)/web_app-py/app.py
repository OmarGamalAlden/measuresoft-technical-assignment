from flask import Flask, render_template, request

app = Flask(__name__)

# values calculated before from data analysis
averageChange = 3.939133713043478
standardDeviation = 49.01342953750396

# if value is far from normal -> anomaly
Z_THRESHOLD = 3


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    details = None

    if request.method == "POST":
        previousPrice = float(request.form["prev_price"])
        currentPrice = float(request.form["curr_price"])

        # calculate price difference
        change = currentPrice - previousPrice

        # measure how unusual this change is
        zScore = abs((change - averageChange) / standardDeviation)

        if zScore > Z_THRESHOLD:
            result = "Anomaly detected"
        else:
            result = "Normal price movement"

        details = {
            "change": round(change, 2),
            "zScore": round(zScore, 2)
        }

    return render_template(
        "index.html",
        result=result,
        details=details
    )


if __name__ == "__main__":
    app.run(debug=True)
