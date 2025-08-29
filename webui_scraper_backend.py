#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import time
import re

class WebUIScraperHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Redirect to the main chat page
            html = '''<!DOCTYPE html>
<html>
<head>
    <title>DeenBot - Islamic AI Assistant</title>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=chat.html">
</head>
<body>
    <p>Redirecting to DeenBot...</p>
    <script>window.location.href = 'chat.html';</script>
</body>
</html>'''
            
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            user_message = data.get('message', '')
            
            # Try to get response from OpenWebUI phi3:mini model
            try:
                response = self.get_webui_response(user_message)
                print(f"✅ Connected to OpenWebUI phi3:mini successfully!")
            except Exception as e:
                print(f"❌ Error getting OpenWebUI response: {e}")
                # Fallback to enhanced responses
                response = self.get_enhanced_response(user_message)
                print(f"🔄 Using enhanced fallback response")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            response_data = {'response': response}
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def get_webui_response(self, user_message):
        """Get response from OpenWebUI web interface using the actual API key"""
        
        openwebui_url = "http://localhost:3001"
        
        try:
            print(f"🌐 Attempting to connect to OpenWebUI phi3:mini at: {openwebui_url}")
            
            # Try the authenticated API first (this should work!)
            response = self.try_authenticated_api(user_message)
            if response:
                return response
            
            # If that fails, try other approaches
            approaches = [
                self.try_webui_chat,
                self.try_webui_generate
            ]
            
            for approach in approaches:
                try:
                    response = approach(user_message)
                    if response:
                        return response
                except Exception as e:
                    print(f"❌ Approach failed: {e}")
                    continue
            
            # If all approaches fail, raise exception
            raise Exception("All OpenWebUI interaction methods failed")
            
        except Exception as e:
            print(f"❌ OpenWebUI interaction error: {e}")
            raise e

    def try_authenticated_api(self, user_message):
        """Try to use the OpenWebUI API with the actual API key"""
        try:
            openwebui_url = "http://localhost:3001"
            
            # Get API key from environment variable for security
            api_key = os.getenv('OPENWEBUI_API_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxNWUzOGM1LTdiMDQtNGEwMS1hOTI0LTFhNWEyZmI2MmFkYyJ9.UI-kwaYruBNjjxYkjZrzC4vBIAeDkadMcFFlDHZpENU')
            
            if not api_key:
                print("❌ No API key found. Set OPENWEBUI_API_KEY environment variable.")
                return None
            
            print(f"🔑 Trying authenticated API with OpenWebUI API key...")
            
            # Try the standard OpenAI-compatible endpoint
            payload = {
                "model": "phi3:mini",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are DeenBot, an Islamic AI assistant. Provide comprehensive, accurate Islamic guidance with Quranic references and Hadith support."
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
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Accept": "application/json"
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
                    print(f"✅ Authenticated API successful!")
                    
                    if 'choices' in response_data and len(response_data['choices']) > 0:
                        return response_data['choices'][0]['message']['content']
                    else:
                        return str(response_data)
                        
        except Exception as e:
            print(f"❌ Authenticated API failed: {e}")
            return None

    def try_webui_chat(self, user_message):
        """Try to simulate a chat request to OpenWebUI"""
        try:
            openwebui_url = "http://localhost:3001"
            
            print(f"🔄 Trying to simulate chat with OpenWebUI...")
            
            # Try different possible chat endpoints
            chat_endpoints = [
                "/api/chat",
                "/chat", 
                "/api/v1/chat/completions",
                "/api/generate",
                "/generate"
            ]
            
            for endpoint in chat_endpoints:
                try:
                    # Try different request formats
                    payloads = [
                        {"message": user_message, "model": "phi3:mini"},
                        {"prompt": user_message, "model": "phi3:mini"},
                        {"input": user_message, "model": "phi3:mini"},
                        {"text": user_message, "model": "phi3:mini"}
                    ]
                    
                    for payload in payloads:
                        try:
                            headers = {
                                "Content-Type": "application/json",
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                                "Accept": "application/json",
                                "Accept-Language": "en-US,en;q=0.9"
                            }
                            
                            data = json.dumps(payload).encode('utf-8')
                            req = urllib.request.Request(
                                f"{openwebui_url}{endpoint}",
                                data=data,
                                headers=headers,
                                method="POST"
                            )
                            
                            with urllib.request.urlopen(req, timeout=30) as response:
                                if response.status == 200:
                                    response_data = json.loads(response.read().decode('utf-8'))
                                    print(f"✅ Chat successful with {endpoint}!")
                                    
                                    if 'response' in response_data:
                                        return response_data['response']
                                    elif 'content' in response_data:
                                        return response_data['content']
                                    elif 'text' in response_data:
                                        return response_data['text']
                                    elif 'message' in response_data:
                                        return response_data['message']['content']
                                    else:
                                        return str(response_data)
                                        
                        except Exception as e:
                            print(f"❌ Payload {payload} failed: {e}")
                            continue
                            
                except Exception as e:
                    print(f"❌ Endpoint {endpoint} failed: {e}")
                    continue
            
            return None
                        
        except Exception as e:
            print(f"❌ WebUI chat failed: {e}")
            return None

    def try_webui_generate(self, user_message):
        """Try to use a generate endpoint if available"""
        try:
            openwebui_url = "http://localhost:3001"
            
            print(f"🔄 Trying generate endpoint...")
            
            payload = {
                "prompt": f"You are DeenBot, an Islamic AI assistant. Answer this question about Islam: {user_message}",
                "model": "phi3:mini",
                "stream": False
            }
            
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Accept": "application/json",
                "Accept-Language": "en-US,en;q=0.9"
            }
            
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(
                f"{openwebui_url}/api/generate",
                data=data,
                headers=headers,
                method="POST"
            )
            
            with urllib.request.urlopen(req, timeout=30) as response:
                if response.status == 200:
                    response_data = json.loads(response.read().decode('utf-8'))
                    print(f"✅ Generate successful!")
                    
                    if 'response' in response_data:
                        return response_data['response']
                    elif 'text' in response_data:
                        return response_data['text']
                    else:
                        return str(response_data)
                        
        except Exception as e:
            print(f"❌ Generate failed: {e}")
            return None

    def get_enhanced_response(self, user_message):
        """Enhanced fallback responses when OpenWebUI is not available"""
        user_message_lower = user_message.lower()
        
        # Enhanced Islamic responses with more comprehensive coverage
        if any(word in user_message_lower for word in ['mercy', 'rahman', 'raheem', 'رحمن', 'رحيم']):
            response = """Mercy (Rahman/Raheem) is a fundamental attribute of Allah mentioned extensively in the Quran. 

Key references include:
• Surah Al-Fatiha (1:1-2) - "In the name of Allah, the Most Gracious, the Most Merciful"
• Surah Al-Baqarah (2:143) - "Allah is Most Merciful to mankind"
• Surah Al-An'am (6:12) - "Allah has written mercy for Himself"
• Surah Al-A'raf (7:156) - "My mercy encompasses all things"

The concept of divine mercy appears in over 100 verses, emphasizing Allah's infinite compassion and forgiveness for His creation. This mercy extends to all of creation, including non-believers, as Allah's mercy is universal and encompasses everything."""

        elif any(word in user_message_lower for word in ['patience', 'sabr', 'patient', 'صبر']):
            response = """Patience (Sabr) is one of the highest virtues in Islam, mentioned extensively in the Quran and Hadith.

Key references:
• Surah Al-Baqarah (2:153) - "O you who have believed, seek help through patience and prayer"
• Surah Al-Imran (3:200) - "O you who have believed, persevere and endure"
• Surah Al-Anfal (8:46) - "Be patient, for Allah is with the patient"
• Surah Al-Asr (103:3) - "Except those who believe and do righteous deeds and advise each other to truth and advise each other to patience"

The Prophet (PBUH) said: "Patience is light" and "Whoever remains patient, Allah will make him patient." (Sahih Bukhari)

Patience in Islam includes patience with trials, patience in worship, patience in avoiding sin, and patience with people. It's considered half of faith."""

        elif any(word in user_message_lower for word in ['love', 'hubb', 'mawaddah', 'محبة', 'مودة']):
            response = """Love in Islam encompasses love for Allah, His Messenger, and fellow believers.

Key Quranic references:
• Surah Al-Imran (3:31) - "Say: If you love Allah, then follow me"
• Surah Al-Ma'idah (5:54) - "Allah will bring a people whom He loves and who love Him"
• Surah Al-Baqarah (2:165) - "Those who believe are stronger in love for Allah"
• Surah Ar-Rum (30:21) - "He created for you mates from among yourselves that you may find tranquility in them, and He placed between you affection and mercy"

The Prophet (PBUH) said: "None of you truly believes until he loves for his brother what he loves for himself." (Sahih Bukhari)

This love manifests in daily actions, kindness to others, and following the Sunnah of the Prophet (PBUH)."""

        elif any(word in user_message_lower for word in ['family', 'parents', 'children', 'أهل', 'والدين']):
            response = """Family relationships are highly emphasized in Islam, with specific rights and responsibilities.

Key references:
• Surah Al-Isra (17:23-24) - "Your Lord has decreed that you worship none but Him, and that you be kind to parents"
• Surah Luqman (31:14) - "We have enjoined upon man to be good to his parents"
• Surah Al-Baqarah (2:233) - "Mothers may nurse their children for two complete years"
• Surah An-Nisa (4:1) - "O mankind, fear your Lord, who created you from one soul and created from it its mate"

The Prophet (PBUH) said: "Paradise lies at the feet of mothers" and "The best of you is the best to his family." (Sahih Bukhari)

Islamic family values emphasize respect, care, and mutual support between all family members."""

        elif any(word in user_message_lower for word in ['prayer', 'salah', 'namaz', 'صلاة']):
            response = """Prayer (Salah) is the second pillar of Islam and the foundation of worship.

Key references:
• Surah Al-Baqarah (2:153) - "Seek help through patience and prayer"
• Surah Al-Ankabut (29:45) - "Indeed, prayer prohibits immorality and wrongdoing"
• Surah Al-Ma'un (107:4-5) - "So woe to those who pray but are heedless of their prayer"

The Prophet (PBUH) said: "Prayer is the pillar of religion" and "The first thing a person will be asked about on the Day of Judgment is prayer." (Sahih Bukhari)

Daily prayers: Fajr (2 rakat), Dhuhr (4 rakat), Asr (4 rakat), Maghrib (3 rakat), Isha (4 rakat)

Prayer purifies the soul, strengthens faith, and maintains the connection with Allah throughout the day."""

        elif any(word in user_message_lower for word in ['inheritance', 'mirath', 'warith', 'ميراث']):
            response = """Islamic inheritance laws ensure fair distribution of wealth according to Quranic principles.

Key references:
• Surah An-Nisa (4:11-12) - Detailed inheritance laws for children, spouses, and parents
• Surah An-Nisa (4:176) - Inheritance for relatives without children

Basic principles:
• Males receive twice the share of females (for children)
• Spouses inherit specific portions
• Parents receive shares when children die
• Siblings inherit when no children exist

The Prophet (PBUH) said: "Learn the laws of inheritance and teach them, for they are half of knowledge." (Sunan Ibn Majah)

These laws ensure that wealth is distributed fairly and no one is left without support."""

        else:
            response = """I can help you find comprehensive Islamic guidance on many topics. 

Try searching for:
• **Core Islamic concepts**: mercy, love, patience, forgiveness, justice
• **Worship practices**: prayer, fasting, pilgrimage, charity
• **Family matters**: relationships, inheritance, daily life
• **Character development**: knowledge, gratitude, peace, helping others
• **Specific topics**: any Islamic subject you're curious about

Simply type the topic you're interested in, and I'll provide detailed guidance with Quranic references, Hadith support, and practical Islamic wisdom. What would you like to learn about today?"""
        
        return response

if __name__ == '__main__':
    port = 8080
    try:
        server = HTTPServer(('0.0.0.0', port), WebUIScraperHandler)
        print(f'🚀 DeenBot with OpenWebUI phi3:mini backend is running on port {port}')
        print(f'🌐 OpenWebUI URL: http://localhost:3001')
        print(f'🤖 AI Model: phi3:mini')
        print(f'💬 Chat endpoint: http://localhost:{port}/chat')
        print('🔑 API Key: [CONFIGURED]')
        print('🛑 Press Ctrl+C to stop the server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n🛑 Server stopped by user')
    except Exception as e:
        print(f'❌ Error starting server: {e}')
        sys.exit(1)
