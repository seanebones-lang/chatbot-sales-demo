#!/bin/bash

echo "🕌 DeenBot Local Startup Script"
echo "================================"
echo ""

# Check if DeenBot is already running
if curl -s http://localhost:8080/health > /dev/null 2>&1; then
    echo "✅ DeenBot is already running on port 8080"
    echo "🌐 Health check: http://localhost:8080/health"
    echo "💬 Chat endpoint: http://localhost:8080/chat"
    exit 0
fi

# Kill any existing processes on port 8080
echo "🔫 Checking for existing processes on port 8080..."
lsof -ti:8080 | xargs kill -9 2>/dev/null || echo "No existing processes found"

# Wait a moment for cleanup
sleep 2

# Check if virtual environment exists
if [ -d "deenbot_env" ]; then
    echo "🔧 Activating virtual environment..."
    source deenbot_env/bin/activate
else
    echo "⚠️ Virtual environment not found, using system Python"
fi

# Install required dependencies
echo "📦 Installing required dependencies..."
pip install psutil requests

# Start the comprehensive backend
echo "🚀 Starting Comprehensive DeenBot Backend..."
echo "📚 This will load the full Islamic knowledge base..."
echo "⏳ Please wait for startup (this may take a few moments)..."

# Start the service manager
python3 deenbot_service_manager.py &

# Wait for startup
echo "⏳ Waiting for service to start..."
sleep 15

# Check if service is running
if curl -s http://localhost:8080/health > /dev/null 2>&1; then
    echo ""
    echo "🎉 DeenBot is now running successfully!"
    echo "======================================"
    echo "🌐 Health check: http://localhost:8080/health"
    echo "💬 Chat endpoint: http://localhost:8080/chat"
    echo "📊 Status endpoint: http://localhost:8080/status"
    echo ""
    echo "📋 To view logs: tail -f deenbot_service.log"
    echo "🛑 To stop: pkill -f deenbot_service_manager.py"
    echo ""
    echo "✅ Service is now stable and monitored"
else
    echo "❌ Failed to start DeenBot"
    echo "📋 Check logs: tail -f deenbot_service.log"
    exit 1
fi
