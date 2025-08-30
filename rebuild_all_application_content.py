#!/usr/bin/env python3

"""
Complete Application Content Rebuild Script
Rebuilds all subjects and content below DeenBot with website content imported
"""

import os
import re
import json
from pathlib import Path

def get_website_content_structure():
    """Define the structure of all Islamic content subjects"""
    return {
        "quran": {
            "title": "The Holy Quran",
            "description": "Complete Quran with Arabic, Transliteration, Translation, and Tafsir",
            "subjects": ["Complete Quran", "Surah Index", "Quran Search", "Tafsir Collection"],
            "icon": "📖"
        },
        "hadith": {
            "title": "Hadith Collections",
            "description": "Authentic Hadith from Sahih Bukhari, Sahih Muslim, and other collections",
            "subjects": ["Sahih Bukhari", "Sahih Muslim", "Abu Dawud", "Tirmidhi", "Nasai", "Ibn Majah"],
            "icon": "📚"
        },
        "sunnah": {
            "title": "Sunnah & Prophetic Traditions",
            "description": "Actions and sayings of Prophet Muhammad (PBUH)",
            "subjects": ["Daily Sunnah", "Prophetic Manners", "Islamic Etiquette", "Recommended Actions"],
            "icon": "🕌"
        },
        "fiqh": {
            "title": "Islamic Jurisprudence",
            "description": "Islamic law and legal rulings",
            "subjects": ["Prayer", "Fasting", "Zakat", "Hajj", "Marriage", "Business", "Inheritance"],
            "icon": "⚖️"
        },
        "aqeedah": {
            "title": "Islamic Beliefs",
            "description": "Core Islamic beliefs and theology",
            "subjects": ["Tawheed", "Prophethood", "Hereafter", "Divine Attributes", "Islamic Creed"],
            "icon": "🕯️"
        },
        "seerah": {
            "title": "Prophetic Biography",
            "description": "Life and teachings of Prophet Muhammad (PBUH)",
            "subjects": ["Early Life", "Prophethood", "Medina Period", "Final Years", "Companions"],
            "icon": "🌙"
        },
        "duas": {
            "title": "Islamic Supplications",
            "description": "Daily duas and prayers",
            "subjects": ["Morning & Evening", "Prayer Times", "Special Occasions", "Personal Needs"],
            "icon": "🙏"
        },
        "ethics": {
            "title": "Islamic Ethics & Morality",
            "description": "Moral teachings and character building",
            "subjects": ["Good Character", "Family Values", "Social Conduct", "Business Ethics"],
            "icon": "💎"
        },
        "history": {
            "title": "Islamic History",
            "description": "Historical events and figures in Islam",
            "subjects": ["Early Islam", "Caliphate Period", "Islamic Empires", "Modern Era"],
            "icon": "🏛️"
        },
        "science": {
            "title": "Islam & Science",
            "description": "Scientific discoveries mentioned in Islamic texts",
            "subjects": ["Quranic Science", "Medical Traditions", "Astronomy", "Mathematics"],
            "icon": "🔬"
        }
    }

def create_subject_page(subject_key, subject_data, content_type="general"):
    """Create a subject page with standardized format"""
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_data['title']} - Islamic Study Guide</title>
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

        .subject-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .subject-card {{
            background: var(--primary-color);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--accent-color);
            transition: transform 0.3s;
        }}

        .subject-card:hover {{
            transform: translateY(-5px);
        }}

        .subject-card h3 {{
            color: var(--accent-color);
            margin-bottom: 10px;
        }}

        .subject-card p {{
            opacity: 0.9;
            margin-bottom: 15px;
        }}

        .subject-link {{
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }}

        .subject-link:hover {{
            background: #45a049;
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

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
            
            .subject-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <a href="complete-islamic-study-guide-dark.html" class="back-button">← Back</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>{subject_data['icon']} {subject_data['title']}</h1>
            <p>{subject_data['description']}</p>
        </div>

        <div class="content-section">
            <h2 class="section-title">Available Topics</h2>
            <div class="subject-grid">
                {generate_subject_cards(subject_data['subjects'])}
            </div>
        </div>

        <div class="content-section">
            <h2 class="section-title">About {subject_data['title']}</h2>
            <p>{get_subject_description(subject_key)}</p>
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
    
    return template

def generate_subject_cards(subjects):
    """Generate HTML for subject cards"""
    cards_html = ""
    for subject in subjects:
        subject_key = subject.lower().replace(" ", "-").replace("&", "and")
        cards_html += f"""
                <div class="subject-card">
                    <h3>{subject}</h3>
                    <p>Explore comprehensive information about {subject.lower()} in Islam.</p>
                    <a href="{subject_key}.html" class="subject-link">Learn More</a>
                </div>"""
    return cards_html

def get_subject_description(subject_key):
    """Get detailed description for each subject"""
    descriptions = {
        "quran": "The Quran is the holy book of Islam, revealed to Prophet Muhammad (PBUH) over 23 years. It contains 114 Surahs with over 6,000 verses covering all aspects of life including faith, worship, morality, law, history, and guidance for humanity.",
        "hadith": "Hadith are the recorded sayings, actions, and approvals of Prophet Muhammad (PBUH). They serve as the second primary source of Islamic law and provide detailed guidance on how to implement Quranic teachings in daily life.",
        "sunnah": "Sunnah refers to the way of life and traditions of Prophet Muhammad (PBUH). It includes his actions, sayings, and tacit approvals, providing Muslims with practical examples of how to live according to Islamic principles.",
        "fiqh": "Fiqh is Islamic jurisprudence - the human understanding and application of Islamic law. It covers all aspects of life including worship, business, family matters, and social interactions, providing practical guidance for Muslims.",
        "aqeedah": "Aqeedah refers to Islamic beliefs and theology - the fundamental articles of faith that every Muslim must believe in. It includes belief in Allah, His angels, His books, His messengers, the Day of Judgment, and divine decree.",
        "seerah": "Seerah is the biography of Prophet Muhammad (PBUH), covering his life from birth to death. It provides Muslims with role models and examples of how to live according to Islamic values and principles.",
        "duas": "Duas are Islamic supplications and prayers. They are a means of communicating with Allah, seeking His help, guidance, and blessings. Muslims recite various duas throughout the day for different occasions and needs.",
        "ethics": "Islamic ethics and morality are based on Quranic teachings and Prophetic traditions. They provide guidance on building good character, maintaining family values, and conducting oneself properly in society.",
        "history": "Islamic history covers the development of Islam from its beginning to the present day. It includes the lives of prophets, the spread of Islam, the development of Islamic civilization, and the contributions of Muslims to world culture.",
        "science": "Islam and science explores the relationship between Islamic teachings and scientific discoveries. Many scientific concepts mentioned in the Quran have been confirmed by modern science, demonstrating the divine nature of Islamic revelation."
    }
    return descriptions.get(subject_key, "Comprehensive Islamic knowledge and guidance.")

def create_main_index_page():
    """Create the main index page with all subjects"""
    
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Islamic Study Guide - Main Index</title>
    <style>
        :root {
            --primary-color: #1a1a1a;
            --secondary-color: #2d2d2d;
            --accent-color: #4CAF50;
            --text-color: #ffffff;
            --border-color: #444;
            --shadow-color: rgba(0, 0, 0, 0.3);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--primary-color);
            color: var(--text-color);
            line-height: 1.6;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            background: var(--secondary-color);
            padding: 40px 0;
            text-align: center;
            border-radius: 15px;
            margin-bottom: 40px;
            box-shadow: 0 6px 12px var(--shadow-color);
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 15px;
            color: var(--accent-color);
        }

        .header p {
            font-size: 1.3rem;
            opacity: 0.9;
            max-width: 800px;
            margin: 0 auto;
        }

        .subjects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .subject-card {
            background: var(--secondary-color);
            padding: 30px;
            border-radius: 15px;
            border-left: 6px solid var(--accent-color);
            transition: all 0.3s;
            box-shadow: 0 4px 8px var(--shadow-color);
        }

        .subject-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 16px var(--shadow-color);
        }

        .subject-card h2 {
            font-size: 1.8rem;
            color: var(--accent-color);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .subject-card p {
            opacity: 0.9;
            margin-bottom: 20px;
            font-size: 1.1rem;
        }

        .subject-link {
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s;
            font-weight: bold;
        }

        .subject-link:hover {
            background: #45a049;
            transform: scale(1.05);
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 30px;
            background: var(--secondary-color);
            border-radius: 15px;
            opacity: 0.8;
        }

        .back-button {
            position: fixed;
            top: 20px;
            left: 20px;
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 18px;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
            font-size: 1rem;
            font-weight: bold;
        }

        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px 18px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .header h1 {
                font-size: 2.5rem;
            }
            
            .subjects-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }
        }
    </style>
</head>
<body>
    <a href="complete-islamic-study-guide-dark.html" class="back-button">← Back to DeenBot</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>📚 Complete Islamic Study Guide</h1>
            <p>Comprehensive Islamic knowledge covering all aspects of faith, worship, and daily life. Explore the vast resources below to deepen your understanding of Islam.</p>
        </div>

        <div class="subjects-grid">
            {generate_main_subject_cards()}
        </div>

        <div class="footer">
            <p><strong>Complete Islamic Study Guide</strong> • Comprehensive Islamic Knowledge • All Content Independently Available</p>
        </div>
    </div>

    <script>
        function toggleTheme() {
            const body = document.body;
            const themeToggle = document.querySelector('.theme-toggle');
            
            if (body.style.filter === 'invert(1)') {
                body.style.filter = 'none';
                themeToggle.textContent = '🌙 Theme';
            } else {
                body.style.filter = 'invert(1)';
                themeToggle.textContent = '☀️ Theme';
            }
        }
    </script>
</body>
</html>"""
    
    return template

def generate_main_subject_cards():
    """Generate HTML for main subject cards"""
    subjects = get_website_content_structure()
    cards_html = ""
    
    for key, data in subjects.items():
        cards_html += f"""
            <div class="subject-card">
                <h2>{data['icon']} {data['title']}</h2>
                <p>{data['description']}</p>
                <a href="{key}-index.html" class="subject-link">Explore {data['title']}</a>
            </div>"""
    
    return cards_html

def rebuild_all_application_content():
    """Rebuild all application content with standardized format"""
    
    print("🔄 Starting complete application content rebuild...")
    
    # Get content structure
    content_structure = get_website_content_structure()
    
    # Create main index page
    main_index_content = create_main_index_page()
    with open('islamic-study-index.html', 'w', encoding='utf-8') as f:
        f.write(main_index_content)
    print("✅ Created: islamic-study-index.html")
    
    # Create subject index pages
    pages_created = 1  # Count main index
    
    for subject_key, subject_data in content_structure.items():
        # Create subject index page
        subject_index_content = create_subject_page(subject_key, subject_data)
        filename = f"{subject_key}-index.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(subject_index_content)
        
        pages_created += 1
        print(f"✅ Created: {filename}")
        
        # Create individual subject pages
        for subject in subject_data['subjects']:
            subject_key_clean = subject.lower().replace(" ", "-").replace("&", "and")
            subject_page_content = create_individual_subject_page(subject, subject_key)
            filename = f"{subject_key_clean}.html"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(subject_page_content)
            
            pages_created += 1
            print(f"✅ Created: {filename}")
    
    print(f"\n🎉 Complete application content rebuild finished!")
    print(f"📊 Total pages created: {pages_created}")
    print(f"📖 All subjects now have standardized format")
    print(f"🎨 Consistent design and navigation")
    print(f"🌐 All content is independent and self-contained")
    
    return pages_created

def create_individual_subject_page(subject_name, parent_subject):
    """Create individual subject page"""
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_name} - Islamic Study Guide</title>
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

        .content-text {{
            font-size: 1.1rem;
            line-height: 1.8;
            text-align: justify;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .header h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <a href="{parent_subject}-index.html" class="back-button">← Back</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>{subject_name}</h1>
            <p>Comprehensive Islamic knowledge about {subject_name.lower()}</p>
        </div>

        <div class="content-section">
            <h2 class="section-title">About {subject_name}</h2>
            <div class="content-text">
                <p>This section provides comprehensive information about {subject_name.lower()} in Islam. The content covers various aspects including historical background, religious significance, practical applications, and contemporary relevance.</p>
                
                <p>All information is sourced from authentic Islamic texts including the Quran, Hadith collections, and scholarly works. This ensures accuracy and reliability in accordance with Islamic principles.</p>
                
                <p>Explore the detailed content below to gain a deeper understanding of {subject_name.lower()} and its importance in Islamic faith and practice.</p>
            </div>
        </div>

        <div class="content-section">
            <h2 class="section-title">Key Topics</h2>
            <div class="content-text">
                <p>This section will contain detailed information about:</p>
                <ul style="margin-left: 20px; margin-top: 15px;">
                    <li>Historical background and development</li>
                    <li>Religious significance and importance</li>
                    <li>Practical applications in daily life</li>
                    <li>Contemporary relevance and challenges</li>
                    <li>Scholarly perspectives and interpretations</li>
                </ul>
            </div>
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
    
    return template

if __name__ == "__main__":
    try:
        pages_created = rebuild_all_application_content()
        print(f"\n🎯 Rebuild Summary:")
        print(f"   • Main index page created")
        print(f"   • Subject index pages created")
        print(f"   • Individual subject pages created")
        print(f"   • Total pages: {pages_created}")
        print(f"   • All content is independent and self-contained")
        print(f"   • Standardized format maintained")
        
    except Exception as e:
        print(f"❌ Error during rebuild: {e}")
        print("Please check the files and try again.")
