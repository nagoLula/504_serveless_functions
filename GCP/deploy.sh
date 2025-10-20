#!/bin/bash
gcloud functions deploy potassium_triage \
  --gen2 \
  --runtime python310 \
  --region us-central1 \
  --entry-point potassium_triage \
  --source=. \
  --trigger-http \
  --allow-unauthenticated


