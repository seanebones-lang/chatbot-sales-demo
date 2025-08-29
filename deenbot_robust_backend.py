#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import time
import re
import threading
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/supervisor/deenbot.log'),
        logging.StreamHandler()
    ]
)

class RobustDeenBotHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.health_status = "healthy"
        self.last_health_check = time.time()
        self.request_count = 0
        self.error_count = 0
        self.start_time = time.time()
        super().__init__(*args, **kwargs)
    
    def log_message(self, format, *args):
        logging.info(f"{self.client_address[0]} - {format % args}")
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '''<!DOCTYPE html>
<html>
<head>
    <title>DeenBot - Islamic AI Assistant</title>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=deenbot.html">
</head>
<body>
    <p>Redirecting to DeenBot...</p>
    <script>window.location.href = 'deenbot.html';</script>
</body>
</html>'''
            
            self.wfile.write(html.encode())
        elif self.path == '/health':
            # Health check endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            uptime = time.time() - self.start_time
            health_data = {
                'status': self.health_status,
                'uptime_seconds': int(uptime),
                'uptime_formatted': f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s",
                'request_count': self.request_count,
                'error_count': self.error_count,
                'error_rate': f"{(self.error_count / max(self.request_count, 1)) * 100:.2f}%" if self.request_count > 0 else "0%",
                'timestamp': datetime.now().isoformat(),
                'version': '2.0.0'
            }
            
            self.wfile.write(json.dumps(health_data, indent=2).encode())
        elif self.path == '/status':
            # Detailed status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            status_data = {
                'service': 'DeenBot Islamic AI Assistant',
                'status': 'operational',
                'backend': 'Robust Multi-Layer System',
                'features': [
                    'AI-powered Islamic guidance',
                    'Quran and Hadith references',
                    'Auto-recovery system',
                    'Health monitoring',
                    'Multiple fallback layers'
                ],
                'uptime': time.time() - self.start_time,
                'requests_processed': self.request_count,
                'last_updated': datetime.now().isoformat()
            }
            
            self.wfile.write(json.dumps(status_data, indent=2).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/chat':
            self.request_count += 1
            
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                
                user_message = data.get('message', '')
                
                if not user_message:
                    self.send_error_response("No message provided")
                    return
                
                # Try multiple AI backends with fallback
                response = self.get_robust_response(user_message)
                
                self.send_success_response(response)
                self.health_status = "healthy"
                
            except Exception as e:
                self.error_count += 1
                logging.error(f"Error processing chat request: {e}")
                self.send_error_response(f"Processing error: {str(e)}")
                self.health_status = "degraded"
        else:
            self.send_response(404)
            self.end_headers()

    def get_robust_response(self, user_message):
        """Multi-layer response system with fallbacks"""
        
        # Layer 1: Try OpenWebUI AI
        try:
            response = self.get_openwebui_response(user_message)
            if response:
                logging.info("✅ OpenWebUI AI response successful")
                return response
        except Exception as e:
            logging.warning(f"⚠️ OpenWebUI failed: {e}")
        
        # Layer 2: Try enhanced local knowledge base
        try:
            response = self.get_enhanced_local_response(user_message)
            if response:
                logging.info("✅ Enhanced local knowledge response successful")
                return response
        except Exception as e:
            logging.warning(f"⚠️ Enhanced local failed: {e}")
        
        # Layer 3: Basic fallback response
        try:
            response = self.get_basic_fallback_response(user_message)
            logging.info("✅ Basic fallback response successful")
            return response
        except Exception as e:
            logging.error(f"❌ All response layers failed: {e}")
            return self.get_emergency_response(user_message)

    def get_openwebui_response(self, user_message):
        """Get response from OpenWebUI AI"""
        try:
            openwebui_url = "http://localhost:3001"
            
            # Test connection first
            if not self.test_connection(openwebui_url):
                return None
            
            api_key = os.getenv('OPENWEBUI_API_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxNWUzOGM1LTdiMDQtNGEwMS1hOTI0LTFhNWEyZmI2MmFkYyJ9.UI-kwaYruBNjjxYkjZrzC4vBIAeDkadMcFFlDHZpENU')
            
            payload = {
                "model": "phi3:mini",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are DeenBot, an Islamic AI assistant. Provide comprehensive, accurate Islamic guidance with Quranic references and Hadith support. Always be helpful, respectful, and accurate in your responses."
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                "stream": False,
                "temperature": 0.7,
                "max_tokens": 1000
            }
            
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
                "User-Agent": "DeenBot/2.0.0"
            }
            
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(
                f"{openwebui_url}/api/v1/chat/completions",
                data=data,
                headers=headers,
                method="POST"
            )
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status == 200:
                    response_data = json.loads(response.read().decode('utf-8'))
                    
                    if 'choices' in response_data and len(response_data['choices']) > 0:
                        return response_data['choices'][0]['message']['content']
                    
            return None
            
        except Exception as e:
            logging.error(f"OpenWebUI error: {e}")
            return None

    def get_enhanced_local_response(self, user_message):
        """Enhanced local knowledge base with Islamic wisdom"""
        user_message_lower = user_message.lower()
        
        # Comprehensive Islamic knowledge database
        islamic_knowledge = {
            'prayer': {
                'response': "Prayer (Salah) is the second pillar of Islam and a direct connection with Allah. The Prophet (PBUH) said: 'The prayer is the pillar of religion.' (Sahih Bukhari) Prayer purifies the heart, brings peace, and strengthens faith. It's recommended to pray in congregation at the mosque, especially for Friday prayers.",
                'quran_ref': "Al-Baqarah 2:238 - 'Maintain with care the prayers and the middle prayer and stand before Allah, devoutly obedient.'",
                'hadith_ref': "Sahih Bukhari - 'The prayer is the pillar of religion.'"
            },
            'quran': {
                'response': "The Quran is Allah's final revelation to humanity, revealed to Prophet Muhammad (PBUH) over 23 years. It contains guidance for all aspects of life. The Prophet (PBUH) said: 'The best of you is the one who learns the Quran and teaches it.' (Sahih Bukhari) Reading and understanding the Quran brings immense blessings and guidance.",
                'quran_ref': "Al-Baqarah 2:2 - 'This is the Book about which there is no doubt, a guidance for those conscious of Allah.'",
                'hadith_ref': "Sahih Bukhari - 'The best of you is the one who learns the Quran and teaches it.'"
            },
            'patience': {
                'response': "Patience (Sabr) is highly valued in Islam. Allah says: 'Indeed, Allah is with the patient.' (Al-Baqarah 2:153) The Prophet (PBUH) said: 'Patience is light.' (Sahih Muslim) Patience during difficulties brings great rewards and strengthens our faith. It's a quality that Allah loves and rewards abundantly.",
                'quran_ref': "Al-Baqarah 2:153 - 'O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient.'",
                'hadith_ref': "Sahih Muslim - 'Patience is light.'"
            },
            'mercy': {
                'response': "Allah is Ar-Rahman (The Most Merciful) and Ar-Raheem (The Especially Merciful). His mercy encompasses everything. The Prophet (PBUH) said: 'Allah has divided mercy into one hundred parts, and He kept ninety-nine parts with Him and sent down one part to the earth.' (Sahih Bukhari) We should show mercy to all creation.",
                'quran_ref': "Al-Fatiha 1:1-2 - 'In the name of Allah, the Entirely Merciful, the Especially Merciful.'",
                'hadith_ref': "Sahih Bukhari - 'Allah has divided mercy into one hundred parts...'"
            },
            'family': {
                'response': "Family is the foundation of Islamic society. The Prophet (PBUH) said: 'The best of you is the best to his family.' (Sahih Bukhari) Islam teaches us to be kind to parents, spouses, and children. Family relationships are sacred and should be maintained with love, respect, and Islamic values.",
                'quran_ref': "Al-Isra 17:23-24 - 'Your Lord has decreed that you worship none but Him, and that you be kind to parents.'",
                'hadith_ref': "Sahih Bukhari - 'The best of you is the best to his family.'"
            },
            'knowledge': {
                'response': "Seeking knowledge is obligatory for every Muslim. The Prophet (PBUH) said: 'Seek knowledge from the cradle to the grave.' (Various sources) Knowledge brings us closer to Allah and helps us serve His creation better. Both religious and worldly knowledge are valuable when used for good purposes.",
                'quran_ref': "Al-Baqarah 2:269 - 'He gives wisdom to whom He wills, and whoever has been given wisdom has certainly been given much good.'",
                'hadith_ref': "Various sources - 'Seek knowledge from the cradle to the grave.'"
            }
        }
        
        # Check for specific topics
        for topic, info in islamic_knowledge.items():
            if topic in user_message_lower:
                return f"{info['response']}\n\n📖 Quran Reference: {info['quran_ref']}\n📚 Hadith Reference: {info['hadith_ref']}"
        
        # General Islamic guidance
        return "I'm here to provide you with authentic Islamic guidance. I can help you with topics like prayer, Quran, Hadith, family matters, patience, mercy, and many other aspects of Islam. What specific area would you like to learn about? Feel free to ask me anything about Islamic teachings, practices, or guidance for daily life."

    def get_basic_fallback_response(self, user_message):
        """Basic fallback response system"""
        return "Assalamu alaikum! I'm here to help you with Islamic guidance. While I'm experiencing some technical difficulties with my advanced AI features, I can still provide you with basic Islamic knowledge and guidance. Please try asking about prayer, Quran, Hadith, or other Islamic topics, and I'll do my best to help you."

    def get_emergency_response(self, user_message):
        """Emergency response when all systems fail"""
        return "Assalamu alaikum! I apologize, but I'm currently experiencing technical difficulties. Please try again in a moment, or contact the site administrator. In the meantime, remember that Allah is always with you, and you can find Islamic guidance in the Quran and authentic Hadith collections."

    def test_connection(self, url, timeout=5):
        """Test if a service is accessible"""
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.status == 200
        except Exception:
            return False

    def send_success_response(self, response_text):
        """Send successful response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response_data = {
            'response': response_text,
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'backend': 'Robust DeenBot System'
        }
        
        self.wfile.write(json.dumps(response_data).encode())

    def send_error_response(self, error_message):
        """Send error response"""
        self.send_response(500)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        error_data = {
            'error': error_message,
            'status': 'error',
            'timestamp': datetime.now().isoformat()
        }
        
        self.wfile.write(json.dumps(error_data).encode())

def start_health_monitor():
    """Background health monitoring thread"""
    def monitor():
        while True:
            try:
                # Check system resources
                import psutil
                cpu_percent = psutil.cpu_percent()
                memory_percent = psutil.virtual_memory().percent
                
                if cpu_percent > 80 or memory_percent > 80:
                    logging.warning(f"High resource usage: CPU {cpu_percent}%, Memory {memory_percent}%")
                
                time.sleep(60)  # Check every minute
                
            except Exception as e:
                logging.error(f"Health monitor error: {e}")
                time.sleep(60)
    
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()

if __name__ == '__main__':
    try:
        # Start health monitoring
        start_health_monitor()
        
        # Start the server
        server = HTTPServer(('0.0.0.0', 8080), RobustDeenBotHandler)
        logging.info('🚀 Robust DeenBot Islamic AI Assistant is running on port 8080')
        logging.info('🌟 Features: Multi-layer AI, Auto-recovery, Health monitoring, Fallback systems')
        server.serve_forever()
        
    except KeyboardInterrupt:
        logging.info('🛑 DeenBot server stopped by user')
    except Exception as e:
        logging.error(f'❌ DeenBot server error: {e}')
        sys.exit(1)
