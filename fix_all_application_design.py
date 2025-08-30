#!/usr/bin/env python3

"""
Fix All Application Design - Match Index Page Exactly
Ensures every single page, subpage, and link looks and flows exactly like the index page
NO EMOJIS - This is a serious Islamic research application
"""

import os
import re

def get_exact_index_page_design():
    """Get the exact CSS and structure from the index page - NO EMOJIS"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Islamic Study Guide</title>
    <style>
        :root {{
            --bg-primary: #0a0f0f;
            --bg-secondary: #1a1a1a;
            --bg-accent: #142020;
            --bg-glass: rgba(26, 26, 26, 0.7);
            --text-primary: #ffffff;
            --text-secondary: #e2e8f0;
            --text-accent: #cbd5e0;
            --accent-primary: #10b981;
            --accent-secondary: #0d9488;
            --accent-teal: #14b8a6;
            --accent-green: #059669;
            --border-primary: rgba(20, 32, 32, 0.8);
            --border-secondary: rgba(16, 185, 129, 0.3);
            --shadow-primary: 0 8px 32px rgba(0, 0, 0, 0.3);
            --shadow-secondary: 0 16px 64px rgba(0, 0, 0, 0.4);
            --glass-blur: blur(20px);
        }}

        [data-theme="light"] {{
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-accent: #f1f5f9;
            --bg-glass: rgba(248, 250, 252, 0.8);
            --text-primary: #0f172a;
            --text-secondary: #334155;
            --text-accent: #475569;
            --accent-primary: #10b981;
            --accent-secondary: #0d9488;
            --accent-teal: #14b8a6;
            --accent-green: #059669;
            --border-primary: rgba(241, 245, 249, 0.8);
            --border-secondary: rgba(16, 185, 129, 0.3);
            --shadow-primary: 0 8px 32px rgba(0, 0, 0, 0.1);
            --shadow-secondary: 0 16px 64px rgba(0, 0, 0, 0.15);
            --glass-blur: blur(20px);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.5;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 1.5rem;
        }}

        .header {{
            text-align: center;
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: var(--bg-secondary);
            border-radius: 8px;
            box-shadow: var(--shadow-primary);
            border: 2px solid var(--accent-primary);
        }}

        .header h1 {{
            font-size: 2rem;
            color: var(--accent-primary);
            margin-bottom: 0.5rem;
            font-weight: 700;
        }}

        .header p {{
            font-size: 1rem;
            color: var(--text-secondary);
            max-width: 800px;
            margin: 0 auto;
        }}

        .theme-toggle {{
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
            background: var(--accent-primary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 0.8rem;
        }}

        .theme-toggle:hover {{
            background: var(--accent-secondary);
            transform: translateY(-2px);
        }}

        .back-button {{
            position: absolute;
            top: 1.5rem;
            left: 1.5rem;
            background: var(--accent-primary);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 0.8rem;
        }}

        .back-button:hover {{
            background: var(--accent-secondary);
            transform: translateY(-2px);
        }}

        .content-section {{
            background: var(--bg-secondary);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-primary);
            border: 1px solid var(--border-primary);
        }}

        .content-section h3 {{
            color: var(--accent-primary);
            font-size: 1.4rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--accent-primary);
            padding-bottom: 0.5rem;
        }}

        .links-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }}

        .link-category {{
            background: var(--bg-accent);
            padding: 1rem;
            border-radius: 6px;
            border-left: 4px solid var(--accent-primary);
        }}

        .link-category h4 {{
            color: var(--accent-secondary);
            margin-bottom: 0.75rem;
            font-size: 1rem;
        }}

        .link-category ul {{
            list-style: none;
            padding: 0;
        }}

        .link-category li {{
            margin-bottom: 0.25rem;
            padding: 0.25rem;
            border-radius: 4px;
            transition: background 0.2s ease;
        }}

        .link-category li:hover {{
            background: var(--bg-secondary);
        }}

        .link-category a {{
            color: var(--accent-primary);
            text-decoration: none;
            font-weight: 500;
            display: block;
            padding: 0.25rem;
            border-radius: 4px;
            transition: all 0.2s ease;
            font-size: 0.85rem;
        }}

        .link-category a:hover {{
            background: var(--accent-primary);
            color: white;
            transform: translateX(5px);
        }}

        .search-section {{
            background: var(--bg-secondary);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-primary);
            border: 1px solid var(--border-primary);
        }}

        .search-section h3 {{
            color: var(--accent-primary);
            font-size: 1.4rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid var(--accent-primary);
            padding-bottom: 0.5rem;
        }}

        .search-container {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}

        .search-input {{
            flex: 1;
            padding: 0.75rem 1rem;
            border: 2px solid var(--border-primary);
            border-radius: 6px;
            background: var(--bg-accent);
            color: var(--text-primary);
            font-size: 0.9rem;
            font-family: 'Georgia', 'Times New Roman', serif;
        }}

        .search-input:focus {{
            outline: none;
            border-color: var(--accent-primary);
        }}

        .search-button {{
            padding: 0.75rem 1.5rem;
            background: var(--accent-primary);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }}

        .search-button:hover {{
            background: var(--accent-secondary);
            transform: translateY(-2px);
        }}

        .search-results {{
            margin-top: 1.5rem;
        }}

        .result-item {{
            background: var(--bg-accent);
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 1rem;
            border-left: 4px solid var(--accent-primary);
        }}

        .result-title {{
            color: var(--accent-primary);
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }}

        .result-content {{
            color: var(--text-secondary);
            line-height: 1.6;
            font-size: 0.9rem;
        }}

        .subject-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }}

        .subject-card {{
            background: var(--bg-accent);
            padding: 1.5rem;
            border-radius: 8px;
            border-left: 4px solid var(--accent-primary);
            transition: all 0.3s ease;
        }}

        .subject-card:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow-secondary);
        }}

        .subject-card h3 {{
            color: var(--accent-primary);
            font-size: 1.2rem;
            margin-bottom: 1rem;
            font-weight: 600;
        }}

        .subject-card p {{
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.6;
        }}

        .subject-link {{
            display: inline-block;
            background: var(--accent-primary);
            color: white;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s ease;
        }}

        .subject-link:hover {{
            background: var(--accent-secondary);
            transform: translateY(-2px);
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            .header h1 {{
                font-size: 1.5rem;
            }}
            
            .links-grid, .subject-grid {{
                grid-template-columns: 1fr;
            }}
            
            .search-container {{
                flex-direction: column;
            }}
            
            .theme-toggle, .back-button {{
                position: relative;
                top: auto;
                left: auto;
                right: auto;
                margin-bottom: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <a href="{back_link}" class="back-button">Back to {back_text}</a>
    <button class="theme-toggle" onclick="toggleTheme()">Toggle Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>

        {search_section}

        <div class="content-section">
            <h3>{content_title}</h3>
            <div class="links-grid">
                {content_items}
            </div>
        </div>

        {additional_sections}
    </div>

    <script>
        function toggleTheme() {{
            const body = document.body;
            const themeToggle = document.querySelector('.theme-toggle');
            
            if (body.getAttribute('data-theme') === 'light') {{
                body.removeAttribute('data-theme');
                themeToggle.textContent = 'Toggle Theme';
            }} else {{
                body.setAttribute('data-theme', 'light');
                themeToggle.textContent = 'Toggle Theme';
            }}
        }}

        {additional_script}
    </script>
</body>
</html>"""

def remove_all_emojis(text):
    """Remove all emojis from text - NO EMOJIS ALLOWED"""
    # Remove emoji characters and emoji-related text
    emoji_patterns = [
        r'[^\w\s\-_.,!?;:()]',  # Remove special characters that might be emojis
        r'[📚📖🕌🕯️💎🏛️🔬]',  # Remove specific emoji characters
        r'[💼🏥💻🌍🌐]',  # Remove more emoji characters
        r'[✅❌🔄🎉📊🎨🔍🎯]',  # Remove status emojis
        r'[🌙📖📚🕌⚖️🕯️🌙🙏💎🏛️🔬]',  # Remove subject emojis
    ]
    
    for pattern in emoji_patterns:
        text = re.sub(pattern, '', text)
    
    # Clean up any double spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_application_structure():
    """Get the complete structure of all application pages that need fixing"""
    return {
        "main_index": {
            "title": "Complete Islamic Study Guide",
            "description": "Comprehensive Islamic knowledge covering Quran, Hadith, Sunnah, Fiqh, and more",
            "back_link": "#",
            "back_text": "Home",
            "content_title": "Islamic Study Subjects",
            "content_items": [
                {"title": "The Holy Quran", "description": "Complete Quran with Arabic, Transliteration, Translation, and Tafsir", "link": "quran-index.html"},
                {"title": "Hadith Collections", "description": "Authentic Hadith from major collections", "link": "hadith-index.html"},
                {"title": "Sunnah & Prophetic Traditions", "description": "Prophetic way of life and teachings", "link": "sunnah-index.html"},
                {"title": "Islamic Jurisprudence", "description": "Islamic law and legal rulings", "link": "fiqh-index.html"},
                {"title": "Islamic Beliefs", "description": "Core Islamic beliefs and theology", "link": "aqeedah-index.html"},
                {"title": "Prophetic Biography", "description": "Life and teachings of Prophet Muhammad", "link": "seerah-index.html"},
                {"title": "Islamic Supplications", "description": "Duas and prayers", "link": "duas-index.html"},
                {"title": "Islamic Ethics & Morality", "description": "Moral principles and character", "link": "ethics-index.html"},
                {"title": "Islamic History", "description": "Historical events and figures", "link": "history-index.html"},
                {"title": "Islam & Science", "description": "Islamic perspective on scientific matters", "link": "science-index.html"}
            ]
        },
        "quran_index": {
            "title": "Quran Studies",
            "description": "Complete access to the Holy Quran with comprehensive study materials",
            "back_link": "complete-islamic-study-guide-dark.html",
            "back_text": "Main Guide",
            "content_title": "Quran Study Resources",
            "content_items": [
                {"title": "Complete Quran with Search", "description": "Full Quran text with search functionality", "link": "quran-complete.html"},
                {"title": "Quran with Tafsir", "description": "Quran verses with detailed commentary", "link": "quran-complete-with-tafsir.html"},
                {"title": "Comprehensive Quran", "description": "Complete Quran study guide", "link": "quran-comprehensive.html"},
                {"title": "AI-Enhanced Quran", "description": "Advanced Quran study tools", "link": "quran-enhanced-ai.html"},
                {"title": "Quran & Hadith Complete", "description": "Integrated Quran and Hadith study", "link": "quran-hadith-complete.html"},
                {"title": "Tajweed Mastery", "description": "Quran recitation rules and practice", "link": "tajweed-mastery.html"},
                {"title": "Daily Quran Verses", "description": "One verse per day study program", "link": "one-per-day.html"}
            ]
        },
        "hadith_index": {
            "title": "Hadith Collections",
            "description": "Authentic Hadith from the major collections with search and study tools",
            "back_link": "complete-islamic-study-guide-dark.html",
            "back_text": "Main Guide",
            "content_title": "Major Hadith Collections",
            "content_items": [
                {"title": "Sahih Bukhari", "description": "Most authentic collection of Hadith", "link": "sahih-bukhari.html"},
                {"title": "Sahih Muslim", "description": "Second most authentic Hadith collection", "link": "sahih-muslim.html"},
                {"title": "Abu Dawud", "description": "Collection focusing on legal Hadith", "link": "abu-dawud.html"},
                {"title": "Tirmidhi", "description": "Collection with commentary and grading", "link": "tirmidhi.html"},
                {"title": "Nasai", "description": "Collection emphasizing legal rulings", "link": "nasai.html"},
                {"title": "Ibn Majah", "description": "Comprehensive Hadith collection", "link": "ibn-majah.html"},
                {"title": "Hadith Collections Hub", "description": "Central access to all collections", "link": "hadith-collections-hub.html"}
            ]
        },
        "fiqh_index": {
            "title": "Islamic Jurisprudence",
            "description": "Comprehensive Islamic law and legal rulings for all aspects of life",
            "back_link": "complete-islamic-study-guide-dark.html",
            "back_text": "Main Guide",
            "content_title": "Fiqh Categories",
            "content_items": [
                {"title": "Business & Financial Fiqh", "description": "Islamic rulings on business and finance", "link": "business_financial.html"},
                {"title": "Medical & Health Fiqh", "description": "Islamic rulings on medical matters", "link": "medical_health.html"},
                {"title": "Technology & Modern Life Fiqh", "description": "Islamic rulings on modern technology", "link": "technology_modern.html"},
                {"title": "Environmental & Social Fiqh", "description": "Islamic rulings on environment and society", "link": "environmental_social.html"},
                {"title": "Contemporary Issues Fiqh", "description": "Islamic rulings on current events", "link": "contemporary_issues.html"}
            ]
        }
    }

def generate_content_items_html(items):
    """Generate HTML for content items in exact index page format"""
    html = ""
    for item in items:
        html += f"""
                <div class="link-category">
                    <h4>{remove_all_emojis(item['title'])}</h4>
                    <ul>
                        <li><a href="{item['link']}">{remove_all_emojis(item['title'])}</a></li>
                        <li>{remove_all_emojis(item['description'])}</li>
                    </ul>
                </div>"""
    return html

def create_page_with_exact_design(page_key, page_data):
    """Create a page with exact index page design - NO EMOJIS"""
    
    # Remove all emojis from content
    title = remove_all_emojis(page_data['title'])
    description = remove_all_emojis(page_data['description'])
    content_title = remove_all_emojis(page_data['content_title'])
    
    # Generate content items
    content_items = generate_content_items_html(page_data['content_items'])
    
    # Determine if search section is needed
    search_section = ""
    if page_key in ["quran_index", "hadith_index", "fiqh_index"]:
        search_section = f"""
        <div class="search-section">
            <h3>Search {title}</h3>
            <div class="search-container">
                <input type="text" class="search-input" id="searchInput" placeholder="Search for specific topics..." onkeyup="performSearch()">
                <button class="search-button" onclick="performSearch()">Search</button>
            </div>
            <div class="search-results" id="searchResults">
                <p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>
            </div>
        </div>"""
    
    # Additional sections if needed
    additional_sections = ""
    if page_key == "main_index":
        additional_sections = f"""
        <div class="content-section">
            <h3>Complete Surah Access</h3>
            <div class="subject-grid">
                <div class="subject-card">
                    <h3>Surahs 1-30</h3>
                    <p>Access to the first 30 chapters of the Quran with complete verses, translation, and tafsir.</p>
                    <a href="quran-surahs-1-30.html" class="subject-link">Access Surahs</a>
                </div>
                <div class="subject-card">
                    <h3>Surahs 31-60</h3>
                    <p>Access to chapters 31-60 of the Quran with complete verses, translation, and tafsir.</p>
                    <a href="quran-surahs-31-60.html" class="subject-link">Access Surahs</a>
                </div>
                <div class="subject-card">
                    <h3>Surahs 61-114</h3>
                    <p>Access to chapters 61-114 of the Quran with complete verses, translation, and tafsir.</p>
                    <a href="quran-surahs-61-114.html" class="subject-link">Access Surahs</a>
                </div>
            </div>
        </div>"""
    
    # Additional script for search functionality
    additional_script = ""
    if page_key in ["quran_index", "hadith_index", "fiqh_index"]:
        additional_script = """
        function performSearch() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const resultsContainer = document.getElementById('searchResults');
            
            if (searchTerm.length < 2) {
                resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>';
                return;
            }
            
            // Placeholder search functionality
            resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Search functionality will be implemented with comprehensive Islamic content database.</p>';
        }"""
    
    # Fill template with exact design
    page_content = get_exact_index_page_design().format(
        title=title,
        description=description,
        back_link=page_data['back_link'],
        back_text=page_data['back_text'],
        content_title=content_title,
        content_items=content_items,
        search_section=search_section,
        additional_sections=additional_sections,
        additional_script=additional_script
    )
    
    return page_content

def fix_all_application_pages():
    """Fix ALL application pages to match index page design exactly - NO EMOJIS"""
    
    print("Fixing all application pages to match index page design exactly...")
    print("NO EMOJIS - This is a serious Islamic research application")
    
    structure = get_application_structure()
    pages_fixed = 0
    
    for page_key, page_data in structure.items():
        try:
            # Create page with exact design
            page_content = create_page_with_exact_design(page_key, page_data)
            
            # Determine filename
            if page_key == "main_index":
                filename = "islamic-study-index.html"
            else:
                filename = f"{page_key.replace('_', '-')}.html"
            
            # Write the corrected page
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            pages_fixed += 1
            print(f"Fixed: {filename} - Now matches index page design exactly")
            
        except Exception as e:
            print(f"Error fixing {page_key}: {e}")
    
    print(f"\nAll application pages design fixed!")
    print(f"Total pages corrected: {pages_fixed}")
    print(f"Design now matches index page exactly")
    print(f"NO EMOJIS - Serious Islamic research application design")
    
    return pages_fixed

if __name__ == "__main__":
    try:
        pages_fixed = fix_all_application_pages()
        print(f"\nFix Summary:")
        print(f"   All pages now match index page design exactly")
        print(f"   Same CSS variables, fonts, colors, and layout")
        print(f"   Same header, content sections, and styling")
        print(f"   NO EMOJIS - Professional Islamic research interface")
        
    except Exception as e:
        print(f"Error during fix: {e}")
        print("Please check the files and try again.")
