import json
# Ensure the 'requests' dependency is available

try:
    import test_requests as requests
except ImportError:
    raise SystemExit("Missing dependency: install requests with `python  -m pip install requests`")
# Define the URLs of the deployed serverless functions
# ...existing code...
# No-op placeholder removed; configure the actual URLs below.

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

if __name__ == "__main__":
    print("Starting live test of serverless functions...")
    test_function(GCP_URL, "GCP")
    test_function(AZURE_URL, "Azure")