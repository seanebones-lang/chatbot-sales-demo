#!/bin/bash

echo "🚀 Starting Islamic AI Chat System..."
echo "======================================"

# Function to cleanup background processes
cleanup() {
    echo -e "\n🛑 Shutting down servers..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Start Python backend on port 8080
echo "🐍 Starting Python AI Backend on port 8080..."
python3 quran_ai_backend.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Start frontend server on port 8001
echo "🌐 Starting Frontend Server on port 8001..."
python3 -m http.server 8001 &
FRONTEND_PID=$!

echo ""
echo "✅ Servers are running!"
echo "🌐 Frontend: http://localhost:8001"
echo "🐍 Backend: http://localhost:8080"
echo "💬 Chat: http://localhost:8001/chat.html"
echo ""
echo "🛑 Press Ctrl+C to stop both servers"
echo ""

# Wait for user to stop
wait
