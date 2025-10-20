# 504_serverless_functions
**Assignment 3**  
**Naira Khergiani**  
**HHA 504 – Cloud Computing**

---

## Cloud Environments Used
- **Google Cloud Platform (GCP)** – Region: `us-central1`
- **Microsoft Azure** – Region: `East US`

---

## Lab Rules Implemented

**Lab Value Chosen:**  
**Serum Potassium (mmol/L)**

**Reference Range:**  
Normal serum potassium is **3.6–5.2 mmol/L** (based on Mayo Clinic).

**Clinical Rule:**  
- **Normal:** 3.6 ≤ potassium ≤ 5.2 mmol/L  
- **Abnormal:** potassium < 3.6 or potassium > 5.2 mmol/L

**Citations:**  
- Mayo Clinic. ["Potassium test"](https://www.mayocliniclabs.com/tests-procedures/potassium-test/about/pac-20384753)  
- Mayo Clinic Laboratories. ["Potassium, Serum"](https://www.mayocliniclabs.com/test-catalog/Overview/602352)

---

## Public Endpoints
- GCP Function: [https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier](https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier)  
- Azure Function: [https://YOURAPP.azurewebsites.net/api/potassium_triage](#) *(replace when deployed)*

---

## Example Test Outputs (GCP)
```json
- Input: {"potassium": 4.0}, Status Code: 200, Response: {"potassium": 4.0, "status": "normal", "category": "Normal (3.5–5.0 mmol/L)"}
- Input: {"potassium": 5.5}, Status Code: 200, Response: {"potassium": 5.5, "status": "abnormal", "category": "Abnormal (<3.5 or >5.0 mmol/L)"}




