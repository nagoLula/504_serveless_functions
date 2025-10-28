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

## Public Endpoints

- GCP Function: [https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier](https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier)  
- Azure Function: [https://potassiumfunc504-hqcfd8ebhhdfdxd0.eastus2-01.azurewebsites.net/api/potassium]
---


## Azure Function Deployment Walkthrough

### 1. Function App Overview
![Function App Overview](img width="1634" height="879" alt="Screenshot 2025-10-27 203327" src="https://github.com/user-attachments/assets/b86b81e6-741c-4412-afcb-b354a9c7652a" /)


### 2. Creating the HTTP Trigger
![Create Function Trigger](screenshots/02_create_function_trigger.png)

### 3. Uploading Code via Code + Test
![Code + Test Panel](screenshots/03_code_test_panel.png)

### 4. Adding function.json
![Function JSON Added](screenshots/04_function_json_added.png)

### 5. Testing the Function
![Test Run Success](screenshots/05_test_run_success.png)

### 6. Viewing Logs
![Logs Showing Successful Run](screenshots/06_logs_successful_run.png)

### 7. External Python Test
![Python Terminal Output](screenshots/07_python_test_terminal.png)


## Example Test Outputs (GCP)

```json

- Input: {"potassium": 4.0}, Status Code: 200, Response: {"potassium": 4.0, "status": "normal", "category": "Normal (3.6–5.2 mmol/L)"}
- Input: {"potassium": 5.5}, Status Code: 200, Response: {"potassium": 5.5, "status": "abnormal", "category": "Abnormal (<3.6 or >5.2 mmol/L)"}

---

## Demo recording

**LOOM**:

- Watch the demo video showcasing the deployment and testing of the GCP serverless function:

https://www.loom.com/share/cadc4d3fb49b4abaa3d75eb9be329721?sid=cac9dfb7-4efa-4686-89d1-5eb9edb840f7
----
![Deployment Screenshot](GCP/screenshot_deploy.png)
![Logs Screenshot](GCP/screenshots_logs.png)




