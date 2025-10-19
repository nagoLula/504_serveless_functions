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

## Public Endpoints
- GCP Function: [https://REGION-PROJECT.cloudfunctions.net/potassium_triage](#)
- Azure Function: [https://YOURAPP.azurewebsites.net/api/potassium_triage](#)

## Demo Recording
[ Loom Link Here]
---
## Comparison of Cloud Platforms:
- Deploying the function on Google Cloud Platform (GCP) was more straightforward — the CLI setup and gcloud functions deploy command made it fast to test and publish.

- The Azure Function App required a bit more setup (especially configuring function.json and authentication), but it offered a detailed monitoring dashboard and tighter integration with Visual Studio Code. GCP felt easier for quick testing, while Azure provided more robust management tools once deployed.



