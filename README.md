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

- GCP Function:
- [https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier](https://us-central1-serverless-functions-475623.cloudfunctions.net/potassium_classifier)  
- Azure Function:
- [https://potassiumfunc504-hqcfd8ebhhdfdxd0.eastus2-01.azurewebsites.net/api/potassium]
---


## Azure Function Deployment Walkthrough

### 1. Function App Overview
![Function App Overview] (img width="1634" height="879" alt="Screenshot 2025-10-27 203327" src="https://github.com/user-attachments/assets/b86b81e6-741c-4412-afcb-b354a9c7652a" /)


### 2. Creating the HTTP Trigger
![Create Function Trigger] (img width="854" height="334" alt="Screenshot 2025-10-27 203431" src="https://github.com/user-attachments/assets/46fe5dcd-278e-40d3-ad65-7e0e8322adf8" /)


### 3. Uploading Code via Code + Test
![Code + Test Panel] (img width="634" height="915" alt="Screenshot 2025-10-27 203843" src="https://github.com/user-attachments/assets/ae489d44-f724-4987-9056-a1425d67b18f" /)

### 4. Adding function.json
![Function JSON Added] ("https://github.com/user-attachments/assets/480041a1-f4f2-4653-9f0d-5262b5b51300" /


### 5. Testing the Function
![Test Run Success] ("https://github.com/user-attachments/assets/0d41569a-366d-4d4b-b822-a57be58e23fb")


### 6. Viewing Logs
![Logs Showing Successful Run] ("https://github.com/user-attachments/assets/76ffbf54-3351-4b15-8c43-f33184c6ce2c")



### 7. External Python Test
![Python Terminal Output] ("https://github.com/user-attachments/assets/92085ef6-83bb-4808-ad74-d221ef61b308")


---

## GCP deployment

Input: {"potassium": 4.0}
Status Code: 200
Response: {"potassium": 4.0, "status": "normal", "category": "Normal (3.6–5.2 mmol/L)"}

Input: {"potassium": 5.5}
Status Code: 200
Response: {"potassium": 5.5, "status": "abnormal", "category": "Abnormal (<3.6 or >5.2 mmol/L)"}

---

## Demo recording

**LOOM**:

- Watch the demo video showcasing the deployment and testing of the GCP serverless function:

- (https://www.loom.com/share/cadc4d3fb49b4abaa3d75eb9be329721?sid=cac9dfb7-4efa-4686-89d1-5eb9edb840f7)
- (https://www.loom.com/share/cadc4d3fb49b4abaa3d75eb9be329721)
----
![Deployment Screenshot] (img width="1207" height="610" alt="Screenshot 2025-10-17 235530" src="https://github.com/user-attachments/assets/8e03ef83-d0f8-4640-8eba-edea4ea7b44e" /)






