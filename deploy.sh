#!/bin/bash

# 🕌 Islamic Study Site - DigitalOcean Deployment Script
# This script will help you deploy your site to DigitalOcean

echo "🕌 Welcome to Islamic Study Site Deployment!"
echo "=============================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Build the Docker image
echo "🔨 Building Docker image..."
docker-compose build

if [ $? -ne 0 ]; then
    echo "❌ Failed to build Docker image"
    exit 1
fi

echo "✅ Docker image built successfully"
echo ""

# Ask for DigitalOcean droplet IP
echo "🌐 Please enter your DigitalOcean droplet IP address:"
read -p "Droplet IP: " DROPLET_IP

if [ -z "$DROPLET_IP" ]; then
    echo "❌ IP address is required"
    exit 1
fi

# Ask for username (usually 'root' for DigitalOcean)
echo "👤 Please enter your DigitalOcean droplet username (usually 'root'):"
read -p "Username: " USERNAME

if [ -z "$USERNAME" ]; then
    USERNAME="root"
fi

echo ""

# Deploy to DigitalOcean
echo "🚀 Deploying to DigitalOcean..."
echo "   Droplet IP: $DROPLET_IP"
echo "   Username: $USERNAME"
echo ""

# Copy files to droplet
echo "📁 Copying files to droplet..."
scp -r . $USERNAME@$DROPLET_IP:/root/islamic-study-site

if [ $? -ne 0 ]; then
    echo "❌ Failed to copy files to droplet"
    echo "   Make sure you can SSH to your droplet and have the correct credentials"
    exit 1
fi

echo "✅ Files copied successfully"
echo ""

# SSH to droplet and start the application
echo "🔑 Connecting to droplet and starting application..."
echo "   You will be prompted for your droplet password"
echo ""

ssh $USERNAME@$DROPLET_IP << 'EOF'
    cd /root/islamic-study-site
    
    # Stop any existing containers
    docker-compose down 2>/dev/null
    
    # Start the application
    echo "Starting Islamic Study Site..."
    docker-compose up -d
    
    # Check status
    echo "Checking application status..."
    docker-compose ps
    
    echo ""
    echo "🎉 Deployment complete!"
    echo "Your Islamic Study Site is now running at: http://$(curl -s ifconfig.me)"
    echo "Backend API: http://$(curl -s ifconfig.me):8080"
EOF

echo ""
echo "🎉 Deployment script completed!"
echo "Your Islamic Study Site should now be running on your DigitalOcean droplet."
echo ""
echo "🌐 To access your site: http://$DROPLET_IP"
echo "🔧 To check logs: ssh $USERNAME@$DROPLET_IP 'cd /root/islamic-study-site && docker-compose logs'"
echo "🛑 To stop: ssh $USERNAME@$DROPLET_IP 'cd /root/islamic-study-site && docker-compose down'"
