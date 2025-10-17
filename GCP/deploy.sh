#!/bin/bash
gcloud functions deploy potassiumClassifier \
  --gen2 \
  --runtime python314 \
  --region us-central1 \
  --entry-point app \
  --source=. \
  --trigger-http \
  --allow-unauthenticated
