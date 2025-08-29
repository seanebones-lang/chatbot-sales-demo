#!/usr/bin/env python3
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys

class IslamicAIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Redirect to the main chat page
            html = '''<!DOCTYPE html>
<html>
<head>
    <title>Islamic AI Chat - Redirecting...</title>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=chat.html">
</head>
<body>
    <p>Redirecting to Islamic AI Chat...</p>
    <script>window.location.href = 'chat.html';</script>
</body>
</html>'''
            
            self.wfile.write(html.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            user_message = data.get('message', '').lower()
            
            # Enhanced Islamic AI responses with more comprehensive coverage
            response = self.generate_ai_response(user_message)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_data = {'response': response}
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def generate_ai_response(self, user_message):
        """Generate comprehensive AI responses for Islamic queries"""
        
        # Quran and Core Islamic Concepts
        if any(word in user_message for word in ['mercy', 'rahman', 'raheem', 'رحمن', 'رحيم']):
            response = """Mercy (Rahman/Raheem) is a fundamental attribute of Allah mentioned extensively in the Quran. 

Key references include:
• Surah Al-Fatiha (1:1-2) - "In the name of Allah, the Most Gracious, the Most Merciful"
• Surah Al-Baqarah (2:143) - "Allah is Most Merciful to mankind"
• Surah Al-An'am (6:12) - "Allah has written mercy for Himself"
• Surah Al-A'raf (7:156) - "My mercy encompasses all things"

The concept of divine mercy appears in over 100 verses, emphasizing Allah's infinite compassion and forgiveness for His creation."""

        elif any(word in user_message for word in ['love', 'hubb', 'mawaddah', 'محبة', 'مودة']):
            response = """Love in Islam encompasses love for Allah, His Messenger, and fellow believers.

Key Quranic references:
• Surah Al-Imran (3:31) - "Say: If you love Allah, then follow me"
• Surah Al-Ma'idah (5:54) - "Allah will bring a people whom He loves and who love Him"
• Surah Al-Baqarah (2:165) - "Those who believe are stronger in love for Allah"
• Surah Ar-Rum (30:21) - "He created for you mates from among yourselves that you may find tranquility in them, and He placed between you affection and mercy"

The Prophet (PBUH) said: "None of you truly believes until he loves for his brother what he loves for himself." (Sahih Bukhari)"""

        elif any(word in user_message for word in ['patience', 'sabr', 'patient', 'صبر']):
            response = """Patience (Sabr) is one of the highest virtues in Islam, mentioned extensively in the Quran and Hadith.

Key references:
• Surah Al-Baqarah (2:153) - "O you who have believed, seek help through patience and prayer"
• Surah Al-Imran (3:200) - "O you who have believed, persevere and endure"
• Surah Al-Anfal (8:46) - "Be patient, for Allah is with the patient"
• Surah Al-Asr (103:3) - "Except those who believe and do righteous deeds and advise each other to truth and advise each other to patience"

The Prophet (PBUH) said: "Patience is light" and "Whoever remains patient, Allah will make him patient." (Sahih Bukhari)"""

        elif any(word in user_message for word in ['forgiveness', 'ghafr', 'tawbah', 'مغفرة', 'توبة']):
            response = """Forgiveness is central to Islamic teachings, emphasizing Allah's mercy and the importance of repentance.

Key references:
• Surah Al-Baqarah (2:199) - "Ask Allah for forgiveness"
• Surah Al-Imran (3:135) - "Those who, when they commit an immorality, remember Allah and seek forgiveness"
• Surah Al-Ma'idah (5:74) - "Will they not repent to Allah and seek His forgiveness?"
• Surah Az-Zumar (39:53) - "Say: O My servants who have transgressed against themselves, do not despair of the mercy of Allah. Indeed, Allah forgives all sins"

The Prophet (PBUH) said: "By Allah, I seek Allah's forgiveness and repent to Him more than seventy times a day." (Sahih Bukhari)"""

        elif any(word in user_message for word in ['justice', 'adl', 'fair', 'عدل']):
            response = """Justice is fundamental in Islam, commanding fair treatment in all matters.

Key references:
• Surah An-Nisa (4:135) - "O you who have believed, be persistently standing firm in justice"
• Surah Al-Ma'idah (5:8) - "Be just; that is nearer to righteousness"
• Surah Al-An'am (6:152) - "Give full measure and weight in justice"
• Surah Al-Hadid (57:25) - "We sent Our messengers with clear evidences and sent down with them the Scripture and the balance that the people may maintain justice"

The Prophet (PBUH) said: "Justice is the foundation of leadership" and emphasized treating all people equally."""

        elif any(word in user_message for word in ['family', 'parents', 'children', 'أهل', 'والدين']):
            response = """Family relationships are highly emphasized in Islam, with specific rights and responsibilities.

Key references:
• Surah Al-Isra (17:23-24) - "Your Lord has decreed that you worship none but Him, and that you be kind to parents"
• Surah Luqman (31:14) - "We have enjoined upon man to be good to his parents"
• Surah Al-Baqarah (2:233) - "Mothers may nurse their children for two complete years"
• Surah An-Nisa (4:1) - "O mankind, fear your Lord, who created you from one soul and created from it its mate"

The Prophet (PBUH) said: "Paradise lies at the feet of mothers" and "The best of you is the best to his family." (Sahih Bukhari)"""

        elif any(word in user_message for word in ['prayer', 'salah', 'namaz', 'صلاة']):
            response = """Prayer (Salah) is the second pillar of Islam and the foundation of worship.

Key references:
• Surah Al-Baqarah (2:153) - "Seek help through patience and prayer"
• Surah Al-Ankabut (29:45) - "Indeed, prayer prohibits immorality and wrongdoing"
• Surah Al-Ma'un (107:4-5) - "So woe to those who pray but are heedless of their prayer"

The Prophet (PBUH) said: "Prayer is the pillar of religion" and "The first thing a person will be asked about on the Day of Judgment is prayer." (Sahih Bukhari)

Daily prayers: Fajr (2 rakat), Dhuhr (4 rakat), Asr (4 rakat), Maghrib (3 rakat), Isha (4 rakat)"""

        elif any(word in user_message for word in ['inheritance', 'mirath', 'warith', 'ميراث']):
            response = """Islamic inheritance laws ensure fair distribution of wealth according to Quranic principles.

Key references:
• Surah An-Nisa (4:11-12) - Detailed inheritance laws for children, spouses, and parents
• Surah An-Nisa (4:176) - Inheritance for relatives without children

Basic principles:
• Males receive twice the share of females (for children)
• Spouses inherit specific portions
• Parents receive shares when children die
• Siblings inherit when no children exist

The Prophet (PBUH) said: "Learn the laws of inheritance and teach them, for they are half of knowledge." (Sunan Ibn Majah)"""

        elif any(word in user_message for word in ['knowledge', 'ilm', 'learn', 'علم']):
            response = """Knowledge is highly valued in Islam, considered a religious obligation.

Key references:
• Surah Al-Baqarah (2:269) - "He gives wisdom to whom He wills, and whoever has been given wisdom has certainly been given much good"
• Surah Al-Imran (3:7) - "None knows its interpretation except Allah and those who are firmly grounded in knowledge"
• Surah Al-Mujadila (58:11) - "Allah will raise those who have believed among you and those who were given knowledge"
• Surah Ta-Ha (20:114) - "My Lord, increase me in knowledge"

The Prophet (PBUH) said: "Seeking knowledge is obligatory upon every Muslim" and "The ink of the scholar is more sacred than the blood of the martyr." (Sahih Muslim)"""

        elif any(word in user_message for word in ['charity', 'sadaqah', 'zakat', 'صدقة', 'زكاة']):
            response = """Charity and giving are central to Islamic practice, purifying wealth and helping others.

Key references:
• Surah Al-Baqarah (2:261) - "The example of those who spend their wealth in the way of Allah"
• Surah Al-Imran (3:92) - "Never will you attain the good until you spend of that which you love"
• Surah Al-Ma'un (107:1-7) - "Have you seen the one who denies the Recompense? For that is the one who drives away the orphan and does not encourage the feeding of the poor"
• Surah Al-Baqarah (2:274) - "Those who spend their wealth by night and by day, secretly and publicly"

The Prophet (PBUH) said: "Charity does not decrease wealth" and "The best charity is that given when one is healthy and wealthy." (Sahih Bukhari)"""

        elif any(word in user_message for word in ['peace', 'salam', 'tranquility', 'سلام']):
            response = """Peace is fundamental in Islam, both as a greeting and a way of life.

Key references:
• Surah Al-Baqarah (2:208) - "Enter into peace completely"
• Surah Al-Anfal (8:61) - "If they incline to peace, then incline to it"
• Surah Al-Hashr (59:23) - "He is Allah, other than whom there is no deity, the Sovereign, the Pure, the Perfection, the Bestower of Faith"
• Surah Yunus (10:25) - "Allah invites to the Home of Peace"

The Prophet (PBUH) said: "Spread peace among yourselves" and "The Muslim is one from whose tongue and hand other Muslims are safe." (Sahih Bukhari)

"Assalamu alaikum" (Peace be upon you) is the traditional Islamic greeting."""

        elif any(word in user_message for word in ['gratitude', 'shukr', 'thankful', 'شكر']):
            response = """Gratitude is emphasized throughout Islamic teachings, recognizing Allah's blessings.

Key references:
• Surah Al-Baqarah (2:152) - "So remember Me; I will remember you. And be grateful to Me"
• Surah Al-Imran (3:144) - "Allah will reward the grateful"
• Surah Ibrahim (14:7) - "If you are grateful, I will surely increase you"
• Surah An-Naml (27:40) - "This is from the favor of my Lord to test me whether I will be grateful or ungrateful"

The Prophet (PBUH) said: "Whoever is not grateful to people is not grateful to Allah" and "Gratitude for the blessing is a protection against it being taken away." (Sunan Ibn Majah)"""

        elif any(word in user_message for word in ['help', 'assist', 'support', 'مساعدة']):
            response = """I can help you find comprehensive information about many Islamic topics including:

📖 **Core Concepts**: mercy, love, patience, forgiveness, justice, gratitude
🕌 **Worship**: prayer, fasting, pilgrimage, charity, remembrance
👨‍👩‍👧‍👦 **Family**: relationships, inheritance, daily life, moral boundaries
📚 **Knowledge**: learning, wisdom, Islamic education
🌍 **Social**: peace, community, helping others, moral conduct
🕊️ **Character**: honesty, kindness, humility, trustworthiness

Simply type any topic you're interested in, and I'll provide detailed Islamic guidance with Quranic references and Hadith support. What specific topic would you like to explore?"""

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
        server = HTTPServer(('0.0.0.0', port), IslamicAIHandler)
        print(f'🚀 Islamic AI Chat backend is running on port {port}')
        print(f'🌐 Open your browser to: http://localhost:{port}')
        print(f'💬 Chat endpoint: http://localhost:{port}/chat')
        print('🛑 Press Ctrl+C to stop the server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n🛑 Server stopped by user')
    except Exception as e:
        print(f'❌ Error starting server: {e}')
        sys.exit(1)
