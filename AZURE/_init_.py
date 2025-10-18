# To install the Azure Functions Python package, run this in your shell:
# pip install azure-functions 
import logging
import json 
import azure.functions as func  


logging.basicConfig(level=logging.INFO)

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse JSON input
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON format."}),
            status_code=400,
            mimetype="application/json"
        )

    potassium = req_body.get("potassium")

    if potassium is None:
        return func.HttpResponse(
            json.dumps({"error": "'potassium' field is required."}),
            status_code=400,
            mimetype="application/json"
        )

    if not isinstance(potassium, (int, float)):
        return func.HttpResponse(
            json.dumps({"error": "'potassium' must be a number."}),
            status_code=400,
            mimetype="application/json"
        )

    # Classification logic
    threshold = 5.0  # Normal range upper limit
    status = "normal" if potassium < threshold else "abnormal"
    category = f"Normal (<{threshold})" if status == "normal" else f"Abnormal (≥{threshold})"

    # Return structured response
    result = {
        "potassium": potassium,
        "status": status,
        "category": category
    }

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )

