#!/usr/bin/env python3
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class QuranIndexHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '''<!DOCTYPE html>
<html>
<head>
    <title>Quran Index - AI Assistant</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #121212;
            color: #E0E0E0;
            margin: 20px;
            padding: 0;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .header h1 {
            color: #F0F0F0;
            font-size: 28px;
            margin: 0;
        }
        .subtitle {
            color: #1E90FF;
            font-size: 16px;
            margin-top: 10px;
        }
        .chat-container {
            max-width: 600px;
            margin: 0 auto;
            background: #181818;
            padding: 20px;
            border: 1px solid #444444;
            border-radius: 10px;
        }
        .messages {
            height: 300px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding: 15px;
            background: #121212;
            border: 1px solid #444444;
            border-radius: 5px;
        }
        .message {
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 5px;
        }
        .user-message {
            background: #1E90FF;
            color: #FFFFFF;
            text-align: right;
        }
        .bot-message {
            background: #444444;
            color: #F7F7F7;
        }
        .input-area {
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 15px;
            border: 1px solid #444444;
            border-radius: 5px;
            background: #181818;
            color: #E0E0E0;
            font-size: 16px;
        }
        button {
            padding: 15px 25px;
            background: #1E90FF;
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        button:hover {
            background: #004D61;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>QURAN INDEX</h1>
        <div class="subtitle">AI ASSISTANT</div>
    </div>
    
    <div class="chat-container">
        <div class="messages" id="messages">
            <div class="message bot-message">
                Assalamu alaikum. I am your Quran Index assistant. I can help you find verses by topic, such as love, mercy, patience, forgiveness, justice, and many more. Simply type a topic and I will show you where it is mentioned in the Quran. What would you like to search for?
            </div>
        </div>
        
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Type a topic (e.g., mercy, love, patience)..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">SEARCH</button>
        </div>
    </div>
    <script>
        function addMessage(message, isUser) {
            const container = document.getElementById("messages");
            const messageDiv = document.createElement("div");
            messageDiv.className = "message " + (isUser ? "user-message" : "bot-message");
            messageDiv.textContent = message;
            container.appendChild(messageDiv);
            container.scrollTop = container.scrollHeight;
        }
        function handleKeyPress(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        }
        function sendMessage() {
            const input = document.getElementById("userInput");
            const message = input.value.trim();
            
            if (!message) return;
            
            addMessage(message, true);
            input.value = "";
            
            fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response, false);
            })
            .catch(error => {
                console.error("Error:", error);
                addMessage("I apologize, but I encountered an error processing your request. Please try again.", false);
            });
        }
    </script>
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
            
            # Quran Index responses
            if 'mercy' in user_message or 'rahman' in user_message or 'raheem' in user_message:
                response = "Mercy (Rahman/Raheem) is mentioned extensively in the Quran. Key references include: Surah Al-Fatiha (1:1-2) - 'In the name of Allah, the Most Gracious, the Most Merciful', Surah Al-Baqarah (2:143) - 'Allah is Most Merciful to mankind', Surah Al-An'am (6:12) - 'Allah has written mercy for Himself', and many more. The concept of divine mercy appears in over 100 verses."
            elif 'love' in user_message or 'hubb' in user_message or 'mawaddah' in user_message:
                response = "Love is mentioned in several contexts in the Quran. Key references include: Surah Al-Imran (3:31) - 'Say: If you love Allah, then follow me', Surah Al-Ma'idah (5:54) - 'Allah will bring a people whom He loves and who love Him', Surah Al-Baqarah (2:165) - 'Those who believe are stronger in love for Allah', and Surah Ar-Rum (30:21) - 'He created for you mates from among yourselves that you may find tranquility in them, and He placed between you affection and mercy'."
            elif 'patience' in user_message or 'sabr' in user_message or 'patient' in user_message:
                response = "Patience (Sabr) is highly emphasized in the Quran. Key references include: Surah Al-Baqarah (2:153) - 'O you who have believed, seek help through patience and prayer', Surah Al-Imran (3:200) - 'O you who have believed, persevere and endure', Surah Al-Anfal (8:46) - 'Be patient, for Allah is with the patient', and Surah Al-Asr (103:3) - 'Except those who believe and do righteous deeds and advise each other to truth and advise each other to patience'."
            elif 'forgiveness' in user_message or 'ghafr' in user_message or 'tawbah' in user_message:
                response = "Forgiveness is a central theme in the Quran. Key references include: Surah Al-Baqarah (2:199) - 'Ask Allah for forgiveness', Surah Al-Imran (3:135) - 'Those who, when they commit an immorality, remember Allah and seek forgiveness', Surah Al-Ma'idah (5:74) - 'Will they not repent to Allah and seek His forgiveness?', and Surah Az-Zumar (39:53) - 'Say: O My servants who have transgressed against themselves, do not despair of the mercy of Allah. Indeed, Allah forgives all sins'."
            elif 'justice' in user_message or 'adl' in user_message or 'fair' in user_message:
                response = "Justice is fundamental in the Quran. Key references include: Surah An-Nisa (4:135) - 'O you who have believed, be persistently standing firm in justice', Surah Al-Ma'idah (5:8) - 'Be just; that is nearer to righteousness', Surah Al-An'am (6:152) - 'Give full measure and weight in justice', and Surah Al-Hadid (57:25) - 'We sent Our messengers with clear evidences and sent down with them the Scripture and the balance that the people may maintain justice'."
            elif 'gratitude' in user_message or 'shukr' in user_message or 'thankful' in user_message:
                response = "Gratitude is emphasized throughout the Quran. Key references include: Surah Al-Baqarah (2:152) - 'So remember Me; I will remember you. And be grateful to Me', Surah Al-Imran (3:144) - 'Allah will reward the grateful', Surah Ibrahim (14:7) - 'If you are grateful, I will surely increase you', and Surah An-Naml (27:40) - 'This is from the favor of my Lord to test me whether I will be grateful or ungrateful'."
            elif 'knowledge' in user_message or 'ilm' in user_message or 'learn' in user_message:
                response = "Knowledge is highly valued in the Quran. Key references include: Surah Al-Baqarah (2:269) - 'He gives wisdom to whom He wills, and whoever has been given wisdom has certainly been given much good', Surah Al-Imran (3:7) - 'None knows its interpretation except Allah and those who are firmly grounded in knowledge', Surah Al-Mujadila (58:11) - 'Allah will raise those who have believed among you and those who were given knowledge', and Surah Ta-Ha (20:114) - 'My Lord, increase me in knowledge'."
            elif 'charity' in user_message or 'sadaqah' in user_message or 'zakat' in user_message:
                response = "Charity and giving are central to Islamic practice. Key references include: Surah Al-Baqarah (2:261) - 'The example of those who spend their wealth in the way of Allah', Surah Al-Imran (3:92) - 'Never will you attain the good until you spend of that which you love', Surah Al-Ma'un (107:1-7) - 'Have you seen the one who denies the Recompense? For that is the one who drives away the orphan and does not encourage the feeding of the poor', and Surah Al-Baqarah (2:274) - 'Those who spend their wealth by night and by day, secretly and publicly'."
            elif 'peace' in user_message or 'salam' in user_message or 'tranquility' in user_message:
                response = "Peace is a fundamental concept in the Quran. Key references include: Surah Al-Baqarah (2:208) - 'Enter into peace completely', Surah Al-Anfal (8:61) - 'If they incline to peace, then incline to it', Surah Al-Hashr (59:23) - 'He is Allah, other than whom there is no deity, the Sovereign, the Pure, the Perfection, the Bestower of Faith, the Overseer, the Exalted in Might, the Compeller, the Superior', and Surah Yunus (10:25) - 'Allah invites to the Home of Peace'."
            elif 'family' in user_message or 'parents' in user_message or 'children' in user_message:
                response = "Family relationships are emphasized in the Quran. Key references include: Surah Al-Isra (17:23-24) - 'Your Lord has decreed that you worship none but Him, and that you be kind to parents', Surah Luqman (31:14) - 'We have enjoined upon man to be good to his parents', Surah Al-Baqarah (2:233) - 'Mothers may nurse their children for two complete years', and Surah An-Nisa (4:1) - 'O mankind, fear your Lord, who created you from one soul and created from it its mate'."
            elif 'help' in user_message or 'assist' in user_message or 'support' in user_message:
                response = "I can help you find verses about many topics including: mercy, love, patience, forgiveness, justice, gratitude, knowledge, charity, peace, family, prayer, fasting, pilgrimage, and many more. Simply type the topic you are interested in and I will show you relevant verses from the Quran. What specific topic would you like to explore?"
            else:
                response = "I can help you find verses about many topics in the Quran. Try searching for: mercy, love, patience, forgiveness, justice, gratitude, knowledge, charity, peace, family, prayer, fasting, or any other topic you are interested in. Simply type the topic and I will show you where it is mentioned in the Quran."
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_data = {'response': response}
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), QuranIndexHandler)
    print('Quran Index AI backend is running on port 8080')
    server.serve_forever()
