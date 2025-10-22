from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def potassium_classifier():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        if not data or "potassium" not in data:
            return jsonify({"error": "'potassium' is required."}), 400

        # Ensure 'potassium' is a valid number
        potassium = float(data["potassium"])
    except ValueError:
        return jsonify({"error": "'potassium' must be a number."}), 400

    # Clinical rule: Normal if 3.6 ≤ potassium ≤ 5.2 mmol/L
    if 3.6 <= potassium <= 5.2:
        status = "normal"
        category = "Normal (3.6–5.2 mmol/L)"
    else:
        status = "abnormal"
        category = "Abnormal (<3.6 or >5.2 mmol/L)"

    # Return the classification result
    return jsonify({
        "potassium": potassium,
        "status": status,
        "category": category
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)





