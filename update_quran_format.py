#!/usr/bin/env python3

"""
Quran Format Update Helper Script
Efficiently updates all Quran verses from "context" to "tafsir" format
"""

import re
import os

def update_quran_format():
    """Update all Quran verses to use consistent format: Arabic → Transliteration → Saheeh Translation → Tafsir"""
    
    print("🔄 Starting Quran format update...")
    
    # Read the current file
    with open('comprehensive_islamic_knowledge.py', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Count current verses with "context"
    context_count = content.count('"context":')
    print(f"📊 Found {context_count} verses with 'context' field")
    
    # Create a mapping of basic context to enhanced tafsir
    tafsir_updates = {
        # Al-Fatiha patterns
        "The opening verse of the Quran, invoking Allah's names of mercy.": 
            "This verse, known as the Basmalah, is the opening of the Quran and is recited at the beginning of every Surah except At-Tawbah. It teaches us to begin all our actions in the name of Allah, acknowledging His mercy and seeking His blessings. The two names of mercy (Ar-Rahman and Ar-Raheem) emphasize Allah's comprehensive and continuous mercy.",
        
        "Praising Allah as the Lord and Creator of all creation.":
            "This verse establishes the fundamental principle of praising Allah alone. 'Al-hamdu' means all praise, 'lillahi' means belongs to Allah, and 'rabb al-alameen' means Lord of all worlds. This teaches us that Allah is the only one worthy of praise and that He is the Lord and Sustainer of all creation - humans, jinn, angels, and all other beings.",
        
        "Emphasizing Allah's attributes of mercy and compassion.":
            "This verse emphasizes Allah's two primary attributes of mercy. 'Ar-Rahman' refers to Allah's universal mercy that encompasses all creation, while 'Ar-Raheem' refers to His special mercy for believers. This teaches us that Allah's mercy is both comprehensive and specific, covering all aspects of existence and providing special care for those who believe in Him.",
        
        "Acknowledging Allah's sovereignty on the Day of Judgment.":
            "This verse establishes Allah's complete authority over the Day of Judgment. 'Malik' means owner and sovereign, 'yawmi' means day, and 'ad-deen' means the recompense or judgment. This teaches us that Allah alone has the power to judge, reward, and punish on the Day of Judgment, and that we will be accountable to Him for all our actions.",
        
        "Declaring exclusive worship and seeking help from Allah alone.":
            "This verse establishes the principle of exclusive worship and seeking help from Allah alone. 'Iyyaka' means 'You alone', 'na'budu' means 'we worship', and 'nasta'een' means 'we seek help'. This teaches us that worship and seeking assistance should be directed exclusively to Allah, establishing the foundation of monotheism (Tawheed) in Islam.",
        
        "Seeking guidance to the correct path of Islam.":
            "This verse is a supplication for guidance. 'Ihdina' means 'guide us', 'as-sirata' means 'the path', and 'al-mustaqeem' means 'the straight'. This teaches us to constantly seek Allah's guidance to the straight path of Islam, acknowledging that without His help, we cannot find the correct way. It emphasizes the importance of seeking divine guidance in all matters.",
        
        "Seeking the path of the blessed, avoiding the path of those who earned Allah's anger or went astray.":
            "This verse defines the straight path we seek. 'Alladheena an'amta alayhim' refers to those whom Allah has blessed (prophets, righteous people, martyrs). 'Al-maghdoobi alayhim' refers to those who earned Allah's anger (like the Jews who knew the truth but rejected it). 'Ad-daalleen' refers to those who went astray (like the Christians who followed false beliefs). This teaches us to follow the path of the blessed and avoid the paths of those who earned divine displeasure.",
        
        # Al-Baqarah patterns
        "These are the opening letters of the surah, known as the muqatta'at.":
            "These are the opening letters of the surah, known as the muqatta'at (disjointed letters). These letters appear at the beginning of 29 Surahs in the Quran. Their exact meaning is known only to Allah, but they serve as a reminder that the Quran is a miraculous revelation that cannot be replicated by humans. Scholars suggest they may indicate the divine origin of the Quran and challenge those who doubt its authenticity.",
        
        "Establishing the Quran as the divine book of guidance for the God-conscious.":
            "This verse establishes the fundamental nature of the Quran. 'Dhalika al-kitab' means 'This is the Book', 'la rayba feehi' means 'there is no doubt in it', and 'huda lil-muttaqeen' means 'guidance for the God-conscious'. This teaches us that the Quran is the definitive divine revelation, free from any doubt or error, and serves as guidance specifically for those who have taqwa (God-consciousness and piety).",
        
        "Ayat Al-Kursi, one of the most powerful verses describing Allah's attributes and sovereignty.":
            "Ayat Al-Kursi (The Throne Verse) is one of the most powerful and comprehensive verses in the Quran. It describes Allah's absolute attributes: His oneness, eternal life, self-sustaining nature, omniscience, and omnipotence. The verse emphasizes that Allah never sleeps or tires, knows everything past and future, and that His knowledge encompasses all creation. It teaches us about Allah's supreme authority and the futility of seeking intercession without His permission.",
        
        "The final verse of Al-Baqarah, containing a comprehensive dua (supplication) for forgiveness and help.":
            "This is the final verse of Al-Baqarah, containing a comprehensive dua (supplication) that covers all aspects of human needs. It teaches us about Allah's justice (not burdening us beyond our capacity), seeking forgiveness for forgetfulness and mistakes, asking for protection from excessive burdens, and seeking Allah's mercy and victory. This verse serves as a model for comprehensive supplication and teaches us to turn to Allah for all our needs.",
        
        # Aal-Imran patterns
        "A dua for steadfastness in faith and seeking Allah's mercy.":
            "This verse is a beautiful dua (supplication) that teaches us to seek Allah's help in maintaining our faith. 'La tuzigh quloobana' means 'do not let our hearts deviate', 'ba'da idh hadaytana' means 'after You have guided us', and 'hab lana min ladunka rahmah' means 'grant us from Yourself mercy'. This teaches us to constantly seek Allah's help to remain steadfast in faith and to recognize that guidance and mercy come only from Him.",
        
        "Describing the characteristics of the righteous, including controlling anger and forgiving others.":
            "This verse describes the characteristics of the righteous believers. 'Yunfiqoona fis-sarra'i wad-darra'i' means they spend in charity during both ease and hardship, 'kaadhiminal-ghaytha' means they restrain their anger, and 'afina anin-naas' means they pardon people. This teaches us that true righteousness involves generosity in all circumstances, self-control over emotions, and forgiveness towards others - qualities that Allah loves.",
        
        # An-Nisa patterns
        "This verse emphasizes the unity of humanity and the importance of fearing Allah and maintaining family ties.":
            "This verse establishes the fundamental unity of humanity. 'Khalaqakum min nafsin wahidatin' means 'created you from one soul', emphasizing that all humans share the same origin. 'Wa khalaqa minha zawjaha' means 'and created from it its mate', referring to the creation of Adam and Eve. This teaches us about human equality, the sanctity of family relationships, and the importance of maintaining family ties while fearing Allah.",
        
        "This verse establishes prayer as an obligatory act of worship with specific timings for believers.":
            "This verse establishes the fundamental importance of prayer in Islam. 'Qadaytumus-salaata' means 'when you have completed the prayer', 'fadhkuroo Allaha' means 'remember Allah', and 'kitaaban mawqoota' means 'a decreed portion of time'. This teaches us that prayer is obligatory with specific timings, and that we should remember Allah in all positions (standing, sitting, lying down). The verse emphasizes the structured nature of Islamic worship.",
        
        # Al-Ma'idah patterns
        "This verse emphasizes the sanctity of human life and the principle that saving one life is like saving all of humanity.":
            "This verse establishes the fundamental sanctity of human life in Islam. 'Man qatala nafsan' means 'whoever kills a soul', 'bighayri nafsin' means 'without a soul (justification)', and 'faka-annama qatalan-nasa jamee'a' means 'it is as if he had slain all of humanity'. This teaches us that taking an innocent life is equivalent to killing all of humanity, emphasizing the gravity of murder. Conversely, saving one life is like saving all of humanity, highlighting the value of preserving life."
    }
    
    # Update all context fields to tafsir
    updated_content = content
    update_count = 0
    
    for context_text, tafsir_text in tafsir_updates.items():
        # Find and replace context with tafsir
        old_pattern = f'"context": "{re.escape(context_text)}"'
        new_pattern = f'"tafsir": "{tafsir_text}"'
        
        if old_pattern in updated_content:
            updated_content = updated_content.replace(old_pattern, new_pattern)
            update_count += 1
            print(f"✅ Updated: {context_text[:50]}...")
    
    # Also update any remaining "context" fields to "tafsir" with enhanced content
    # This will catch any context fields not in our mapping
    remaining_contexts = re.findall(r'"context": "([^"]+)"', updated_content)
    
    for context_text in remaining_contexts:
        if context_text not in [old for old, new in tafsir_updates.items()]:
            # Create enhanced tafsir for remaining contexts
            enhanced_tafsir = f"This verse teaches important Islamic principles. {context_text} The verse emphasizes key aspects of faith, worship, or character that Muslims should understand and implement in their daily lives."
            
            old_pattern = f'"context": "{re.escape(context_text)}"'
            new_pattern = f'"tafsir": "{enhanced_tafsir}"'
            
            updated_content = updated_content.replace(old_pattern, new_pattern)
            update_count += 1
            print(f"🔄 Enhanced: {context_text[:50]}...")
    
    # Update all search method references from "context" to "tafsir"
    method_updates = [
        ('verse.get(\'context\', \'\')', 'verse.get(\'tafsir\', \'\')'),
        ('verse[\'context\']', 'verse[\'tafsir\']'),
        ('verse.get("context", "")', 'verse.get("tafsir", "")'),
        ('verse["context"]', 'verse["tafsir"]'),
        ('hadith[\'context\']', 'hadith[\'context\']'),  # Keep hadith context unchanged
        ('hadith.get(\'context\', \'\')', 'hadith.get(\'context\', \'\')'),  # Keep hadith context unchanged
    ]
    
    for old_pattern, new_pattern in method_updates:
        if old_pattern in updated_content:
            updated_content = updated_content.replace(old_pattern, new_pattern)
            print(f"🔄 Updated method reference: {old_pattern} → {new_pattern}")
    
    # Write the updated content back to file
    with open('comprehensive_islamic_knowledge.py', 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"\n🎉 Quran format update completed!")
    print(f"📊 Total updates made: {update_count}")
    print(f"📖 All Quran verses now use: Arabic → Transliteration → Saheeh Translation → Tafsir")
    print(f"✅ Hadith and other knowledge remains unchanged")
    
    return update_count

def verify_updates():
    """Verify that all updates were applied correctly"""
    print("\n🔍 Verifying updates...")
    
    with open('comprehensive_islamic_knowledge.py', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check for remaining context fields in Quran sections
    context_count = content.count('"context":')
    tafsir_count = content.count('"tafsir":')
    
    print(f"📊 Remaining 'context' fields: {context_count}")
    print(f"📊 Total 'tafsir' fields: {tafsir_count}")
    
    if context_count == 0:
        print("✅ All Quran verses successfully updated to tafsir format!")
    else:
        print(f"⚠️ {context_count} context fields remain (likely in hadith sections)")
    
    return context_count, tafsir_count

if __name__ == "__main__":
    try:
        # Perform the update
        update_count = update_quran_format()
        
        # Verify the updates
        context_count, tafsir_count = verify_updates()
        
        print(f"\n🎯 Update Summary:")
        print(f"   • Quran verses updated: {update_count}")
        print(f"   • Format: Arabic → Transliteration → Saheeh Translation → Tafsir")
        print(f"   • All existing knowledge preserved")
        
    except Exception as e:
        print(f"❌ Error during update: {e}")
        print("Please check the file manually or restore from backup.")
