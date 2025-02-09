#!/bin/bash

# Define variables
IMAGE_NAME="my-node-app"
CONTAINER_NAME="my-node-container"
PORT=3333

# Build the Docker image
echo "[*] Building Docker image..."
docker build -t $IMAGE_NAME .

# Remove any existing container with the same name
echo "[*] Removing existing container (if any)..."
docker rm -f $CONTAINER_NAME 2>/dev/null

# Run the container
echo "[*] Running the container..."
docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME

echo "[*] Container is running. Access it at http://localhost:$PORT"
