#!/bin/bash

echo "🤖 Starting Rasa Chatbot Server..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run ./train.sh first."
    exit 1
fi

# Check if models exist
if [ ! -d "models" ]; then
    echo "❌ No trained models found. Run ./train.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start Rasa server with REST API enabled
echo "🚀 Starting Rasa server on port 5005 with REST API enabled..."
rasa run --enable-api --cors "*" --port 5005
