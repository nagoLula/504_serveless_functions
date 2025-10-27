import requests # pyright: ignore[reportMissingModuleSource]
from typing import List, Dict, Any

# Replace these with your actual deployed URLs
GCP_URL = "https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier"
AZURE_URL = "https://<your-app-name>.azurewebsites.net/api/potassium_classifier"  # Update this when deployed

# Test cases
test_cases: List[Dict[str, Any]] = [
    {"potassium": 4.0},       # Normal
    {"potassium": 5.5},       # Abnormal
    {"potassium": "five"},    # Non-numeric
    {}                        # Missing field
]

def test_function(url: str, label: str) -> None:
    print(f"\nTesting {label} endpoint: {url}")
    for case in test_cases:
        try:
            response = requests.post(url, json=case)
            print(f"Input: {case}, Status Code: {response.status_code}, Response: {response.json()}")
        except Exception as e:
            print(f"Error testing {label}: {e}")

if __name__ == "__main__":
    print("Starting live test of serverless functions...")
    test_function(GCP_URL, "GCP")
    test_function(AZURE_URL, "Azure")

# --- IGNORE ---