#!/bin/bash

echo "🚀 Setting up NextEleven Main Rasa Chatbot..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Train the model
echo "🧠 Training Rasa model..."
rasa train

echo "✅ Training complete!"
echo ""
echo "🚀 Next steps:"
echo "1. Start action server: ./run_actions.sh"
echo "2. Start Rasa server: ./run_rasa.sh"
echo "3. Start frontend: cd frontend && npm start"
