#!/bin/bash
# Deployment script for Streamlit app in Docker
set -e

echo "Building Docker image..."
docker build -t python-devops-app .

echo "Running Streamlit app in Docker..."
docker run -d -p 8501:8501 --name python-devops-app python-devops-app

echo "App deployed at http://localhost:8501"
