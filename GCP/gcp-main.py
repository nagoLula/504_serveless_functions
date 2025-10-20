from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def potassium_classifier():
    try:
        # Parse JSON data from the request
        data = request.get_json(force=True)
        potassium = data.get("potassium")

        # Validate the presence of 'potassium'
        if potassium is None:
            return jsonify({"error": "'potassium' is required."}), 400

        # Ensure 'potassium' is a valid number
        potassium = float(potassium)
    except ValueError:
        return jsonify({"error": "'potassium' must be a number."}), 400

    # Classify potassium levels
    if 3.5 <= potassium <= 5.0:
        status = "normal"
        category = "Normal (3.5–5.0 mmol/L)"
    else:
        status = "abnormal"
        category = "Abnormal (<3.5 or >5.0 mmol/L)"

    # Return the classification result
    return jsonify({
        "potassium": potassium,
        "status": status,
        "category": category
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)




