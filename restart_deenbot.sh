#!/bin/bash

echo "🔄 DeenBot Restart Script for DigitalOcean"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ Please run this script from your project directory"
    echo "   cd /root/islamic-study-site"
    exit 1
fi

echo "✅ Found docker-compose.yml"
echo ""

# Stop current containers
echo "🛑 Stopping current containers..."
docker-compose down
echo "✅ Containers stopped"
echo ""

# Wait a moment
sleep 3

# Start fresh containers
echo "🚀 Starting fresh containers..."
docker-compose up -d
echo "✅ Containers started"
echo ""

# Wait for startup
echo "⏳ Waiting for services to start up..."
sleep 10

# Check status
echo "📊 Checking container status..."
docker-compose ps
echo ""

# Check logs for any errors
echo "📋 Recent logs (last 20 lines):"
docker-compose logs --tail=20
echo ""

echo "🎉 Restart complete!"
echo ""
echo "🌐 Test your DeenBot at: http://$(curl -s ifconfig.me)"
echo "🔧 To check logs anytime: docker-compose logs -f"
echo "🛑 To stop: docker-compose down"
