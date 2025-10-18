"""Azure Functions handler for this function app.

This file defines the `main(req: func.HttpRequest) -> func.HttpResponse` entry
point used by the Azure Functions Python worker. It was moved here from
`_init_.py` so the runtime can find `__init__.py` as the function script file.

To run locally or in Azure, make sure the `azure-functions` package is
installed in the active interpreter (see project `AZURE/requirements.txt`).
"""

import logging
import json
from typing import Optional


logging.basicConfig(level=logging.INFO)

def main(req) -> object:
	# Lazy import so the package can be imported by editors or tests that
	# don't have 'azure-functions' installed. At runtime the azure.functions
	# package must be available; otherwise we raise a helpful error.
	try:
		import azure.functions as func  # type: ignore
	except Exception as e:
		raise RuntimeError(
			"azure.functions is required at runtime. Install with: \n"
			"python -m pip install azure-functions"
		) from e

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
