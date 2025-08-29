#!/usr/bin/env python3
"""
DeenBot Service Manager - Comprehensive Process Management
Ensures 100% uptime for all DeenBot services with automatic recovery
"""

import os
import sys
import time
import json
import logging
import signal
import subprocess
import threading
import psutil
from datetime import datetime
import requests

# Configure comprehensive logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('deenbot_service.log'),
        logging.StreamHandler()
    ]
)

class DeenBotServiceManager:
    """Manages all DeenBot services with automatic recovery"""
    
    def __init__(self):
        self.services = {
            'comprehensive_backend': {
                'script': 'comprehensive_deenbot_backend.py',
                'port': 8080,
                'process': None,
                'health_endpoint': '/health',
                'max_restarts': 5,
                'restart_cooldown': 60,
                'restart_count': 0,
                'last_restart': 0,
                'status': 'stopped'
            }
        }
        
        self.running = True
        self.monitor_interval = 30
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
        
        logging.info("🚀 DeenBot Service Manager initialized")
    
    def signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        logging.info(f"🛑 Received signal {signum}, shutting down gracefully...")
        self.running = False
        self.stop_all_services()
        sys.exit(0)
    
    def check_port_available(self, port):
        """Check if a port is available"""
        try:
            import socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                return True
        except OSError:
            return False
    
    def kill_process_on_port(self, port):
        """Kill any process using the specified port"""
        try:
            for proc in psutil.process_iter(['pid', 'name', 'connections']):
                try:
                    for conn in proc.connections():
                        if conn.lport == port:
                            logging.info(f"🔫 Killing process {proc.pid} using port {port}")
                            proc.terminate()
                            proc.wait(timeout=5)
                            return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                    continue
        except Exception as e:
            logging.error(f"❌ Error killing process on port {port}: {e}")
        return False
    
    def start_service(self, service_name):
        """Start a specific service"""
        service = self.services[service_name]
        
        # Check if already running
        if service['process'] and service['process'].poll() is None:
            logging.info(f"✅ {service_name} is already running")
            return True
        
        # Kill any existing process on the port
        if not self.check_port_available(service['port']):
            self.kill_process_on_port(service['port'])
            time.sleep(2)
        
        try:
            # Activate virtual environment if it exists
            if os.path.exists('deenbot_env/bin/activate'):
                activate_cmd = f"source deenbot_env/bin/activate && python3 {service['script']}"
                process = subprocess.Popen(
                    activate_cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    preexec_fn=os.setsid
                )
            else:
                process = subprocess.Popen(
                    [sys.executable, service['script']],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            
            service['process'] = process
            service['status'] = 'starting'
            
            # Wait for startup
            time.sleep(10)
            
            # Check if service is healthy
            if self.check_service_health(service_name):
                service['status'] = 'running'
                service['restart_count'] = 0
                logging.info(f"✅ {service_name} started successfully on port {service['port']}")
                return True
            else:
                service['status'] = 'failed'
                logging.error(f"❌ {service_name} failed to start properly")
                return False
                
        except Exception as e:
            service['status'] = 'error'
            logging.error(f"❌ Error starting {service_name}: {e}")
            return False
    
    def check_service_health(self, service_name):
        """Check if a service is healthy"""
        service = self.services[service_name]
        
        try:
            response = requests.get(
                f"http://localhost:{service['port']}{service['health_endpoint']}",
                timeout=10
            )
            if response.status_code == 200:
                return True
        except Exception as e:
            logging.debug(f"Health check failed for {service_name}: {e}")
        
        return False
    
    def restart_service(self, service_name):
        """Restart a specific service"""
        service = self.services[service_name]
        current_time = time.time()
        
        # Check cooldown period
        if current_time - service['last_restart'] < service['restart_cooldown']:
            logging.info(f"⏳ {service_name} restart cooldown active")
            return False
        
        # Check restart limit
        if service['restart_count'] >= service['max_restarts']:
            logging.error(f"🚨 {service_name} reached maximum restart attempts!")
            return False
        
        logging.info(f"🔄 Restarting {service_name} (attempt {service['restart_count'] + 1}/{service['max_restarts']})")
        
        # Stop service
        self.stop_service(service_name)
        time.sleep(5)
        
        # Start service
        if self.start_service(service_name):
            service['restart_count'] += 1
            service['last_restart'] = current_time
            return True
        else:
            return False
    
    def stop_service(self, service_name):
        """Stop a specific service"""
        service = self.services[service_name]
        
        if service['process']:
            try:
                if hasattr(service['process'], 'terminate'):
                    service['process'].terminate()
                    service['process'].wait(timeout=10)
                else:
                    os.killpg(os.getpgid(service['process'].pid), signal.SIGTERM)
                
                service['status'] = 'stopped'
                service['process'] = None
                logging.info(f"🛑 {service_name} stopped")
                
            except Exception as e:
                logging.error(f"❌ Error stopping {service_name}: {e}")
    
    def stop_all_services(self):
        """Stop all services"""
        logging.info("🛑 Stopping all services...")
        for service_name in self.services:
            self.stop_service(service_name)
    
    def monitor_services(self):
        """Monitor all services and restart if needed"""
        while self.running:
            try:
                for service_name, service in self.services.items():
                    if service['status'] == 'running':
                        if not self.check_service_health(service_name):
                            logging.warning(f"⚠️ {service_name} is not responding, attempting restart...")
                            if not self.restart_service(service_name):
                                logging.error(f"❌ Failed to restart {service_name}")
                    
                    elif service['status'] in ['stopped', 'failed', 'error']:
                        logging.info(f"🔄 Attempting to start {service_name}...")
                        if not self.start_service(service_name):
                            logging.error(f"❌ Failed to start {service_name}")
                
                # Log status
                self.log_status()
                
                # Wait before next check
                time.sleep(self.monitor_interval)
                
            except Exception as e:
                logging.error(f"❌ Error in monitoring loop: {e}")
                time.sleep(self.monitor_interval)
    
    def log_status(self):
        """Log current status of all services"""
        status_summary = {}
        for service_name, service in self.services.items():
            status_summary[service_name] = {
                'status': service['status'],
                'port': service['port'],
                'restart_count': service['restart_count'],
                'uptime': time.time() - service['last_restart'] if service['last_restart'] > 0 else 0
            }
        
        logging.info(f"📊 Service Status: {json.dumps(status_summary, indent=2)}")
    
    def start_all_services(self):
        """Start all services"""
        logging.info("🚀 Starting all DeenBot services...")
        
        for service_name in self.services:
            if not self.start_service(service_name):
                logging.error(f"❌ Failed to start {service_name}")
        
        # Start monitoring in background
        monitor_thread = threading.Thread(target=self.monitor_services, daemon=True)
        monitor_thread.start()
        
        logging.info("✅ All services started, monitoring active")
    
    def run(self):
        """Main run loop"""
        try:
            self.start_all_services()
            
            # Keep main thread alive
            while self.running:
                time.sleep(1)
                
        except KeyboardInterrupt:
            logging.info("🛑 Interrupted by user")
        except Exception as e:
            logging.error(f"❌ Unexpected error: {e}")
        finally:
            self.stop_all_services()
            logging.info("🔒 Service Manager shutdown complete")

def main():
    """Main entry point"""
    logging.info("🕌 DeenBot Service Manager - Islamic AI Assistant")
    logging.info("==================================================")
    
    # Check if running as root (for port binding)
    if os.geteuid() == 0:
        logging.info("✅ Running with root privileges")
    else:
        logging.warning("⚠️ Not running as root - some ports may be restricted")
    
    # Create and run service manager
    manager = DeenBotServiceManager()
    manager.run()

if __name__ == '__main__':
    main()
