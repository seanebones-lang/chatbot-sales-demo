#!/bin/bash

echo "🕌 DeenBot Production Deployment - DigitalOcean"
echo "================================================"
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ This script must be run as root (use sudo)"
    exit 1
fi

# Configuration
DEENBOT_DIR="/root/islamic-study-site"
SERVICE_NAME="deenbot"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

echo "🚀 Starting production deployment..."

# Install system dependencies
echo "📦 Installing system dependencies..."
apt-get update
apt-get install -y python3 python3-pip python3-venv nginx supervisor curl wget git

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
pip3 install psutil requests

# Create application directory
echo "📁 Setting up application directory..."
mkdir -p $DEENBOT_DIR
cd $DEENBOT_DIR

# Copy application files (assuming they're in current directory)
echo "📋 Copying application files..."
cp -r . $DEENBOT_DIR/ 2>/dev/null || echo "⚠️ Files may already exist"

# Create virtual environment
echo "🔧 Setting up Python virtual environment..."
python3 -m venv deenbot_env
source deenbot_env/bin/activate
pip install -r requirements.txt
pip install psutil requests

# Create logs directory
mkdir -p logs
chmod 755 logs

# Install systemd service
echo "⚙️ Installing systemd service..."
cp deenbot.service $SERVICE_FILE
systemctl daemon-reload
systemctl enable $SERVICE_NAME

# Configure nginx
echo "🌐 Configuring nginx..."
cat > /etc/nginx/sites-available/deenbot << 'EOF'
server {
    listen 80;
    server_name _;
    
    # Frontend static files
    location / {
        root /root/islamic-study-site;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
    
    # Backend API proxy
    location /api/ {
        proxy_pass http://localhost:8080/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Health check endpoint
    location /health {
        proxy_pass http://localhost:8080/health;
        proxy_set_header Host $host;
    }
    
    # Status endpoint
    location /status {
        proxy_pass http://localhost:8080/status;
        proxy_set_header Host $host;
    }
    
    # Chat endpoint
    location /chat {
        proxy_pass http://localhost:8080/chat;
        proxy_set_header Host $host;
        proxy_set_header Content-Type application/json;
    }
}
EOF

# Enable nginx site
ln -sf /etc/nginx/sites-available/deenbot /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

# Test nginx configuration
nginx -t
if [ $? -eq 0 ]; then
    systemctl restart nginx
    systemctl enable nginx
    echo "✅ Nginx configured and started"
else
    echo "❌ Nginx configuration error"
    exit 1
fi

# Start DeenBot service
echo "🚀 Starting DeenBot service..."
systemctl start $SERVICE_NAME

# Wait for service to start
echo "⏳ Waiting for service to start..."
sleep 15

# Check service status
if systemctl is-active --quiet $SERVICE_NAME; then
    echo "✅ DeenBot service is running"
else
    echo "❌ DeenBot service failed to start"
    systemctl status $SERVICE_NAME
    exit 1
fi

# Check if backend is responding
echo "🔍 Testing backend connectivity..."
if curl -s http://localhost:8080/health > /dev/null; then
    echo "✅ Backend is responding on port 8080"
else
    echo "❌ Backend is not responding on port 8080"
    exit 1
fi

# Check if frontend is accessible
echo "🌐 Testing frontend accessibility..."
if curl -s http://localhost/ > /dev/null; then
    echo "✅ Frontend is accessible on port 80"
else
    echo "❌ Frontend is not accessible on port 80"
    exit 1
fi

# Setup monitoring and logging
echo "📊 Setting up monitoring..."
cat > /etc/logrotate.d/deenbot << 'EOF'
/root/islamic-study-site/logs/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 644 root root
}
EOF

# Create monitoring script
cat > /root/monitor_deenbot.sh << 'EOF'
#!/bin/bash
# Simple monitoring script for DeenBot

LOG_FILE="/root/islamic-study-site/logs/monitor.log"
SERVICE_NAME="deenbot"

echo "$(date): Checking DeenBot status..." >> $LOG_FILE

# Check systemd service
if ! systemctl is-active --quiet $SERVICE_NAME; then
    echo "$(date): Service is down, attempting restart..." >> $LOG_FILE
    systemctl restart $SERVICE_NAME
    sleep 10
    
    if systemctl is-active --quiet $SERVICE_NAME; then
        echo "$(date): Service restarted successfully" >> $LOG_FILE
    else
        echo "$(date): Service restart failed!" >> $LOG_FILE
    fi
fi

# Check backend health
if ! curl -s http://localhost:8080/health > /dev/null; then
    echo "$(date): Backend not responding, restarting service..." >> $LOG_FILE
    systemctl restart $SERVICE_NAME
fi

echo "$(date): Monitoring check complete" >> $LOG_FILE
EOF

chmod +x /root/monitor_deenbot.sh

# Add monitoring to crontab
(crontab -l 2>/dev/null; echo "*/5 * * * * /root/monitor_deenbot.sh") | crontab -

echo ""
echo "🎉 DeenBot Production Deployment Complete!"
echo "=========================================="
echo ""
echo "🌐 Frontend: http://$(curl -s ifconfig.me)"
echo "🔧 Backend API: http://$(curl -s ifconfig.me):8080"
echo "📊 Service Status: systemctl status $SERVICE_NAME"
echo "📋 Service Logs: journalctl -u $SERVICE_NAME -f"
echo "📁 Application Logs: $DEENBOT_DIR/logs/"
echo "🔄 Restart Service: systemctl restart $SERVICE_NAME"
echo "🛑 Stop Service: systemctl stop $SERVICE_NAME"
echo ""
echo "📊 Monitoring is active and will check every 5 minutes"
echo "✅ Service will auto-start on system reboot"
echo "🔄 Automatic restart on failure is enabled"
echo ""
echo "🔍 To test the system:"
echo "   curl http://localhost:8080/health"
echo "   curl http://localhost/"
echo ""
echo "📝 For troubleshooting, check:"
echo "   - Service logs: journalctl -u $SERVICE_NAME -f"
echo "   - Application logs: tail -f $DEENBOT_DIR/logs/*.log"
echo "   - Nginx logs: tail -f /var/log/nginx/error.log"
