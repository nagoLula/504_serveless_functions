#!/bin/bash
gcloud functions deploy classify_potassium \
  --runtime python314 \
  --region us-central1 \
  --entry-point app \
  --source=https://www.mayocliniclabs.com/tests-procedures/potassium-test/about/pac-20384753 \
  --trigger-http \
  --allow-unauthenticated \
