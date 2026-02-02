from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# -----------------------------------
# Load trained ML model
# -----------------------------------
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    zResult = None

    if request.method == "POST":
        prev_price = float(request.form["prev_price"])
        curr_price = float(request.form["curr_price"])

        # calculate feature (same as training)
        price_change = curr_price - prev_price

        # model expects 2D array
        prediction = model.predict([[price_change]])

        if prediction[0] == -1:
            result = "Anomaly detected"
        else:
            result = "Normal price movement"

        zResult = round(price_change, 2)

    return render_template(
        "index.html",
        result=result,
        price_change=zResult
    )

if __name__ == "__main__":
    app.run(debug=True)
