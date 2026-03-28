#!/bin/bash
# Example deployment script for Linux
set -e

echo "Running tests..."
pytest

echo "Building Docker image..."
docker build -t python-devops-app .

echo "Deploying container..."
docker run -d --name python-devops-app python-devops-app
