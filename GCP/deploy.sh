#!/bin/bash
gcloud functions deploy potassium_classifier \
  --gen2 \
  --runtime python310 \
  --region us-central1 \
  --entry-point potassium_classifier \
  --source=. \
  --trigger-http \
  --allow-unauthenticated \
  --project=serverless-functions-475623


