#!/bin/bash

echo "🚀 Training Rasa Chatbot Model..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Train the model
echo "🧠 Training NLU and Core models..."
rasa train

echo "✅ Training complete! Model saved to models/ directory."
echo ""
echo "🚀 To run the chatbot:"
echo "1. Start action server: ./run_actions.sh"
echo "2. Start Rasa server: ./run_rasa.sh"
echo "3. Start frontend: cd frontend && npm start"
