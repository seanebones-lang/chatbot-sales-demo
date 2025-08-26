#!/bin/bash

echo "🔧 Activating virtual environment..."
source venv/bin/activate

echo "🚀 Starting action server on port 5055..."
rasa run actions --port 5055
