#!/bin/bash

echo "🚀 Setting up Rasa Dual Bots - Mariam & Ozzy"

# Create virtual environment
echo "📦 Creating virtual environment..."
python -m venv venv
source venv/bin/activate

# Install requirements
echo "📥 Installing requirements..."
pip install -r requirements.txt

# Train Mariam Bot
echo "🤖 Training Mariam Bot..."
cd mariam-bot
rasa train
cd ..

# Train Ozzy Bot
echo "🎨 Training Ozzy Bot..."
cd ozzy-bot
rasa train
cd ..

echo "✅ Setup complete! Both bots are trained and ready."
echo ""
echo "🚀 To run both bots:"
echo "Terminal 1: cd mariam-bot && rasa run actions"
echo "Terminal 2: cd mariam-bot && rasa run --enable-api --cors '*'"
echo "Terminal 3: cd ozzy-bot && rasa run actions"
echo "Terminal 4: cd ozzy-bot && rasa run --enable-api --cors '*'"
echo ""
echo "🌐 Mariam will run on: http://localhost:5005"
echo "🌐 Ozzy will run on: http://localhost:5006"
