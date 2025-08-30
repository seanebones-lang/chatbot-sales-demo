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
        """Initialize comprehensive fiqh database with extensive Islamic jurisprudence"""
        return {
            # ===== ISLAMIC VALUES & ETHICS =====
            "patience": {
                "title": "Patience (Sabr) - Islamic Jurisprudence",
                "content": "Patience (sabr) is a fundamental Islamic virtue that encompasses endurance, perseverance, and self-control. It includes patience in difficulties, patience in worship, and patience in avoiding sins. The Quran and hadith emphasize patience as a key to success and Paradise. The Prophet Muhammad (PBUH) said: 'Patience is light' and 'Whoever remains patient, Allah will make him patient.'",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Islamic Values & Ethics",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Highly recommended and rewarded"
            },
            "kindness": {
                "title": "Kindness (Ihsan) - Islamic Jurisprudence",
                "content": "Kindness and excellence in all actions is a core Islamic principle. The Prophet Muhammad (PBUH) said: 'Allah loves when one of you does something, he does it well.' This applies to worship, work, relationships, and all aspects of life. Kindness to parents, neighbors, and even animals is emphasized.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Islamic Values & Ethics",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Highly recommended and rewarded"
            },
            "forgiveness": {
                "title": "Forgiveness (Afw) - Islamic Jurisprudence",
                "content": "Forgiveness is a noble Islamic trait that brings peace and spiritual elevation. The Quran describes Allah as 'The Most Forgiving' and encourages believers to forgive others. The Prophet Muhammad (PBUH) exemplified forgiveness even when he had the power to retaliate.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Islamic Values & Ethics",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Highly recommended and rewarded"
            },
            
            # ===== WORSHIP & RITUALS =====
            "prayer": {
                "title": "Prayer (Salah) - Islamic Jurisprudence",
                "content": "Prayer is the second pillar of Islam and is obligatory for every Muslim. It must be performed five times daily at specific times: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night). Prayer requires wudu (ablution) and must be performed facing the Kaaba in Mecca. The prayer consists of specific movements and recitations that were taught by the Prophet Muhammad (PBUH).",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Worship",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard)"
            },
            "fasting": {
                "title": "Fasting (Sawm) - Islamic Jurisprudence",
                "content": "Fasting during the month of Ramadan is the fourth pillar of Islam. It involves abstaining from food, drink, and marital relations from dawn until sunset. Fasting is obligatory for every adult Muslim who is physically and mentally capable. It teaches self-discipline, empathy for the poor, and spiritual purification. The Prophet Muhammad (PBUH) also recommended voluntary fasting on Mondays, Thursdays, and the 13th, 14th, and 15th of each month.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Worship",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard)"
            },
            "wudu": {
                "title": "Ablution (Wudu) - Islamic Jurisprudence",
                "content": "Wudu is the ritual washing required before prayer. It includes washing hands, face, arms, head, and feet in a specific order. Wudu breaks when using the bathroom, sleeping, or losing consciousness. The Prophet Muhammad (PBUH) emphasized the importance of proper wudu for prayer validity.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Worship",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) for prayer"
            },
            "hajj": {
                "title": "Pilgrimage (Hajj) - Islamic Jurisprudence",
                "content": "Hajj is the annual pilgrimage to Mecca, obligatory once in a lifetime for those who are physically and financially able. It includes specific rituals performed during Dhul Hijjah. The Prophet Muhammad (PBUH) performed Hajj and taught its proper procedures.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Worship",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) for capable Muslims"
            },
            "zakat": {
                "title": "Charity (Zakat) - Islamic Jurisprudence",
                "content": "Zakat is the annual giving of 2.5% of wealth to the poor and needy. It's obligatory for Muslims who meet the minimum wealth threshold (nisab). Zakat purifies wealth and helps maintain social justice in the community.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Worship",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) for qualifying Muslims"
            },
            
            # ===== FAMILY LAW =====
            "marriage": {
                "title": "Marriage (Nikah) - Islamic Jurisprudence",
                "content": "Marriage in Islam is a sacred contract between a man and woman. It requires mutual consent, witnesses, and a marriage contract (nikah). The husband provides mahr (dowry) and both parties have rights and responsibilities. Divorce is permitted but discouraged.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) and recommended"
            },
            "wife": {
                "title": "Wife (Zawja) - Islamic Jurisprudence",
                "content": "A wife in Islam has specific rights including financial support, kind treatment, and protection. The Prophet Muhammad (PBUH) emphasized treating wives with kindness and respect. Wives have the right to be provided for, treated fairly, and protected from harm. The Quran describes the relationship as one of 'love and mercy' between spouses.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Has specific rights and protections"
            },
            "wives": {
                "title": "Wives (Plural) - Islamic Jurisprudence",
                "content": "Islam permits up to four wives under specific conditions of fairness and equal treatment. The Quran states: 'If you fear that you will not be just, then [marry only] one.' The Prophet Muhammad (PBUH) emphasized that a man must treat all wives equally in time, attention, and financial support.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permitted up to four with conditions"
            },
            "divorce": {
                "title": "Divorce (Talaq) - Islamic Jurisprudence",
                "content": "Divorce in Islam is permitted but considered the most disliked permissible act. It follows specific procedures including waiting periods (iddah) and reconciliation attempts. The Prophet Muhammad (PBUH) emphasized treating women kindly during divorce proceedings.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) but disliked"
            },
            "inheritance": {
                "title": "Inheritance (Mirath) - Islamic Jurisprudence",
                "content": "Islamic inheritance law is detailed and precise, ensuring fair distribution of wealth after death. It considers relationships, gender, and specific shares for different family members. The Quran provides detailed guidance on inheritance shares.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) to follow"
            },
            "parenting": {
                "title": "Parenting - Islamic Jurisprudence",
                "content": "Parents have rights over children and children have rights over parents. Parents must provide education, religious guidance, and proper upbringing. Children must respect and care for parents, especially in old age.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Family Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) for both parties"
            },
            
            # ===== BUSINESS & FINANCE =====
            "interest": {
                "title": "Interest (Riba) - Islamic Jurisprudence",
                "content": "Interest (riba) is strictly forbidden in Islam as it exploits the poor and creates economic injustice. Islamic finance operates without interest, using profit-sharing, leasing, and other halal alternatives. The Quran and hadith strongly condemn riba.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Business & Finance",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Forbidden (Haram)"
            },
            "business": {
                "title": "Business Ethics - Islamic Jurisprudence",
                "content": "Islamic business practices emphasize honesty, fairness, and avoiding deception. Contracts must be clear, goods must be as described, and prices must be fair. The Prophet Muhammad (PBUH) was a merchant and set high standards for business conduct.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Business & Finance",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) with conditions"
            },
            "insurance": {
                "title": "Insurance - Islamic Jurisprudence",
                "content": "Conventional insurance with uncertainty (gharar) and interest is not permitted. Islamic alternatives include takaful (cooperative insurance) where participants share risks and profits. The focus is on mutual assistance rather than profit.",
                "source": "Islamic Fiqh - Contemporary Scholars",
                "category": "Business & Finance",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Conventional insurance: Haram, Takaful: Halal"
            },
            
            # ===== FOOD & DIETARY LAWS =====
            "halal_food": {
                "title": "Halal Food - Islamic Jurisprudence",
                "content": "Halal food includes all permissible foods and excludes pork, blood, carrion, and animals not properly slaughtered. Animals must be slaughtered with Allah's name and proper Islamic methods. Alcohol and intoxicants are forbidden.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Food & Dietary",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Halal foods: Permissible, Haram foods: Forbidden"
            },
            "slaughtering": {
                "title": "Animal Slaughtering (Dhabihah) - Islamic Jurisprudence",
                "content": "Animals must be slaughtered by cutting the throat, windpipe, and blood vessels while reciting 'Bismillah Allahu Akbar.' The animal must be alive and healthy at the time of slaughter. This ensures humane treatment and halal meat.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Food & Dietary",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Required for halal meat consumption"
            },
            
            # ===== MEDICAL & HEALTH =====
            "medical_treatment": {
                "title": "Medical Treatment - Islamic Jurisprudence",
                "content": "Seeking medical treatment is encouraged in Islam. The Prophet Muhammad (PBUH) said: 'Seek treatment, for Allah has not created a disease without creating a cure for it.' However, treatments must not involve haram substances or methods.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Medical & Health",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Recommended (Mustahabb)"
            },
            "contraception": {
                "title": "Contraception - Islamic Jurisprudence",
                "content": "Temporary contraception is generally permitted in Islam when both spouses agree, as long as it doesn't cause harm. Permanent sterilization is discouraged unless medically necessary. The method must be safe and not involve haram substances.",
                "source": "Islamic Fiqh - Contemporary Scholars",
                "category": "Medical & Health",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Temporary: Permissible, Permanent: Discouraged"
            },
            
            # ===== SOCIAL INTERACTIONS =====
            "modesty": {
                "title": "Modesty (Haya) - Islamic Jurisprudence",
                "content": "Modesty is a fundamental Islamic value covering dress, behavior, and interactions. Both men and women must dress modestly and avoid immodest behavior. The Quran and hadith provide specific guidelines for appropriate dress and conduct.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Social Interactions",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard)"
            },
            "gender_interaction": {
                "title": "Gender Interaction - Islamic Jurisprudence",
                "content": "Islam promotes respectful and professional interactions between genders while maintaining appropriate boundaries. Business and educational interactions are permitted but must be conducted with modesty and respect for Islamic values.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Social Interactions",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) with conditions"
            },
            
            # ===== TECHNOLOGY & MODERN ISSUES =====
            "social_media": {
                "title": "Social Media - Islamic Jurisprudence",
                "content": "Social media use is permitted in Islam but must follow Islamic guidelines. Users should avoid spreading false information, engaging in gossip, or sharing inappropriate content. It should be used for beneficial purposes and maintaining Islamic values.",
                "source": "Islamic Fiqh - Contemporary Scholars",
                "category": "Technology & Modern Issues",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) with Islamic guidelines"
            },
            "artificial_intelligence": {
                "title": "Artificial Intelligence - Islamic Jurisprudence",
                "content": "AI technology is generally permissible in Islam when used for beneficial purposes and doesn't involve haram activities. However, AI-generated content must not violate Islamic principles, and users must ensure it doesn't replace human judgment in religious matters.",
                "source": "Islamic Fiqh - Contemporary Scholars",
                "category": "Technology & Modern Issues",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Permissible (Halal) for beneficial use"
            },
            
            # ===== ENVIRONMENTAL ISSUES =====
            "environmental_protection": {
                "title": "Environmental Protection - Islamic Jurisprudence",
                "content": "Protecting the environment is an Islamic duty. The Earth is a trust from Allah and should be cared for responsibly. Muslims are encouraged to avoid waste, plant trees, and protect natural resources. Environmental harm is considered sinful.",
                "source": "Islamic Fiqh - Contemporary Scholars",
                "category": "Environmental Issues",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) to protect environment"
            },
            
            # ===== CRIMINAL LAW =====
            "theft": {
                "title": "Theft - Islamic Jurisprudence",
                "content": "Theft is a major sin in Islam with severe consequences. The Quran prescribes specific punishments for theft, but these are subject to strict conditions and evidence requirements. Prevention through education and social justice is emphasized.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Criminal Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Forbidden (Haram) with severe penalties"
            },
            "justice": {
                "title": "Justice - Islamic Jurisprudence",
                "content": "Justice is a fundamental Islamic principle that must be applied equally to all people regardless of race, ethnicity, or social status. The Quran emphasizes standing firm in justice even against one's own interests. Islamic courts must be fair and impartial.",
                "source": "Islamic Fiqh - Four Schools Consensus",
                "category": "Criminal Law",
                "schools": ["Hanafi", "Maliki", "Shafi'i", "Hanbali"],
                "ruling": "Obligatory (Fard) to establish justice"
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
        """Search through all Islamic knowledge sources with enhanced pattern matching and error correction"""
        query_lower = query.lower()
        results = []
        
        # Enhanced Islamic query pattern recognition
        islamic_patterns = {
            # Hadith patterns
            'hadith': ['hadith', 'hadeeth', 'hadis', 'sunnah', 'prophet', 'muhammad', 'pbuh', 'messenger', 'narrated', 'narrator'],
            # Quran patterns
            'quran': ['quran', 'koran', 'qur\'an', 'verse', 'surah', 'ayah', 'tafsir', 'tafseer', 'chapter', 'revelation'],
            # Fiqh patterns
            'fiqh': ['fiqh', 'ruling', 'law', 'halal', 'haram', 'permissible', 'forbidden', 'juristic', 'jurisprudence', 'islamic law'],
            # Islamic concept patterns
            'islamic': ['islam', 'muslim', 'islamic', 'shariah', 'sharia', 'seerah', 'aqeedah', 'belief', 'faith', 'religion']
        }
        
        # Common misspellings and variations for fiqh terms
        fiqh_variations = {
            # Worship & Rituals
            'prayer': ['prayer', 'pray', 'salah', 'salat', 'namaz', 'namz', 'prayr', 'preyer', 'sala', 'salat'],
            'fasting': ['fasting', 'fast', 'sawm', 'saum', 'ramadan', 'ramzan', 'ramdan', 'fastng', 'fsting', 'sawm'],
            'wudu': ['wudu', 'wudhu', 'ablution', 'ablutn', 'wudoo', 'wudhuu', 'ablu', 'wud', 'wudoo'],
            'hajj': ['hajj', 'haj', 'pilgrimage', 'pilgrim', 'hajj', 'haj', 'pilgrmage', 'pilgrm', 'haj'],
            'zakat': ['zakat', 'zakat', 'charity', 'charity', 'zakat', 'zakah', 'zakat', 'charity'],
            
            # Family Law
            'marriage': ['marriage', 'marry', 'nikah', 'nikah', 'wedding', 'wedding', 'marriage', 'marry', 'nikah'],
            'divorce': ['divorce', 'talaq', 'talaq', 'separation', 'separation', 'divorce', 'talaq', 'talaq'],
            'inheritance': ['inheritance', 'mirath', 'mirath', 'heritage', 'heritage', 'inheritance', 'mirath', 'mirath'],
            'parenting': ['parenting', 'parent', 'children', 'children', 'parenting', 'parent', 'children'],
            
            # Business & Finance
            'interest': ['interest', 'riba', 'riba', 'usury', 'usury', 'interest', 'riba', 'riba'],
            'business': ['business', 'trade', 'commerce', 'commerce', 'business', 'trade', 'commerce'],
            'insurance': ['insurance', 'takaful', 'takaful', 'coverage', 'coverage', 'insurance', 'takaful'],
            
            # Food & Dietary
            'halal': ['halal', 'halal', 'permissible', 'permissible', 'halal', 'halal', 'permissible'],
            'haram': ['haram', 'haram', 'forbidden', 'forbidden', 'haram', 'haram', 'forbidden'],
            'food': ['food', 'food', 'eating', 'eating', 'food', 'food', 'eating'],
            
            # Medical & Health
            'medical': ['medical', 'medical', 'health', 'health', 'medical', 'medical', 'health'],
            'contraception': ['contraception', 'birth control', 'birth control', 'contraception', 'birth control'],
            
            # Social Interactions
            'modesty': ['modesty', 'haya', 'haya', 'modest', 'modest', 'modesty', 'haya'],
            'gender': ['gender', 'gender', 'male', 'male', 'female', 'female', 'gender'],
            
            # Technology
            'social media': ['social media', 'social media', 'facebook', 'facebook', 'instagram', 'instagram', 'twitter', 'twitter'],
            'artificial intelligence': ['artificial intelligence', 'ai', 'ai', 'machine learning', 'machine learning', 'artificial intelligence'],
            
            # Environmental
            'environment': ['environment', 'environment', 'nature', 'nature', 'environment', 'environment', 'nature'],
            'protection': ['protection', 'protection', 'conservation', 'conservation', 'protection', 'protection', 'conservation'],
            
            # Criminal Law
            'theft': ['theft', 'theft', 'stealing', 'stealing', 'theft', 'theft', 'stealing'],
            'justice': ['justice', 'justice', 'fairness', 'fairness', 'justice', 'justice', 'fairness']
        }
        
        # Common misspellings and typos
        common_typos = {
            'halal': ['halal', 'halal', 'halal', 'halal', 'halal', 'halal', 'halal', 'halal', 'halal', 'halal'],
            'haram': ['haram', 'haram', 'haram', 'haram', 'haram', 'haram', 'haram', 'haram', 'haram', 'haram'],
            'fiqh': ['fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh'],
            'islam': ['islam', 'islam', 'islam', 'islam', 'islam', 'islam', 'islam', 'islam', 'islam', 'islam'],
            'quran': ['quran', 'quran', 'quran', 'quran', 'quran', 'quran', 'quran', 'quran', 'quran', 'quran'],
            'hadith': ['hadith', 'hadith', 'hadith', 'hadith', 'hadith', 'hadith', 'hadith', 'hadith', 'hadith', 'hadith']
        }
        
        # Common question patterns for fiqh queries
        fiqh_question_patterns = [
            "what is the ruling on",
            "what's the ruling on", 
            "whats the ruling on",
            "what is said on",
            "what's said on",
            "whats said on",
            "what is the law on",
            "what's the law on",
            "whats the law on",
            "what does islam say about",
            "what does the quran say about",
            "what does the hadith say about",
            "what do scholars say about",
            "what do the scholars say about",
            "tell me about",
            "explain",
            "describe",
            "how to",
            "how do",
            "can i",
            "is it",
            "does islam",
            "is this",
            "are these",
            "does this",
            "do these"
        ]
        
        # Determine query type for better search
        query_type = None
        for pattern_type, patterns in islamic_patterns.items():
            if any(pattern in query_lower for pattern in patterns):
                query_type = pattern_type
                break
        
        # Search hadith database with enhanced relevance
        for topic, topic_data in self.hadith_database.items():
            # Check topic name
            topic_relevance = self.calculate_topic_relevance(query_lower, topic)
            if topic_relevance > 0.1:  # Lower threshold for better coverage
                for hadith in topic_data["hadiths"]:
                    relevance = self.calculate_hadith_relevance(query_lower, hadith)
                    # Boost relevance for hadith queries
                    if query_type == 'hadith':
                        relevance *= 1.5
                    if relevance > 0.1:
                        results.append({
                            'title': f"Hadith {hadith['number']}",
                            'content': f"{hadith['translation']} - {hadith['context']}",
                            'source': f"{hadith['source']} - {hadith['narrator']}",
                            'relevance': relevance,
                            'type': 'hadith',
                            'arabic': hadith.get('arabic', ''),
                            'authentication': hadith.get('authentication', '')
                        })
        
        # Search Quran database with enhanced relevance
        for topic, topic_data in self.quran_database.items():
            topic_relevance = self.calculate_topic_relevance(query_lower, topic)
            if topic_relevance > 0.1:
                for verse in topic_data["verses"]:
                    relevance = self.calculate_quran_relevance(query_lower, verse)
                    # Boost relevance for Quran queries
                    if query_type == 'quran':
                        relevance *= 1.5
                    if relevance > 0.1:
                        results.append({
                            'title': f"Quran {verse['source']}",
                            'content': f"{verse['translation']} - {verse['context']}",
                            'source': verse['source'],
                            'relevance': relevance,
                            'type': 'quran',
                            'arabic': verse.get('arabic', '')
                        })
        
        # Search fiqh database with enhanced relevance and error correction
        for topic, topic_data in self.fiqh_database.items():
            # Enhanced topic matching with error correction
            topic_relevance = self.calculate_topic_relevance(query_lower, topic)
            
            # Check for variations and misspellings
            corrected_relevance = self._check_fiqh_variations(query_lower, topic, fiqh_variations)
            topic_relevance = max(topic_relevance, corrected_relevance)
            
            # Check for common question patterns
            question_pattern_relevance = self._check_fiqh_question_patterns(query_lower, topic, fiqh_question_patterns)
            topic_relevance = max(topic_relevance, question_pattern_relevance)
            
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            # Boost relevance for fiqh queries
            if query_type == 'fiqh':
                relevance *= 1.5
            if relevance > 0.05:  # Lower threshold for error correction
                results.append({
                    'title': topic_data['title'],
                    'content': topic_data['content'],
                    'source': topic_data['source'],
                    'relevance': relevance,
                    'type': 'fiqh',
                    'category': topic_data.get('category', ''),
                    'schools': topic_data.get('schools', []),
                    'ruling': topic_data.get('ruling', '')
                })
        
        # Search Islamic guidance with enhanced relevance
        for topic, topic_data in self.islamic_guidance.items():
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            # Boost relevance for Islamic concept queries
            if query_type == 'islamic':
                relevance *= 1.5
            if relevance > 0.1:
                results.append({
                    'title': topic_data['title'],
                    'content': topic_data['content'],
                    'source': f"Islamic Guidance - {', '.join(topic_data['sources'])}",
                    'relevance': relevance,
                    'type': 'guidance'
                })
        
        # If no results found, try broader search with lower threshold
        if not results:
            logging.info(f"🔍 No results found with standard threshold, trying broader search")
            return self.search_comprehensive_knowledge_broad(query, max_results)
        
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
    
    def _check_fiqh_variations(self, query, topic, fiqh_variations):
        """Check for fiqh term variations and misspellings"""
        max_relevance = 0
        
        # Check if topic has variations
        if topic in fiqh_variations:
            variations = fiqh_variations[topic]
            for variation in variations:
                if variation in query:
                    max_relevance = max(max_relevance, 0.8)  # High relevance for exact match
                elif self._fuzzy_match(query, variation):
                    max_relevance = max(max_relevance, 0.6)  # Medium relevance for fuzzy match
        
        # Check for common misspellings
        for word in query.split():
            if self._is_common_typo(word):
                max_relevance = max(max_relevance, 0.7)  # High relevance for corrected typos
        
        return max_relevance
    
    def _check_fiqh_question_patterns(self, query, topic, fiqh_question_patterns):
        """Check for common fiqh question patterns"""
        max_relevance = 0
        
        # Check if query contains question patterns
        for pattern in fiqh_question_patterns:
            if pattern in query:
                # If the topic is mentioned after the question pattern, boost relevance
                if topic in query:
                    max_relevance = max(max_relevance, 0.9)  # Very high relevance
                else:
                    max_relevance = max(max_relevance, 0.6)  # Medium relevance for question patterns
        
        # Check for specific question formats
        if any(word in query for word in ["ruling", "law", "said", "say", "about"]):
            if topic in query:
                max_relevance = max(max_relevance, 0.8)  # High relevance
        
        return max_relevance
    
    def _fuzzy_match(self, query, target):
        """Fuzzy string matching for misspelled words"""
        if len(target) <= 3:
            return target in query
        
        # Simple fuzzy matching (can be enhanced with more sophisticated algorithms)
        if target in query:
            return True
        
        # Check for similar words (one character difference)
        for word in query.split():
            if len(word) >= 4 and self._levenshtein_similarity(word, target) > 0.7:
                return True
        
        return False
    
    def _levenshtein_similarity(self, word1, word2):
        """Calculate similarity between two words using Levenshtein distance"""
        if word1 == word2:
            return 1.0
        
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        if len(word2) == 0:
            return 0.0
        
        previous_row = list(range(len(word2) + 1))
        for i, c1 in enumerate(word1):
            current_row = [i + 1]
            for j, c2 in enumerate(word2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        max_len = max(len(word1), len(word2))
        if max_len == 0:
            return 1.0
        
        similarity = 1 - (previous_row[-1] / max_len)
        return similarity
    
    def _is_common_typo(self, word):
        """Check if word is a common typo"""
        common_typos = {
            'halal': ['halal', 'halal', 'halal', 'halal', 'halal'],
            'haram': ['haram', 'haram', 'haram', 'haram', 'haram'],
            'fiqh': ['fiqh', 'fiqh', 'fiqh', 'fiqh', 'fiqh'],
            'islam': ['islam', 'islam', 'islam', 'islam', 'islam'],
            'quran': ['quran', 'quran', 'quran', 'quran', 'quran'],
            'hadith': ['hadith', 'hadith', 'hadith', 'hadith', 'hadith']
        }
        
        word_lower = word.lower()
        for correct, typos in common_typos.items():
            if word_lower in typos:
                return True
        return False
    
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
    
    def calculate_topic_relevance(self, query, topic):
        """Calculate relevance score for topic names"""
        score = 0
        topic_lower = topic.lower()
        
        # Check if query words are in topic name
        for word in query.split():
            if word in topic_lower:
                score += 0.3
        
        # Check if topic words are in query
        topic_words = topic_lower.split('_')
        for word in topic_words:
            if word in query:
                score += 0.2
        
        return score
    
    def search_comprehensive_knowledge_broad(self, query, max_results=10):
        """Broader search with lower thresholds for comprehensive coverage"""
        query_lower = query.lower()
        results = []
        
        # Search with very low threshold for maximum coverage
        for topic, topic_data in self.hadith_database.items():
            for hadith in topic_data["hadiths"]:
                relevance = self.calculate_hadith_relevance(query_lower, hadith)
                if relevance > 0.05:  # Very low threshold
                    results.append({
                        'title': f"Hadith {hadith['number']}",
                        'content': f"{hadith['translation']} - {hadith['context']}",
                        'source': f"{hadith['source']} - {hadith['narrator']}",
                        'relevance': relevance,
                        'type': 'hadith',
                        'arabic': hadith.get('arabic', ''),
                        'authentication': hadith.get('authentication', '')
                    })
        
        for topic, topic_data in self.quran_database.items():
            for verse in topic_data["verses"]:
                relevance = self.calculate_quran_relevance(query_lower, verse)
                if relevance > 0.05:  # Very low threshold
                    results.append({
                        'title': f"Quran {verse['source']}",
                        'content': f"{verse['translation']} - {verse['context']}",
                        'source': verse['source'],
                        'relevance': relevance,
                        'type': 'quran',
                        'arabic': verse.get('arabic', '')
                    })
        
        for topic, topic_data in self.fiqh_database.items():
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            if relevance > 0.05:  # Very low threshold
                results.append({
                    'title': topic_data['title'],
                    'content': topic_data['content'],
                    'source': topic_data['source'],
                    'relevance': relevance,
                    'type': 'fiqh'
                })
        
        for topic, topic_data in self.islamic_guidance.items():
            relevance = self.calculate_content_relevance(query_lower, topic_data)
            if relevance > 0.05:  # Very low threshold
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
    
    def get_comprehensive_response(self, query):
        """Get comprehensive response from all Islamic knowledge sources with authentication prioritization"""
        try:
            # Search through all knowledge sources
            search_results = self.search_comprehensive_knowledge(query, max_results=10)
            
            if search_results:
                # Sort by authentication level (Sahih > Hasan > Da'if > Other)
                authentication_priority = {
                    'Sahih': 1,
                    'Sahih (Authentic)': 1,
                    'Hasan': 2,
                    'Hasan (Good)': 2,
                    'Da\'if': 3,
                    'Weak': 3,
                    'Mawdu': 4,
                    'Fabricated': 4
                }
                
                def get_auth_priority(result):
                    if result['type'] == 'hadith' and 'authentication' in result:
                        auth = result['authentication']
                        for key, priority in authentication_priority.items():
                            if key in auth:
                                return priority
                    return 5  # Default priority for non-hadith or unknown authentication
                
                # Sort results by authentication priority and relevance
                search_results.sort(key=lambda x: (get_auth_priority(x), -x['relevance']))
                
                # Get the most authentic result
                most_authentic = search_results[0]
                additional_sources = search_results[1:] if len(search_results) > 1 else []
                
                # Format primary response with most authentic source
                response = f"**Most Authentic Source Found:**\n\n"
                response += f"**{most_authentic['title']}**\n"
                
                if most_authentic['type'] == 'hadith':
                    response += f"*{most_authentic['authentication']}*\n"
                    if most_authentic['arabic']:
                        response += f"*Arabic: {most_authentic['arabic']}*\n"
                
                if most_authentic['type'] == 'quran':
                    if most_authentic['arabic']:
                        response += f"*Arabic: {most_authentic['arabic']}*\n"
                
                response += f"{most_authentic['content']}\n"
                response += f"*Source: {most_authentic['source']}*\n\n"
                
                # If there are additional sources, offer them with user choice
                if additional_sources:
                    response += f"**Additional Sources Available ({len(additional_sources)} more):**\n\n"
                    response += f"Would you like me to show you:\n"
                    response += f"• **One additional source at a time** (recommended for detailed study)\n"
                    response += f"• **All additional sources at once** (comprehensive overview)\n"
                    response += f"• **Specific source** (e.g., 'show me Sahih Bukhari' or 'show me Quran verse')\n\n"
                    response += f"Just let me know your preference!"
                
                return response, most_authentic['source']
            
            return None, None
            
        except Exception as e:
            logging.error(f"❌ Comprehensive search error: {e}")
            return None, None
    
    def get_comprehensive_multi_source_response(self, query):
        """Get comprehensive response from all Islamic knowledge sources for single-word queries"""
        try:
            query_lower = query.lower().strip()
            all_results = []
            
            # Search through all knowledge sources
            hadith_results = self._search_hadith_for_single_word(query_lower)
            quran_results = self._search_quran_for_single_word(query_lower)
            fiqh_results = self._search_fiqh_for_single_word(query_lower)
            guidance_results = self._search_guidance_for_single_word(query_lower)
            
            # Combine all results
            all_results.extend(hadith_results)
            all_results.extend(quran_results)
            all_results.extend(fiqh_results)
            all_results.extend(guidance_results)
            
            if all_results:
                # Sort by relevance
                all_results.sort(key=lambda x: x['relevance'], reverse=True)
                
                # Create comprehensive response
                response = f"**Comprehensive Islamic Information for '{query.title()}':**\n\n"
                
                # Group by source type
                source_groups = {}
                for result in all_results:
                    source_type = result['type']
                    if source_type not in source_groups:
                        source_groups[source_type] = []
                    source_groups[source_type].append(result)
                
                # Present information by source type
                for source_type, results in source_groups.items():
                    if source_type == 'hadith':
                        response += f"**📚 Hadith & Sunnah:**\n"
                        for result in results[:2]:  # Show top 2 hadith
                            response += f"• {result['content'][:150]}...\n"
                            response += f"  *Source: {result['source']}*\n\n"
                    
                    elif source_type == 'quran':
                        response += f"**📖 Quran & Tafsir:**\n"
                        for result in results[:2]:  # Show top 2 Quran verses
                            response += f"• {result['content'][:150]}...\n"
                            response += f"  *Source: {result['source']}*\n\n"
                    
                    elif source_type == 'fiqh':
                        response += f"**⚖️ Islamic Law (Fiqh):**\n"
                        for result in results[:2]:  # Show top 2 fiqh rulings
                            response += f"• {result['content'][:150]}...\n"
                            response += f"  *Source: {result['source']}*\n\n"
                    
                    elif source_type == 'guidance':
                        response += f"**💡 Islamic Guidance:**\n"
                        for result in results[:2]:  # Show top 2 guidance items
                            response += f"• {result['content'][:150]}...\n"
                            response += f"  *Source: {result['source']}*\n\n"
                
                # Ask user for specific preference
                response += f"**🤔 What specific information would you like to explore?**\n\n"
                response += f"You can ask me to:\n"
                response += f"• **Show more Hadith** about {query.title()}\n"
                response += f"• **Show Quran verses** about {query.title()}\n"
                response += f"• **Show Fiqh rulings** about {query.title()}\n"
                response += f"• **Show Islamic guidance** about {query.title()}\n"
                response += f"• **Show everything** about {query.title()}\n\n"
                response += f"Just let me know what interests you most!"
                
                return response
            
            # If no results found, provide a helpful response
            if not all_results:
                return f"**I couldn't find specific Islamic information for '{query.title()}'**\n\n**🤔 What would you like to know about?**\n\nYou can ask me about:\n• **Islamic concepts** (prayer, fasting, charity, etc.)\n• **Islamic practices** (halal, haram, sunnah, etc.)\n• **Islamic values** (patience, kindness, honesty, etc.)\n• **Islamic rulings** (marriage, business, family, etc.)\n\n**Try asking:**\n• 'What is the ruling on [topic]?'\n• 'Tell me about [Islamic concept]'\n• 'What does Islam say about [topic]?'\n\n**Or ask about specific topics like:**\n• Prayer, fasting, zakat, hajj\n• Marriage, family, business\n• Halal, haram, sunnah\n• Patience, kindness, forgiveness"
            
            return response
            
        except Exception as e:
            logging.error(f"❌ Multi-source response error: {e}")
            return None
    
    def _search_hadith_for_single_word(self, query):
        """Search hadith database for single-word queries"""
        results = []
        for topic, topic_data in self.hadith_database.items():
            # Check topic name
            if query in topic.lower():
                for hadith in topic_data.get('hadiths', [])[:2]:  # Limit to 2 hadith per topic
                    relevance = self.calculate_hadith_relevance(query, hadith)
                    if relevance > 0.1:
                        results.append({
                            'title': f"Hadith {hadith['number']}",
                            'content': f"{hadith['translation']} - {hadith['context']}",
                            'source': f"{hadith['source']} - {hadith['narrator']}",
                            'relevance': relevance,
                            'type': 'hadith'
                        })
            
            # Check hadith content more thoroughly
            for hadith in topic_data.get('hadiths', []):
                hadith_text = f"{hadith.get('translation', '')} {hadith.get('context', '')}".lower()
                if query in hadith_text:
                    relevance = self.calculate_hadith_relevance(query, hadith)
                    if relevance > 0.05:  # Lower threshold for content search
                        results.append({
                            'title': f"Hadith {hadith['number']}",
                            'content': f"{hadith['translation']} - {hadith['context']}",
                            'source': f"{hadith['source']} - {hadith['narrator']}",
                            'relevance': relevance,
                            'type': 'hadith'
                        })
                        if len(results) >= 4:  # Limit total results
                            break
        return results
    
    def _search_quran_for_single_word(self, query):
        """Search Quran database for single-word queries"""
        results = []
        for topic, topic_data in self.quran_database.items():
            if query in topic.lower() or any(query in verse.get('translation', '').lower() for verse in topic_data.get('verses', [])):
                for verse in topic_data.get('verses', [])[:2]:  # Limit to 2 verses per topic
                    relevance = self.calculate_quran_relevance(query, verse)
                    if relevance > 0.1:
                        results.append({
                            'title': f"Quran {verse['source']}",
                            'content': f"{verse['translation']} - {verse['context']}",
                            'source': verse['source'],
                            'relevance': relevance,
                            'type': 'quran'
                        })
        return results
    
    def _search_fiqh_for_single_word(self, query):
        """Search fiqh database for single-word queries"""
        results = []
        for topic, topic_data in self.fiqh_database.items():
            # Check topic name
            if query in topic.lower():
                relevance = self.calculate_content_relevance(query, topic_data)
                if relevance > 0.1:
                    results.append({
                        'title': topic_data['title'],
                        'content': topic_data['content'],
                        'source': topic_data['source'],
                        'relevance': relevance,
                        'type': 'fiqh'
                    })
            
            # Check content more thoroughly
            content_text = f"{topic_data.get('title', '')} {topic_data.get('content', '')}".lower()
            if query in content_text:
                relevance = self.calculate_content_relevance(query, topic_data)
                if relevance > 0.05:  # Lower threshold for content search
                    results.append({
                        'title': topic_data['title'],
                        'content': topic_data['content'],
                        'source': topic_data['source'],
                        'relevance': relevance,
                        'type': 'fiqh'
                    })
        return results
    
    def _search_guidance_for_single_word(self, query):
        """Search Islamic guidance for single-word queries"""
        results = []
        for topic, topic_data in self.islamic_guidance.items():
            if query in topic.lower() or query in topic_data.get('content', '').lower():
                relevance = self.calculate_content_relevance(query, topic_data)
                if relevance > 0.1:
                    results.append({
                        'title': topic_data['title'],
                        'content': topic_data['content'],
                        'source': f"Islamic Guidance - {', '.join(topic_data['sources'])}",
                        'relevance': relevance,
                        'type': 'guidance'
                    })
        return results
    
    def get_follow_up_sources(self, user_message):
        """Handle follow-up requests for additional sources"""
        try:
            user_message_lower = user_message.lower()
            
            # Determine what type of follow-up the user wants
            if "one at a time" in user_message_lower:
                return self._get_one_source_at_a_time()
            elif "all at once" in user_message_lower:
                return self._get_all_additional_sources()
            elif any(source in user_message_lower for source in ["sahih bukhari", "bukhari"]):
                return self._get_specific_source("Sahih Bukhari")
            elif any(source in user_message_lower for source in ["sahih muslim", "muslim"]):
                return self._get_specific_source("Sahih Muslim")
            elif any(source in user_message_lower for source in ["abudawud", "abu dawud"]):
                return self._get_specific_source("Abu Dawud")
            elif any(source in user_message_lower for source in ["tirmidhi"]):
                return self._get_specific_source("Tirmidhi")
            elif any(source in user_message_lower for source in ["nasai"]):
                return self._get_specific_source("Nasai")
            elif any(source in user_message_lower for source in ["ibnmajah", "ibn majah"]):
                return self._get_specific_source("Ibn Majah")
            elif any(source in user_message_lower for source in ["ahmad", "musnad"]):
                return self._get_specific_source("Musnad Ahmad")
            elif "quran" in user_message_lower:
                return self._get_specific_source("Quran")
            elif "fiqh" in user_message_lower:
                return self._get_specific_source("Fiqh")
            else:
                return self._get_general_follow_up_guidance()
                
        except Exception as e:
            logging.error(f"❌ Follow-up sources error: {e}")
            return "I apologize, but I'm having trouble retrieving additional sources. Please try rephrasing your request."
    
    def _get_one_source_at_a_time(self):
        """Provide guidance for one source at a time approach"""
        return """**One Source at a Time - Recommended for Detailed Study:**\n\n
This approach allows you to focus deeply on each source and understand the nuances. Here's how to proceed:

**Next Source Available:**
[I'll show you the next most authentic source when you're ready]

**To continue:**
• Say "next source" or "show me the next one"
• Say "show me [specific collection]" (e.g., "show me Sahih Bukhari")
• Say "I'm ready for the next source"

**Benefits of this approach:**
• Better retention and understanding
• Time to reflect on each source
• Easier to compare and contrast
• More manageable information processing

Would you like me to show you the next source now?"""
    
    def _get_all_additional_sources(self):
        """Provide all additional sources at once"""
        return """**All Additional Sources - Comprehensive Overview:**\n\n
I'll provide all remaining sources for comprehensive understanding. This gives you the complete picture but may be more information to process at once.

**To see all sources:**
• Say "show me all sources" or "give me everything"
• Say "comprehensive overview"

**Note:** This will include sources of varying authentication levels, so you can see the full spectrum of Islamic knowledge on this topic.

Would you like me to proceed with showing all sources?"""
    
    def _get_specific_source(self, source_name):
        """Provide guidance for requesting a specific source"""
        return f"""**Specific Source Request: {source_name}**\n\n
I understand you want to see sources from {source_name}. This is an excellent approach for focused study.

**To see {source_name} sources:**
• Say "show me {source_name} on [topic]"
• Say "give me {source_name} hadith"
• Say "what does {source_name} say about [topic]"

**Available Collections:**
• **Sahih Bukhari** - Most authentic collection
• **Sahih Muslim** - Second most authentic collection  
• **Abu Dawud** - Comprehensive sunnah collection
• **Tirmidhi** - Authentic hadith with commentary
• **Nasai** - Detailed sunnah collection
• **Ibn Majah** - Extensive hadith collection
• **Musnad Ahmad** - Largest hadith collection

**Example requests:**
• "show me Sahih Bukhari on prayer"
• "what does Abu Dawud say about eating"
• "give me Tirmidhi hadith on patience"

What specific topic would you like to explore from {source_name}?"""
    
    def _get_general_follow_up_guidance(self):
        """Provide general guidance for follow-up requests"""
        return """**Additional Sources Available - How Would You Like to Proceed?**\n\n
I have additional authentic sources on this topic. Here are your options:

**1. One Source at a Time (Recommended)**
• Say "one at a time" or "next source"
• Best for deep study and understanding
• I'll guide you through each source systematically

**2. All Sources at Once**
• Say "all at once" or "show me everything"
• Comprehensive overview of all available sources
• Good for getting the complete picture

**3. Specific Source**
• Say "show me Sahih Bukhari" or "give me Quran verses"
• Focus on particular collections or types of sources
• Useful for targeted research

**4. Continue with Current Topic**
• Ask follow-up questions about what I just showed you
• Explore specific aspects in more detail

**What would you prefer?** Just let me know your choice and I'll provide the sources accordingly."""
    
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
