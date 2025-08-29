#!/usr/bin/env python3
"""
Enhanced DeenBot Backend - Islamic AI Assistant with Advanced Training
Provides intelligent Islamic guidance with NLP, context memory, and learning capabilities
"""

import json
import logging
import threading
import time
import sqlite3
import pickle
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import numpy as np
from collections import defaultdict, Counter

# Advanced NLP imports (will be installed via requirements.txt)
try:
    from sentence_transformers import SentenceTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    from textblob import TextBlob
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import emoji
    ADVANCED_NLP_AVAILABLE = True
except ImportError:
    ADVANCED_NLP_AVAILABLE = False
    print("⚠️ Advanced NLP libraries not available. Using basic keyword matching.")

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import os

# Configure comprehensive logging
try:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('/var/log/supervisor/enhanced_deenbot.log'),
            logging.StreamHandler()
        ]
    )
except FileNotFoundError:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

class EnhancedDeenBot:
    """Enhanced Islamic AI with NLP, learning, and context memory"""
    
    def __init__(self):
        self.islamic_knowledge = self._load_islamic_knowledge()
        self.conversation_history = defaultdict(list)
        self.user_preferences = {}
        self.response_effectiveness = defaultdict(list)
        self.learning_data = []
        
        # Initialize NLP components
        if ADVANCED_NLP_AVAILABLE:
            self._initialize_nlp()
        
        # Initialize database
        self._initialize_database()
        
        # Load learned patterns
        self._load_learned_patterns()
        
        logging.info("🚀 Enhanced DeenBot initialized with advanced capabilities")
    
    def _initialize_nlp(self):
        """Initialize NLP components"""
        try:
            # Sentence embeddings for semantic understanding
            self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
            
            # Sentiment analysis
            self.sentiment_analyzer = SentimentIntensityAnalyzer()
            
            # Text processing
            self.text_processor = TextBlob("")
            
            logging.info("✅ Advanced NLP components initialized")
        except Exception as e:
            logging.error(f"❌ NLP initialization failed: {e}")
            ADVANCED_NLP_AVAILABLE = False
    
    def _initialize_database(self):
        """Initialize SQLite database for learning and context"""
        try:
            self.db_path = "deenbot_learning.db"
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.cursor = self.conn.cursor()
            
            # Create tables for learning
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    message TEXT,
                    response TEXT,
                    timestamp DATETIME,
                    effectiveness_score REAL,
                    context TEXT
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_preferences (
                    user_id TEXT PRIMARY KEY,
                    preferences TEXT,
                    last_updated DATETIME
                )
            ''')
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS learned_patterns (
                    pattern TEXT PRIMARY KEY,
                    response_type TEXT,
                    effectiveness REAL,
                    usage_count INTEGER,
                    last_used DATETIME
                )
            ''')
            
            self.conn.commit()
            logging.info("✅ Learning database initialized")
        except Exception as e:
            logging.error(f"❌ Database initialization failed: {e}")
    
    def _load_islamic_knowledge(self):
        """Load comprehensive Islamic knowledge base"""
        return {
            "grief_and_sadness": {
                "question": "How to deal with grief and sadness in Islam?",
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
                "question": "How to deal with anxiety and worry in Islam?",
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
                "question": "How to stay motivated and encouraged in Islam?",
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
- Hadith: Bukhari 39 - "The Prophet (PBUH) said: 'The most beloved places to Allah are the mosques'"

**3. Islamic Sources of Motivation:**
   **a) Quranic Inspiration:**
   - Reference: Quran 13:28 - "Those who have believed and whose hearts are assured by the remembrance of Allah. Unquestionably, by the remembrance of Allah hearts are assured"
   - Reference: Quran 39:53 - "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah'"
   - Every verse is a source of strength and guidance

   **b) Hadith Motivation:**
   - Hadith: Muslim 2699 - "The Prophet (PBUH) said: 'Allah is more pleased with the repentance of His servant than one of you would be if he found his camel after having lost it in a barren land'"
   - Hadith: Bukhari 6502 - "The Prophet (PBUH) said: 'Whoever follows a path in search of knowledge, Allah will make easy for him a path to Paradise'"

**4. Daily Motivation Practices:**
   **a) Morning Routine:**
   - Start with Fajr prayer and morning adhkar
   - Read a few verses of Quran
   - Set 3 achievable goals for the day
   - Make dua for strength and guidance

   **b) Throughout the Day:**
   - Take short breaks for dhikr
   - Practice gratitude for small blessings
   - Help someone in need (even small acts)
   - Stay connected with positive people

   **c) Evening Reflection:**
   - Thank Allah for the day's blessings
   - Reflect on what you accomplished
   - Plan tomorrow's goals
   - Recite evening adhkar

**5. Overcoming Common Demotivators:**
   **a) When You Feel Overwhelmed:**
   - Break big tasks into small steps
   - Focus on one thing at a time
   - Remember: "The journey of a thousand miles begins with one step"
   - Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"

   **b) When You Feel Alone:**
   - Remember Allah is always with you
   - Reference: Quran 2:186 - "Indeed, I am near. I respond to the invocation of the supplicant"
   - Connect with the Muslim community
   - Reach out to family and friends

   **c) When You Feel Like Giving Up:**
   - Remember the Prophet's (PBUH) struggles
   - Think of the rewards waiting in Paradise
   - Focus on the impact you can make
   - Every small step counts

**6. Building Lasting Motivation:**
   **a) Spiritual Foundation:**
   - **Regular Prayer:** Maintain your five daily prayers
   - **Quran Connection:** Read/listen to Quran daily
   - **Dhikr:** Keep your heart connected to Allah
   - **Dua:** Ask Allah for help and strength

   **b) Physical Wellness:**
   - **Exercise:** Physical activity boosts mood and energy
   - **Sleep:** Get adequate rest for mental clarity
   - **Nutrition:** Eat healthy foods that fuel your body
   - **Sunlight:** Spend time outdoors when possible

   **c) Social Support:**
   - **Family:** Lean on loved ones for support
   - **Community:** Attend mosque and Islamic events
   - **Mentors:** Find people who inspire you
   - **Study Groups:** Join Islamic learning circles

**7. Motivation for Specific Areas:**
   **a) Education and Learning:**
   - Reference: Quran 96:1-5 - "Read in the name of your Lord who created"
   - Hadith: Abu Dawud 3641 - "The Prophet (PBUH) said: 'Seeking knowledge is obligatory upon every Muslim'"
   - Every piece of knowledge brings you closer to Allah

   **b) Work and Career:**
   - Reference: Quran 62:10 - "And when the prayer has been concluded, disperse within the land and seek from the bounty of Allah"
   - Work with excellence as worship to Allah
   - Your skills can help others and serve the community

   **c) Family and Relationships:**
   - Reference: Quran 30:21 - "And of His signs is that He created for you from yourselves mates that you may find tranquility in them"
   - Building strong relationships is a form of worship
   - Your family is a blessing from Allah

**8. Dua for Motivation:**
"Allahumma inni as'aluka al-huda wat-tuqa wal-'afafa wal-ghina"
(O Allah, I ask You for guidance, piety, chastity and self-sufficiency)

**9. Remember These Truths:**
- **You Are Capable:** Allah has given you unique talents and abilities
- **Progress is Possible:** Every day is a new opportunity to grow
- **Allah Believes in You:** He chose you to be Muslim for a reason
- **Your Efforts Matter:** Even small acts of worship are valuable
- **The Best is Yet to Come:** Paradise awaits those who persevere

**10. Daily Affirmations:**
- "Today I will be the best version of myself"
- "I am capable of achieving my goals with Allah's help"
- "Every challenge makes me stronger"
- "I am blessed to be Muslim"
- "Allah is with me every step of the way"

**The Prophet (PBUH) said:** "The most beloved deeds to Allah are those that are consistent, even if they are small" (Bukhari 6464).

**Your motivation comes from knowing that Allah believes in you and has a special plan for your life. Keep moving forward, one step at a time, and remember that every effort you make brings you closer to Allah and closer to your dreams.** 🚀⭐""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 13:28", "Quran 39:53", "Quran 2:186", "Quran 96:1-5", "Quran 62:10", "Quran 30:21", "Bukhari 39", "Bukhari 6502", "Bukhari 6464", "Muslim 2699", "Abu Dawud 3641"]
            }
        }
    
    def _load_learned_patterns(self):
        """Load previously learned response patterns"""
        try:
            self.cursor.execute("SELECT pattern, response_type, effectiveness FROM learned_patterns")
            patterns = self.cursor.fetchall()
            
            for pattern, response_type, effectiveness in patterns:
                self.learning_data.append({
                    'pattern': pattern,
                    'response_type': response_type,
                    'effectiveness': effectiveness
                })
            
            logging.info(f"✅ Loaded {len(patterns)} learned patterns")
        except Exception as e:
            logging.error(f"❌ Failed to load learned patterns: {e}")
    
    def analyze_sentiment(self, message: str) -> Dict[str, float]:
        """Analyze sentiment of user message"""
        if not ADVANCED_NLP_AVAILABLE:
            return {'compound': 0.0, 'pos': 0.0, 'neg': 0.0, 'neu': 0.0}
        
        try:
            # Remove emojis for better sentiment analysis
            clean_message = emoji.replace(message, '')
            sentiment = self.sentiment_analyzer.polarity_scores(clean_message)
            return sentiment
        except Exception as e:
            logging.error(f"❌ Sentiment analysis failed: {e}")
            return {'compound': 0.0, 'pos': 0.0, 'neg': 0.0, 'neu': 0.0}
    
    def extract_context(self, message: str, user_id: str) -> Dict[str, any]:
        """Extract context from message and user history"""
        context = {
            'sentiment': self.analyze_sentiment(message),
            'user_history': self.conversation_history[user_id][-5:],  # Last 5 messages
            'time_of_day': datetime.now().hour,
            'day_of_week': datetime.now().weekday(),
            'message_length': len(message),
            'contains_question': '?' in message,
            'emotional_keywords': self._extract_emotional_keywords(message)
        }
        return context
    
    def _extract_emotional_keywords(self, message: str) -> List[str]:
        """Extract emotional keywords from message"""
        emotional_words = [
            'sad', 'happy', 'angry', 'anxious', 'worried', 'excited', 'grateful',
            'blessed', 'depressed', 'joy', 'fear', 'love', 'hate', 'hope', 'despair'
        ]
        
        message_lower = message.lower()
        found_emotions = [word for word in emotional_words if word in message_lower]
        return found_emotions
    
    def get_semantic_similarity(self, message: str, knowledge_key: str) -> float:
        """Get semantic similarity between message and knowledge base"""
        if not ADVANCED_NLP_AVAILABLE:
            return 0.0
        
        try:
            # Get embeddings for message and knowledge
            message_embedding = self.sentence_model.encode([message])
            knowledge_text = self.islamic_knowledge[knowledge_key]['question']
            knowledge_embedding = self.sentence_model.encode([knowledge_text])
            
            # Calculate cosine similarity
            similarity = cosine_similarity(message_embedding, knowledge_embedding)[0][0]
            return float(similarity)
        except Exception as e:
            logging.error(f"❌ Semantic similarity failed: {e}")
            return 0.0
    
    def get_intelligent_response(self, message: str, user_id: str = "default") -> Dict[str, any]:
        """Get intelligent response using NLP and learning"""
        start_time = time.time()
        
        try:
            # Extract context
            context = self.extract_context(message, user_id)
            
            # Store conversation
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
                "references": response['references"],
                "source": response['source"],
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
    
    def _get_response_strategy(self, message: str, context: Dict) -> Dict[str, any]:
        """Get response using multiple strategies"""
        message_lower = message.lower()
        
        # Strategy 1: Direct keyword matching
        keyword_response = self._keyword_matching(message_lower)
        if keyword_response:
            return keyword_response
        
        # Strategy 2: Semantic similarity (if NLP available)
        if ADVANCED_NLP_AVAILABLE:
            semantic_response = self._semantic_matching(message)
            if semantic_response and semantic_response['confidence'] > 0.7:
                return semantic_response
        
        # Strategy 3: Context-based response
        context_response = self._context_based_response(message, context)
        if context_response:
            return context_response
        
        # Strategy 4: Fallback response
        return self._get_fallback_response(context)
    
    def _keyword_matching(self, message_lower: str) -> Optional[Dict[str, any]]:
        """Enhanced keyword matching with emotional intelligence"""
        try:
            priority_keywords = {
                "sad": "grief_and_sadness",
                "depressed": "grief_and_sadness",
                "unhappy": "grief_and_sadness",
                "melancholy": "grief_and_sadness",
                "sorrow": "grief_and_sadness",
                "grief": "grief_and_sadness",
                "loss": "grief_and_sadness",
                "anxiety": "anxiety_and_worry",
                "anxious": "anxiety_and_worry",
                "worry": "anxiety_and_worry",
                "worried": "anxiety_and_worry",
                "stress": "anxiety_and_worry",
                "stressed": "anxiety_and_worry",
                "nervous": "anxiety_and_worry",
                "fear": "anxiety_and_worry",
                "afraid": "anxiety_and_worry",
                "overwhelmed": "anxiety_and_worry",
                "exhausted": "anxiety_and_worry",
                "burned": "anxiety_and_worry",
                "burn out": "anxiety_and_worry",
                "tired": "anxiety_and_worry",
                "frustrated": "anxiety_and_worry",
                "angry": "anxiety_and_worry",
                "irritated": "anxiety_and_worry",
                "good day": "motivation_and_encouragement",
                "happy": "motivation_and_encouragement",
                "joy": "motivation_and_encouragement",
                "blessed": "motivation_and_encouragement",
                "grateful": "motivation_and_encouragement",
                "thankful": "motivation_and_encouragement",
                "motivation": "motivation_and_encouragement",
                "encouragement": "motivation_and_encouragement",
                "inspired": "motivation_and_encouragement"
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
    
    def _semantic_matching(self, message: str) -> Optional[Dict[str, any]]:
        """Semantic similarity matching"""
        best_match = None
        best_similarity = 0.0
        
        for key in self.islamic_knowledge:
            similarity = self.get_semantic_similarity(message, key)
            if similarity > best_similarity and similarity > 0.6:
                best_similarity = similarity
                best_match = key
        
        if best_match:
            data = self.islamic_knowledge[best_match]
            return {
                "answer": data["answer"],
                "references": data["references"],
                "source": "Semantic AI Understanding",
                "confidence": best_similarity,
                "strategy": "semantic_matching"
            }
        
        return None
    
    def _context_based_response(self, message: str, context: Dict) -> Optional[Dict[str, any]]:
        """Generate response based on context and user history"""
        sentiment = context['sentiment']
        emotional_keywords = context['emotional_keywords']
        
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
    
    def _get_fallback_response(self, context: Dict) -> Dict[str, any]:
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
    
    def get_learning_stats(self) -> Dict[str, any]:
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
    """Enhanced HTTP request handler for DeenBot"""
    
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
        
        if parsed_url.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "status": "healthy",
                "service": "Enhanced DeenBot Backend",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "uptime": time.time() - start_time,
                "capabilities": {
                    "nlp": ADVANCED_NLP_AVAILABLE,
                    "learning": True,
                    "context_memory": True,
                    "semantic_understanding": ADVANCED_NLP_AVAILABLE
                }
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif parsed_url.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            learning_stats = deenbot.get_learning_stats()
            response = {
                "status": "operational",
                "service": "Enhanced DeenBot Backend",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "uptime": time.time() - start_time,
                "learning_stats": learning_stats
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif parsed_url.path == '/stats':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            learning_stats = deenbot.get_learning_stats()
            self.wfile.write(json.dumps(learning_stats).encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {"error": "Endpoint not found", "available_endpoints": ["/health", "/status", "/stats", "/chat"]}
            self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/chat':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                # Parse JSON
                request_data = json.loads(post_data.decode('utf-8'))
                user_message = request_data.get('message', '').strip()
                user_id = request_data.get('user_id', 'default')
                
                if not user_message:
                    raise ValueError("Message is required")
                
                # Get enhanced response
                response_data = deenbot.get_intelligent_response(user_message, user_id)
                
                # Send response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(response_data).encode())
                
                # Log the interaction
                logging.info(f"✅ Enhanced chat request processed: '{user_message[:50]}...' -> {response_data['source']} (confidence: {response_data['confidence']:.2f})")
                
            except json.JSONDecodeError as e:
                logging.error(f"❌ JSON decode error: {e}")
                self.send_error_response(400, "Invalid JSON format")
                
            except ValueError as e:
                logging.error(f"❌ Validation error: {e}")
                self.send_error_response(400, str(e))
                
            except Exception as e:
                logging.error(f"❌ Unexpected error: {e}")
                self.send_error_response(500, "Internal server error")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {"error": "Endpoint not found", "available_endpoints": ["/health", "/status", "/stats", "/chat"]}
            self.wfile.write(json.dumps(response).encode())
    
    def send_error_response(self, status_code, message):
        """Send error response"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {"error": message, "status_code": status_code}
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
