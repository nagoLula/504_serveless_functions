#!/bin/bash
# Make sure your are logged in to Azure CLI and have selected the correct subscription
# Navigate to the Azure function folder
cd "$(dirname "$0")" 

# Deploy the Azure Function
func azure functionapp publish classify_potassium 
