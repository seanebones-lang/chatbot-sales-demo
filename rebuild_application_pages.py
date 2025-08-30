#!/usr/bin/env python3

"""
Application Rebuild Helper Script
Rebuilds all application pages with standardized format and independent content
"""

import os
import re
from pathlib import Path

def get_application_template():
    """Get the base application template structure"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary-color: #1a1a1a;
            --secondary-color: #2d2d2d;
            --accent-color: #4CAF50;
            --text-color: #ffffff;
            --border-color: #444;
            --shadow-color: rgba(0, 0, 0, 0.3);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--primary-color);
            color: var(--text-color);
            line-height: 1.6;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }}

        .header {{
            background: var(--secondary-color);
            padding: 30px 0;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px var(--shadow-color);
        }}

        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            color: var(--accent-color);
        }}

        .header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}

        .content-section {{
            background: var(--secondary-color);
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 2px 4px var(--shadow-color);
        }}

        .section-title {{
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--accent-color);
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 10px;
        }}

        .verse-container {{
            background: var(--primary-color);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid var(--accent-color);
        }}

        .verse-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border-color);
        }}

        .verse-number {{
            background: var(--accent-color);
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-weight: bold;
        }}

        .verse-reference {{
            color: var(--accent-color);
            font-weight: bold;
        }}

        .verse-arabic {{
            font-size: 1.4rem;
            text-align: right;
            margin: 15px 0;
            line-height: 2;
            direction: rtl;
        }}

        .verse-transliteration {{
            font-size: 1.1rem;
            margin: 15px 0;
            padding: 15px;
            background: rgba(76, 175, 80, 0.1);
            border-radius: 5px;
            border-left: 3px solid var(--accent-color);
        }}

        .verse-translation {{
            font-size: 1.1rem;
            margin: 15px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 5px;
        }}

        .verse-tafsir {{
            font-size: 1rem;
            margin: 15px 0;
            padding: 15px;
            background: rgba(76, 175, 80, 0.05);
            border-radius: 5px;
            border-left: 3px solid var(--accent-color);
            font-style: italic;
        }}

        .navigation {{
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
            padding: 20px;
            background: var(--secondary-color);
            border-radius: 10px;
        }}

        .nav-button {{
            background: var(--accent-color);
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }}

        .nav-button:hover {{
            background: #45a049;
        }}

        .footer {{
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: var(--secondary-color);
            border-radius: 10px;
            opacity: 0.8;
        }}

        .theme-toggle {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9rem;
        }}

        .back-button {{
            position: fixed;
            top: 20px;
            left: 20px;
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-size: 0.9rem;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
            
            .verse-arabic {{
                font-size: 1.2rem;
            }}
        }}
    </style>
</head>
<body>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Theme</button>
    <a href="complete-islamic-study-guide-dark.html" class="back-button">← Back</a>
    
    <div class="container">
        <div class="header">
            <h1>{surah_name}</h1>
            <p>{arabic_name} • {translation}</p>
        </div>

        <div class="content-section">
            <h2 class="section-title">Surah Information</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                <div><strong>Surah Number:</strong> {surah_number}</div>
                <div><strong>Number of Verses:</strong> {verses}</div>
                <div><strong>Revelation:</strong> {revelation}</div>
                <div><strong>Juz:</strong> {juz}</div>
                <div><strong>Pages:</strong> {pages}</div>
                <div><strong>Rukus:</strong> {rukus}</div>
            </div>
        </div>

        <div class="content-section">
            <h2 class="section-title">Complete Verses</h2>
            {verses_content}
        </div>

        <div class="navigation">
            {navigation_buttons}
        </div>

        <div class="footer">
            <p><strong>{surah_name}</strong> • {arabic_name} • {verses} verses • {revelation} revelation</p>
        </div>
    </div>

    <script>
        function toggleTheme() {{
            const body = document.body;
            const themeToggle = document.querySelector('.theme-toggle');
            
            if (body.style.filter === 'invert(1)') {{
                body.style.filter = 'none';
                themeToggle.textContent = '🌙 Theme';
            }} else {{
                body.style.filter = 'invert(1)';
                themeToggle.textContent = '☀️ Theme';
            }}
        }}
    </script>
</body>
</html>"""

def create_surah_page(surah_data, surah_number):
    """Create a complete Surah page with standardized format"""
    
    # Generate navigation buttons
    prev_surah = surah_number - 1 if surah_number > 1 else None
    next_surah = surah_number + 1 if surah_number < 114 else None
    
    navigation_buttons = ""
    if prev_surah:
        navigation_buttons += f'<a href="surah-{prev_surah}-{get_surah_name_for_file(prev_surah)}.html" class="nav-button">← Previous Surah</a>'
    else:
        navigation_buttons += '<span class="nav-button" style="opacity: 0.5; cursor: not-allowed;">← Previous Surah</span>'
    
    if next_surah:
        navigation_buttons += f'<a href="surah-{next_surah}-{get_surah_name_for_file(next_surah)}.html" class="nav-button">Next Surah →</a>'
    else:
        navigation_buttons += '<span class="nav-button" style="opacity: 0.5; cursor: not-allowed;">Next Surah →</span>'
    
    # Generate verses content
    verses_content = ""
    for verse in surah_data.get('verses_data', []):
        verses_content += f"""
            <div class="verse-container">
                <div class="verse-header">
                    <span class="verse-number">Verse {verse['ayah']}</span>
                    <span class="verse-reference">{surah_data['surah_name']} {verse['ayah']}</span>
                </div>
                <div class="verse-arabic">{verse['arabic']}</div>
                <div class="verse-transliteration">{verse['transliteration']}</div>
                <div class="verse-translation">{verse['translation']}</div>
                <div class="verse-tafsir">{verse.get('tafsir', 'Tafsir available')}</div>
            </div>
        """
    
    # Fill template
    page_content = get_application_template().format(
        title=f"{surah_data['surah_name']} - {surah_data['arabic_name']}",
        surah_name=surah_data['surah_name'],
        arabic_name=surah_data['arabic_name'],
        translation=surah_data['translation'],
        surah_number=surah_data['surah_number'],
        verses=surah_data['verses'],
        revelation=surah_data['revelation'],
        juz=surah_data['juz'],
        pages=surah_data['pages'],
        rukus=surah_data['rukus'],
        verses_content=verses_content,
        navigation_buttons=navigation_buttons
    )
    
    return page_content

def get_surah_name_for_file(surah_number):
    """Get standardized filename for Surah"""
    surah_names = {
        1: "al-fatiha", 2: "al-baqarah", 3: "aal-imran", 4: "an-nisa", 5: "al-maidah",
        6: "al-anam", 7: "al-araf", 8: "al-anfal", 9: "at-tawbah", 10: "yunus",
        11: "hud", 12: "yusuf", 13: "ar-rad", 14: "ibrahim", 15: "al-hijr",
        16: "an-nahl", 17: "al-isra", 18: "al-kahf", 19: "maryam", 20: "ta-ha",
        21: "al-anbiya", 22: "al-hajj", 23: "al-muminun", 24: "an-nur", 25: "al-furqan",
        26: "ash-shuara", 27: "an-naml", 28: "al-qasas", 29: "al-ankabut", 30: "ar-rum",
        31: "luqman", 32: "as-sajdah", 33: "al-ahzab", 34: "saba", 35: "fatir",
        36: "yasin", 37: "as-saffat", 38: "sad", 39: "az-zumar", 40: "ghafir",
        41: "fussilat", 42: "ash-shura", 43: "az-zukhruf", 44: "ad-dukhan", 45: "al-jathiyah",
        46: "al-ahqaf", 47: "muhammad", 48: "al-fath", 49: "al-hujurat", 50: "qaf",
        51: "ad-dhariyat", 52: "at-tur", 53: "an-najm", 54: "al-qamar", 55: "ar-rahman",
        56: "al-waqiah", 57: "al-hadid", 58: "al-mujadilah", 59: "al-hashr", 60: "al-mumtahanah",
        61: "as-saff", 62: "al-jumuah", 63: "al-munafiqun", 64: "at-taghabun", 65: "at-talaq",
        66: "at-tahrim", 67: "al-mulk", 68: "al-qalam", 69: "al-haqqah", 70: "al-maarij",
        71: "nuh", 72: "al-jinn", 73: "al-muzzammil", 74: "al-muddathir", 75: "al-qiyamah",
        76: "al-insan", 77: "al-mursalat", 78: "an-naba", 79: "an-naziat", 80: "abasa",
        81: "at-takwir", 82: "al-infitar", 83: "al-mutaffifin", 84: "al-inshiqaq", 85: "al-buruj",
        86: "at-tariq", 87: "al-ala", 88: "al-ghashiyah", 89: "al-fajr", 90: "al-balad",
        91: "ash-shams", 92: "al-layl", 93: "ad-duha", 94: "ash-sharh", 95: "at-tin",
        96: "al-alaq", 97: "al-qadr", 98: "al-bayyinah", 99: "az-zalzalah", 100: "al-adiyat",
        101: "al-qariah", 102: "at-takathur", 103: "al-asr", 104: "al-humazah", 105: "al-fil",
        106: "quraysh", 107: "al-maun", 108: "al-kawthar", 109: "al-kafirun", 110: "an-nasr",
        111: "al-masad", 112: "al-ikhlas", 113: "al-falaq", 114: "an-nas"
    }
    return surah_names.get(surah_number, f"surah-{surah_number}")

def rebuild_all_surah_pages():
    """Rebuild all 114 Surah pages with standardized format"""
    
    print("🔄 Starting application rebuild...")
    
    # Import the knowledge base to get Surah data
    try:
        from comprehensive_islamic_knowledge import ComprehensiveIslamicKnowledge
        kb = ComprehensiveIslamicKnowledge()
        print(f"✅ Loaded knowledge base with {len(kb.quran_database)} Surahs")
    except ImportError as e:
        print(f"❌ Error loading knowledge base: {e}")
        return
    
    # Create pages directory if it doesn't exist
    os.makedirs("pages", exist_ok=True)
    
    # Generate all Surah pages
    pages_created = 0
    for surah_key, surah_data in kb.quran_database.items():
        surah_number = surah_data['surah_number']
        filename = f"surah-{surah_number}-{get_surah_name_for_file(surah_number)}.html"
        
        try:
            page_content = create_surah_page(surah_data, surah_number)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            pages_created += 1
            print(f"✅ Created: {filename}")
            
        except Exception as e:
            print(f"❌ Error creating {filename}: {e}")
    
    print(f"\n🎉 Application rebuild completed!")
    print(f"📊 Total pages created: {pages_created}")
    print(f"📖 All Surahs now use standardized format")
    print(f"🎨 Consistent design and navigation")
    
    return pages_created

if __name__ == "__main__":
    try:
        pages_created = rebuild_all_surah_pages()
        print(f"\n🎯 Rebuild Summary:")
        print(f"   • Surah pages created: {pages_created}")
        print(f"   • Format: Arabic → Transliteration → Saheeh Translation → Tafsir")
        print(f"   • All pages are independent and self-contained")
        
    except Exception as e:
        print(f"❌ Error during rebuild: {e}")
        print("Please check the knowledge base and try again.")
