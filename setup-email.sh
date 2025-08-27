#!/bin/bash

echo "🚀 Setting up NextEleven Email Service"
echo "======================================"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3 first."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv email-env

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source email-env/bin/activate

# Install requirements
echo "📚 Installing dependencies..."
pip install -r email-requirements.txt

# Check if .env file exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp email.env.example .env
    echo ""
    echo "⚠️  IMPORTANT: Please edit the .env file with your email credentials!"
    echo "   - SENDER_EMAIL: Your Gmail address"
    echo "   - SENDER_PASSWORD: Your Gmail app password"
    echo "   - SMTP_SERVER: smtp.gmail.com"
    echo "   - SMTP_PORT: 587"
    echo ""
    echo "📧 For Gmail setup:"
    echo "   1. Enable 2-factor authentication"
    echo "   2. Generate an 'App Password'"
    echo "   3. Use the app password (not your regular password)"
    echo ""
    echo "🔧 Edit .env file now, then run this script again to start the service."
    exit 0
fi

# Check if .env has been configured
if grep -q "your-email@gmail.com" .env; then
    echo "❌ Please configure your .env file with actual email credentials first!"
    echo "   Edit .env and set your SENDER_EMAIL and SENDER_PASSWORD"
    exit 1
fi

echo "✅ Environment configured"

# Test email service
echo "🧪 Testing email service..."
python3 email-service.py

echo ""
echo "🚀 Starting Email API server..."
echo "📧 Emails will be sent to: nexteleven@icloud.com"
echo "🌐 API will be available at: http://localhost:5001"
echo "📋 Health check: http://localhost:5001/health"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the API server
python3 email-api.py
