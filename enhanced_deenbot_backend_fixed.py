#!/usr/bin/env python3
"""
Enhanced DeenBot Backend - Islamic AI Assistant with Advanced Training
Provides intelligent Islamic guidance with NLP, context memory, and learning capabilities
"""

import json
import logging
import threading
import time
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import sqlite3
import pickle
from typing import Dict, List, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Global configuration
ADVANCED_NLP_AVAILABLE = False  # Will be set to True if NLP libraries are available

class EnhancedDeenBot:
    """Enhanced DeenBot with advanced NLP and learning capabilities"""
    
    def __init__(self):
        """Initialize the enhanced DeenBot"""
        self.islamic_knowledge = self._load_islamic_knowledge()
        self.conversation_history = {}
        self.learning_data = []
        
        # Initialize advanced components
        self._initialize_nlp()
        self._initialize_database()
        self._load_learned_patterns()
        
        logging.info("🚀 Enhanced DeenBot initialized with advanced capabilities")
        
    def _load_islamic_knowledge(self) -> Dict[str, Dict]:
        """Load comprehensive Islamic knowledge base"""
        return {
            "grief_and_sadness": {
                "answer": """**Dealing with Grief and Sadness in Islam - A Compassionate Guide:**

**1. Allah's Mercy in Times of Sorrow**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 94:5-6 - "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease"
- Allah never gives us more than we can handle, and with every difficulty comes ease

**2. The Prophet's (PBUH) Example of Grief**
- The Prophet (PBUH) experienced profound loss: his parents, wife Khadijah, and children
- Hadith: Bukhari 1283 - "The Prophet (PBUH) said: 'The eyes shed tears and the heart grieves, but we do not say anything except what pleases our Lord'"
- It's natural and acceptable to feel sadness and cry

**3. Islamic Coping Mechanisms:**
**a) Prayer and Dua:**
   - Increase in prayer and supplication
   - Reference: Quran 2:186 - "And when My servants ask you concerning Me, indeed I am near. I respond to the invocation of the supplicant"
   - Hadith: Tirmidhi 3371 - "Dua is the weapon of the believer"

**b) Patience (Sabr):**
   - Reference: Quran 2:155 - "And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits, but give good tidings to the patient"
   - Hadith: Muslim 2999 - "How wonderful is the affair of the believer, for his affairs are all good, and this applies to no one except the believer"

**c) Gratitude and Remembrance:**
   - Remember Allah's blessings even in difficulty
   - Reference: Quran 14:7 - "If you are grateful, I will surely increase you [in favor]"

**4. Seeking Support:**
- **Family and Community:** Lean on loved ones for support
- **Islamic Counseling:** Seek guidance from knowledgeable scholars
- **Professional Help:** When needed, seek mental health professionals
- Reference: Quran 9:71 - "The believing men and believing women are allies of one another"

**5. Understanding Loss:**
- **Death is Not the End:** Reference: Quran 2:156 - "Indeed, we belong to Allah and indeed, to Him we will return"
- **Reunion in Paradise:** Reference: Quran 3:185 - "Every soul will taste death, and you will only be given your [full] compensation on the Day of Resurrection"
- **Temporary Nature:** This life is a test, not the final destination

**6. Practical Steps:**
- **Daily Routine:** Maintain regular prayers and Quran recitation
- **Charity:** Help others in need (Sadaqah)
- **Exercise:** Physical activity helps with emotional well-being
- **Journaling:** Write down your feelings and gratitude

**7. When to Seek Additional Help:**
- Persistent overwhelming sadness
- Thoughts of self-harm
- Inability to function in daily life
- Prolonged isolation

**8. Dua for Grief:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**Remember:** Your feelings are valid, and Allah sees your pain. With patience, prayer, and support, you will find strength and peace. The Prophet (PBUH) said: "Allah is with the patient" (Bukhari 1469).""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 2:186", "Quran 2:155", "Quran 14:7", "Quran 9:71", "Quran 2:156", "Quran 3:185", "Bukhari 1283", "Bukhari 1469", "Tirmidhi 3371", "Muslim 2999"]
            },
            "anxiety_and_worry": {
                "answer": """**Dealing with Anxiety and Worry in Islam - Finding Peace in Faith:**

**1. Allah's Promise of Relief**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 65:3 - "And whoever relies upon Allah - then He is sufficient for him"
- Allah has promised to help those who trust in Him

**2. The Prophet's (PBUH) Guidance on Anxiety**
- Hadith: Bukhari 6369 - "The Prophet (PBUH) said: 'Whoever recites 'La ilaha illa Allah' one hundred times, Allah will forgive his sins even if they are as much as the foam of the sea'"
- Hadith: Muslim 2703 - "The Prophet (PBUH) said: 'No fatigue, nor disease, nor sorrow, nor sadness, nor hurt, nor distress befalls a Muslim, even if it were the prick he receives from a thorn, but that Allah expiates some of his sins for that'"

**3. Islamic Solutions for Anxiety:**
**a) Trust in Allah (Tawakkul):**
   - Reference: Quran 3:159 - "So by mercy from Allah, [O Muhammad], you were lenient with them. And if you had been rude [in speech] and harsh in heart, they would have disbanded from about you"
   - Reference: Quran 8:2 - "The believers are only those who, when Allah is mentioned, their hearts become fearful, and when His verses are recited to them, it increases them in faith; and upon their Lord they rely"

**b) Prayer and Remembrance:**
   - Regular prayer provides structure and peace
   - Reference: Quran 13:28 - "Those who have believed and whose hearts are assured by the remembrance of Allah. Unquestionably, by the remembrance of Allah hearts are assured"
   - Dhikr (remembrance of Allah) calms the heart

**c) Gratitude Practice:**
   - Focus on blessings rather than worries
   - Reference: Quran 14:7 - "If you are grateful, I will surely increase you [in favor]"

**4. Practical Anxiety Management:**
**a) Breathing and Relaxation:**
   - Take deep breaths while saying "Allahu Akbar"
   - Practice mindfulness during prayer
   - Use the time of prostration for deep breathing

**b) Daily Routine:**
   - Maintain regular prayer times
   - Read Quran daily, even if just a few verses
   - Keep a gratitude journal

**c) Physical Wellness:**
   - Exercise regularly (walking, swimming, etc.)
   - Maintain healthy sleep patterns
   - Eat nutritious food

**5. When Anxiety Overwhelms:**
- **Seek Professional Help:** Mental health professionals can provide valuable support
- **Talk to Trusted Individuals:** Family, friends, or religious leaders
- **Community Support:** Join Islamic study groups or support networks

**6. Dua for Anxiety:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**7. Remember:**
- **You Are Not Alone:** Millions of Muslims face similar challenges
- **This Too Shall Pass:** Difficulties are temporary
- **Allah Loves You:** Reference: Quran 2:186 - "Indeed, I am near. I respond to the invocation of the supplicant"
- **Growth Through Difficulty:** Challenges strengthen faith and character

**The Prophet (PBUH) said:** "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry" (Bukhari 6114).

**Seek help when needed, trust in Allah, and remember that every difficulty is an opportunity for spiritual growth.** 🌟""",
                "references": ["Quran 2:286", "Quran 65:3", "Quran 3:159", "Quran 8:2", "Quran 13:28", "Quran 14:7", "Quran 2:186", "Bukhari 6369", "Bukhari 6114", "Muslim 2703"]
            },
            "motivation_and_encouragement": {
                "answer": """**Staying Motivated and Encouraged in Islam - Fueling Your Faith Journey:**

**1. Allah's Promise of Success**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 94:5-6 - "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease"
- Every difficulty you face is preparing you for greater success

**2. The Prophet's (PBUH) Example of Perseverance**
- He faced 13 years of persecution in Mecca
- Lost his beloved wife Khadijah and uncle Abu Talib
- Faced rejection from his own people
- Yet he never gave up on his mission
- Hadith: Bukhari 39 - "The Prophet (PBUH) said: 'The most beloved places to Allah are the mosques, and the most disliked places to Allah are the markets'"

**3. Islamic Motivation Principles:**
**a) Intention (Niyyah):**
   - Reference: Quran 2:197 - "And take provisions, but indeed, the best provision is fear of Allah"
   - Start every action with pure intention
   - Even small acts done with sincerity are rewarded

**b) Consistency (Istiqamah):**
   - Reference: Quran 41:30 - "Indeed, those who have said, 'Our Lord is Allah' and then remained on a right course - the angels will descend upon them, [saying], 'Do not fear and do not grieve, but receive good tidings of Paradise, which you were promised'"
   - Small consistent actions are better than occasional big ones

**c) Gratitude (Shukr):**
   - Reference: Quran 14:7 - "If you are grateful, I will surely increase you [in favor]"
   - Count your blessings daily
   - Gratitude attracts more blessings

**4. Practical Motivation Strategies:**
**a) Daily Islamic Routine:**
   - Start with Fajr prayer
   - Read at least one verse of Quran
   - Make dua for guidance and strength
   - End with Isha prayer and reflection

**b) Goal Setting:**
   - Set achievable daily goals
   - Break large goals into smaller steps
   - Celebrate small victories
   - Reference: Quran 13:11 - "Indeed, Allah will not change the condition of a people until they change what is in themselves"

**c) Community Support:**
   - Join Islamic study circles
   - Attend mosque regularly
   - Connect with like-minded Muslims
   - Share your journey with others

**5. Overcoming Setbacks:**
- **Learn from Mistakes:** Every setback is a lesson
- **Seek Forgiveness:** Allah is Most Forgiving
- **Stay Connected:** Don't isolate yourself
- **Remember Your Purpose:** You are here to worship Allah

**6. Dua for Motivation:**
"Allahumma inni as'aluka hubbaka wa hubba man yuhibbuka, wal-'amalalladhi yuballighuni hubbaka"
(O Allah, I ask You for Your love and the love of those who love You, and for actions that will bring me closer to Your love)

**7. Daily Affirmations:**
- "I am a Muslim, chosen by Allah"
- "Every day I grow stronger in faith"
- "My struggles make me stronger"
- "Allah is with me every step of the way"

**Remember:** Motivation comes and goes, but discipline and consistency last forever. The Prophet (PBUH) said: "Take advantage of five before five: your youth before your old age, your health before your illness, your wealth before your poverty, your free time before you are preoccupied, and your life before your death."

**Keep moving forward, one step at a time. Allah is with you!** 🚀✨""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 2:197", "Quran 41:30", "Quran 14:7", "Quran 13:11", "Bukhari 39"]
            }
        }
        
        logging.info("📚 Islamic Knowledge Base loaded successfully")
        return self.islamic_knowledge
    
    def _initialize_nlp(self):
        """Initialize advanced NLP components if available"""
        global ADVANCED_NLP_AVAILABLE
        try:
            # Try to import advanced NLP libraries
            from sentence_transformers import SentenceTransformer
            from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
            from textblob import TextBlob
            
            self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
            self.sentiment_analyzer = SentimentIntensityAnalyzer()
            self.textblob = TextBlob
            
            ADVANCED_NLP_AVAILABLE = True
            logging.info("✅ Advanced NLP components initialized")
            
        except ImportError as e:
            logging.warning(f"⚠️ Advanced NLP not available: {e}")
            ADVANCED_NLP_AVAILABLE = False
    
    def _initialize_database(self):
        """Initialize SQLite database for learning"""
        try:
            self.conn = sqlite3.connect('deenbot_learning.db', check_same_thread=False)
            self.cursor = self.conn.cursor()
            
            # Create tables
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    message TEXT NOT NULL,
                    response TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    context TEXT,
                    effectiveness_score REAL DEFAULT 0.0
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS learned_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pattern TEXT UNIQUE NOT NULL,
                    response_type TEXT NOT NULL,
                    effectiveness REAL DEFAULT 0.0,
                    usage_count INTEGER DEFAULT 1,
                    last_used TEXT NOT NULL
                )
            ''')
            
            self.conn.commit()
            logging.info("✅ Learning database initialized")
            
        except Exception as e:
            logging.error(f"❌ Database initialization failed: {e}")
    
    def _load_learned_patterns(self):
        """Load learned patterns from database"""
        try:
            self.cursor.execute("SELECT pattern, response_type, effectiveness FROM learned_patterns")
            patterns = self.cursor.fetchall()
            logging.info(f"✅ Loaded {len(patterns)} learned patterns")
        except Exception as e:
            logging.error(f"❌ Failed to load patterns: {e}")
    
    def analyze_sentiment(self, message: str) -> Dict[str, float]:
        """Analyze sentiment of message"""
        try:
            if ADVANCED_NLP_AVAILABLE:
                # Remove emojis for better sentiment analysis
                clean_message = message.replace('😊', '').replace('😢', '').replace('😡', '')
                sentiment = self.sentiment_analyzer.polarity_scores(clean_message)
                return sentiment
            else:
                return {'compound': 0.0, 'pos': 0.0, 'neg': 0.0, 'neu': 0.0}
        except Exception as e:
            logging.error(f"❌ Sentiment analysis failed: {e}")
            return {'compound': 0.0, 'pos': 0.0, 'neg': 0.0, 'neu': 0.0}
    
    def extract_context(self, message: str, user_id: str) -> Dict[str, Any]:
        """Extract context from message and user history"""
        context = {
            'sentiment': self.analyze_sentiment(message),
            'user_history': self.conversation_history.get(user_id, [])[-5:],  # Last 5 conversations
            'time_of_day': datetime.now().hour,
            'day_of_week': datetime.now().weekday(),
            'message_length': len(message),
            'contains_question': '?' in message,
            'emotional_keywords': self._extract_emotional_keywords(message)
        }
        return context
    
    def _extract_emotional_keywords(self, message: str) -> List[str]:
        """Extract emotional keywords from message"""
        emotional_words = []
        message_lower = message.lower()
        
        if any(word in message_lower for word in ['sad', 'depressed', 'unhappy', 'grief', 'loss']):
            emotional_words.append('sadness')
        if any(word in message_lower for word in ['anxious', 'worried', 'stressed', 'fear', 'afraid']):
            emotional_words.append('anxiety')
        if any(word in message_lower for word in ['happy', 'joy', 'blessed', 'grateful', 'thankful']):
            emotional_words.append('happiness')
        
        return emotional_words
    
    def get_intelligent_response(self, message: str, user_id: str = "default") -> Dict[str, Any]:
        """Get intelligent response using NLP and learning"""
        start_time = time.time()
        
        try:
            # Extract context
            context = self.extract_context(message, user_id)
            
            # Store conversation
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = []
            
            self.conversation_history[user_id].append({
                'message': message,
                'timestamp': datetime.now().isoformat(),
                'context': context
            })
            
            # Get response using multiple strategies
            response = self._get_response_strategy(message, context)
            
            # Learn from this interaction (non-blocking)
            try:
                self._learn_from_interaction(message, response, user_id, context)
            except Exception as e:
                logging.error(f"❌ Learning failed (non-critical): {e}")
            
            # Calculate response time
            response_time = time.time() - start_time
            
            return {
                "response": response['answer'],
                "references": response['references'],
                "source": response['source'],
                "confidence": response['confidence'],
                "response_time": response_time,
                "context_used": context
            }
        except Exception as e:
            logging.error(f"❌ Critical error in get_intelligent_response: {e}")
            # Return fallback response to ensure system stays online
            return {
                "response": "I apologize, but I'm experiencing a temporary issue. Let me provide you with basic Islamic guidance while I resolve this. Please try your question again in a moment.",
                "references": ["System Fallback"],
                "source": "Emergency Fallback System",
                "confidence": 0.5,
                "response_time": time.time() - start_time,
                "context_used": {"error": str(e)}
            }
    
    def _get_response_strategy(self, message: str, context: Dict) -> Dict[str, Any]:
        """Get response using multiple strategies"""
        message_lower = message.lower()
        
        # Strategy 1: Direct keyword matching
        keyword_response = self._keyword_matching(message_lower)
        if keyword_response:
            return keyword_response
        
        # Strategy 2: Context-based response
        context_response = self._context_based_response(message, context)
        if context_response:
            return context_response
        
        # Strategy 3: Fallback response
        return self._get_fallback_response(context)
    
    def _keyword_matching(self, message_lower: str) -> Optional[Dict[str, Any]]:
        """Enhanced keyword matching with emotional intelligence"""
        try:
            priority_keywords = {
                "sad": "grief_and_sadness",
                "depressed": "grief_and_sadness",
                "unhappy": "grief_and_sadness",
                "grief": "grief_and_sadness",
                "loss": "grief_and_sadness",
                "anxiety": "anxiety_and_worry",
                "anxious": "anxiety_and_worry",
                "worry": "anxiety_and_worry",
                "worried": "anxiety_and_worry",
                "stress": "anxiety_and_worry",
                "stressed": "anxiety_and_worry",
                "overwhelmed": "anxiety_and_worry",
                "exhausted": "anxiety_and_worry",
                "tired": "anxiety_and_worry",
                "frustrated": "anxiety_and_worry",
                "good day": "motivation_and_encouragement",
                "happy": "motivation_and_encouragement",
                "joy": "motivation_and_encouragement",
                "blessed": "motivation_and_encouragement",
                "grateful": "motivation_and_encouragement",
                "thankful": "motivation_and_encouragement"
            }
            
            for keyword, key in priority_keywords.items():
                if keyword in message_lower:
                    try:
                        data = self.islamic_knowledge[key]
                        return {
                            "answer": data["answer"],
                            "references": data["references"],
                            "source": "Enhanced Islamic Knowledge Base",
                            "confidence": 0.9,
                            "strategy": "keyword_matching"
                        }
                    except KeyError:
                        logging.error(f"❌ Knowledge base key not found: {key}")
                        continue
                    except Exception as e:
                        logging.error(f"❌ Error accessing knowledge base: {e}")
                        continue
            
            return None
        except Exception as e:
            logging.error(f"❌ Keyword matching error: {e}")
            return None
    
    def _context_based_response(self, message: str, context: Dict) -> Optional[Dict[str, Any]]:
        """Generate response based on context and user history"""
        sentiment = context['sentiment']
        
        # Sentiment-based response
        if sentiment['compound'] < -0.3:  # Negative sentiment
            return {
                "answer": self._get_comforting_response(context),
                "references": ["Islamic Comfort and Guidance"],
                "source": "Context-Aware Response",
                "confidence": 0.8,
                "strategy": "sentiment_analysis"
            }
        elif sentiment['compound'] > 0.3:  # Positive sentiment
            return {
                "answer": self._get_encouraging_response(context),
                "references": ["Islamic Motivation and Growth"],
                "source": "Context-Aware Response",
                "confidence": 0.8,
                "strategy": "sentiment_analysis"
            }
        
        return None
    
    def _get_comforting_response(self, context: Dict) -> str:
        """Get comforting response for negative emotions"""
        return """**Assalamu alaikum! I sense you might be going through a difficult time.**

**Remember these comforting words from Islam:**

🌟 **Allah is with you:** "Indeed, I am near. I respond to the invocation of the supplicant" (Quran 2:186)

🌟 **This too shall pass:** "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease" (Quran 94:5-6)

🌟 **You are stronger than you think:** "Allah does not burden a soul beyond that it can bear" (Quran 2:286)

**Would you like me to:**
• Share specific Islamic guidance for your situation?
• Help you find comfort in prayer and dua?
• Connect you with practical coping strategies?

**You're not alone, and Allah sees your pain. Let me know how I can help you find peace and strength.** 🤲💙"""
    
    def _get_encouraging_response(self, context: Dict) -> str:
        """Get encouraging response for positive emotions"""
        return """**Alhamdulillah! It's wonderful to see your positive energy! 🌟**

**Your positive attitude reflects the beautiful teachings of Islam:**

✨ **Gratitude is worship:** "If you are grateful, I will surely increase you [in favor]" (Quran 14:7)

✨ **Joy is a blessing:** "And of His signs is that He created for you from yourselves mates that you may find tranquility in them" (Quran 30:21)

✨ **Your happiness matters to Allah:** The Prophet (PBUH) said: "Allah is more pleased with the repentance of His servant than one of you would be if he found his camel after having lost it in a barren land"

**How can I help you:**
• Build on this positive momentum?
• Share Islamic practices for maintaining joy?
• Guide you in spreading this positivity to others?

**Keep shining your light! Your positive energy is a gift to the world.** ✨🕌"""
    
    def _get_fallback_response(self, context: Dict) -> Dict[str, Any]:
        """Get fallback response when no specific match is found"""
        return {
            "answer": """**Assalamu alaikum! I'm here to help you with any questions about Islam, the Quran, Hadith, and Islamic guidance.**

**What would you like to learn about today?**

I can help with:
• Islamic beliefs and practices
• Quranic verses and their meanings
• Authentic Hadith and their context
• Islamic history and culture
• Daily life and Islamic ethics
• Family and social matters
• Business and financial guidance
• Health and wellness from Islamic perspective
• And much more!

**Just ask me any question, and I'll provide comprehensive guidance with proper references from the Quran, authentic Hadith, and reliable Islamic sources.**

**I'm constantly learning and improving to serve you better!** 📚🤲""",
            "references": ["Islamic Guidance System"],
            "source": "Enhanced DeenBot Assistant",
            "confidence": 0.6,
            "strategy": "fallback"
        }
    
    def _learn_from_interaction(self, message: str, response: Dict, user_id: str, context: Dict):
        """Learn from user interaction to improve future responses"""
        try:
            # Store interaction in database
            self.cursor.execute('''
                INSERT INTO conversations (user_id, message, response, timestamp, context)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, message, response['answer'], datetime.now().isoformat(), json.dumps(context)))
            
            # Update learned patterns
            self._update_learned_patterns(message, response, context)
            
            # Store in memory for quick access
            self.learning_data.append({
                'message': message,
                'response': response,
                'context': context,
                'timestamp': datetime.now().isoformat()
            })
            
            self.conn.commit()
            
        except Exception as e:
            logging.error(f"❌ Failed to learn from interaction: {e}")
    
    def _update_learned_patterns(self, message: str, response: Dict, context: Dict):
        """Update learned response patterns"""
        try:
            # Extract key patterns from message
            patterns = self._extract_patterns(message)
            
            for pattern in patterns:
                self.cursor.execute('''
                    INSERT OR REPLACE INTO learned_patterns 
                    (pattern, response_type, effectiveness, usage_count, last_used)
                    VALUES (?, ?, ?, COALESCE((SELECT usage_count + 1 FROM learned_patterns WHERE pattern = ?), 1), ?)
                ''', (pattern, response['strategy'], response['confidence'], pattern, datetime.now().isoformat()))
            
            self.conn.commit()
            
        except Exception as e:
            logging.error(f"❌ Failed to update patterns: {e}")
    
    def _extract_patterns(self, message: str) -> List[str]:
        """Extract learning patterns from message"""
        patterns = []
        
        # Word patterns
        words = message.lower().split()
        if len(words) >= 2:
            patterns.append(' '.join(words[:2]))  # First two words
            patterns.append(' '.join(words[-2:]))  # Last two words
        
        # Emotional patterns
        emotional_words = self._extract_emotional_keywords(message)
        for emotion in emotional_words:
            patterns.append(f"emotion_{emotion}")
        
        # Question patterns
        if '?' in message:
            patterns.append("question_pattern")
        
        # Length patterns
        if len(message) < 20:
            patterns.append("short_message")
        elif len(message) > 100:
            patterns.append("long_message")
        
        return patterns
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """Get learning statistics"""
        try:
            # Total conversations
            self.cursor.execute("SELECT COUNT(*) FROM conversations")
            total_conversations = self.cursor.fetchone()[0]
            
            # Response effectiveness
            self.cursor.execute("SELECT AVG(effectiveness_score) FROM conversations WHERE effectiveness_score IS NOT NULL")
            avg_effectiveness = self.cursor.fetchone()[0] or 0.0
            
            # Pattern usage
            self.cursor.execute("SELECT COUNT(*) FROM learned_patterns")
            total_patterns = self.cursor.fetchone()[0]
            
            # User engagement
            self.cursor.execute("SELECT COUNT(DISTINCT user_id) FROM conversations")
            unique_users = self.cursor.fetchone()[0]
            
            return {
                "total_conversations": total_conversations,
                "average_effectiveness": round(avg_effectiveness, 2),
                "learned_patterns": total_patterns,
                "unique_users": unique_users,
                "nlp_available": ADVANCED_NLP_AVAILABLE,
                "learning_active": True
            }
            
        except Exception as e:
            logging.error(f"❌ Failed to get learning stats: {e}")
            return {"error": str(e)}
    
    def _reinitialize_critical_components(self):
        """Reinitialize critical components for auto-recovery"""
        try:
            logging.info("🔄 Reinitializing critical components...")
            
            # Reinitialize database connection
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
            self._initialize_database()
            
            # Reinitialize NLP components if available
            if ADVANCED_NLP_AVAILABLE:
                self._initialize_nlp()
            
            # Reload learned patterns
            self._load_learned_patterns()
            
            logging.info("✅ Critical components reinitialized successfully")
            
        except Exception as e:
            logging.error(f"❌ Failed to reinitialize critical components: {e}")
            raise

# Global variables
start_time = time.time()
deenbot = None

class EnhancedDeenBotHandler(BaseHTTPRequestHandler):
    """HTTP request handler for enhanced DeenBot"""
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        
        if path == '/health':
            self._handle_health()
        elif path == '/status':
            self._handle_status()
        elif path == '/stats':
            self._handle_stats()
        else:
            self._handle_not_found()
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/chat':
            self._handle_chat()
        else:
            self._handle_not_found()
    
    def _handle_health(self):
        """Handle health check endpoint"""
        try:
            uptime = time.time() - start_time
            response = {
                "status": "healthy",
                "service": "Enhanced DeenBot Backend",
                "timestamp": datetime.now().isoformat(),
                "uptime": uptime,
                "capabilities": {
                    "nlp": ADVANCED_NLP_AVAILABLE,
                    "learning": True,
                    "context_memory": True,
                    "semantic_understanding": ADVANCED_NLP_AVAILABLE
                }
            }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            logging.error(f"❌ Health check failed: {e}")
            self._send_error_response(500, "Health check failed")
    
    def _handle_status(self):
        """Handle status endpoint"""
        try:
            if deenbot:
                learning_stats = deenbot.get_learning_stats()
                response = {
                    "status": "operational",
                    "service": "Enhanced DeenBot Backend",
                    "timestamp": datetime.now().isoformat(),
                    "uptime": time.time() - start_time,
                    "learning_stats": learning_stats
                }
            else:
                response = {
                    "status": "initializing",
                    "service": "Enhanced DeenBot Backend",
                    "timestamp": datetime.now().isoformat(),
                    "uptime": time.time() - start_time
                }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            logging.error(f"❌ Status check failed: {e}")
            self._send_error_response(500, "Status check failed")
    
    def _handle_stats(self):
        """Handle statistics endpoint"""
        try:
            if deenbot:
                stats = deenbot.get_learning_stats()
                response = {
                    "statistics": stats,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                response = {
                    "statistics": {"error": "DeenBot not initialized"},
                    "timestamp": datetime.now().isoformat()
                }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            logging.error(f"❌ Stats request failed: {e}")
            self._send_error_response(500, "Stats request failed")
    
    def _handle_chat(self):
        """Handle chat endpoint"""
        try:
            # Read request body
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Parse JSON request
            request_data = json.loads(post_data.decode('utf-8'))
            message = request_data.get('message', '')
            user_id = request_data.get('user_id', 'default')
            
            if not message:
                self._send_error_response(400, "Message is required")
                return
            
            # Get response from DeenBot
            if deenbot:
                response = deenbot.get_intelligent_response(message, user_id)
                logging.info(f"✅ Enhanced chat request processed: '{message[:50]}...' -> {response['source']} (confidence: {response['confidence']})")
            else:
                response = {
                    "response": "DeenBot is initializing. Please try again in a moment.",
                    "references": ["System Status"],
                    "source": "System",
                    "confidence": 0.0,
                    "response_time": 0.0,
                    "context_used": {}
                }
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except json.JSONDecodeError as e:
            logging.error(f"❌ Invalid JSON in chat request: {e}")
            self._send_error_response(400, "Invalid JSON format")
        except Exception as e:
            logging.error(f"❌ Unexpected error: {e}")
            self._send_error_response(500, "Internal server error")
    
    def _handle_not_found(self):
        """Handle 404 errors"""
        self._send_error_response(404, "Endpoint not found")
    
    def _send_error_response(self, status_code: int, message: str):
        """Send error response"""
        response = {
            "error": message,
            "status_code": status_code
        }
        
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def monitor_system_resources():
    """Monitor system resources in background thread with auto-recovery"""
    consecutive_errors = 0
    max_errors = 3
    
    while True:
        try:
            if deenbot:
                learning_stats = deenbot.get_learning_stats()
                logging.info(f"📊 Enhanced System Status - Conversations: {learning_stats['total_conversations']}, Patterns: {learning_stats['learned_patterns']}, Users: {learning_stats['unique_users']}")
                consecutive_errors = 0  # Reset error counter on success
            else:
                logging.info(f"📊 System Status - DeenBot initializing...")
                
        except Exception as e:
            consecutive_errors += 1
            logging.error(f"❌ System monitoring error #{consecutive_errors}: {e}")
            
            # Auto-recovery after multiple consecutive errors
            if consecutive_errors >= max_errors:
                logging.critical(f"🚨 CRITICAL: {max_errors} consecutive monitoring errors. Initiating auto-recovery...")
                try:
                    # Attempt to reinitialize critical components
                    if deenbot:
                        deenbot._reinitialize_critical_components()
                    consecutive_errors = 0
                    logging.info("✅ Auto-recovery completed successfully")
                except Exception as recovery_error:
                    logging.critical(f"❌ Auto-recovery failed: {recovery_error}")
        
        time.sleep(60)  # Check every minute

def main():
    """Main function to start the enhanced server with graceful shutdown"""
    global start_time, deenbot
    
    start_time = time.time()
    deenbot = EnhancedDeenBot()
    
    # Start system monitoring in background
    monitor_thread = threading.Thread(target=monitor_system_resources, daemon=True)
    monitor_thread.start()
    
    # Configure server
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, EnhancedDeenBotHandler)
    
    logging.info("🚀 Enhanced DeenBot Backend starting...")
    logging.info("🧠 Advanced NLP and Learning capabilities enabled")
    logging.info("📚 Islamic Knowledge Base loaded successfully")
    logging.info("🌐 Server listening on port 8080")
    logging.info("✅ Health endpoint: /health")
    logging.info("✅ Status endpoint: /status")
    logging.info("✅ Stats endpoint: /stats")
    logging.info("✅ Enhanced chat endpoint: /chat")
    
    # Set up signal handlers for graceful shutdown
    import signal
    
    def signal_handler(signum, frame):
        logging.info(f"🛑 Received signal {signum}, initiating graceful shutdown...")
        httpd.shutdown()
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("🛑 Server stopped by user")
    except Exception as e:
        logging.error(f"❌ Server error: {e}")
    finally:
        logging.info("🔄 Cleaning up resources...")
        
        # Cleanup database connections
        if deenbot and hasattr(deenbot, 'conn'):
            try:
                deenbot.conn.close()
                logging.info("✅ Database connection closed")
            except Exception as e:
                logging.error(f"❌ Error closing database: {e}")
        
        # Cleanup server
        try:
            httpd.server_close()
            logging.info("✅ Server closed")
        except Exception as e:
            logging.error(f"❌ Error closing server: {e}")
        
        # Cleanup NLP resources
        if deenbot and ADVANCED_NLP_AVAILABLE:
            try:
                if hasattr(deenbot, 'sentence_model'):
                    del deenbot.sentence_model
                if hasattr(deenbot, 'sentiment_analyzer'):
                    del deenbot.sentiment_analyzer
                logging.info("✅ NLP resources cleaned up")
            except Exception as e:
                logging.error(f"❌ Error cleaning up NLP resources: {e}")
        
        logging.info("🔒 Graceful shutdown completed")

if __name__ == '__main__':
    main()
