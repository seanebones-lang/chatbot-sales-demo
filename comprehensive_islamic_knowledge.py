#!/usr/bin/env python3
"""
Comprehensive Islamic Knowledge Base for DeenBot
Permanent solution ensuring authentic Islamic responses
"""

import logging
from datetime import datetime

class ComprehensiveIslamicKnowledge:
    """Comprehensive Islamic knowledge base with authentic hadith and Quran"""
    
    def __init__(self):
        self.hadith_database = self.initialize_hadith_database()
        self.quran_database = self.initialize_quran_database()
        self.fiqh_database = self.initialize_fiqh_database()
        self.islamic_guidance = self.initialize_islamic_guidance()
        
        logging.info(f"✅ Comprehensive Islamic Knowledge Base initialized")
        logging.info(f"📚 Hadith entries: {len(self.hadith_database)}")
        logging.info(f"📖 Quran entries: {len(self.quran_database)}")
        logging.info(f"⚖️ Fiqh entries: {len(self.fiqh_database)}")
        logging.info(f"📖 Islamic guidance topics: {len(self.islamic_guidance)}")
    
    def initialize_hadith_database(self):
        """Initialize comprehensive hadith database"""
        return {
            "anger_management": {
                "hadiths": [
                    {
                        "number": "Sahih Bukhari 6114",
                        "arabic": "لَيْسَ الشَّدِيدُ بِالصُّرَعَةِ، إِنَّمَا الشَّدِيدُ الَّذِي يَمْلِكُ نَفْسَهُ عِنْدَ الْغَضَبِ",
                        "translation": "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry.",
                        "context": "This hadith teaches that true strength lies in self-control, especially during anger. It emphasizes the importance of managing emotions according to Islamic principles.",
                        "narrator": "Abu Hurairah",
                        "source": "Sahih Bukhari",
                        "authentication": "Sahih (Authentic)",
                        "category": "Character & Self-Control"
                    },
                    {
                        "number": "Abu Dawud 4782",
                        "arabic": "إِذَا غَضِبَ أَحَدُكُمْ وَهُوَ قَائِمٌ فَلْيَجْلِسْ، فَإِنْ ذَهَبَ عَنْهُ الْغَضَبُ وَإِلَّا فَلْيَضْطَجِعْ",
                        "translation": "When one of you becomes angry while standing, he should sit down. If the anger leaves him, well and good; otherwise he should lie down.",
                        "context": "This hadith provides practical steps for anger management: change position to help calm emotions.",
                        "narrator": "Abu Dharr",
                        "source": "Abu Dawud",
                        "authentication": "Hasan (Good)",
                        "category": "Character & Self-Control"
                    },
                    {
                        "number": "Abu Dawud 4784",
                        "arabic": "إِنَّ الْغَضَبَ مِنَ الشَّيْطَانِ، وَإِنَّ الشَّيْطَانَ خُلِقَ مِنَ النَّارِ، وَإِنَّمَا تُطْفَأُ النَّارُ بِالْمَاءِ، فَإِذَا غَضِبَ أَحَدُكُمْ فَلْيَتَوَضَّأْ",
                        "translation": "Anger comes from the devil, and the devil was created from fire. Water extinguishes fire, so when one of you becomes angry, he should perform ablution.",
                        "context": "This hadith teaches that anger is from Satan and provides a spiritual solution through wudu (ablution).",
                        "narrator": "Atiyyah as-Sa'di",
                        "source": "Abu Dawud",
                        "authentication": "Hasan (Good)",
                        "category": "Character & Self-Control"
                    }
                ],
                "summary": "The Prophet Muhammad (PBUH) provided comprehensive guidance on managing anger through authentic hadith. Key teachings include: 1) True strength is controlling oneself during anger, 2) Change position when angry (stand to sit to lie down), 3) Perform wudu to calm anger, 4) Seek refuge in Allah, and 5) Remain silent. These hadith provide practical steps for anger management that align with Islamic principles of self-control and spiritual development."
            },
            "prayer": {
                "hadiths": [
                    {
                        "number": "Sahih Bukhari 43",
                        "arabic": "إِنَّ أَوَّلَ مَا يُحَاسَبُ بِهِ الْعَبْدُ يَوْمَ الْقِيَامَةِ مِنْ عَمَلِهِ صَلَاتُهُ، فَإِنْ صَلُحَتْ فَقَدْ أَفْلَحَ وَأَنْجَحَ، وَإِنْ فَسَدَتْ فَقَدْ خَابَ وَخَسِرَ",
                        "translation": "The first thing that will be judged among a person's deeds on the Day of Resurrection is the prayer. If it is good, then the rest of his deeds will be good. If it is bad, then the rest of his deeds will be bad.",
                        "context": "This hadith emphasizes the fundamental importance of prayer in Islam and its role in determining the value of other deeds.",
                        "narrator": "Abu Hurairah",
                        "source": "Sahih Bukhari",
                        "authentication": "Sahih (Authentic)",
                        "category": "Prayer & Worship"
                    },
                    {
                        "number": "Sahih Muslim 151",
                        "arabic": "بَيْنَ الرَّجُلِ وَبَيْنَ الشِّرْكِ وَالْكُفْرِ تَرْكُ الصَّلَاةِ",
                        "translation": "Between a person and disbelief is the abandonment of prayer.",
                        "context": "This hadith shows the critical importance of prayer in maintaining faith and avoiding disbelief.",
                        "narrator": "Jabir ibn Abdullah",
                        "source": "Sahih Muslim",
                        "authentication": "Sahih (Authentic)",
                        "category": "Prayer & Worship"
                    }
                ],
                "summary": "Prayer (Salah) is the cornerstone of Islamic worship. The Prophet Muhammad (PBUH) emphasized its importance through authentic hadith, teaching that prayer is the first deed judged on the Day of Resurrection and that abandoning prayer can lead to disbelief. Prayer serves as a direct connection with Allah and a means of spiritual purification."
            },
            "knowledge": {
                "hadiths": [
                    {
                        "number": "Ibn Majah 224",
                        "arabic": "طَلَبُ الْعِلْمِ فَرِيضَةٌ عَلَى كُلِّ مُسْلِمٍ",
                        "translation": "Seeking knowledge is obligatory upon every Muslim.",
                        "context": "This hadith establishes that seeking knowledge is a religious obligation for every Muslim, emphasizing the importance of education in Islam.",
                        "narrator": "Anas ibn Malik",
                        "source": "Ibn Majah",
                        "authentication": "Hasan (Good)",
                        "category": "Knowledge & Education"
                    }
                ],
            },
            "sorrow_and_sadness": {
                "hadiths": [
                    {
                        "number": "Sahih Muslim 2999",
                        "arabic": "مَا أَصَابَ أَحَدًا قَطُّ هَمٌّ وَلَا حُزْنٌ فَقَالَ: اللَّهُمَّ إِنِّي عَبْدُكَ، وَابْنُ عَبْدِكَ، وَابْنُ أَمَتِكَ، نَاصِيَتِي بِيَدِكَ، مَاضٍ فِيَّ حُكْمُكَ، عَدْلٌ فِيَّ قَضَاؤُكَ، أَسْأَلُكَ بِكُلِّ اسْمٍ هُوَ لَكَ، سَمَّيْتَ بِهِ نَفْسَكَ، أَوْ أَنْزَلْتَهُ فِي كِتَابِكَ، أَوْ عَلَّمْتَهُ أَحَدًا مِنْ خَلْقِكَ، أَوِ اسْتَأْثَرْتَ بِهِ فِي عِلْمِ الْغَيْبِ عِنْدَكَ، أَنْ تَجْعَلَ الْقُرْآنَ رَبِيعَ قَلْبِي، وَنُورَ صَدْرِي، وَجَلَاءَ حُزْنِي، وَذَهَابَ هَمِّي",
                        "translation": "Whenever any person is afflicted with anxiety and grief, he should say: 'O Allah, I am Your servant, son of Your servant, son of Your maidservant. My forehead is in Your hand, Your command over me is forever executed, and Your decree over me is just. I ask You by every name belonging to You with which You have named Yourself, or which You have sent down in Your Book, or which You have taught to any of Your creation, or which You have kept to Yourself in the knowledge of the unseen, that You make the Quran the life of my heart, the light of my chest, the removal of my grief, and the departure of my anxiety.'",
                        "context": "This hadith provides a comprehensive dua (supplication) for relief from sorrow, anxiety, and grief. It teaches Muslims to turn to Allah in times of emotional distress.",
                        "narrator": "Abdullah ibn Mas'ud",
                        "source": "Sahih Muslim",
                        "authentication": "Sahih (Authentic)",
                        "category": "Emotional Well-being & Supplication"
                    },
                    {
                        "number": "Abu Dawud 1525",
                        "arabic": "مَنْ لَزِمَ الِاسْتِغْفَارَ جَعَلَ اللَّهُ لَهُ مِنْ كُلِّ ضِيقٍ مَخْرَجًا، وَمِنْ كُلِّ هَمٍّ فَرَجًا، وَرَزَقَهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
                        "translation": "Whoever persists in seeking forgiveness, Allah will provide him a way out of every difficulty, relief from every anxiety, and will provide for him from sources he could never imagine.",
                        "context": "This hadith teaches that consistent istighfar (seeking forgiveness) helps overcome sorrow and anxiety, providing both spiritual and material relief.",
                        "narrator": "Abu Hurairah",
                        "source": "Abu Dawud",
                        "authentication": "Hasan (Good)",
                        "category": "Emotional Well-being & Supplication"
                    },
                    {
                        "number": "Tirmidhi 3506",
                        "arabic": "إِنَّ اللَّهَ لَا يَضَعُ حَزَنًا فِي قَلْبِ عَبْدٍ إِلَّا لِيُعْطِيَهُ مِنْهُ عِوَضًا",
                        "translation": "Allah does not place sorrow in the heart of a servant except to give him compensation for it.",
                        "context": "This hadith provides comfort by teaching that Allah's tests and trials come with blessings and compensation, helping Muslims understand the wisdom behind difficulties.",
                        "narrator": "Abu Hurairah",
                        "source": "Tirmidhi",
                        "authentication": "Hasan (Good)",
                        "category": "Emotional Well-being & Supplication"
                    }
                ],
                "summary": "The Prophet Muhammad (PBUH) provided comprehensive guidance on dealing with sorrow and sadness through authentic hadith. Key teachings include: 1) Turning to Allah with specific duas for relief from grief, 2) The power of istighfar (seeking forgiveness) in overcoming emotional distress, 3) Understanding that Allah's tests come with compensation and blessings, 4) Using the Quran as a source of comfort and light for the heart, and 5) Recognizing that emotional difficulties are temporary and can be overcome through faith and supplication."
            },
            "knowledge": {
                "hadiths": [
                    {
                        "number": "Ibn Majah 224",
                        "arabic": "طَلَبُ الْعِلْمِ فَرِيضَةٌ عَلَى كُلِّ مُسْلِمٍ",
                        "translation": "Seeking knowledge is obligatory upon every Muslim.",
                        "context": "This hadith establishes that seeking knowledge is a religious obligation for every Muslim, emphasizing the importance of education in Islam.",
                        "narrator": "Anas ibn Malik",
                        "source": "Ibn Majah",
                        "authentication": "Hasan (Good)",
                        "category": "Knowledge & Education"
                    }
                ],
                "summary": "Islam places great emphasis on seeking knowledge as a religious obligation. The Prophet Muhammad (PBUH) taught that seeking knowledge is obligatory for every Muslim, highlighting the importance of education and continuous learning in Islamic tradition."
            }
        }
    
    def initialize_quran_database(self):
        """Initialize comprehensive Quran database"""
        return {
            "anger": {
                "verses": [
                    {
                        "surah": 3,
                        "ayah": 134,
                        "arabic": "الَّذِينَ يُنفِقُونَ فِي السَّرَّاءِ وَالضَّرَّاءِ وَالْكَاظِمِينَ الْغَيْظَ وَالْعَافِينَ عَنِ النَّاسِ ۗ وَاللَّهُ يُحِبُّ الْمُحْسِنِينَ",
                        "translation": "Who spend [in the cause of Allah] during ease and hardship and who restrain anger and who pardon the people. And Allah loves the doers of good.",
                        "context": "This verse describes the characteristics of the righteous, including controlling anger and forgiving others.",
                        "source": "Quran 3:134"
                    }
                ],
                "summary": "The Quran provides guidance on anger management, teaching that restraining anger and forgiving others are characteristics of the righteous that Allah loves."
            },
            "prayer": {
                "verses": [
                    {
                        "surah": 4,
                        "ayah": 103,
                        "arabic": "إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَّوْقُوتًا",
                        "translation": "Indeed, prayer has been decreed upon the believers a [decreed] portion of time.",
                        "context": "This verse establishes prayer as an obligatory act of worship with specific timings.",
                        "source": "Quran 4:103"
                    }
                ],
                "summary": "The Quran establishes prayer as a fundamental obligation for believers, emphasizing its importance in Islamic practice."
            }
        }
    
    def initialize_fiqh_database(self):
        """Initialize comprehensive fiqh database"""
        return {
            "prayer": {
                "title": "Prayer (Salah) - Islamic Jurisprudence",
                "content": "Prayer is the second pillar of Islam and is obligatory for every Muslim. It must be performed five times daily at specific times: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night). Prayer requires wudu (ablution) and must be performed facing the Kaaba in Mecca. The prayer consists of specific movements and recitations that were taught by the Prophet Muhammad (PBUH).",
                "source": "Islamic Fiqh",
                "category": "Worship"
            },
            "fasting": {
                "title": "Fasting (Sawm) - Islamic Jurisprudence",
                "content": "Fasting during the month of Ramadan is the fourth pillar of Islam. It involves abstaining from food, drink, and marital relations from dawn until sunset. Fasting is obligatory for every adult Muslim who is physically and mentally capable. It teaches self-discipline, empathy for the poor, and spiritual purification. The Prophet Muhammad (PBUH) also recommended voluntary fasting on Mondays, Thursdays, and the 13th, 14th, and 15th of each month.",
                "source": "Islamic Fiqh",
                "category": "Worship"
            }
        }
    
    def initialize_islamic_guidance(self):
        """Initialize comprehensive Islamic guidance"""
        return {
            "anger_management": {
                "title": "Anger Management in Islam",
                "content": "Islam provides comprehensive guidance on managing anger through authentic hadith and Quranic teachings. The Prophet Muhammad (PBUH) taught practical steps: 1) Change position when angry (stand to sit to lie down), 2) Perform wudu (ablution), 3) Seek refuge in Allah, 4) Remain silent, and 5) Remember that true strength lies in self-control. The Quran teaches that restraining anger and forgiving others are characteristics of the righteous that Allah loves.",
                "sources": ["Quran 3:134", "Sahih Bukhari 6114", "Abu Dawud 4782", "Abu Dawud 4784"],
                "category": "Character Development"
            },
            "prayer_importance": {
                "title": "Importance of Prayer in Islam",
                "content": "Prayer (Salah) is the cornerstone of Islamic worship and the second pillar of Islam. The Prophet Muhammad (PBUH) emphasized that prayer is the first deed judged on the Day of Resurrection and that abandoning prayer can lead to disbelief. Prayer serves as a direct connection with Allah, provides spiritual purification, and establishes a daily routine of remembrance and gratitude. It must be performed five times daily at specific times and requires proper wudu (ablution).",
                "sources": ["Quran 4:103", "Sahih Bukhari 43", "Sahih Muslim 151"],
                "category": "Worship"
            }
        }
    
    def search_comprehensive_knowledge(self, query, max_results=10):
        """Search through all Islamic knowledge sources"""
        query_lower = query.lower()
        results = []
        
        # Search hadith database
        for topic, topic_data in self.hadith_database.items():
            if any(word in topic.lower() for word in query_lower.split()):
                for hadith in topic_data["hadiths"]:
                    relevance = self.calculate_hadith_relevance(query_lower, hadith)
                    if relevance > 0.3:
                        results.append({
                            'title': f"Hadith {hadith['number']}",
                            'content': f"{hadith['translation']} - {hadith['context']}",
                            'source': f"{hadith['source']} - {hadith['narrator']}",
                            'relevance': relevance,
                            'type': 'hadith',
                            'arabic': hadith.get('arabic', ''),
                            'authentication': hadith.get('authentication', '')
                        })
        
        # Search Quran database
        for topic, topic_data in self.quran_database.items():
            if any(word in topic.lower() for word in query_lower.split()):
                for verse in topic_data["verses"]:
                    relevance = self.calculate_quran_relevance(query_lower, verse)
                    if relevance > 0.3:
                        results.append({
                            'title': f"Quran {verse['source']}",
                            'content': f"{verse['translation']} - {verse['context']}",
                            'source': verse['source'],
                            'relevance': relevance,
                            'type': 'quran',
                            'arabic': verse.get('arabic', '')
                        })
        
        # Search fiqh database
        for topic, topic_data in self.fiqh_database.items():
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            if relevance > 0.3:
                results.append({
                    'title': topic_data['title'],
                    'content': topic_data['content'],
                    'source': topic_data['source'],
                    'relevance': relevance,
                    'type': 'fiqh'
                })
        
        # Search Islamic guidance
        for topic, topic_data in self.islamic_guidance.items():
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            if relevance > 0.3:
                results.append({
                    'title': topic_data['title'],
                    'content': topic_data['content'],
                    'source': f"Islamic Guidance - {', '.join(topic_data['sources'])}",
                    'relevance': relevance,
                    'type': 'guidance'
                })
        
        # Sort by relevance and return top results
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results[:max_results]
    
    def calculate_hadith_relevance(self, query, hadith):
        """Calculate relevance score for hadith"""
        score = 0
        
        # Check translation
        if 'translation' in hadith:
            translation_lower = hadith['translation'].lower()
            for word in query.split():
                if word in translation_lower:
                    score += 0.3
        
        # Check context
        if 'context' in hadith:
            context_lower = hadith['context'].lower()
            for word in query.split():
                if word in context_lower:
                    score += 0.2
        
        # Check category
        if 'category' in hadith:
            category_lower = hadith['category'].lower()
            for word in query.split():
                if word in category_lower:
                    score += 0.3
        
        return score
    
    def calculate_quran_relevance(self, query, verse):
        """Calculate relevance score for Quran verse"""
        score = 0
        
        # Check translation
        if 'translation' in verse:
            translation_lower = verse['translation'].lower()
            for word in query.split():
                if word in translation_lower:
                    score += 0.3
        
        # Check context
        if 'context' in verse:
            context_lower = verse['context'].lower()
            for word in query.split():
                if word in context_lower:
                    score += 0.2
        
        return score
    
    def calculate_content_relevance(self, query, content_data):
        """Calculate relevance score for content"""
        score = 0
        
        # Check title
        if 'title' in content_data:
            title_lower = content_data['title'].lower()
            for word in query.split():
                if word in title_lower:
                    score += 0.5
        
        # Check content
        if 'content' in content_data:
            content_lower = content_data['content'].lower()
            for word in query.split():
                if word in content_lower:
                    score += 0.1
        
        return score
    
    def get_comprehensive_response(self, query):
        """Get comprehensive response from all Islamic knowledge sources"""
        try:
            # Search through all knowledge sources
            search_results = self.search_comprehensive_knowledge(query, max_results=5)
            
            if search_results:
                # Format comprehensive response
                response = f"**Found in Islamic Knowledge Base:**\n\n"
                
                for i, result in enumerate(search_results, 1):
                    response += f"**{i}. {result['title']}**\n"
                    
                    if result['type'] == 'hadith':
                        response += f"*{result['authentication']}*\n"
                        if result['arabic']:
                            response += f"*Arabic: {result['arabic']}*\n"
                    
                    if result['type'] == 'quran':
                        if result['arabic']:
                            response += f"*Arabic: {result['arabic']}*\n"
                    
                    response += f"{result['content']}\n"
                    response += f"*Source: {result['source']}*\n\n"
                
                return response, search_results[0]['source']
            
            return None, None
            
        except Exception as e:
            logging.error(f"❌ Comprehensive search error: {e}")
            return None, None
    
    def get_comprehensive_response_with_scanning(self, query):
        """Get comprehensive response with instant content scanning"""
        try:
            # FIRST: Search comprehensive knowledge base (fastest)
            comprehensive_results = self.search_comprehensive_knowledge(query, max_results=5)
            
            if comprehensive_results:
                # Format comprehensive response from knowledge base
                response = f"**Found in Islamic Knowledge Base:**\n\n"
                
                for i, result in enumerate(comprehensive_results, 1):
                    response += f"**{i}. {result['title']}**\n"
                    
                    if result['type'] == 'hadith':
                        response += f"*{result['authentication']}*\n"
                        if result['arabic']:
                            response += f"*Arabic: {result['arabic']}*\n"
                    
                    if result['type'] == 'quran':
                        if result['arabic']:
                            response += f"*Arabic: {result['arabic']}*\n"
                    
                    response += f"{result['content']}\n"
                    response += f"*Source: {result['source']}*\n\n"
                
                return response, "Islamic Knowledge Base"
            
            # If no results found in knowledge base, return None to trigger online search
            return None, None
            
        except Exception as e:
            logging.error(f"❌ Content scanning error: {e}")
            return None, None
    
    def get_status(self):
        """Get knowledge base status"""
        return {
            'hadith_entries': sum(len(topic_data['hadiths']) for topic_data in self.hadith_database.values()),
            'quran_entries': sum(len(topic_data['verses']) for topic_data in self.quran_database.values()),
            'fiqh_entries': len(self.fiqh_database),
            'guidance_topics': len(self.islamic_guidance),
            'last_updated': datetime.now().isoformat()
        }

# Global instance
comprehensive_knowledge = ComprehensiveIslamicKnowledge()

if __name__ == "__main__":
    print("Comprehensive Islamic Knowledge Base Status:", comprehensive_knowledge.get_status())
    
    print("\nTesting search for 'hadith on anger':")
    results = comprehensive_knowledge.search_comprehensive_knowledge('hadith on anger', max_results=3)
    print(f"Found {len(results)} results")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']} - {result['source']} (Type: {result['type']})")
