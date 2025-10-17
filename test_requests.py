import requests

# Replace these with your actual deployed URLs
GCP_URL = "https://your-gcp-function-url"
AZURE_URL = "https://your-azure-function-url"

# Test cases
test_cases = [
    {"potassium": 4.0},  # Normal
    {"potassium": 5.5}   # Abnormal
]

def test_function(url, label):
    print(f"\nTesting {label} endpoint: {url}")
    for case in test_cases:
        try:
            response = requests.post(url, json=case)
            print(f"Input: {case}, Status Code: {response.status_code}, Response: {response.json()}")
        except Exception as e:
            print(f"Error testing {label}: {e}")

print("Starting live test of serverless functions...")
test_function(GCP_URL, "GCP")
test_function(AZURE_URL, "Azure")