#!/bin/bash

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🚀 Starting Rasa server on port 5005 with REST API enabled..."
rasa run --enable-api --cors "*" --port 5005
