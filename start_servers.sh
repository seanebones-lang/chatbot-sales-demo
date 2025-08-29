#!/bin/bash

# DeenBot Server Startup Script
# This script starts the DeenBot backend and frontend servers

echo "🚀 Starting DeenBot Islamic AI Assistant..."

# Check if config.env exists and load it
if [ -f "config.env" ]; then
    echo "📁 Loading configuration from config.env..."
    export $(cat config.env | xargs)
else
    echo "⚠️  No config.env found. Using default settings."
    echo "💡 Create config.env from config.env.example for custom settings."
fi

# Set default values if not in config
export OPENWEBUI_API_KEY=${OPENWEBUI_API_KEY:-"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxNWUzOGM1LTdiMDQtNGEwMS1hOTI0LTFhNWEyZmI2MmFkYyJ9.UI-kwaYruBNjjxYkjZrzC4vBIAeDkadMcFFlDHZpENU"}
export DEENBOT_PORT=${DEENBOT_PORT:-8080}

echo "🔑 API Key: ${OPENWEBUI_API_KEY:0:20}..."
echo "🌐 OpenWebUI URL: ${OPENWEBUI_URL:-http://localhost:3001}"
echo "💬 DeenBot Port: ${DEENBOT_PORT}"

# Kill any existing processes on the ports
echo "🧹 Cleaning up existing processes..."
pkill -f "webui_scraper_backend.py" 2>/dev/null
pkill -f "python3.*8080" 2>/dev/null

# Start the DeenBot backend
echo "Starting DeenBot backend..."
python3 webui_scraper_backend.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Check if backend started successfully
if kill -0 $BACKEND_PID 2>/dev/null; then
    echo "Backend started successfully (PID: $BACKEND_PID)"
else
    echo "❌ Failed to start backend"
    exit 1
fi

# Start the frontend server
echo "🌐 Starting frontend server..."
python3 -m http.server 8001 &
FRONTEND_PID=$!

# Wait a moment for frontend to start
sleep 2

# Check if frontend started successfully
if kill -0 $FRONTEND_PID 2>/dev/null; then
    echo "Frontend started successfully (PID: $FRONTEND_PID)"
else
    echo "❌ Failed to start frontend"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

echo ""
echo "🎉 DeenBot is now running!"
echo "🌐 Frontend: http://localhost:8001"
echo "Backend: http://localhost:${DEENBOT_PORT}"
echo "💬 Chat: http://localhost:8001/chat.html"
echo ""
echo "🛑 Press Ctrl+C to stop all servers"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🧹 Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    echo "All servers stopped"
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for user to stop
wait
