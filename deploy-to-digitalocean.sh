#!/bin/bash

echo "🕌 Islamic Study Site - DigitalOcean Deployment"
echo "================================================"
echo ""

# Check if we have the necessary files
if [ ! -f "docker-compose.yml" ] || [ ! -f "Dockerfile" ]; then
    echo "❌ Missing required files. Please run this from your project directory."
    exit 1
fi

echo "✅ All required files found"
echo ""

# Get DigitalOcean droplet information
echo "🌐 Please provide your DigitalOcean droplet details:"
echo ""

read -p "Enter your droplet IP address: " DROPLET_IP
if [ -z "$DROPLET_IP" ]; then
    echo "❌ IP address is required"
    exit 1
fi

read -p "Enter username (usually 'root'): " USERNAME
if [ -z "$USERNAME" ]; then
    USERNAME="root"
fi

echo ""
echo "🚀 Starting deployment to: $USERNAME@$DROPLET_IP"
echo ""

# Create logs directory
mkdir -p logs

# Copy files to DigitalOcean
echo "📁 Copying files to DigitalOcean..."
scp -r . $USERNAME@$DROPLET_IP:/root/islamic-study-site

if [ $? -ne 0 ]; then
    echo "❌ Failed to copy files. Please check:"
    echo "   - Your droplet IP is correct"
    echo "   - You can SSH to your droplet"
    echo "   - Your SSH key is set up"
    exit 1
fi

echo "✅ Files copied successfully"
echo ""

# Deploy on DigitalOcean
echo "🔑 Connecting to droplet and deploying..."
echo "   You will be prompted for your droplet password"
echo ""

ssh $USERNAME@$DROPLET_IP << 'EOF'
    cd /root/islamic-study-site
    
    # Install Docker if not present
    if ! command -v docker &> /dev/null; then
        echo "Installing Docker..."
        curl -fsSL https://get.docker.com -o get-docker.sh
        sh get-docker.sh
        usermod -aG docker $USER
    fi
    
    # Install Docker Compose if not present
    if ! command -v docker-compose &> /dev/null; then
        echo "Installing Docker Compose..."
        curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        chmod +x /usr/local/bin/docker-compose
    fi
    
    # Stop any existing containers
    docker-compose down 2>/dev/null
    
    # Start the application
    echo "Starting Islamic Study Site..."
    docker-compose up -d
    
    # Wait for startup
    sleep 10
    
    # Check status
    echo "Checking application status..."
    docker-compose ps
    
    echo ""
    echo "🎉 Deployment complete!"
    echo "Your site is running at: http://$(curl -s ifconfig.me)"
EOF

echo ""
echo "🎉 Deployment completed!"
echo ""
echo "🌐 Your Islamic Study Site is now live at: http://$DROPLET_IP"
echo "🔧 To check logs: ssh $USERNAME@$DROPLET_IP 'cd /root/islamic-study-site && docker-compose logs'"
echo "🛑 To stop: ssh $USERNAME@$DROPLET_IP 'cd /root/islamic-study-site && docker-compose down'"
echo "🔄 To update: ssh $USERNAME@$DROPLET_IP 'cd /root/islamic-study-site && git pull && docker-compose up -d --build'"
