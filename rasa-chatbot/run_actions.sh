#!/bin/bash

echo "🔧 Starting Rasa Action Server..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run ./train.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start action server
echo "🚀 Starting action server on port 5055..."
rasa run actions --port 5055
