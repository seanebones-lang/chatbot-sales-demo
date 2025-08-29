#!/bin/bash
# DeenBot Monitor and Auto-Restart Script
# Ensures 100% uptime for the Islamic AI Assistant

echo "🚀 DeenBot Monitor and Auto-Restart System Starting..."
echo "=================================================="

# Configuration
DEENBOT_SCRIPT="enhanced_deenbot_backend.py"
DEENBOT_PORT=8080
CHECK_INTERVAL=30
MAX_RESTART_ATTEMPTS=5
RESTART_COOLDOWN=60
LOG_FILE="deenbot_monitor.log"

# Initialize counters
restart_count=0
last_restart_time=0

# Function to check if DeenBot is running
check_deenbot() {
    if curl -s http://localhost:$DEENBOT_PORT/health > /dev/null 2>&1; then
        return 0  # Running
    else
        return 1  # Not running
    fi
}

# Function to start DeenBot
start_deenbot() {
    echo "$(date): 🔄 Starting DeenBot..." | tee -a $LOG_FILE
    
    # Activate virtual environment and start backend
    source deenbot_env/bin/activate
    nohup python3 $DEENBOT_SCRIPT > deenbot.log 2>&1 &
    
    # Wait for startup
    sleep 20
    
    # Check if started successfully
    if check_deenbot; then
        echo "$(date): ✅ DeenBot started successfully" | tee -a $LOG_FILE
        return 0
    else
        echo "$(date): ❌ DeenBot failed to start" | tee -a $LOG_FILE
        return 1
    fi
}

# Function to restart DeenBot
restart_deenbot() {
    current_time=$(date +%s)
    
    # Check cooldown period
    if [ $((current_time - last_restart_time)) -lt $RESTART_COOLDOWN ]; then
        echo "$(date): ⏳ Cooldown period active, waiting..." | tee -a $LOG_FILE
        return 1
    fi
    
    # Check restart limit
    if [ $restart_count -ge $MAX_RESTART_ATTEMPTS ]; then
        echo "$(date): 🚨 CRITICAL: Maximum restart attempts reached!" | tee -a $LOG_FILE
        echo "$(date): 🚨 Manual intervention required!" | tee -a $LOG_FILE
        return 1
    fi
    
    echo "$(date): 🔄 Restarting DeenBot (attempt $((restart_count + 1))/$MAX_RESTART_ATTEMPTS)..." | tee -a $LOG_FILE
    
    # Kill existing process
    pkill -f $DEENBOT_SCRIPT
    
    # Wait for cleanup
    sleep 5
    
    # Start fresh
    if start_deenbot; then
        restart_count=$((restart_count + 1))
        last_restart_time=$current_time
        echo "$(date): ✅ DeenBot restarted successfully" | tee -a $LOG_FILE
        return 0
    else
        echo "$(date): ❌ DeenBot restart failed" | tee -a $LOG_FILE
        return 1
    fi
}

# Function to log status
log_status() {
    if check_deenbot; then
        echo "$(date): ✅ DeenBot is running normally" | tee -a $LOG_FILE
    else
        echo "$(date): ❌ DeenBot is not responding" | tee -a $LOG_FILE
    fi
}

# Main monitoring loop
echo "$(date): 📡 Starting monitoring loop..." | tee -a $LOG_FILE

while true; do
    # Check DeenBot status
    if check_deenbot; then
        # DeenBot is running normally
        if [ $restart_count -gt 0 ]; then
            echo "$(date): ✅ DeenBot recovered successfully after $restart_count restart(s)" | tee -a $LOG_FILE
            restart_count=0  # Reset counter on successful recovery
        fi
    else
        # DeenBot is not responding
        echo "$(date): 🚨 DeenBot is not responding!" | tee -a $LOG_FILE
        
        # Attempt restart
        if restart_deenbot; then
            echo "$(date): ✅ DeenBot restarted successfully" | tee -a $LOG_FILE
        else
            echo "$(date): ❌ Failed to restart DeenBot" | tee -a $LOG_FILE
        fi
    fi
    
    # Log current status
    log_status
    
    # Wait before next check
    sleep $CHECK_INTERVAL
done
