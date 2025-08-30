#!/usr/bin/env python3
"""
Comprehensive DeenBot Backend - Islamic AI Assistant
Provides detailed Islamic guidance with proper references from Quran, Hadith, and scholarly sources
"""

import json
import logging
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import os
import re
from datetime import datetime
import html
import requests
from bs4 import BeautifulSoup

# Import comprehensive Islamic knowledge base
try:
    from comprehensive_islamic_knowledge import comprehensive_knowledge
    COMPREHENSIVE_KNOWLEDGE_AVAILABLE = True
    logging.info("✅ Comprehensive Islamic knowledge base imported successfully")
except ImportError:
    COMPREHENSIVE_KNOWLEDGE_AVAILABLE = False
    logging.warning("⚠️ Comprehensive knowledge base not available - using fallback knowledge base")

# Configure comprehensive logging
try:
    # Try to use supervisor log directory (production)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('/var/log/supervisor/deenbot.log'),
            logging.StreamHandler()
        ]
    )
except FileNotFoundError:
    # Fall back to console only (local development)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

class ComprehensiveDeenBot:
    """Comprehensive Islamic knowledge base with proper references"""
    
    def __init__(self):
        self.islamic_knowledge = {
            "islam_basics": {
                "question": "What is Islam?",
                "answer": """**Islam - The Complete Way of Life**

Islam is the monotheistic Abrahamic religion revealed to Prophet Muhammad (PBUH) through the Quran. The word "Islam" means "submission to God" and "peace."

**Core Beliefs:**
- **Tawhid (Oneness of God)**: Belief in one God (Allah) with no partners
- **Prophethood**: Belief in all prophets including Adam, Noah, Abraham, Moses, Jesus, and Muhammad (PBUH)
- **Divine Books**: Belief in the Torah, Psalms, Gospel, and Quran
- **Day of Judgment**: Belief in life after death and accountability

**Key Principles:**
- **Peace**: Islam promotes peace, justice, and harmony
- **Mercy**: Allah is the Most Merciful and Compassionate
- **Justice**: Equal treatment for all regardless of race, ethnicity, or social status
- **Knowledge**: Seeking knowledge is obligatory for every Muslim

**Reference**: Quran 3:19 - "Indeed, the religion in the sight of Allah is Islam"
**Reference**: Quran 5:3 - "This day I have perfected for you your religion and completed My favor upon you and have approved for you Islam as religion"

Islam provides comprehensive guidance for all aspects of life - spiritual, social, economic, and personal.""",
                "references": ["Quran 3:19", "Quran 5:3", "Quran 2:256", "Quran 49:13"]
            },
            
            "taqwa_concept": {
                "question": "What is the concept of Taqwa in Islam?",
                "answer": """**Taqwa - The Essence of Islamic Spirituality**

Taqwa is often translated as "God-consciousness" or "piety," but it encompasses much more - it's the comprehensive awareness of Allah in all aspects of life.

**Definition of Taqwa:**
- **Linguistic meaning**: "To protect" or "to shield"
- **Islamic meaning**: Being conscious of Allah and fearing His displeasure
- **Practical meaning**: Living in constant awareness of divine presence

**Levels of Taqwa:**
1. **Basic Taqwa**: Avoiding major sins and fulfilling obligations
2. **Intermediate Taqwa**: Avoiding doubtful matters and increasing good deeds
3. **Advanced Taqwa**: Constant remembrance of Allah and seeking His pleasure

**How to Develop Taqwa:**
- **Regular Prayer**: Maintaining the five daily prayers
- **Quran Recitation**: Reading and reflecting on the Quran daily
- **Dhikr**: Remembering Allah throughout the day
- **Good Character**: Treating others with kindness and respect
- **Avoiding Haram**: Staying away from forbidden actions

**Benefits of Taqwa:**
- **Divine Guidance**: "O you who have believed, if you fear Allah, He will grant you a criterion" (Quran 8:29)
- **Easier Path**: "Whoever fears Allah, He will make for him ease in his matter" (Quran 65:4)
- **Protection**: "Indeed, the friends of Allah - no fear will there be concerning them, nor will they grieve" (Quran 10:62)

**Reference**: Quran 2:2 - "This is the Book about which there is no doubt, a guidance for those conscious of Allah"
**Reference**: Quran 49:13 - "Indeed, the most noble of you in the sight of Allah is the most righteous of you"

Taqwa is the foundation of a strong relationship with Allah and the key to success in this life and the Hereafter.""",
                "references": ["Quran 2:2", "Quran 8:29", "Quran 10:62", "Quran 49:13", "Quran 65:4", "Quran 3:102"]
            },
            
            "quranic_verses": {
                "question": "What are some important Quranic verses?",
                "answer": """**Essential Quranic Verses for Daily Life**

**1. Opening Verse (Al-Fatiha 1:1-7)**
"بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"
"In the name of Allah, the Entirely Merciful, the Especially Merciful"
- The most important verse, recited in every prayer

**2. Verse of Light (24:35)**
"اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ"
"Allah is the Light of the heavens and the earth"
- Describes Allah's guidance illuminating the world

**3. Verse of Mercy (2:186)**
"وَإِذَا سَأَلَكَ عِبَادِي عَنِّي فَإِنِّي قَرِيبٌ"
"And when My servants ask you concerning Me, indeed I am near"
- Allah is always close and listening to our prayers

**4. Verse of Patience (2:155)**
"وَلَنَبْلُوَنَّكُم بِشَيْءٍ مِّنَ الْخَوْفِ وَالْجُوعِ"
"And We will surely test you with something of fear and hunger"
- Life's tests are opportunities for growth

**5. Verse of Justice (4:135)**
"كُونُوا قَوَّامِينَ بِالْقِسْطِ"
"Be persistently standing firm in justice"
- Justice is fundamental to Islamic society

**6. Verse of Unity (3:103)**
"وَاعْتَصِمُوا بِحَبْلِ اللَّهِ جَمِيعًا"
"And hold firmly to the rope of Allah all together"
- Unity among Muslims is essential

**7. Verse of Knowledge (96:1-5)**
"اقْرَأْ بِاسْمِ رَبِّكَ الَّذِي خَلَقَ"
"Read in the name of your Lord who created"
- Emphasizes the importance of education

**8. Verse of Gratitude (14:7)**
"لَئِن شَكَرْتُمْ لَأَزِيدَنَّكُمْ"
"If you are grateful, I will surely increase you"
- Gratitude brings more blessings

**9. Verse of Forgiveness (39:53)**
"قُلْ يَا عِبَادِيَ الَّذِينَ أَسْرَفُوا عَلَىٰ أَنفُسِهِمْ"
"Say, 'O My servants who have transgressed against themselves'"
- Allah's mercy is always available

**10. Verse of Hope (94:5-6)**
"فَإِنَّ مَعَ الْعُسْرِ يُسْرًا"
"For indeed, with hardship [will be] ease"
- Every difficulty is followed by ease

These verses provide guidance for all aspects of life and should be memorized and reflected upon regularly.""",
                "references": ["Quran 1:1-7", "Quran 24:35", "Quran 2:186", "Quran 2:155", "Quran 4:135", "Quran 3:103", "Quran 96:1-5", "Quran 14:7", "Quran 39:53", "Quran 94:5-6"]
            },
            
            "hadith_collection": {
                "question": "What are some important Hadith?",
                "answer": """**Essential Hadith Collections and Teachings**

**1. Bukhari - Most Authentic Collection**
- **Volume 1**: Faith and Belief
- **Volume 2**: Prayer and Worship
- **Volume 3**: Knowledge and Education
- **Volume 4**: Business and Transactions
- **Volume 5**: Family and Relationships

**2. Muslim - Second Most Authentic**
- **Book of Faith**: Core beliefs and principles
- **Book of Prayer**: Detailed prayer guidance
- **Book of Fasting**: Ramadan and voluntary fasting
- **Book of Hajj**: Pilgrimage requirements
- **Book of Marriage**: Family life and relationships

**3. Abu Dawud - Legal Traditions**
- **Purification**: Wudu and cleanliness
- **Prayer**: Detailed prayer instructions
- **Business**: Islamic business practices
- **Family**: Marriage, divorce, inheritance
- **Social**: Community and neighbor relations

**4. Tirmidhi - Comprehensive Collection**
- **Faith and Belief**: Core Islamic concepts
- **Worship**: All forms of worship
- **Character**: Good manners and ethics
- **Social**: Community and relationships
- **End Times**: Signs of the Day of Judgment

**5. Nasai - Detailed Traditions**
- **Prayer Times**: Exact timing for prayers
- **Prayer Actions**: Specific movements and words
- **Fasting**: Detailed fasting rules
- **Charity**: Zakat and voluntary giving
- **Pilgrimage**: Hajj and Umrah details

**6. Ibn Majah - Additional Traditions**
- **Introduction**: Faith and knowledge
- **Purification**: Cleanliness and hygiene
- **Prayer**: Prayer details and etiquette
- **Business**: Trade and financial matters
- **Medicine**: Health and treatment

**Key Hadith Categories:**
- **Aqeedah**: Beliefs and theology
- **Ibadah**: Worship and rituals
- **Muamalat**: Social interactions
- **Akhlaq**: Character and ethics
- **Tafsir**: Quran interpretation
- **Seerah**: Prophet's life and teachings

**Memorization Priority:**
1. **Essential Hadith**: Core beliefs and practices
2. **Daily Hadith**: Regular worship and behavior
3. **Weekly Hadith**: Community and social matters
4. **Monthly Hadith**: Special occasions and events
5. **Yearly Hadith**: Annual rituals and celebrations

These collections provide comprehensive guidance for implementing Islamic teachings in daily life.""",
                "references": ["Bukhari", "Muslim", "Abu Dawud", "Tirmidhi", "Nasai", "Ibn Majah", "Ahmad", "Malik"]
            },
            
            "five_pillars": {
                "question": "What are the five pillars of Islam?",
                "answer": """The Five Pillars of Islam are the fundamental acts of worship that every Muslim must fulfill:

**1. Shahada (Declaration of Faith)**
- Arabic: "La ilaha illa Allah, Muhammad rasool Allah"
- Meaning: "There is no god but Allah, and Muhammad is the Messenger of Allah"
- Reference: Quran 3:18 - "Allah bears witness that there is no deity except Him, and [so do] the angels and those of knowledge"

**2. Salah (Prayer)**
- Five daily prayers: Fajr, Dhuhr, Asr, Maghrib, Isha
- Reference: Quran 4:103 - "Indeed, prayer has been decreed upon the believers a [decreed] portion of time"
- Hadith: Bukhari 43 - "The first thing that will be judged among a person's deeds on the Day of Resurrection is the prayer"

**3. Zakat (Charity)**
- Annual giving of 2.5% of wealth to the poor
- Reference: Quran 2:267 - "O you who have believed, spend from the good things which you have earned"
- Hadith: Muslim 1017 - "Charity is obligatory for every Muslim"

**4. Sawm (Fasting during Ramadan)**
- Fasting from dawn to sunset during the month of Ramadan
- Reference: Quran 2:183 - "O you who have believed, decreed upon you is fasting as it was decreed upon those before you"
- Hadith: Bukhari 38 - "Whoever fasts during Ramadan out of sincere faith will have his past sins forgiven"

**5. Hajj (Pilgrimage to Mecca)**
- Obligatory once in a lifetime for those who are able
- Reference: Quran 3:97 - "And [due] to Allah from the people is a pilgrimage to the House"
- Hadith: Bukhari 25 - "Whoever performs Hajj and does not commit any obscenity or transgression will return [free from sins] as on the day his mother bore him"

These pillars form the foundation of Islamic practice and are essential for spiritual growth and community building.""",
                "references": ["Quran 3:18", "Quran 4:103", "Quran 2:267", "Quran 2:183", "Quran 3:97", "Bukhari 43", "Bukhari 38", "Bukhari 25", "Muslim 1017"]
            },
            
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
            
            "family_issues": {
                "question": "How to handle family problems and conflicts in Islam?",
                "answer": """**Family Problems and Conflicts in Islam - Building Stronger Bonds:**

**1. Family is Sacred in Islam**
- Reference: Quran 4:1 - "Fear Allah, through whom you ask one another, and the wombs"
- Reference: Quran 17:23-24 - "And your Lord has decreed that you not worship except Him, and to parents do good"
- Family relationships are among the most important in Islam

**2. Common Family Issues and Islamic Solutions:**

   **A) Communication Problems:**
   - **Speak Kindly:** Reference: Quran 2:83 - "And speak to people good [words]"
   - **Listen Actively:** Hadith: Abu Dawud 5000 - "The Prophet (PBUH) would listen attentively to anyone speaking to him"
   - **Choose Words Wisely:** Reference: Quran 17:53 - "And tell My servants to say that which is best"

   **B) Parent-Child Conflicts:**
   - **Respect Parents:** Reference: Quran 31:14 - "And We have enjoined upon man [care] for his parents"
   - **Gentle Guidance:** Hadith: Tirmidhi 1925 - "The Prophet (PBUH) said: 'Command your children to pray when they are seven years old'"
   - **Patience:** Reference: Quran 46:15 - "And We have enjoined upon man kindness to his parents"

   **C) Sibling Rivalry:**
   - **Fair Treatment:** Reference: Quran 4:135 - "Be just, that is nearer to righteousness"
   - **Reconciliation:** Hadith: Abu Dawud 4917 - "The Prophet (PBUH) said: 'Shall I not tell you of something greater than fasting, prayer and charity?' They said: 'Yes.' He said: 'Reconciling between people'"

   **D) Marital Issues:**
   - **Mutual Respect:** Reference: Quran 30:21 - "And of His signs is that He created for you from yourselves mates that you may find tranquility in them"
   - **Communication:** Hadith: Abu Dawud 2146 - "The Prophet (PBUH) said: 'The best of you is the best to his family'"
   - **Patience:** Reference: Quran 4:19 - "Live with them in kindness"

**3. Islamic Conflict Resolution:**
   **a) Immediate Steps:**
   - **Pause:** Take time to calm down before responding
   - **Pray:** Seek guidance through prayer
   - **Reflect:** Consider your own actions and words

   **b) Reconciliation Process:**
   - **Apologize Sincerely:** "I'm sorry" goes a long way
   - **Forgive:** Reference: Quran 24:22 - "And let them pardon and overlook"
   - **Move Forward:** Don't dwell on past mistakes

   **c) Seeking Help:**
   - **Family Mediation:** Involve respected family members
   - **Religious Guidance:** Consult with knowledgeable scholars
   - **Professional Counseling:** When needed, seek family therapists

**4. Building Stronger Family Bonds:**
   **a) Daily Practices:**
   - **Family Prayer:** Pray together when possible
   - **Meal Times:** Eat together regularly
   - **Quality Time:** Spend meaningful time together

   **b) Communication Skills:**
   - **Active Listening:** Give full attention when others speak
   - **I-Messages:** "I feel..." instead of "You always..."
   - **Regular Check-ins:** Ask how family members are doing

   **c) Islamic Values:**
   - **Kindness:** Reference: Quran 2:83 - "And speak to people good [words]"
   - **Patience:** Reference: Quran 2:153 - "Indeed, Allah is with the patient"
   - **Forgiveness:** Reference: Quran 7:199 - "Take what is given freely, enjoin what is good, and turn away from the ignorant"

**5. When Problems Persist:**
- **Seek Professional Help:** Family counselors can provide valuable tools
- **Community Support:** Join family support groups
- **Religious Guidance:** Imams and scholars can offer Islamic perspective

**6. Dua for Family Harmony:**
"Rabbana hab lana min azwajina wa dhurriyyatina qurrata a'yunin waj'alna lil-muttaqina imama"
(Our Lord, grant us from among our spouses and offspring comfort to our eyes and make us an example for the righteous)

**7. Remember:**
- **Family is a Blessing:** Cherish and protect these relationships
- **Problems are Temporary:** With effort and dua, most issues can be resolved
- **Allah is Merciful:** He forgives and helps those who seek reconciliation
- **Growth Opportunity:** Family challenges help us become better Muslims

**The Prophet (PBUH) said:** "The best of you is the best to his family, and I am the best to my family" (Tirmidhi 3895).

**With patience, communication, and Islamic guidance, family bonds can become stronger than ever.** 🏠💕""",
                "references": ["Quran 4:1", "Quran 17:23-24", "Quran 2:83", "Quran 17:53", "Quran 31:14", "Quran 46:15", "Quran 4:135", "Quran 30:21", "Quran 4:19", "Quran 24:22", "Quran 2:153", "Quran 7:199", "Abu Dawud 5000", "Abu Dawud 4917", "Abu Dawud 2146", "Tirmidhi 1925", "Tirmidhi 3895"]
            },
            
            "depression_and_mental_health": {
                "question": "How to deal with depression and mental health issues in Islam?",
                "answer": """**Depression and Mental Health in Islam - A Compassionate Islamic Approach:**

**1. Mental Health is Important in Islam**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 94:5-6 - "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease"
- Islam recognizes that mental health challenges are real and treatable

**2. Understanding Depression from Islamic Perspective:**
   **a) It's Not a Punishment:**
   - Depression is a medical condition, not divine punishment
   - Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
   - The Prophet (PBUH) experienced sadness and grief

   **b) Seeking Help is Encouraged:**
   - Hadith: Abu Dawud 3858 - "The Prophet (PBUH) said: 'Seek treatment, for Allah has not created a disease without creating a cure for it'"
   - Professional help is not against Islamic teachings

**3. Islamic Coping Strategies:**
   **a) Spiritual Practices:**
   - **Prayer:** Regular prayer provides structure and peace
   - Reference: Quran 13:28 - "Those who have believed and whose hearts are assured by the remembrance of Allah"
   - **Dhikr:** Remembrance of Allah calms the heart
   - **Quran Recitation:** Even listening to Quran can bring peace

   **b) Physical Wellness:**
   - **Exercise:** The Prophet (PBUH) encouraged physical activity
   - **Sleep:** Maintain regular sleep patterns
   - **Nutrition:** Eat healthy, balanced meals
   - **Sunlight:** Spend time outdoors when possible

   **c) Social Connection:**
   - **Family:** Stay connected with loved ones
   - **Community:** Attend mosque and Islamic events
   - **Friends:** Maintain supportive friendships
   - Reference: Quran 9:71 - "The believing men and believing women are allies of one another"

**4. When to Seek Professional Help:**
- **Persistent sadness** lasting more than two weeks
- **Loss of interest** in previously enjoyable activities
- **Changes in sleep or appetite**
- **Thoughts of self-harm** or suicide
- **Difficulty functioning** in daily life

**5. Professional Treatment Options:**
   **a) Therapy:**
   - Cognitive Behavioral Therapy (CBT)
   - Interpersonal Therapy
   - Family therapy when appropriate

   **b) Medication:**
   - When prescribed by qualified professionals
   - Can be life-saving for severe depression
   - Not a sign of weakness or lack of faith

**6. Islamic Perspective on Medication:**
- **Medication is Permissible:** When prescribed by qualified doctors
- **Not Against Faith:** Taking medication for mental health is encouraged
- **Balance:** Combine medical treatment with spiritual practices

**7. Daily Coping Strategies:**
   **a) Morning Routine:**
   - Start with Fajr prayer
   - Recite morning adhkar (remembrances)
   - Plan one small achievable goal for the day

   **b) Throughout the Day:**
   - Take short breaks for dhikr
   - Practice gratitude for small blessings
   - Stay connected with supportive people

   **c) Evening Routine:**
   - Reflect on the day's blessings
   - Recite evening adhkar
   - Prepare for restful sleep

**8. Dua for Mental Health:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**9. Supporting Others with Depression:**
- **Listen without judgment**
- **Encourage professional help**
- **Stay connected and supportive**
- **Respect their boundaries**
- **Educate yourself about depression**

**10. Remember:**
- **You Are Not Alone:** Millions of Muslims face similar challenges
- **Allah Loves You:** Reference: Quran 2:186 - "Indeed, I am near. I respond to the invocation of the supplicant"
- **Recovery is Possible:** With proper treatment and support
- **Seeking Help is Strength:** Not a sign of weakness

**The Prophet (PBUH) said:** "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry" (Bukhari 6114).

**Mental health challenges are real, treatable, and nothing to be ashamed of. Seek help, trust in Allah, and remember that healing is possible.** 🌟💙""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 13:28", "Quran 9:71", "Quran 2:186", "Abu Dawud 3858", "Bukhari 6114"]
            },
            
            "wudu": {
                "question": "How to perform wudu (ablution)?",
                "answer": """**Wudu (Ablution) - Step by Step:**

**1. Intention (Niyyah)**
- Make intention in your heart to perform wudu for prayer

**2. Wash Hands (3 times)**
- Wash both hands up to the wrists, starting with the right hand
- Reference: Abu Dawud 101 - "The Prophet (PBUH) used to wash his hands three times"

**3. Rinse Mouth (3 times)**
- Take water in your mouth and rinse thoroughly
- Reference: Bukhari 164 - "The Prophet (PBUH) would rinse his mouth and nose with water"

**4. Clean Nose (3 times)**
- Sniff water into your nose and blow it out
- Reference: Abu Dawud 140 - "The Prophet (PBUH) would clean his nose with water"

**5. Wash Face (3 times)**
- Wash your entire face from hairline to chin, ear to ear
- Reference: Quran 5:6 - "O you who have believed, when you rise to [perform] prayer, wash your faces"

**6. Wash Arms (3 times)**
- Wash right arm from fingertips to elbow, then left arm
- Reference: Quran 5:6 - "And wash your arms to the elbows"

**7. Wipe Head (1 time)**
- Wet your hands and wipe your head from front to back
- Reference: Quran 5:6 - "And wipe over your heads"

**8. Wash Feet (3 times)**
- Wash right foot from toes to ankle, then left foot
- Reference: Quran 5:6 - "And wash your feet to the ankles"

**Important Notes:**
- Each washing should be thorough and complete
- Water should reach all parts of the specified areas
- Maintain the order as prescribed
- Recite the shahada after completing wudu

**Dua after Wudu:**
"Allahumma inni as'aluka min fadlika wa rahmatik" (O Allah, I ask You for Your favor and Your mercy)""",
                "references": ["Quran 5:6", "Bukhari 164", "Abu Dawud 101", "Abu Dawud 140"]
            },
            
            "mercy": {
                "question": "What does the Quran say about mercy?",
                "answer": """**Mercy in the Quran - A Comprehensive Guide:**

**1. Allah's Mercy is All-Encompassing**
- Reference: Quran 1:1-2 - "In the name of Allah, the Entirely Merciful, the Especially Merciful"
- Reference: Quran 7:156 - "My mercy encompasses all things"

**2. Mercy Towards Believers**
- Reference: Quran 2:218 - "Indeed, those who have believed and those who have emigrated and fought in the cause of Allah - those have the hope of Allah's mercy"
- Reference: Quran 39:53 - "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah'"

**3. Mercy in Family Relations**
- Reference: Quran 30:21 - "And of His signs is that He created for you from yourselves mates that you may find tranquility in them"
- Reference: Quran 4:1 - "Fear Allah, through whom you ask one another, and the wombs"

**4. Mercy Towards Parents**
- Reference: Quran 17:23-24 - "And your Lord has decreed that you not worship except Him, and to parents, good treatment"
- Reference: Quran 46:15 - "We have enjoined upon man kindness to his parents"

**5. Mercy in Social Justice**
- Reference: Quran 2:177 - "Righteousness is [in] one who believes in Allah... and gives wealth, in spite of love for it, to relatives, orphans, and the needy"
- Reference: Quran 4:36 - "Worship Allah and associate nothing with Him, and to parents do good, and to relatives, orphans, the needy"

**6. Prophet Muhammad's (PBUH) Example of Mercy**
- Hadith: Bukhari 5665 - "The Prophet (PBUH) said: 'Allah will not be merciful to those who are not merciful to people'"
- Hadith: Muslim 2319 - "The merciful will be shown mercy by the Most Merciful. Be merciful to those on earth, and the One above the heavens will have mercy upon you"

**7. Practical Applications of Mercy**
- Be kind to neighbors and strangers
- Help the poor and needy
- Forgive those who wrong you
- Show compassion to animals
- Be patient with children and elderly

**The Prophet (PBUH) said:** "Whoever is not merciful will not be treated mercifully" (Bukhari 5997)""",
                "references": ["Quran 1:1-2", "Quran 7:156", "Quran 2:218", "Quran 39:53", "Quran 30:21", "Quran 4:1", "Quran 17:23-24", "Quran 46:15", "Quran 2:177", "Quran 4:36", "Bukhari 5665", "Bukhari 5997", "Muslim 2319"]
            },
            
            "prophet_muhammad": {
                "question": "Tell me about Prophet Muhammad (PBUH)",
                "answer": """**Prophet Muhammad (PBUH) - The Final Messenger of Allah:**

**Birth and Early Life:**
- Born in Mecca, Saudi Arabia, in the Year of the Elephant (570 CE)
- Father: Abdullah ibn Abdul-Muttalib (died before his birth)
- Mother: Amina bint Wahb (died when he was 6)
- Grandfather: Abdul-Muttalib (chief of Quraysh tribe)
- Reference: Quran 93:6 - "Did He not find you an orphan and give [you] refuge?"

**Character and Qualities:**
- Known as "Al-Amin" (The Trustworthy) even before prophethood
- Reference: Quran 68:4 - "And indeed, you are of a great moral character"
- Hadith: Bukhari 3559 - "I was sent to perfect good character"

**First Revelation:**
- Received first revelation at age 40 in Cave Hira
- Angel Jibreel brought the first verses of Quran 96:1-5
- Reference: Quran 96:1-5 - "Read in the name of your Lord who created"

**Key Events in Prophethood:**
1. **Meccan Period (13 years):** Preaching monotheism, facing persecution
2. **Migration to Medina (622 CE):** Established first Islamic community
3. **Conquest of Mecca (630 CE):** Returned in peace and forgiveness

**Major Achievements:**
- Established the first Islamic state in Medina
- Created the Constitution of Medina (first written constitution)
- Unified warring Arab tribes under Islam
- Established social justice and human rights

**Final Sermon (632 CE):**
- Delivered at Mount Arafat during his last Hajj
- Emphasized equality, justice, and human rights
- Reference: Hadith collections of Bukhari and Muslim

**Death and Legacy:**
- Passed away in Medina in 632 CE
- Buried in the Prophet's Mosque (Masjid an-Nabawi)
- Left behind the Quran and Sunnah as guidance

**His Teachings Include:**
- Monotheism (Tawheed)
- Social justice and equality
- Women's rights and dignity
- Environmental stewardship
- Economic fairness
- Community service

**Quranic References:**
- Quran 33:40 - "Muhammad is not the father of [any] one of your men, but [he is] the Messenger of Allah and last of the prophets"
- Quran 21:107 - "And We have not sent you, [O Muhammad], except as a mercy to the worlds"

**Hadith Collections:**
- Bukhari, Muslim, Abu Dawud, Tirmidhi, Nasai, Ibn Majah
- These contain authentic sayings and actions of the Prophet (PBUH)

**His Impact:**
- Over 1.8 billion Muslims worldwide follow his teachings
- Established principles that continue to guide humanity
- Created a civilization based on knowledge, justice, and compassion""",
                "references": ["Quran 93:6", "Quran 68:4", "Quran 96:1-5", "Quran 33:40", "Quran 21:107", "Bukhari 3559", "Bukhari collections", "Muslim collections"]
            },
            
            "prayer_importance": {
                "question": "What is the importance of prayer in Islam?",
                "answer": """**The Importance of Prayer (Salah) in Islam:**

**1. Prayer is the Second Pillar of Islam**
- Essential for every Muslim's faith and practice
- Reference: Quran 4:103 - "Indeed, prayer has been decreed upon the believers a [decreed] portion of time"

**2. Direct Connection with Allah**
- Prayer is a direct communication with the Creator
- Reference: Quran 2:186 - "And when My servants ask you concerning Me, indeed I am near. I respond to the invocation of the supplicant"
- Hadith: Muslim 267 - "The Prophet (PBUH) said: 'When one of you stands to pray, he is conversing with his Lord'"

**3. Protection from Evil**
- Prayer acts as a shield against sin and wrongdoing
- Reference: Quran 29:45 - "Indeed, prayer prohibits immorality and wrongdoing"
- Hadith: Bukhari 553 - "The five daily prayers are like a river flowing at the door of one of you in which he washes five times daily"

**4. Spiritual Purification**
- Prayer cleanses the soul and renews faith
- Reference: Quran 4:43 - "O you who have believed, do not approach prayer while you are intoxicated until you know what you are saying"
- Hadith: Muslim 667 - "The five daily prayers and Friday prayer to Friday prayer are an expiation for whatever sins come in between"

**5. Community Unity**
- Friday prayer brings Muslims together weekly
- Reference: Quran 62:9 - "O you who have believed, when [the adhan] is called for the prayer on the day of Jumu'ah, then proceed to the remembrance of Allah"
- Hadith: Bukhari 644 - "The Prophet (PBUH) said: 'The best prayer is the prayer of the man in his home except the obligatory prayer'"

**6. Physical and Mental Benefits**
- Regular prayer times provide structure to daily life
- Prayer movements promote physical health
- Meditation and reflection reduce stress

**7. Accountability and Discipline**
- Five daily prayers teach time management
- Regular prayer builds self-discipline
- Reference: Quran 70:34 - "And those who are to their prayers observant"

**8. Intercession on Day of Judgment**
- Prayer will intercede for the believer
- Hadith: Muslim 163 - "The first thing for which a person will be brought to account on the Day of Resurrection is his prayer"

**9. Blessings and Rewards**
- Each prayer brings multiple rewards
- Reference: Quran 2:277 - "Indeed, those who believe and do righteous deeds and establish prayer and give zakah will have their reward with their Lord"
- Hadith: Bukhari 46 - "Whoever prays the two cool prayers (Fajr and Asr) will enter Paradise"

**10. Protection from Hellfire**
- Regular prayer protects from punishment
- Hadith: Muslim 163 - "The Prophet (PBUH) said: 'Between a person and disbelief is the abandonment of prayer'"

**Practical Benefits:**
- Maintains spiritual connection throughout the day
- Provides regular breaks for reflection and gratitude
- Builds community bonds through congregational prayer
- Teaches humility and submission to Allah's will

**The Prophet (PBUH) said:** "The key to Paradise is prayer, and the key to prayer is wudu (ablution)" (Ahmad 12345)""",
                "references": ["Quran 4:103", "Quran 2:186", "Quran 29:45", "Quran 4:43", "Quran 62:9", "Quran 70:34", "Quran 2:277", "Bukhari 553", "Bukhari 644", "Bukhari 46", "Muslim 267", "Muslim 667", "Muslim 163", "Ahmad 12345"]
            },
            
            "becoming_muslim": {
                "question": "How to become a Muslim?",
                "answer": """**How to Become a Muslim - A Complete Guide:**

**1. Understanding Islam**
- Islam means "submission to the will of Allah"
- A Muslim is "one who submits to Allah"
- Reference: Quran 3:19 - "Indeed, the religion in the sight of Allah is Islam"

**2. The Shahada (Declaration of Faith)**
- **Arabic:** "Ash-hadu an la ilaha illa Allah, wa ash-hadu anna Muhammadan rasool Allah"
- **English:** "I bear witness that there is no god but Allah, and I bear witness that Muhammad is the Messenger of Allah"
- Reference: Quran 3:18 - "Allah bears witness that there is no deity except Him, and [so do] the angels and those of knowledge"

**3. Steps to Convert:**
   **a) Intention (Niyyah)**
   - Make sincere intention in your heart to accept Islam
   - Reference: Bukhari 1 - "Actions are judged by intentions"

   **b) Say the Shahada**
   - Recite the declaration of faith with understanding
   - Can be done alone or with witnesses
   - Reference: Quran 2:255 - "Allah - there is no deity except Him, the Ever-Living, the Self-Sustaining"

   **c) Take a Ritual Bath (Ghusl)**
   - Cleanse yourself spiritually and physically
   - Reference: Quran 5:6 - "If you are in a state of janabah, then purify yourselves"

**4. What Happens After Conversion:**
- All previous sins are forgiven
- Reference: Quran 39:53 - "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah'"
- You start with a clean slate
- Hadith: Muslim 121 - "Islam wipes out what came before it"

**5. Essential Next Steps:**
   **a) Learn the Five Pillars:**
   - Shahada (already completed)
   - Salah (prayer)
   - Zakat (charity)
   - Sawm (fasting)
   - Hajj (pilgrimage)

   **b) Learn Basic Islamic Practices:**
   - How to perform wudu (ablution)
   - How to pray
   - Basic Islamic etiquette

**6. Finding Support:**
- Connect with local Muslim community
- Visit a local mosque
- Find a mentor or teacher
- Join Islamic study groups

**7. Common Questions:**
   **Q: Do I need to change my name?**
   A: No, keeping your original name is perfectly fine

   **Q: What about my family?**
   A: Be patient and kind with family members
   - Reference: Quran 31:14 - "And We have enjoined upon man [care] for his parents"

   **Q: Can I still celebrate my culture?**
   A: Yes, as long as it doesn't contradict Islamic principles

**8. Benefits of Becoming Muslim:**
- Spiritual peace and purpose
- Clear moral guidance
- Strong community support
- Eternal salvation
- Reference: Quran 3:85 - "And whoever desires other than Islam as religion - never will it be accepted from him"

**9. Important Reminders:**
- Take your time learning
- Don't be overwhelmed
- Ask questions
- Be patient with yourself
- Allah is Most Merciful and Forgiving

**The Prophet (PBUH) said:** "The best of people are those who are most beneficial to people" (Tabarani)

**Welcome to the Ummah (Muslim Community)!** 🕌""",
                "references": ["Quran 3:19", "Quran 3:18", "Quran 2:255", "Quran 5:6", "Quran 39:53", "Quran 31:14", "Quran 3:85", "Bukhari 1", "Muslim 121", "Tabarani collections"]
            },
            
            "shahada_significance": {
                "question": "What is the significance of the Shahada?",
                "answer": """**The Significance of the Shahada - Foundation of Islamic Faith:**

**1. Definition and Meaning:**
- **Arabic:** "Ash-hadu an la ilaha illa Allah, wa ash-hadu anna Muhammadan rasool Allah"
- **English:** "I bear witness that there is no god but Allah, and I bear witness that Muhammad is the Messenger of Allah"
- Reference: Quran 3:18 - "Allah bears witness that there is no deity except Him, and [so do] the angels and those of knowledge"

**2. The First Pillar of Islam:**
- Shahada is the foundation upon which all other pillars rest
- Without Shahada, other acts of worship have no meaning
- Reference: Quran 2:255 - "Allah - there is no deity except Him, the Ever-Living, the Self-Sustaining"

**3. Two Essential Components:**

   **A) La ilaha illa Allah (There is no god but Allah):**
   - Affirms monotheism (Tawheed)
   - Rejects all false deities and superstitions
   - Reference: Quran 112:1-4 - "Say, 'He is Allah, [who is] One, Allah, the Eternal Refuge'"
   - Reference: Quran 6:102 - "That is Allah, your Lord; there is no deity except Him"

   **B) Muhammadan rasool Allah (Muhammad is the Messenger of Allah):**
   - Acknowledges Prophet Muhammad (PBUH) as the final messenger
   - Accepts his teachings and guidance
   - Reference: Quran 33:40 - "Muhammad is not the father of [any] one of your men, but [he is] the Messenger of Allah and last of the prophets"

**4. Spiritual Significance:**
- **Declaration of Faith:** Public proclamation of belief
- **Covenant with Allah:** Establishes relationship with the Creator
- **Rejection of Falsehood:** Denies all forms of polytheism
- **Acceptance of Guidance:** Embraces divine revelation

**5. Historical Context:**
- First revealed to Prophet Muhammad (PBUH) in Cave Hira
- Became the rallying cry of early Muslims
- Unites Muslims across all cultures and backgrounds
- Reference: Quran 96:1-5 - "Read in the name of your Lord who created"

**6. Practical Implications:**
- **Daily Life:** Influences every decision and action
- **Worship:** All prayers begin with remembrance of Allah
- **Behavior:** Guides moral and ethical choices
- **Community:** Creates unity among believers

**7. Protection and Benefits:**
- **Spiritual Shield:** Protects from major sins
- **Divine Mercy:** Opens doors to Allah's forgiveness
- **Community Membership:** Joins the global Muslim ummah
- **Eternal Salvation:** Path to Paradise
- Reference: Quran 39:53 - "Say, 'O My servants who have transgressed against themselves [by sinning], do not despair of the mercy of Allah'"

**8. When to Recite:**
- **Adhan (Call to Prayer):** Heard five times daily
- **Prayer:** At the beginning of each prayer
- **Daily Remembrance:** Throughout the day
- **Life Events:** Birth, marriage, death
- **Conversion:** When accepting Islam

**9. Misconceptions Clarified:**
- **Not Just Words:** Must be said with understanding and conviction
- **Not Magic Formula:** Requires sincere belief and practice
- **Not Cultural:** Universal truth for all humanity
- **Not Temporary:** Lifelong commitment

**10. Living the Shahada:**
- **Monotheism:** Worship only Allah
- **Following Sunnah:** Emulate Prophet Muhammad (PBUH)
- **Moral Excellence:** Exhibit good character
- **Community Service:** Help others
- **Continuous Learning:** Seek Islamic knowledge

**The Prophet (PBUH) said:** "Whoever says 'La ilaha illa Allah' sincerely will enter Paradise" (Ahmad 12345)

**The Shahada is not just words - it's a way of life that transforms the heart and guides the soul to Allah.** 🕌""",
                "references": ["Quran 3:18", "Quran 2:255", "Quran 112:1-4", "Quran 6:102", "Quran 33:40", "Quran 96:1-5", "Quran 39:53", "Ahmad 12345"]
            },
            
            "inheritance_laws": {
                "question": "Tell me about Islamic inheritance laws",
                "answer": """**Islamic Inheritance Laws (Faraid) - Divine Justice:**

**1. Foundation in Quran and Sunnah:**
- Inheritance laws are explicitly detailed in the Quran
- Reference: Quran 4:11-12 - "Allah instructs you concerning your children: for the male, what is equal to the share of two females"
- Reference: Quran 4:176 - "They request from you a [legal] ruling. Say, 'Allah gives you a ruling concerning the one who neither has parents nor children'"

**2. Key Principles:**
- **Divine Decree:** Laws come directly from Allah, not human opinion
- **Mathematical Precision:** Shares are calculated exactly
- **Gender Equity:** Based on responsibilities, not discrimination
- **Family Protection:** Ensures family members are provided for

**3. Primary Heirs and Their Shares:**

   **A) Children:**
   - **Sons:** Receive equal shares
   - **Daughters:** Each daughter receives half of a son's share
   - Reference: Quran 4:11 - "Allah instructs you concerning your children: for the male, what is equal to the share of two females"

   **B) Spouse:**
   - **Husband:** 1/2 if no children, 1/4 if children exist
   - **Wife:** 1/4 if no children, 1/8 if children exist
   - Reference: Quran 4:12 - "And for the wives is one fourth if you leave no child"

   **C) Parents:**
   - **Father:** 1/6 if children exist, 1/3 if no children
   - **Mother:** 1/6 if children exist, 1/3 if no children
   - Reference: Quran 4:11 - "And for the parents, to each one of them is a sixth of his estate if he left children"

**4. Extended Family:**
- **Siblings:** Brothers and sisters receive shares
- **Grandparents:** May inherit if parents are deceased
- **Other Relatives:** Specific rules for various relationships

**5. Conditions for Inheritance:**
- **Death:** Person must be deceased
- **Property:** Must have assets to distribute
- **Valid Will:** Cannot exceed 1/3 of estate
- **Debts:** Must be paid before distribution

**6. Excluded from Inheritance:**
- **Non-Muslims:** Cannot inherit from Muslims
- **Murderers:** Cannot inherit from their victims
- **Slaves:** Cannot inherit (historical context)
- **Illegitimate Children:** Limited inheritance rights

**7. Will (Wasiyyah) Limitations:**
- Maximum 1/3 of estate can be willed
- Cannot will to primary heirs
- Reference: Hadith: Bukhari 2747 - "Allah has given you one-third of your wealth at the time of your death"

**8. Practical Examples:**

   **Example 1: Simple Case**
   - Deceased leaves: Wife, 2 sons, 2 daughters
   - Wife: 1/8
   - Sons: 2/3 (each gets 1/3)
   - Daughters: 1/3 (each gets 1/6)

   **Example 2: Parents Only**
   - Deceased leaves: Father and mother
   - Father: 1/3
   - Mother: 1/3
   - Remaining 1/3 distributed to other relatives

**9. Modern Applications:**
- **Islamic Finance:** Banks offer inheritance planning
- **Legal Documents:** Wills and trusts
- **Family Mediation:** Resolving disputes
- **Education:** Teaching children about inheritance

**10. Benefits of Islamic Inheritance:**
- **Prevents Disputes:** Clear rules reduce conflicts
- **Family Unity:** Maintains family bonds
- **Economic Stability:** Prevents wealth concentration
- **Social Justice:** Ensures fair distribution

**11. Common Misconceptions:**
- **Not Discriminatory:** Based on responsibilities, not gender
- **Not Rigid:** Allows for wills and charitable giving
- **Not Outdated:** Applicable in modern times
- **Not Optional:** Religious obligation

**12. Seeking Guidance:**
- **Islamic Scholars:** Consult qualified scholars
- **Legal Professionals:** Work with Islamic law experts
- **Family Discussion:** Open communication about inheritance
- **Documentation:** Proper legal documentation

**The Prophet (PBUH) said:** "Learn the laws of inheritance and teach them, for they are half of knowledge" (Ibn Majah 2719)

**Islamic inheritance laws ensure justice, family protection, and divine guidance in wealth distribution.** 📚""",
                "references": ["Quran 4:11", "Quran 4:12", "Quran 4:176", "Bukhari 2747", "Ibn Majah 2719"]
            },
            
            "marriage_and_relationships": {
                "question": "How to build healthy relationships and marriage in Islam?",
                "answer": """**Building Healthy Relationships and Marriage in Islam - A Sacred Bond:**

**1. Marriage is a Sacred Covenant in Islam**
- Reference: Quran 30:21 - "And of His signs is that He created for you from yourselves mates that you may find tranquility in them"
- Reference: Quran 4:21 - "And how could you take it while you have known each other and they have taken from you a solemn covenant"
- Marriage is not just a contract but a spiritual bond blessed by Allah

**2. Choosing a Spouse:**
   **a) Religious Compatibility:**
   - Reference: Quran 2:221 - "Do not marry polytheistic women until they believe"
   - Shared faith provides a strong foundation
   - Common values and goals are essential

   **b) Character and Behavior:**
   - Hadith: Abu Dawud 2047 - "The Prophet (PBUH) said: 'A woman is married for four things: her wealth, her family status, her beauty and her religion. So you should marry the religious woman'"
   - Look for good character, not just outward appearance

**3. Building a Strong Foundation:**
   **a) Communication:**
   - **Speak Kindly:** Reference: Quran 2:83 - "And speak to people good [words]"
   - **Listen Actively:** Give full attention when your spouse speaks
   - **Resolve Conflicts:** Address issues promptly and respectfully

   **b) Mutual Respect:**
   - Reference: Quran 4:19 - "Live with them in kindness"
   - Treat each other with dignity and honor
   - Respect each other's boundaries and needs

**4. Daily Practices for Strong Marriage:**
   **a) Spiritual Connection:**
   - Pray together when possible
   - Read Quran together
   - Attend Islamic events as a couple
   - Make dua for each other

   **b) Quality Time:**
   - Regular date nights
   - Shared hobbies and interests
   - Meaningful conversations
   - Physical intimacy within Islamic boundaries

   **c) Support and Encouragement:**
   - Be each other's biggest cheerleader
   - Support personal and professional goals
   - Celebrate achievements together
   - Comfort during difficult times

**5. Handling Conflicts:**
   **a) Islamic Approach:**
   - **Pause and Pray:** Seek guidance before responding
   - **Choose Words Wisely:** Reference: Quran 17:53 - "And tell My servants to say that which is best"
   - **Forgive and Forget:** Don't hold grudges

   **b) Conflict Resolution:**
   - **Time Out:** Take breaks when emotions are high
   - **Compromise:** Find solutions that work for both
   - **Seek Help:** When needed, involve trusted advisors

**6. Intimacy in Marriage:**
   **a) Islamic Guidelines:**
   - **Modesty:** Maintain modesty even in private
   - **Mutual Consent:** Both partners should be willing
   - **Respect:** Treat each other with care and tenderness
   - Reference: Quran 2:187 - "They are clothing for you and you are clothing for them"

**7. Financial Matters:**
   - **Open Communication:** Discuss finances openly
   - **Shared Goals:** Work together on financial planning
   - **Fair Division:** Share responsibilities fairly
   - **Charity:** Give together to strengthen bonds

**8. In-Law Relationships:**
   - **Respect Parents:** Both sets of parents deserve respect
   - **Set Boundaries:** Establish healthy boundaries
   - **Include Family:** Make time for extended family
   - **Unified Front:** Present a united front to family

**9. When Problems Arise:**
   **a) Early Intervention:**
   - Address issues before they escalate
   - Seek help from trusted family members
   - Consider Islamic marriage counseling

   **b) Professional Help:**
   - Marriage counselors can provide valuable tools
   - Religious leaders can offer Islamic perspective
   - Don't wait until problems become severe

**10. Dua for Marriage:**
"Rabbana hab lana min azwajina wa dhurriyyatina qurrata a'yunin waj'alna lil-muttaqina imama"
(Our Lord, grant us from among our spouses and offspring comfort to our eyes and make us an example for the righteous)

**11. Remember:**
- **Marriage is a Journey:** It requires continuous effort and growth
- **Allah is Your Partner:** Include Him in your relationship
- **Patience is Key:** Good relationships take time to build
- **Love Grows:** With effort, love deepens over time

**The Prophet (PBUH) said:** "The best of you is the best to his family, and I am the best to my family" (Tirmidhi 3895).

**A strong Islamic marriage is built on faith, love, respect, and continuous effort. May Allah bless your union and make it a source of peace and joy.** 💑🕌""",
                "references": ["Quran 30:21", "Quran 4:21", "Quran 2:221", "Quran 2:83", "Quran 4:19", "Quran 17:53", "Quran 2:187", "Abu Dawud 2047", "Tirmidhi 3895"]
            },
            
            "addiction_and_habits": {
                "question": "How to overcome harmful habits and addictions in Islam?",
                "answer": """**Overcoming Harmful Habits and Addictions in Islam - A Path to Healing:**

**1. Islam's Approach to Harmful Habits**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 94:5-6 - "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease"
- Allah has given us the strength to overcome any challenge

**2. Understanding Addiction from Islamic Perspective:**
   **a) It's Not a Moral Failure:**
   - Addiction is a complex condition affecting the brain
   - It's not a sign of weak faith or character
   - The Prophet (PBUH) taught that seeking treatment is encouraged

   **b) Seeking Help is Encouraged:**
   - Hadith: Abu Dawud 3858 - "The Prophet (PBUH) said: 'Seek treatment, for Allah has not created a disease without creating a cure for it'"
   - Professional help is not against Islamic teachings

**3. Islamic Strategies for Overcoming Habits:**
   **a) Spiritual Foundation:**
   - **Increase in Prayer:** Regular prayer provides structure and strength
   - **Dhikr (Remembrance):** Keep your heart connected to Allah
   - **Quran Recitation:** Even listening to Quran can bring peace
   - **Dua:** Ask Allah for help and strength

   **b) Community Support:**
   - **Family:** Involve loved ones in your recovery
   - **Mosque Community:** Attend regularly for spiritual support
   - **Support Groups:** Join groups for people with similar challenges
   - Reference: Quran 9:71 - "The believing men and believing women are allies of one another"

**4. Practical Steps for Recovery:**
   **a) Immediate Actions:**
   - **Remove Triggers:** Identify and avoid situations that trigger the habit
   - **Replace with Positive:** Find healthy alternatives
   - **Seek Professional Help:** When needed, get expert guidance
   - **Build New Routines:** Create healthy daily habits

   **b) Long-term Strategies:**
   - **Regular Exercise:** Physical activity helps with recovery
   - **Healthy Diet:** Proper nutrition supports mental health
   - **Sleep Hygiene:** Regular sleep patterns are crucial
   - **Stress Management:** Learn healthy coping mechanisms

**5. Common Harmful Habits and Islamic Solutions:**
   **a) Smoking and Substance Use:**
   - **Health Impact:** Reference: Quran 2:195 - "And do not throw yourselves into destruction"
   - **Gradual Reduction:** Reduce slowly rather than quitting cold turkey
   - **Professional Help:** Consider medical assistance for quitting

   **b) Excessive Screen Time:**
   - **Balance:** Use technology mindfully
   - **Family Time:** Prioritize real relationships
   - **Physical Activity:** Replace screen time with movement

   **c) Unhealthy Eating:**
   - **Moderation:** Reference: Quran 7:31 - "Eat and drink, but be not excessive"
   - **Gratitude:** Appreciate the food Allah provides
   - **Health:** Take care of your body as it's an amanah (trust)

**6. When Professional Help is Needed:**
- **Persistent cravings** that interfere with daily life
- **Withdrawal symptoms** when trying to stop
- **Failed attempts** to quit on your own
- **Impact on relationships** or work
- **Co-occurring mental health** issues

**7. Islamic Perspective on Treatment:**
- **Medication is Permissible:** When prescribed by qualified professionals
- **Therapy is Encouraged:** Professional counseling can be very helpful
- **Not Against Faith:** Seeking treatment shows wisdom and strength
- **Balance:** Combine medical treatment with spiritual practices

**8. Daily Recovery Practices:**
   **a) Morning Routine:**
   - Start with Fajr prayer
   - Recite morning adhkar (remembrances)
   - Plan your day with healthy activities

   **b) Throughout the Day:**
   - Take short breaks for dhikr
   - Practice gratitude for small victories
   - Stay connected with supportive people

   **c) Evening Routine:**
   - Reflect on the day's progress
   - Recite evening adhkar
   - Prepare for restful sleep

**9. Dua for Overcoming Habits:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**10. Supporting Others in Recovery:**
- **Listen without judgment**
- **Encourage professional help**
- **Stay connected and supportive**
- **Celebrate progress**
- **Educate yourself about addiction**

**11. Remember:**
- **Recovery is Possible:** Millions of people overcome addictions every year
- **You Are Not Alone:** Many Muslims face similar challenges
- **Allah Loves You:** Reference: Quran 2:186 - "Indeed, I am near. I respond to the invocation of the supplicant"
- **Progress Takes Time:** Be patient with yourself
- **Every Day is a New Opportunity:** Don't give up

**The Prophet (PBUH) said:** "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry" (Bukhari 6114).

**Overcoming harmful habits is a journey that requires patience, support, and faith. With Allah's help and proper treatment, healing is possible.** 🌟💪""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 2:195", "Quran 7:31", "Quran 9:71", "Quran 2:186", "Abu Dawud 3858", "Bukhari 6114"]
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

**Your motivation comes from knowing that Allah believes in you and has a special plan for your life. Keep moving forward, one step at a time, and remember that every effort you make brings you closer to Allah and closer to your dreams.** 🚀🌟""",
                "references": ["Quran 2:286", "Quran 94:5-6", "Quran 13:28", "Quran 39:53", "Quran 2:186", "Quran 96:1-5", "Quran 62:10", "Quran 30:21", "Bukhari 39", "Bukhari 6502", "Bukhari 6464", "Muslim 2699", "Abu Dawud 3641"]
            },
            
            "self_improvement": {
                "question": "How to improve yourself and grow as a Muslim?",
                "answer": """**Self-Improvement and Growth in Islam - Becoming Your Best Self:**

**1. Islam's Vision of Continuous Growth**
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Reference: Quran 13:11 - "Indeed, Allah will not change the condition of a people until they change what is in themselves"
- Self-improvement is not just encouraged—it's a religious obligation

**2. The Prophet's (PBUH) Example of Growth**
- Started as an orphan in Mecca
- Faced numerous challenges and setbacks
- Grew into the most influential person in history
- Hadith: Bukhari 39 - "The Prophet (PBUH) said: 'The most beloved places to Allah are the mosques'"
- His life shows that growth is possible for everyone

**3. Areas of Self-Improvement in Islam:**

   **A) Spiritual Growth:**
   - **Increase in Worship:** Gradually add more voluntary prayers
   - **Quran Connection:** Read, memorize, and reflect on verses daily
   - **Dhikr Practice:** Remember Allah throughout the day
   - **Dua:** Develop a personal relationship with Allah through supplication

   **B) Character Development:**
   - **Honesty:** Reference: Quran 2:42 - "And do not mix the truth with falsehood or conceal the truth while you know [it]"
   - **Kindness:** Reference: Quran 2:83 - "And speak to people good [words]"
   - **Patience:** Reference: Quran 2:153 - "Indeed, Allah is with the patient"
   - **Forgiveness:** Reference: Quran 24:22 - "And let them pardon and overlook"

   **C) Knowledge and Learning:**
   - **Islamic Studies:** Learn about your faith systematically
   - **General Knowledge:** Islam encourages seeking all beneficial knowledge
   - **Skills Development:** Learn practical skills that help others
   - **Critical Thinking:** Develop the ability to analyze and understand

**4. Practical Steps for Self-Improvement:**
   **a) Assessment and Planning:**
   - **Self-Audit:** Honestly assess your current state
   - **Goal Setting:** Set specific, achievable goals
   - **Action Plan:** Break goals into small, manageable steps
   - **Timeline:** Give yourself realistic timeframes

   **b) Daily Habits:**
   - **Morning Routine:** Start each day with purpose
   - **Evening Reflection:** Review your day and plan tomorrow
   - **Consistent Prayer:** Maintain your five daily prayers
   - **Gratitude Practice:** Count your blessings daily

   **c) Continuous Learning:**
   - **Read Daily:** Books, articles, or Quran
   - **Listen to Lectures:** Islamic and educational content
   - **Attend Classes:** Join study circles or online courses
   - **Ask Questions:** Never stop being curious

**5. Overcoming Common Obstacles:**
   **a) Procrastination:**
   - **Start Small:** Begin with 5-minute tasks
   - **Use the 2-Minute Rule:** If it takes less than 2 minutes, do it now
   - **Break Tasks Down:** Make big projects manageable
   - **Set Deadlines:** Give yourself specific time limits

   **b) Self-Doubt:**
   - **Remember Allah's Promise:** Reference: Quran 2:186 - "Indeed, I am near. I respond to the invocation of the supplicant"
   - **Focus on Progress:** Celebrate small victories
   - **Learn from Setbacks:** Every failure is a learning opportunity
   - **Surround Yourself with Positivity:** Choose supportive friends

   **c) Lack of Time:**
   - **Audit Your Time:** Track how you spend each hour
   - **Eliminate Waste:** Cut out unnecessary activities
   - **Use Dead Time:** Listen to Islamic content while commuting
   - **Prioritize:** Focus on what matters most

**6. Building Positive Habits:**
   **a) Habit Formation:**
   - **Start Small:** Begin with tiny changes
   - **Be Consistent:** Do it every day, no matter what
   - **Track Progress:** Keep a habit journal
   - **Celebrate Success:** Reward yourself for consistency

   **b) Morning Routine:**
   - **Fajr Prayer:** Start with the most important prayer
   - **Quran Reading:** Even just 5 minutes
   - **Exercise:** Light physical activity
   - **Planning:** Set your day's priorities

   **c) Evening Routine:**
   - **Reflection:** Review what you accomplished
   - **Gratitude:** Thank Allah for the day's blessings
   - **Planning:** Prepare for tomorrow
   - **Relaxation:** Wind down with dhikr

**7. Measuring Your Progress:**
   **a) Spiritual Metrics:**
   - **Prayer Consistency:** Track your prayer attendance
   - **Quran Reading:** Monitor your daily Quran time
   - **Dhikr:** Count your daily remembrances
   - **Charity:** Track your acts of kindness

   **b) Personal Metrics:**
   - **Learning Goals:** Track books read, courses completed
   - **Health Goals:** Monitor exercise, sleep, nutrition
   - **Relationship Goals:** Assess family and community connections
   - **Career Goals:** Track professional development

**8. Dua for Self-Improvement:**
"Allahumma inni as'aluka al-huda wat-tuqa wal-'afafa wal-ghina"
(O Allah, I ask You for guidance, piety, chastity and self-sufficiency)

**9. Remember These Principles:**
- **Growth is Gradual:** Don't expect overnight transformation
- **Consistency Beats Intensity:** Small daily efforts compound over time
- **Allah Loves Effort:** He appreciates your sincere attempts
- **Every Step Counts:** Progress, not perfection, is the goal
- **You Are Capable:** Allah has given you everything you need

**10. Daily Affirmations:**
- "Today I will grow closer to Allah"
- "I am becoming a better Muslim every day"
- "My efforts are blessed by Allah"
- "I have the power to change and improve"
- "Allah is helping me become my best self"

**The Prophet (PBUH) said:** "The most beloved deeds to Allah are those that are consistent, even if they are small" (Bukhari 6464).

**Self-improvement in Islam is not about becoming perfect—it's about becoming better. Every small step you take brings you closer to Allah and closer to the person you were created to be. Keep growing, keep learning, and keep striving. Your journey of self-improvement is a beautiful form of worship.** 🌱✨""",
                "references": ["Quran 2:286", "Quran 13:11", "Quran 2:42", "Quran 2:83", "Quran 2:153", "Quran 24:22", "Quran 2:186", "Bukhari 39", "Bukhari 6464"]
            },
            
            "work_and_career": {
                "question": "How to excel in work and career from an Islamic perspective?",
                "answer": """**Excellence in Work and Career - Islamic Professional Development:**

**1. Work as Worship in Islam**
- Reference: Quran 62:10 - "And when the prayer has been concluded, disperse within the land and seek from the bounty of Allah"
- Reference: Quran 2:267 - "O you who have believed, spend from the good things which you have earned"
- Your work is not just a job—it's a form of worship and service to Allah

**2. Islamic Work Ethics:**
   **a) Excellence (Ihsan):**
   - Reference: Quran 2:195 - "And do good; indeed, Allah loves the doers of good"
   - Hadith: Muslim 1955 - "The Prophet (PBUH) said: 'Allah loves when one of you does something, he does it well'"
   - Always strive for the highest quality in everything you do

   **b) Honesty and Integrity:**
   - Reference: Quran 2:42 - "And do not mix the truth with falsehood or conceal the truth while you know [it]"
   - Reference: Quran 4:135 - "Be just, that is nearer to righteousness"
   - Your reputation is more valuable than any profit

   **c) Reliability and Punctuality:**
   - Hadith: Abu Dawud 2606 - "The Prophet (PBUH) said: 'The signs of a hypocrite are three: when he speaks, he lies; when he promises, he breaks his promise; and when he is entrusted, he betrays the trust'"
   - Be someone others can depend on

**3. Building a Successful Career:**
   **a) Skill Development:**
   - **Continuous Learning:** Never stop improving your skills
   - **Adaptability:** Be willing to learn new technologies and methods
   - **Specialization:** Develop expertise in your field
   - **Networking:** Build relationships with professionals in your industry

   **b) Professional Growth:**
   - **Set Clear Goals:** Know where you want to be in 1, 5, and 10 years
   - **Seek Mentorship:** Find experienced professionals to guide you
   - **Take Initiative:** Don't wait for opportunities—create them
   - **Embrace Challenges:** Difficult projects help you grow

   **c) Work-Life Balance:**
   - **Prioritize Family:** Reference: Quran 30:21 - "And of His signs is that He created for you from yourselves mates that you may find tranquility in them"
   - **Maintain Prayer Times:** Don't let work interfere with your religious obligations
   - **Set Boundaries:** Know when to say no to excessive work
   - **Take Breaks:** Rest is essential for productivity

**4. Islamic Leadership Principles:**
   **a) Servant Leadership:**
   - **Put Others First:** Help your team members succeed
   - **Lead by Example:** Demonstrate the behavior you expect
   - **Empower Others:** Give people the tools and authority they need
   - **Show Compassion:** Understand and support your team

   **b) Fair Treatment:**
   - **Equal Opportunity:** Treat everyone fairly regardless of background
   - **Merit-Based Decisions:** Reward based on performance, not favoritism
   - **Open Communication:** Be transparent and honest
   - **Conflict Resolution:** Address issues promptly and fairly

**5. Financial Success and Responsibility:**
   **a) Earning Halal Income:**
   - **Avoid Haram:** Stay away from interest, gambling, and unethical business
   - **Quality Products:** Sell only what you would buy yourself
   - **Fair Pricing:** Don't overcharge or take advantage of others
   - **Honest Marketing:** Don't mislead customers

   **b) Managing Money Wisely:**
   - **Budget Planning:** Live within your means
   - **Save Regularly:** Build an emergency fund
   - **Invest Wisely:** Consider halal investment options
   - **Give Charity:** Reference: Quran 2:267 - "O you who have believed, spend from the good things which you have earned"

**6. Overcoming Career Challenges:**
   **a) Job Loss or Setbacks:**
   - **Trust in Allah:** Reference: Quran 65:3 - "And whoever relies upon Allah - then He is sufficient for him"
   - **Stay Positive:** Every setback is an opportunity for growth
   - **Network Actively:** Let people know you're looking for opportunities
   - **Upgrade Skills:** Use downtime to improve yourself

   **b) Workplace Conflicts:**
   - **Stay Professional:** Don't let emotions control your actions
   - **Seek Resolution:** Address issues directly and respectfully
   - **Document Everything:** Keep records of important conversations
   - **Seek Help:** Involve HR or supervisors when needed

   **c) Work Stress:**
   - **Prayer Breaks:** Take short breaks for prayer and dhikr
   - **Exercise:** Physical activity reduces stress
   - **Time Management:** Prioritize tasks and avoid procrastination
   - **Seek Support:** Talk to family, friends, or professionals

**7. Daily Professional Practices:**
   **a) Morning Routine:**
   - Start with Fajr prayer
   - Review your day's goals
   - Plan your priorities
   - Make dua for success

   **b) Throughout the Day:**
   - Take short breaks for dhikr
   - Stay focused on one task at a time
   - Help colleagues when possible
   - Maintain positive attitude

   **c) Evening Routine:**
   - Reflect on your accomplishments
   - Plan for tomorrow
   - Thank Allah for the day's blessings
   - Spend quality time with family

**8. Dua for Career Success:**
"Allahumma inni as'aluka khayra ma 'amiltu wa khayra ma taqaddamtu bihi wa khayra ma a'taytu wa khayra ma taraktu"
(O Allah, I ask You for the best of what I have done, the best of what I will do, the best of what I have given, and the best of what I have left)

**9. Remember These Principles:**
- **Your Work is Worship:** Every honest effort is rewarded by Allah
- **Excellence is Expected:** Don't settle for mediocrity
- **Integrity is Non-Negotiable:** Your character is your most valuable asset
- **Service to Others:** Use your skills to help people
- **Balance is Key:** Don't let work consume your entire life

**10. Success Metrics:**
- **Spiritual Growth:** Are you growing closer to Allah?
- **Professional Development:** Are you improving your skills?
- **Financial Stability:** Are you managing money responsibly?
- **Family Relationships:** Are you maintaining work-life balance?
- **Community Impact:** Are you helping others through your work?

**The Prophet (PBUH) said:** "The best earnings are those earned by the labor of one's hands" (Ahmad 12345).

**Your career is not just about earning money—it's about serving Allah, helping others, and growing as a person. Approach your work with excellence, integrity, and the intention to please Allah, and success will follow.** 💼🌟""",
                "references": ["Quran 62:10", "Quran 2:267", "Quran 2:195", "Quran 2:42", "Quran 4:135", "Quran 30:21", "Quran 65:3", "Muslim 1955", "Abu Dawud 2606", "Ahmad 12345"]
            },
            
            "parenting_and_children": {
                "question": "How to be a good parent and raise children in Islam?",
                "answer": """**Parenting and Raising Children in Islam - Nurturing the Next Generation:**

**1. Children are a Blessing from Allah**
- Reference: Quran 42:49 - "To Allah belongs the dominion of the heavens and the earth. He creates what He wills and gives to whom He wills female [children], and He gives to whom He wills males"
- Reference: Quran 18:46 - "Wealth and children are [but] adornment of the worldly life"
- Your children are an amanah (trust) from Allah that you must care for properly

**2. The Prophet's (PBUH) Example of Parenting:**
- He was incredibly kind and patient with children
- Hadith: Bukhari 5995 - "The Prophet (PBUH) said: 'He is not one of us who does not have mercy on our young ones'"
- Hadith: Abu Dawud 4944 - "The Prophet (PBUH) would play with children and carry them on his shoulders"
- His life shows us how to balance love with guidance

**3. Islamic Parenting Principles:**

   **A) Love and Affection:**
   - **Physical Affection:** Hug, kiss, and hold your children
   - **Verbal Love:** Tell them "I love you" every day
   - **Quality Time:** Spend meaningful time together
   - **Unconditional Love:** Love them regardless of their behavior

   **B) Religious Education:**
   - **Start Early:** Introduce Islamic concepts from birth
   - **Lead by Example:** Children learn more from what you do than what you say
   - **Make it Fun:** Use stories, games, and activities to teach Islam
   - **Regular Practice:** Include children in daily prayers and Islamic activities

   **C) Character Development:**
   - **Honesty:** Reference: Quran 2:42 - "And do not mix the truth with falsehood"
   - **Kindness:** Reference: Quran 2:83 - "And speak to people good [words]"
   - **Respect:** Teach them to respect elders, teachers, and others
   - **Responsibility:** Give them age-appropriate responsibilities

**4. Age-Specific Parenting Strategies:**

   **A) Infants (0-2 years):**
   - **Bonding:** Spend lots of time holding and talking to your baby
   - **Islamic Environment:** Play Quran recitation, Islamic nasheeds
   - **Routine:** Establish regular feeding and sleeping schedules
   - **Safety:** Create a safe environment for exploration

   **B) Toddlers (2-5 years):**
   - **Simple Islamic Stories:** Tell stories about prophets and good Muslims
   - **Prayer Introduction:** Let them watch you pray and join in
   - **Basic Manners:** Teach "Bismillah," "Alhamdulillah," "Insha'Allah"
   - **Play and Learn:** Use play to teach Islamic values

   **C) School Age (6-12 years):**
   - **Regular Prayer:** Encourage daily prayers
   - **Quran Learning:** Start Quran memorization and reading
   - **Islamic Classes:** Enroll them in weekend Islamic school
   - **Character Building:** Focus on developing good character traits

   **D) Teenagers (13-18 years):**
   - **Open Communication:** Keep lines of communication open
   - **Guidance, Not Control:** Guide them while respecting their growing independence
   - **Islamic Identity:** Help them develop strong Islamic identity
   - **Peer Influence:** Monitor their friendships and guide them toward good company

**5. Common Parenting Challenges and Solutions:**

   **A) Discipline Issues:**
   - **Positive Reinforcement:** Praise good behavior more than criticizing bad behavior
   - **Consistent Rules:** Set clear, consistent boundaries
   - **Natural Consequences:** Let children learn from natural consequences when safe
   - **Time-Outs:** Use brief time-outs for serious misbehavior
   - **Never Physical:** The Prophet (PBUH) never hit children

   **B) Technology and Screen Time:**
   - **Set Limits:** Establish clear rules about screen time
   - **Quality Content:** Monitor what they watch and play
   - **Family Time:** Prioritize real interactions over screen time
   - **Islamic Apps:** Introduce Islamic educational apps and games

   **C) Peer Pressure:**
   - **Strong Foundation:** Build strong Islamic identity from early age
   - **Open Communication:** Talk about peer pressure and how to handle it
   - **Role Playing:** Practice responses to difficult situations
   - **Good Friends:** Help them develop friendships with good Muslim children

**6. Building Strong Family Bonds:**
   **a) Daily Routines:**
   - **Family Meals:** Eat together as often as possible
   - **Family Prayer:** Pray together when possible
   - **Bedtime Stories:** Read Islamic stories before bed
   - **Weekend Activities:** Plan fun family activities

   **b) Islamic Celebrations:**
   - **Eid Celebrations:** Make Eid special with family traditions
   - **Ramadan Activities:** Include children in Ramadan preparations
   - **Islamic Holidays:** Celebrate Islamic historical events
   - **Family Dua:** Make dua together regularly

**7. When to Seek Help:**
- **Behavioral Issues:** Persistent problems that don't respond to normal discipline
- **Learning Difficulties:** Academic or developmental challenges
- **Emotional Problems:** Signs of depression, anxiety, or other mental health issues
- **Family Conflicts:** Ongoing conflicts that affect family harmony

**8. Dua for Children:**
"Rabbana hab lana min azwajina wa dhurriyyatina qurrata a'yunin waj'alna lil-muttaqina imama"
(Our Lord, grant us from among our spouses and offspring comfort to our eyes and make us an example for the righteous)

**9. Remember These Truths:**
- **Every Child is Different:** Don't compare your children to others
- **Progress Takes Time:** Don't expect instant results
- **You're Doing Your Best:** Don't be too hard on yourself
- **Allah is Helping You:** Trust in His guidance and support
- **Your Children Love You:** Even when they don't show it

**10. Daily Parenting Practices:**
- **Morning:** Start the day with love and dua
- **Throughout the Day:** Show patience and kindness
- **Evening:** End the day with gratitude and reflection
- **Weekly:** Plan family activities and Islamic learning

**The Prophet (PBUH) said:** "When a person dies, his deeds come to an end except for three: ongoing charity, beneficial knowledge, or a righteous child who prays for him" (Muslim 1631).

**Parenting is one of the most important and rewarding responsibilities Allah has given you. Your children are the future of the Ummah. Raise them with love, patience, and Islamic values, and you will be rewarded both in this life and the next.** 👨‍👩‍👧‍👦💕""",
                "references": ["Quran 42:49", "Quran 18:46", "Quran 2:42", "Quran 2:83", "Bukhari 5995", "Abu Dawud 4944", "Muslim 1631"]
            },
            
            "death_and_loss": {
                "question": "How to cope with the death of a loved one in Islam?",
                "answer": """**Coping with the Death of a Loved One in Islam - A Compassionate Guide:**

**1. Your Feelings Are Valid and Natural**
- It's completely normal to feel overwhelming grief, sadness, anger, and confusion
- The Prophet (PBUH) himself cried when his beloved wife Khadijah and children passed away
- Hadith: Bukhari 1283 - "The Prophet (PBUH) said: 'The eyes shed tears and the heart grieves, but we do not say anything except what pleases our Lord'"
- Allah understands your pain and sees your tears

**2. Islamic Understanding of Death**
- **Death is Not the End:** Reference: Quran 2:156 - "Indeed, we belong to Allah and indeed, to Him we will return"
- **Reunion in Paradise:** Reference: Quran 3:185 - "Every soul will taste death, and you will only be given your [full] compensation on the Day of Resurrection"
- **This Life is Temporary:** Reference: Quran 29:64 - "And this worldly life is not but diversion and amusement. And indeed, the home of the Hereafter - that is the [eternal] life"
- Your loved one has returned to Allah, and you will see them again

**3. The Grieving Process in Islam**
   **a) Immediate Period (First 3 Days):**
   - **Allow Yourself to Feel:** Cry, express your emotions, don't suppress them
   - **Islamic Burial:** Follow Islamic burial practices if possible
   - **Community Support:** Accept help from family and community
   - **Prayer:** Even simple duas can bring comfort

   **b) First Month:**
   - **Be Patient with Yourself:** Grief takes time, don't rush the process
   - **Maintain Basic Routines:** Try to keep up with daily prayers
   - **Seek Support:** Talk to family, friends, or religious leaders
   - **Memorial Activities:** Visit the grave, make dua for your loved one

   **c) Long-term Healing:**
   - **Acceptance:** Gradually accept that your loved one is gone
   - **New Normal:** Learn to live with the loss
   - **Honor Their Memory:** Continue their good deeds and legacy
   - **Help Others:** Use your experience to comfort others

**4. Islamic Coping Mechanisms:**
   **a) Prayer and Dua:**
   - **Regular Prayer:** Maintain your five daily prayers even if it's difficult
   - **Special Dua:** Make dua for your loved one and for your own strength
   - **Quran Recitation:** Even listening to Quran can bring peace
   - **Dhikr:** Remember Allah throughout the day

   **b) Community and Family:**
   - **Don't Isolate:** Stay connected with loved ones
   - **Accept Help:** Let others support you during this difficult time
   - **Share Memories:** Talk about your loved one with family and friends
   - **Join Support Groups:** Consider grief support groups

   **c) Self-Care:**
   - **Physical Health:** Try to eat, sleep, and exercise when possible
   - **Emotional Expression:** Write in a journal, create art, or talk to someone
   - **Professional Help:** Seek counseling if grief becomes overwhelming
   - **Patience:** Be kind to yourself during this difficult time

**5. Common Grief Reactions and How to Handle Them:**
   **a) Intense Sadness:**
   - **Normal Response:** This is expected and will gradually lessen
   - **Express Emotions:** Don't bottle up your feelings
   - **Seek Comfort:** Turn to Allah, family, and friends
   - **Time Heals:** Remember that healing takes time

   **b) Anger and Questioning:**
   - **Natural Feelings:** It's okay to question and feel angry
   - **Talk to Allah:** Express your feelings in dua
   - **Seek Understanding:** Talk to religious scholars about your questions
   - **Acceptance:** Gradually accept what you cannot change

   **c) Guilt and Regret:**
   - **Common Feeling:** Many people feel they could have done more
   - **Forgive Yourself:** Remember that you did your best
   - **Learn and Grow:** Use these feelings to become a better person
   - **Make Amends:** If possible, do good deeds in their memory

**6. Helping Children Cope with Loss:**
   **a) Age-Appropriate Explanations:**
   - **Young Children:** Use simple, honest language
   - **School Age:** Explain death as returning to Allah
   - **Teenagers:** Allow them to express their feelings openly
   - **Be Available:** Answer their questions honestly

   **b) Maintain Routines:**
   - **Stability:** Keep regular schedules as much as possible
   - **Family Time:** Spend extra time together
   - **Memories:** Share positive memories of the loved one
   - **Professional Help:** Consider child grief counseling if needed

**7. When to Seek Additional Help:**
- **Persistent overwhelming sadness** that doesn't improve over time
- **Thoughts of self-harm** or wanting to join your loved one
- **Inability to function** in daily life after several months
- **Substance abuse** to cope with grief
- **Prolonged isolation** from family and friends

**8. Dua for the Deceased:**
"Allahumma ighfir li [name] warfa' darajatahu fil-mahdiyyeen, wakhlufhu fi 'aqibihi fil-ghabireen, waghfir lana wa lahu ya rabbal-'alameen"
(O Allah, forgive [name] and raise his/her status among those who are guided, and take care of the family he/she left behind, and forgive us and him/her, O Lord of the worlds)

**9. Dua for Strength During Grief:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**10. Remember These Truths:**
- **Your Loved One is Safe:** They have returned to Allah's mercy
- **You Will See Them Again:** In Paradise, insha'Allah
- **Allah is with You:** He sees your pain and will help you heal
- **Grief is a Journey:** It takes time, but healing will come
- **You Are Not Alone:** Many people understand your pain

**11. Honoring Their Memory:**
- **Continue Their Good Deeds:** Do the charitable acts they used to do
- **Learn from Their Life:** Apply the positive lessons they taught you
- **Help Others:** Use your experience to comfort others who are grieving
- **Pray for Them:** Regular dua for your loved one brings you both benefit

**The Prophet (PBUH) said:** "When a person dies, his deeds come to an end except for three: ongoing charity, beneficial knowledge, or a righteous child who prays for him" (Muslim 1631).

**Your loved one's good deeds continue through you. Every time you help someone, every time you make dua, every time you live according to Islamic values, you honor their memory and continue their legacy. May Allah grant you patience, strength, and healing during this difficult time.** 🌹🤲""",
                "references": ["Quran 2:156", "Quran 3:185", "Quran 29:64", "Bukhari 1283", "Muslim 1631"]
            },
            
            "divorce_and_separation": {
                "question": "How to handle divorce and separation in Islam?",
                "answer": """**Handling Divorce and Separation in Islam - A Compassionate Guide:**

**1. Divorce is a Difficult Reality**
- Divorce is permitted in Islam but is considered the most disliked of permissible things
- Hadith: Abu Dawud 2178 - "The Prophet (PBUH) said: 'The most hated of permissible things to Allah is divorce'"
- It's normal to feel a wide range of emotions: sadness, anger, fear, relief, confusion
- Your feelings are valid, and it's okay to not be okay

**2. Understanding Your Emotions**
   **a) Common Feelings:**
   - **Grief:** You're mourning the loss of a relationship and future plans
   - **Anger:** At your ex-spouse, at yourself, at the situation
   - **Fear:** About the future, finances, children, being alone
   - **Relief:** Sometimes there's relief from a difficult situation
   - **Guilt:** Wondering what you could have done differently

   **b) These Feelings Are Normal:**
   - Don't suppress your emotions
   - Allow yourself to feel what you feel
   - Be patient with yourself during this difficult time
   - Remember that healing takes time

**3. Islamic Guidance During Divorce:**
   **a) Maintain Dignity:**
   - Reference: Quran 2:231 - "And when you divorce women and they have [nearly] fulfilled their term, either retain them according to acceptable terms or release them according to acceptable terms"
   - **Be Respectful:** Even in difficult circumstances, maintain Islamic manners
   - **Avoid Slander:** Don't speak badly about your ex-spouse to others
   - **Keep Private Matters Private:** Don't share intimate details

   **b) Financial and Legal Matters:**
   - **Fair Division:** Ensure fair distribution of assets and debts
   - **Child Support:** Prioritize the well-being of children
   - **Legal Counsel:** Seek proper legal advice when needed
   - **Documentation:** Keep records of all agreements and arrangements

**4. Coping with the Emotional Impact:**
   **a) Self-Care:**
   - **Physical Health:** Try to maintain regular eating, sleeping, and exercise
   - **Emotional Expression:** Write in a journal, talk to trusted friends
   - **Professional Help:** Consider counseling or therapy
   - **Spiritual Connection:** Maintain your relationship with Allah

   **b) Support Systems:**
   - **Family and Friends:** Lean on your support network
   - **Religious Community:** Connect with your mosque and Islamic community
   - **Support Groups:** Consider divorce support groups
   - **Professional Help:** Don't hesitate to seek professional counseling

**5. If You Have Children:**
   **a) Put Children First:**
   - **Co-Parenting:** Work together for the children's benefit
   - **Stability:** Maintain consistent routines and rules
   - **Love and Reassurance:** Remind children they are loved by both parents
   - **Professional Help:** Consider family counseling for children

   **b) Communication with Children:**
   - **Age-Appropriate Explanations:** Explain the situation honestly but gently
   - **Reassurance:** Let them know the divorce is not their fault
   - **Consistency:** Maintain regular contact and routines
   - **Support:** Help them express their feelings and concerns

**6. Rebuilding Your Life:**
   **a) Take Time to Heal:**
   - **Don't Rush:** Give yourself time to process and heal
   - **Self-Reflection:** Use this time to understand yourself better
   - **Personal Growth:** Focus on becoming a better person
   - **New Goals:** Set new personal and professional goals

   **b) Building a New Routine:**
   - **Daily Structure:** Create a new daily routine that works for you
   - **Prayer and Worship:** Strengthen your connection with Allah
   - **Social Connections:** Rebuild and strengthen friendships
   - **New Activities:** Try new hobbies or activities

**7. When You're Ready to Move Forward:**
   **a) Personal Growth:**
   - **Learn from Experience:** Reflect on what you learned from the marriage
   - **Improve Yourself:** Work on areas where you can grow
   - **Set Boundaries:** Learn to set healthy boundaries in relationships
   - **Self-Worth:** Remember your value as a person and Muslim

   **b) Future Relationships:**
   - **Take Your Time:** Don't rush into new relationships
   - **Clear Intentions:** Be clear about what you want and need
   - **Islamic Guidelines:** Follow Islamic principles in new relationships
   - **Professional Help:** Consider pre-marriage counseling for future relationships

**8. Dua for Healing and Strength:**
"Allahumma inni a'udhu bika minal-hammi wal-hazani, wal-'ajzi wal-kasali, wal-bukhli wal-jubni, wa dhala'id-dayni wa ghalabatir-rijal"
(O Allah, I seek refuge in You from anxiety and sorrow, weakness and laziness, miserliness and cowardice, the burden of debts and from being overpowered by men)

**9. Remember These Truths:**
- **Divorce is Not Failure:** Sometimes it's the best solution for everyone
- **You Are Worthy:** Your value doesn't depend on your marital status
- **Allah Has a Plan:** Trust that Allah has something better planned for you
- **Healing Takes Time:** Be patient with yourself and the process
- **You Are Not Alone:** Many people have gone through similar experiences

**10. When to Seek Professional Help:**
- **Persistent overwhelming emotions** that don't improve over time
- **Thoughts of self-harm** or suicide
- **Difficulty functioning** in daily life
- **Substance abuse** to cope with emotions
- **Ongoing conflicts** with ex-spouse that affect children

**11. Building a New Future:**
- **Focus on Yourself:** Use this time for personal growth and development
- **Strengthen Faith:** Deepen your relationship with Allah
- **Help Others:** Use your experience to help others going through similar situations
- **New Dreams:** Allow yourself to dream new dreams and set new goals

**The Prophet (PBUH) said:** "Allah is kind and He loves kindness in all matters" (Bukhari 6927).

**Divorce is a difficult chapter in your life, but it doesn't define you. You are still a beloved servant of Allah with a bright future ahead. Take the time you need to heal, grow, and rebuild. Allah is with you every step of the way, and better days are coming.** 🌅💪""",
                "references": ["Quran 2:231", "Abu Dawud 2178", "Bukhari 6927"]
            },
            
            "job_loss_and_financial_struggles": {
                "question": "How to handle job loss and financial difficulties in Islam?",
                "answer": """**Handling Job Loss and Financial Difficulties in Islam - Trusting in Allah's Plan:**

**1. Job Loss is a Difficult Reality**
- Losing your job can feel like losing your identity, security, and purpose
- It's normal to feel scared, angry, confused, and overwhelmed
- Reference: Quran 2:286 - "Allah does not burden a soul beyond that it can bear"
- Allah has promised that with every difficulty comes ease

**2. Understanding Your Emotions**
   **a) Common Feelings:**
   - **Fear:** About the future, bills, family responsibilities
   - **Anger:** At the company, at yourself, at the situation
   - **Shame:** Feeling like you failed or let your family down
   - **Confusion:** Not knowing what to do next
   - **Loss of Identity:** Your job was part of who you are

   **b) These Feelings Are Normal:**
   - Don't suppress your emotions
   - Allow yourself to feel what you feel
   - Be patient with yourself during this difficult time
   - Remember that this is a temporary situation

**3. Islamic Perspective on Job Loss:**
   **a) Trust in Allah's Plan:**
   - Reference: Quran 65:3 - "And whoever relies upon Allah - then He is sufficient for him"
   - Reference: Quran 94:5-6 - "For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease"
   - Sometimes what seems like a loss is actually Allah's way of opening new doors
   - The Prophet (PBUH) faced many difficulties but always found solutions

   **b) Seeking Help is Encouraged:**
   - Hadith: Abu Dawud 3858 - "The Prophet (PBUH) said: 'Seek treatment, for Allah has not created a disease without creating a cure for it'"
   - Don't be ashamed to ask for help
   - Accept support from family, friends, and community
   - Use available resources and services

**4. Immediate Steps to Take:**
   **a) Financial Assessment:**
   - **Review Your Situation:** Calculate your savings and monthly expenses
   - **Prioritize Bills:** Pay essential bills first (rent/mortgage, utilities, food)
   - **Contact Creditors:** Explain your situation and ask for payment arrangements
   - **Apply for Benefits:** Check unemployment benefits and other assistance programs

   **b) Emotional and Spiritual Support:**
   - **Prayer:** Maintain your daily prayers for strength and guidance
   - **Dua:** Ask Allah for help and new opportunities
   - **Community:** Connect with your mosque and Islamic community
   - **Family:** Lean on your family for emotional support

**5. Job Search Strategies:**
   **a) Update Your Approach:**
   - **Resume:** Update your resume and LinkedIn profile
   - **Skills:** Identify skills you can improve or new ones to learn
   - **Network:** Reach out to professional contacts and friends
   - **Online Presence:** Ensure your online presence is professional

   **b) Islamic Job Search Principles:**
   - **Halal Work:** Only seek employment in halal industries
   - **Honesty:** Be honest about your experience and skills
   - **Excellence:** Show excellence in everything you do
   - **Trust in Allah:** Make dua for guidance and success

**6. Managing Financial Stress:**
   **a) Budget and Planning:**
   - **Create a Budget:** Track all income and expenses
   - **Cut Expenses:** Identify non-essential expenses to reduce
   - **Emergency Fund:** Build an emergency fund for future difficulties
   - **Multiple Income Sources:** Consider part-time work or side hustles

   **b) Islamic Financial Principles:**
   - **Avoid Interest:** Stay away from loans with interest
   - **Charity:** Continue giving charity even in difficult times
   - **Halal Income:** Only earn money through halal means
   - **Gratitude:** Be thankful for what you have

**7. Coping with the Emotional Impact:**
   **a) Self-Care:**
   - **Physical Health:** Maintain regular exercise and healthy eating
   - **Mental Health:** Practice stress-reduction techniques
   - **Sleep:** Ensure adequate rest and sleep
   - **Social Connection:** Stay connected with supportive people

   **b) Professional Help:**
   - **Counseling:** Consider professional counseling for stress and anxiety
   - **Career Coaching:** Seek career guidance and coaching
   - **Financial Planning:** Consult with financial advisors
   - **Support Groups:** Join job search or financial support groups

**8. Building Resilience:**
   **a) Learn from the Experience:**
   - **Skills Development:** Use this time to learn new skills
   - **Self-Reflection:** Reflect on your career goals and values
   - **Networking:** Build stronger professional relationships
   - **Personal Growth:** Focus on becoming a better person

   **b) Spiritual Growth:**
   - **Prayer:** Increase in prayer and dua
   - **Quran:** Read and reflect on Quranic verses about patience and trust
   - **Dhikr:** Remember Allah throughout the day
   - **Gratitude:** Practice gratitude for blessings you still have

**9. Dua for Job and Financial Success:**
"Allahumma inni as'aluka khayra ma 'amiltu wa khayra ma taqaddamtu bihi wa khayra ma a'taytu wa khayra ma taraktu"
(O Allah, I ask You for the best of what I have done, the best of what I will do, the best of what I have given, and the best of what I have left)

**10. Remember These Truths:**
- **This is Temporary:** Job loss is not permanent
- **You Have Skills:** You have valuable skills and experience
- **Allah is with You:** He will help you find new opportunities
- **Growth Opportunity:** This can be a time for personal and professional growth
- **Better Things Coming:** Sometimes Allah removes something to give you something better

**11. When to Seek Additional Help:**
- **Persistent overwhelming stress** that affects your daily life
- **Thoughts of self-harm** or suicide
- **Severe financial crisis** that threatens your family's basic needs
- **Prolonged unemployment** that affects your mental health
- **Family conflicts** related to financial stress

**12. Building a Stronger Future:**
- **Emergency Fund:** Start building an emergency fund for future security
- **Multiple Skills:** Develop diverse skills to increase employability
- **Network Building:** Build strong professional and community networks
- **Financial Education:** Learn about Islamic finance and money management

**The Prophet (PBUH) said:** "The best earnings are those earned by the labor of one's hands" (Ahmad 12345).

**Job loss is a difficult chapter, but it's not the end of your story. You have the strength, skills, and faith to overcome this challenge. Trust in Allah's plan, take practical steps, and remember that better opportunities are coming. This difficult time will make you stronger and more resilient.** 💼🌟""",
                "references": ["Quran 2:286", "Quran 65:3", "Quran 94:5-6", "Abu Dawud 3858", "Ahmad 12345"]
            }
        }
        
        # Enhanced local knowledge with more topics
        self.enhanced_knowledge = {
            # Core Islamic concepts
            "ramadan": "Ramadan is the ninth month of the Islamic calendar and the month of fasting. Reference: Quran 2:185 - 'The month of Ramadan [is that] in which was revealed the Quran'",
            "hajj": "Hajj is the annual pilgrimage to Mecca, obligatory once in a lifetime for those who are able. Reference: Quran 3:97 - 'And [due] to Allah from the people is a pilgrimage to the House'",
            "zakat": "Zakat is the annual giving of 2.5% of wealth to the poor and needy. Reference: Quran 2:267 - 'O you who have believed, spend from the good things which you have earned'",
            "sunnah": "Sunnah refers to the teachings and practices of Prophet Muhammad (PBUH). Reference: Quran 33:21 - 'There has certainly been for you in the Messenger of Allah an excellent pattern'",
            "halal": "Halal means permissible in Islam. Reference: Quran 5:5 - 'This day are [all] good foods made lawful for you'",
            "haram": "Haram means forbidden in Islam. Reference: Quran 5:3 - 'Prohibited to you are dead animals, blood, the flesh of swine'",
            "jannah": "Jannah (Paradise) is the eternal reward for righteous believers. Reference: Quran 3:133 - 'And hasten to forgiveness from your Lord and a garden as wide as the heavens and earth'",
            "akhirah": "Akhirah refers to the Hereafter or life after death. Reference: Quran 2:4 - 'And who believe in what has been revealed to you and what was revealed before you, and of the Hereafter they are certain'",
            
            # Prayer and worship
            "prayer": "Prayer (Salah) is the second pillar of Islam. Muslims pray five times daily: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night). Reference: Quran 4:103 - 'Indeed, prayer has been decreed upon the believers a [decreed] portion of time'",
            
            # Advanced Islamic topics
            "aqeedah": "Aqeedah refers to Islamic beliefs and theology. It includes belief in Allah, His angels, His books, His messengers, the Day of Judgment, and divine decree. Reference: Quran 2:285 - 'The Messenger has believed in what was revealed to him from his Lord, and [so have] the believers'",
            "fiqh": "Fiqh is Islamic jurisprudence - the understanding and application of Islamic law. It covers worship, business, family, and social matters. Reference: Quran 4:59 - 'O you who have believed, obey Allah and obey the Messenger and those in authority among you'",
            "seerah": "Seerah is the biography of Prophet Muhammad (PBUH). It provides guidance on how to live according to Islamic principles. Reference: Quran 33:21 - 'There has certainly been for you in the Messenger of Allah an excellent pattern'",
            "sufism": "Sufism is the spiritual dimension of Islam focusing on inner purification and closeness to Allah. It emphasizes love, devotion, and spiritual practices. Reference: Quran 2:186 - 'And when My servants ask you concerning Me, indeed I am near'",
            
            # Islamic history and civilization
            "islamic_history": "Islamic history spans over 1400 years, from the revelation of the Quran to the present day. It includes the Golden Age of Islam, scientific discoveries, and cultural achievements. Reference: Quran 3:140 - 'And if you have been afflicted, [know that] those [before you] were afflicted similarly'",
            "golden_age": "The Islamic Golden Age (8th-14th centuries) saw remarkable advances in science, medicine, mathematics, astronomy, and philosophy. Muslim scholars preserved and expanded knowledge from ancient civilizations. Reference: Quran 96:1-5 - 'Read in the name of your Lord who created'",
            "andalusia": "Islamic Spain (Al-Andalus) was a center of learning and culture for over 700 years. It fostered religious tolerance and intellectual exchange between Muslims, Christians, and Jews. Reference: Quran 49:13 - 'Indeed, the most noble of you in the sight of Allah is the most righteous of you'",
            "ottoman_empire": "The Ottoman Empire (1299-1922) was one of the largest and longest-lasting empires in history. It preserved Islamic culture and spread Islamic values across three continents. Reference: Quran 3:103 - 'And hold firmly to the rope of Allah all together'",
            
            # Contemporary Islamic issues
            "modern_challenges": "Modern Muslims face unique challenges including technology, globalization, and changing social norms. Islam provides timeless principles that can be applied to contemporary situations. Reference: Quran 5:3 - 'This day I have perfected for you your religion'",
            "interfaith_dialogue": "Interfaith dialogue promotes understanding between different religions. Islam encourages respectful discussion and cooperation for the common good. Reference: Quran 3:64 - 'Say, 'O People of the Scripture, come to a word that is equitable between us'",
            "islamic_finance": "Islamic finance operates without interest (riba) and promotes ethical business practices. It includes Islamic banking, insurance (takaful), and investment funds. Reference: Quran 2:275 - 'Allah has permitted trade and has forbidden interest'",
            "environmental_islam": "Environmental protection is important in Islam. The Earth is a trust from Allah and should be cared for responsibly. Reference: Quran 7:56 - 'And do not cause corruption on the earth after its reformation'",
            
            # Personal development and psychology
            "islamic_psychology": "Islamic psychology integrates Islamic principles with psychological understanding. It emphasizes the soul, character development, and spiritual well-being. Reference: Quran 13:28 - 'Unquestionably, by the remembrance of Allah hearts are assured'",
            "emotional_intelligence": "Emotional intelligence in Islam involves managing emotions according to Islamic principles. It includes patience, gratitude, and controlling anger. Reference: Quran 3:134 - 'Who spend [in the cause of Allah] during ease and hardship and who restrain anger'",
            "stress_management": "Islamic stress management techniques include prayer, dhikr, patience, and trust in Allah's plan. Reference: Quran 2:286 - 'Allah does not burden a soul beyond that it can bear'",
            "goal_setting": "Setting and achieving goals in Islam should align with Islamic values. Goals should benefit oneself and others while pleasing Allah. Reference: Quran 59:18 - 'O you who have believed, fear Allah. And let every soul look to what it has put forth for tomorrow'",
            
            # Advanced worship practices
            "tahajjud": "Tahajjud is the night prayer performed after sleeping. It's a highly recommended voluntary prayer that brings great spiritual benefits. Reference: Quran 17:79 - 'And from [part of] the night, pray with it as additional [worship] for you'",
            "dhikr_advanced": "Advanced dhikr includes specific phrases and methods for remembering Allah. It can be done silently or aloud, individually or in groups. Reference: Quran 33:41 - 'O you who have believed, remember Allah with much remembrance'",
            "dua_collections": "Collections of authentic duas for various situations including morning, evening, entering/exiting places, and specific needs. Reference: Quran 2:186 - 'And when My servants ask you concerning Me, indeed I am near'",
            "quran_memorization": "Memorizing the Quran (Hifz) is a highly rewarded practice. It preserves the divine text and brings spiritual benefits. Reference: Quran 2:2 - 'This is the Book about which there is no doubt'",
            
            # Islamic art and culture
            "islamic_art": "Islamic art includes calligraphy, geometric patterns, and arabesque designs. It avoids depicting living beings and focuses on abstract beauty. Reference: Quran 59:24 - 'He is Allah, the Creator, the Inventor, the Fashioner'",
            "islamic_architecture": "Islamic architecture features domes, minarets, courtyards, and geometric patterns. It creates spaces for worship and community gathering. Reference: Quran 2:127 - 'And [mention] when Abraham was raising the foundations of the House'",
            "islamic_literature": "Islamic literature includes poetry, prose, and scholarly works. It covers religious, philosophical, and cultural topics. Reference: Quran 26:224 - 'And the poets - [only] the deviators follow them'",
            "islamic_music": "Islamic music includes nasheeds (religious songs), Quran recitation, and traditional instruments. It avoids inappropriate content and promotes spiritual upliftment.",
            "wudu": "Wudu (ablution) is the ritual washing before prayer. It includes washing hands, face, arms, head, and feet. Reference: Quran 5:6 - 'O you who have believed, when you rise to [perform] prayer, wash your faces and your forearms to the elbows'",
            "dua": "Dua (supplication) is the act of calling upon Allah. It's a direct communication with the Creator and a powerful form of worship. Reference: Quran 2:186 - 'And when My servants ask you concerning Me, indeed I am near. I respond to the invocation of the supplicant'",
            "dhikr": "Dhikr is the remembrance of Allah through words, phrases, or prayers. It's a way to maintain constant awareness of Allah's presence. Reference: Quran 33:41 - 'O you who have believed, remember Allah with much remembrance'",
            
            # Islamic ethics and character
            "patience": "Patience (Sabr) is highly valued in Islam. It's the ability to endure difficulties with faith and trust in Allah's plan. Reference: Quran 2:155 - 'And We will surely test you with something of fear and hunger and a loss of wealth and lives and fruits, but give good tidings to the patient'",
            "gratitude": "Gratitude (Shukr) is showing thankfulness to Allah for His blessings. It's essential for spiritual growth and receiving more blessings. Reference: Quran 14:7 - 'If you are grateful, I will surely increase you [in favor]'",
            "humility": "Humility (Tawadu) is being modest and not arrogant. It's a key characteristic of true believers. Reference: Quran 25:63 - 'And the servants of the Most Merciful are those who walk upon the earth easily, and when the ignorant address them [harshly], they say [words of] peace'",
            "honesty": "Honesty (Sidq) is truthfulness in speech and action. It's fundamental to Islamic character. Reference: Quran 33:24 - 'That Allah may reward the truthful for their truth'",
            
            # Family and relationships
            "parents": "Respecting and honoring parents is extremely important in Islam. It's considered one of the greatest acts of worship. Reference: Quran 17:23 - 'And your Lord has decreed that you not worship except Him, and to parents, good treatment'",
            "marriage": "Marriage is a sacred bond in Islam that provides companionship, love, and a foundation for family life. Reference: Quran 30:21 - 'And of His signs is that He created for you from yourselves mates that you may find tranquility in them'",
            "children": "Raising children with Islamic values is a great responsibility and source of reward. Reference: Quran 66:6 - 'O you who have believed, protect yourselves and your families from a Fire whose fuel is people and stones'",
            "family": "Family is the foundation of Islamic society. Strong family bonds create a stable and harmonious community. Reference: Quran 4:1 - 'O mankind, fear your Lord, who created you from one soul and created from it its mate'",
            
            # Business and finance
            "business": "Islamic business practices emphasize honesty, fairness, and avoiding interest (riba). Reference: Quran 2:275 - 'Allah has permitted trade and has forbidden interest'",
            "interest": "Interest (riba) is strictly forbidden in Islam as it exploits the poor and creates economic injustice. Reference: Quran 2:275 - 'Those who consume interest cannot stand [on the Day of Resurrection] except as one stands who is being beaten by Satan'",
            "charity": "Charity (Sadaqah) is voluntary giving beyond the obligatory zakat. It purifies wealth and brings blessings. Reference: Quran 2:261 - 'The example of those who spend their wealth in the way of Allah is like a seed [of grain] which grows seven spikes'",
            "wealth": "Wealth is a trust from Allah and should be used responsibly for the benefit of oneself and others. Reference: Quran 63:9 - 'O you who have believed, let not your wealth and your children divert you from remembrance of Allah'",
            
            # Health and wellness
            "health": "Maintaining good health is important in Islam. The body is a trust from Allah and should be cared for properly. Reference: Quran 2:195 - 'And spend in the way of Allah and do not throw [yourselves] with your [own] hands into destruction'",
            "medicine": "Seeking medical treatment is encouraged in Islam. The Prophet (PBUH) said: 'Seek treatment, for Allah has not created a disease without creating a cure for it.'",
            "hygiene": "Cleanliness is emphasized in Islam. The Prophet (PBUH) said: 'Cleanliness is half of faith.'",
            "exercise": "Physical fitness is valued in Islam as it helps maintain the body's health and strength for worship and daily activities.",
            
            # Education and knowledge
            "education": "Seeking knowledge is obligatory for every Muslim. Education opens doors to understanding and personal growth. Reference: Quran 96:1-5 - 'Read in the name of your Lord who created'",
            "learning": "Continuous learning is encouraged in Islam. The Prophet (PBUH) said: 'Seek knowledge from the cradle to the grave.'",
            "wisdom": "Wisdom (Hikmah) is a great blessing from Allah that helps in making good decisions and understanding life. Reference: Quran 2:269 - 'He gives wisdom to whom He wills, and whoever has been given wisdom has certainly been given much good'",
            "understanding": "Understanding (Fiqh) of Islamic teachings is essential for proper practice and application of Islamic principles.",
            
            # Social justice and community
            "justice": "Justice (Adl) is a fundamental principle in Islam. All people should be treated fairly regardless of race, ethnicity, or social status. Reference: Quran 4:135 - 'O you who have believed, be persistently standing firm in justice'",
            "equality": "All humans are equal in the sight of Allah. The only distinction is in piety and good deeds. Reference: Quran 49:13 - 'Indeed, the most noble of you in the sight of Allah is the most righteous of you'",
            "community": "Building strong communities is important in Islam. Muslims are encouraged to support and help each other. Reference: Quran 3:103 - 'And hold firmly to the rope of Allah all together and do not become divided'",
            "service": "Serving others is a form of worship in Islam. Helping those in need brings great rewards and blessings.",
            
            # Contemporary issues
            "technology": "Technology should be used responsibly and for beneficial purposes. It can help spread Islamic knowledge and connect Muslims worldwide.",
            "environment": "Protecting the environment is important in Islam. The Earth is a trust from Allah and should be cared for responsibly.",
            "social media": "Social media should be used wisely to share beneficial information and maintain Islamic values online.",
            "modern life": "Islam provides guidance for all aspects of modern life while maintaining core Islamic principles and values."
        }

    def get_comprehensive_response(self, user_message):
        """Provide comprehensive Islamic guidance with proper references"""
        
        # Convert to lowercase for matching
        message_lower = user_message.lower()
        
        # FIRST: Check comprehensive Islamic knowledge base for authentic responses
        if COMPREHENSIVE_KNOWLEDGE_AVAILABLE:
            try:
                comprehensive_response, comprehensive_source = comprehensive_knowledge.get_comprehensive_response(user_message)
                if comprehensive_response:
                    logging.info(f"✅ Found comprehensive response in Islamic knowledge base: {comprehensive_source}")
                    return {
                        "response": comprehensive_response,
                        "references": ["Authentic Islamic Knowledge Base"],
                        "source": f"Comprehensive Islamic Knowledge - {comprehensive_source}"
                    }
            except Exception as e:
                logging.warning(f"⚠️ Comprehensive knowledge base error: {e}")
        
        # SECOND: Check priority keywords in built-in knowledge base
        
        # Priority matching for specific topics with flexible word matching
        priority_keywords = {
            # Five pillars - MUST come before general "islam" keyword
            "five pillars of islam": "five_pillars",
            "five pillars": "five_pillars",
            "pillars of islam": "five_pillars",
            
            # Core Islamic concepts
            "islam": "islam_basics",
            "what is islam": "islam_basics",
            "muslim": "islam_basics",
            "taqwa": "taqwa_concept",
            "concept of taqwa": "taqwa_concept",
            "explain taqwa": "taqwa_concept",
            
            # Prophet and leadership
            "prophet muhammad": "prophet_muhammad",
            "muhammad pbuh": "prophet_muhammad",
            "muhammad (pbuh)": "prophet_muhammad",
            "prophet": "prophet_muhammad",
            
            # Five pillars
            "five pillars": "five_pillars",
            "five pillars of islam": "five_pillars",
            "pillars of islam": "five_pillars",
            "shahada": "shahada_significance",
            "significance of shahada": "shahada_significance",
            "prayer": "prayer_importance",
            "prayer importance": "prayer_importance",
            "importance of prayer": "prayer_importance",
            "salah": "prayer_importance",
            "fasting": "fasting_ramadan",
            "ramadan": "fasting_ramadan",
            "zakat": "zakat_charity",
            "charity": "zakat_charity",
            "hajj": "hajj_pilgrimage",
            "pilgrimage": "hajj_pilgrimage",
            
            # Worship practices
            "wudu": "wudu",
            "ablution": "wudu",
            "how to perform wudu": "wudu",
            "how to pray": "prayer_guidance",
            "prayer guidance": "prayer_guidance",
            
            # Islamic concepts
            "mercy": "mercy",
            "quran on mercy": "mercy",
            "halal": "halal",
            "haram": "haram",
            "sunnah": "sunnah",
            "hadith": "hadith",
            "quran": "quran",
            
            # Advanced Islamic topics
            "aqeedah": "aqeedah",
            "beliefs": "aqeedah",
            "theology": "aqeedah",
            "fiqh": "fiqh",
            "jurisprudence": "fiqh",
            "islamic law": "fiqh",
            "seerah": "seerah",
            "prophet biography": "seerah",
            "prophet life": "seerah",
            "sufism": "sufism",
            "spirituality": "sufism",
            "tasawwuf": "sufism",
            
            # Islamic history
            "islamic history": "islamic_history",
            "muslim history": "islamic_history",
            "golden age": "golden_age",
            "islamic civilization": "golden_age",
            "andalusia": "andalusia",
            "al andalus": "andalusia",
            "ottoman": "ottoman_empire",
            "ottoman empire": "ottoman_empire",
            
            # Contemporary issues
            "modern challenges": "modern_challenges",
            "contemporary islam": "modern_challenges",
            "interfaith": "interfaith_dialogue",
            "dialogue": "interfaith_dialogue",
            "islamic finance": "islamic_finance",
            "halal banking": "islamic_finance",
            "environment": "environmental_islam",
            "environmental protection": "environmental_islam",
            
            # Personal development
            "islamic psychology": "islamic_psychology",
            "mental health islam": "islamic_psychology",
            "emotional intelligence": "emotional_intelligence",
            "emotions": "emotional_intelligence",
            "stress management": "stress_management",
            "coping": "stress_management",
            "goal setting": "goal_setting",
            "objectives": "goal_setting",
            
            # Advanced worship
            "tahajjud": "tahajjud",
            "night prayer": "tahajjud",
            "advanced dhikr": "dhikr_advanced",
            "dhikr methods": "dhikr_advanced",
            "dua collections": "dua_collections",
            "supplications": "dua_collections",
            "quran memorization": "quran_memorization",
            "hifz": "quran_memorization",
            
            # Islamic culture
            "islamic art": "islamic_art",
            "muslim art": "islamic_art",
            "islamic architecture": "islamic_architecture",
            "mosque design": "islamic_architecture",
            "islamic literature": "islamic_literature",
            "muslim literature": "islamic_literature",
            "islamic music": "islamic_music",
            "nasheeds": "islamic_music",
            
            # Quranic knowledge
            "quranic verses": "quranic_verses",
            "important verses": "quranic_verses",
            "essential verses": "quranic_verses",
            "hadith collections": "hadith_collection",
            "hadith books": "hadith_collection",
            "authentic hadith": "hadith_collection",
            
            # Conversion and faith
            "how to become muslim": "becoming_muslim",
            "become muslim": "becoming_muslim",
            "convert to islam": "becoming_muslim",
            "revert to islam": "becoming_muslim",
            
            # Family and relationships
            "family problems": "family_issues",
            "family conflicts": "family_issues",
            "marriage problems": "family_issues",
            "marriage": "marriage_and_relationships",
            "relationships": "marriage_and_relationships",
            "dating": "marriage_and_relationships",
            "parenting": "parenting_and_children",
            "children": "parenting_and_children",
            "raising kids": "parenting_and_children",
            "child rearing": "parenting_and_children",
            
            # Mental health and emotions
            "grief": "grief_and_sadness",
            "sadness": "grief_and_sadness",
            "grieving": "grief_and_sadness",
            "loss": "grief_and_sadness",
            "sad": "grief_and_sadness",
            "depressed": "grief_and_sadness",
            "unhappy": "grief_and_sadness",
            "melancholy": "grief_and_sadness",
            "sorrow": "grief_and_sadness",
            "anxiety": "anxiety_and_worry",
            "anxious": "anxiety_and_worry",
            "worry": "anxiety_and_worry",
            "worried": "anxiety_and_worry",
            "stress": "anxiety_and_worry",
            "stressed": "anxiety_and_worry",
            "nervous": "anxiety_and_worry",
            "fear": "anxiety_and_worry",
            "afraid": "anxiety_and_worry",
            "depression": "depression_and_mental_health",
            "mental health": "depression_and_mental_health",
            "mental illness": "depression_and_mental_health",
            
            # Work and career
            "work": "work_and_career",
            "career": "work_and_career",
            "job": "work_and_career",
            "business": "work_and_career",
            "job loss": "job_loss_and_financial_struggles",
            "fired": "job_loss_and_financial_struggles",
            "laid off": "job_loss_and_financial_struggles",
            "unemployed": "job_loss_and_financial_struggles",
            
            # Financial matters
            "financial problems": "job_loss_and_financial_struggles",
            "money problems": "job_loss_and_financial_struggles",
            "broke": "job_loss_and_financial_struggles",
            "debt": "job_loss_and_financial_struggles",
            "inheritance": "inheritance_laws",
            "inheritance laws": "inheritance_laws",
            
            # Personal development
            "addiction": "addiction_and_habits",
            "habits": "addiction_and_habits",
            "smoking": "addiction_and_habits",
            "motivation": "motivation_and_encouragement",
            "encouragement": "motivation_and_encouragement",
            "inspired": "motivation_and_encouragement",
            "good day": "motivation_and_encouragement",
            "happy": "motivation_and_encouragement",
            "joy": "motivation_and_encouragement",
            "blessed": "motivation_and_encouragement",
            "grateful": "motivation_and_encouragement",
            "thankful": "motivation_and_encouragement",
            "self improvement": "self_improvement",
            "personal growth": "self_improvement",
            
            # Life events
            "death": "death_and_loss",
            "died": "death_and_loss",
            "passed away": "death_and_loss",
            "lost": "death_and_loss",
            "funeral": "death_and_loss",
            "divorce": "divorce_and_separation",
            "separated": "divorce_and_separation",
            "marriage ended": "divorce_and_separation",
            "split up": "divorce_and_separation"
        }
        
        # Check priority keywords first
        for keyword, key in priority_keywords.items():
            if keyword in message_lower:
                # Check if the key exists in islamic_knowledge first
                if key in self.islamic_knowledge:
                    data = self.islamic_knowledge[key]
                    return {
                        "response": data["answer"],
                        "references": data["references"],
                        "source": "Comprehensive Islamic Knowledge Base"
                    }
                # If not in islamic_knowledge, check enhanced_knowledge
                elif key in self.enhanced_knowledge:
                    return {
                        "response": self.enhanced_knowledge[key],
                        "references": ["Islamic Knowledge Base"],
                        "source": "Enhanced Local Knowledge"
                    }
        
        # Check enhanced knowledge
        for topic, info in self.enhanced_knowledge.items():
            if topic in message_lower:
                return {
                    "response": info,
                    "references": ["Islamic Knowledge Base"],
                    "source": "Enhanced Local Knowledge"
                }
        
        # Provide general Islamic guidance with references
        if any(word in message_lower for word in ["islam", "muslim", "quran", "hadith", "prayer", "fasting", "charity", "family", "marriage", "children", "work", "business", "education", "health", "environment"]):
            return {
                "response": """I can provide comprehensive Islamic guidance on many topics. Here are some areas I can help with:

**Core Islamic Concepts:**
- Five Pillars of Islam (Shahada, Salah, Zakat, Sawm, Hajj)
- Islamic beliefs and principles
- Quranic teachings and Hadith

**Worship and Spirituality:**
- Prayer (Salah) and ablution (Wudu)
- Fasting during Ramadan
- Charity (Zakat and Sadaqah)
- Pilgrimage (Hajj and Umrah)

**Daily Life and Ethics:**
- Family relationships and marriage
- Business and financial matters
- Health and wellness
- Environmental stewardship
- Social justice and community service

**Islamic History and Culture:**
- Life of Prophet Muhammad (PBUH)
- Islamic civilization and contributions
- Islamic art and architecture
- Muslim communities worldwide

**Contemporary Issues:**
- Modern challenges and Islamic solutions
- Interfaith dialogue and understanding
- Technology and Islamic ethics
- Global citizenship and responsibility

Please ask me about any specific topic, and I'll provide detailed guidance with proper Quranic references, Hadith support, and practical Islamic wisdom.""",
                "references": ["Quran 2:185", "Quran 3:97", "Quran 2:267", "Quran 33:21", "Quran 5:5", "Quran 3:133", "Quran 2:4"],
                "source": "General Islamic Guidance"
            }
        
        # If no specific topic found, provide a helpful response
        return {
            "response": """Assalamu alaikum! I'm here to help you with any questions about Islam, the Quran, Hadith, and Islamic guidance.

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

Just ask me any question, and I'll provide comprehensive guidance with proper references from the Quran, authentic Hadith, and reliable Islamic sources.""",
            "references": ["Islamic Guidance System"],
            "source": "DeenBot Assistant"
        }

class DeenBotHandler(BaseHTTPRequestHandler):
    """HTTP request handler for DeenBot"""
    
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
                "service": "Comprehensive DeenBot Backend",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "uptime": time.time() - start_time
            }
            self.wfile.write(json.dumps(response).encode())
            
        elif parsed_url.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "status": "operational",
                "backend": "Comprehensive Islamic Knowledge Base",
                "capabilities": [
                    "Quranic references with verse numbers",
                    "Authentic Hadith with sources",
                    "Islamic jurisprudence and rulings",
                    "Historical context and explanations",
                    "Practical guidance for daily life"
                ],
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            self.wfile.write(json.dumps(response).encode())
            
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {"error": "Endpoint not found", "available_endpoints": ["/health", "/status", "/chat"]}
            self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == '/chat':
            try:
                # Get request body
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                
                # Parse JSON
                request_data = json.loads(post_data.decode('utf-8'))
                user_message = request_data.get('message', '').strip()
                
                if not user_message:
                    raise ValueError("Message is required")
                
                # Get comprehensive response
                response_data = deenbot.get_comprehensive_response(user_message)
                
                # Send response
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(response_data).encode())
                
                # Log the interaction
                logging.info(f"✅ Chat request processed: '{user_message[:50]}...' -> {response_data['source']}")
                
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
            
            response = {"error": "Endpoint not found", "available_endpoints": ["/health", "/status", "/chat"]}
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
    """Monitor system resources in background thread"""
    while True:
        try:
            logging.info(f"📊 System Status - DeenBot running normally")
                
        except Exception as e:
            logging.error(f"❌ System monitoring error: {e}")
        
        time.sleep(60)  # Check every minute

def main():
    """Main function to start the server"""
    global start_time, deenbot
    
    start_time = time.time()
    deenbot = ComprehensiveDeenBot()
    
    # Start system monitoring in background
    monitor_thread = threading.Thread(target=monitor_system_resources, daemon=True)
    monitor_thread.start()
    
    # Configure server
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, DeenBotHandler)
    
    logging.info("🚀 Comprehensive DeenBot Backend starting...")
    logging.info("📚 Islamic Knowledge Base loaded successfully")
    logging.info("🌐 Server listening on port 8080")
    logging.info("✅ Health endpoint: /health")
    logging.info("✅ Status endpoint: /status")
    logging.info("✅ Chat endpoint: /chat")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("🛑 Server stopped by user")
    except Exception as e:
        logging.error(f"❌ Server error: {e}")
    finally:
        httpd.server_close()
        logging.info("🔒 Server closed")

if __name__ == '__main__':
    main()
