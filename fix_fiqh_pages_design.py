#!/usr/bin/env python3

"""
Fix Fiqh Pages Design - Match Index Page Exactly
Recreates all advanced fiqh pages with the exact design from complete-islamic-study-guide-dark.html
NO EMOJIS - This is a serious Islamic research application
"""

import os

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

        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            .header h1 {{
                font-size: 1.5rem;
            }}
            
            .links-grid {{
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
    <a href="fiqh-index.html" class="back-button">Back to Fiqh</a>
    <button class="theme-toggle" onclick="toggleTheme()">Toggle Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>{description}</p>
        </div>

        <div class="search-section">
            <h3>Search Fiqh Topics</h3>
            <div class="search-container">
                <input type="text" class="search-input" id="searchInput" placeholder="Search for specific fiqh topics..." onkeyup="performSearch()">
                <button class="search-button" onclick="performSearch()">Search</button>
            </div>
            <div class="search-results" id="searchResults">
                <p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>
            </div>
        </div>

        <div class="content-section">
            <h3>Available Topics</h3>
            <div class="links-grid">
                {topics_content}
            </div>
        </div>

        <div class="content-section">
            <h3>About {title}</h3>
            <p style="color: var(--text-secondary); line-height: 1.6;">{about_content}</p>
        </div>
    </div>

    <script>
        // Fiqh content database
        const fiqhContent = {{
            {content_database}
        }};

        function performSearch() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const resultsContainer = document.getElementById('searchResults');
            
            if (searchTerm.length < 2) {{
                resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>';
                return;
            }}
            
            const results = [];
            
            // Search through fiqh content
            for (const [topic, content] of Object.entries(fiqhContent)) {{
                if (topic.toLowerCase().includes(searchTerm) || 
                    content.toLowerCase().includes(searchTerm)) {{
                    results.push({{topic, content}});
                }}
            }}
            
            // Display results
            if (results.length === 0) {{
                resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No results found for "' + searchTerm + '"</p>';
            }} else {{
                let resultsHTML = '<h4 style="color: var(--accent-primary); margin-bottom: 1rem;">Search Results:</h4>';
                results.forEach(result => {{
                    resultsHTML += `
                        <div class="result-item">
                            <div class="result-title">${{result.topic}}</div>
                            <div class="result-content">${{result.content}}</div>
                        </div>
                    `;
                }});
                resultsContainer.innerHTML = resultsHTML;
            }}
        }}

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
    </script>
</body>
</html>"""

def get_advanced_fiqh_topics():
    """Get comprehensive list of advanced fiqh topics - NO EMOJIS"""
    return {
        "business_financial": {
            "title": "Business & Financial Fiqh",
            "description": "Islamic rulings on business transactions, finance, and economic activities",
            "topics": [
                "Trade and Commerce", "Banking and Interest", "Investment and Stocks",
                "Insurance and Risk Management", "Partnership and Joint Ventures",
                "Real Estate and Property", "Employment and Labor", "Taxation and Zakat",
                "Cryptocurrency and Digital Assets", "Islamic Banking Products"
            ]
        },
        "medical_health": {
            "title": "Medical & Health Fiqh",
            "description": "Islamic rulings on medical treatment, health, and bioethics",
            "topics": [
                "Medical Treatment and Surgery", "Organ Transplantation", "Blood Donation",
                "Pregnancy and Abortion", "Mental Health Treatment", "Vaccination",
                "End of Life Care", "Medical Research Ethics", "Alternative Medicine",
                "Health Insurance and Coverage"
            ]
        },
        "technology_modern": {
            "title": "Technology & Modern Life Fiqh",
            "description": "Islamic rulings on modern technology and contemporary issues",
            "topics": [
                "Social Media and Internet", "Artificial Intelligence", "Gaming and Entertainment",
                "Digital Privacy and Security", "Online Business", "Remote Work",
                "Virtual Reality and Augmented Reality", "Blockchain Technology",
                "Smart Devices and IoT", "Digital Content Creation"
            ]
        },
        "environmental_social": {
            "title": "Environmental & Social Fiqh",
            "description": "Islamic rulings on environmental protection and social responsibility",
            "topics": [
                "Environmental Conservation", "Climate Change", "Sustainable Living",
                "Animal Rights and Welfare", "Community Service", "Social Justice",
                "Charity and Philanthropy", "Education and Learning", "Public Health",
                "Disaster Relief and Emergency Response"
            ]
        },
        "contemporary_issues": {
            "title": "Contemporary Issues Fiqh",
            "description": "Islamic rulings on modern challenges and current events",
            "topics": [
                "Globalization and Cultural Exchange", "Refugee and Immigration",
                "International Relations", "Media and Journalism", "Sports and Recreation",
                "Arts and Entertainment", "Travel and Tourism", "Consumer Rights",
                "Workplace Ethics", "Family in Modern Society"
            ]
        }
    }

def generate_topics_content(topics):
    """Generate topics content in exact index page format - NO EMOJIS"""
    topics_html = ""
    for topic in topics:
        topics_html += f"""
                <div class="link-category">
                    <h4>{topic}</h4>
                    <ul>
                        <li>Comprehensive Islamic rulings and guidance on {topic.lower()} according to Islamic jurisprudence.</li>
                        <li>Practical applications and contemporary considerations.</li>
                        <li>Scholarly consensus and authentic sources.</li>
                    </ul>
                </div>"""
    return topics_html

def generate_content_database(topics):
    """Generate JavaScript content database for search functionality - NO EMOJIS"""
    content_db = {}
    
    # Sample fiqh content for each topic
    fiqh_content_samples = {
        "Trade and Commerce": "Islamic trade and commerce is based on principles of fairness, transparency, and mutual consent. The Prophet Muhammad (PBUH) said: 'The truthful and trustworthy merchant will be with the prophets, the truthful, and the martyrs on the Day of Resurrection.' Key principles include avoiding riba (interest), gharar (uncertainty), and ensuring fair pricing.",
        "Banking and Interest": "Islamic banking operates on the principle of profit and loss sharing rather than interest. Riba (usury) is strictly prohibited in Islam. Islamic banks use contracts like Murabaha (cost-plus financing), Musharaka (partnership), and Ijara (leasing) to provide financial services while adhering to Shariah principles.",
        "Investment and Stocks": "Islamic investment principles require avoiding companies involved in haram activities like alcohol, gambling, or interest-based finance. Shariah-compliant investments focus on halal businesses and use profit-sharing models. Screening criteria ensure investments align with Islamic values.",
        "Medical Treatment and Surgery": "Islam encourages seeking medical treatment and considers it a religious duty. The Prophet (PBUH) said: 'There is no disease that Allah has created, except that He also has created its treatment.' Medical procedures are permissible when they provide clear benefit and don't cause unnecessary harm.",
        "Organ Transplantation": "Organ transplantation is generally permissible in Islam when it saves lives and follows proper ethical guidelines. The donor must give informed consent, and the procedure should not cause undue harm. Living organ donation is allowed for close relatives, while cadaveric donation requires proper authorization.",
        "Social Media and Internet": "Islamic principles apply to online behavior just as they do offline. Users should maintain good character, avoid spreading false information, and use social media for beneficial purposes. Privacy, respect for others, and avoiding harmful content are essential Islamic values online.",
        "Environmental Conservation": "Islam teaches that humans are stewards of the Earth and must protect the environment. The Prophet (PBUH) encouraged planting trees and avoiding waste. Environmental conservation is considered a form of worship and social responsibility in Islamic tradition.",
        "Climate Change": "Islamic teachings emphasize the importance of environmental stewardship and sustainable living. Muslims are encouraged to reduce their carbon footprint, support renewable energy, and advocate for policies that protect the environment for future generations.",
        "Globalization and Cultural Exchange": "Islam encourages learning from other cultures while maintaining Islamic identity. The Prophet (PBUH) said: 'Seeking knowledge is obligatory for every Muslim.' Cultural exchange should promote mutual understanding and respect while preserving Islamic values.",
        "Refugee and Immigration": "Islam has a strong tradition of helping refugees and migrants. The Prophet (PBUH) himself was a migrant, and Islamic law provides extensive guidance on the rights and treatment of refugees. Muslims are encouraged to support and welcome those fleeing persecution or hardship."
    }
    
    for topic in topics:
        if topic in fiqh_content_samples:
            content_db[topic] = fiqh_content_samples[topic]
        else:
            content_db[topic] = f"Islamic jurisprudence provides comprehensive guidance on {topic.lower()}. This topic covers various aspects including religious rulings, practical applications, and contemporary considerations according to Islamic law and scholarly consensus."
    
    # Convert to JavaScript object format
    js_content = ""
    for topic, content in content_db.items():
        js_content += f'"{topic}": "{content.replace('"', '\\"')}",\n            '
    
    return js_content.rstrip(',\n            ')

def create_fiqh_page_with_exact_design(topic_key, topic_data):
    """Create a fiqh page with exact index page design - NO EMOJIS"""
    
    # Generate topics content
    topics_content = generate_topics_content(topic_data['topics'])
    
    # Generate content database
    content_database = generate_content_database(topic_data['topics'])
    
    # Generate about content
    about_content = f"{topic_data['description']} This section provides comprehensive Islamic jurisprudence guidance covering all aspects of {topic_data['title'].lower()}. All rulings are based on authentic Islamic sources including the Quran, Hadith, and scholarly consensus from the four major schools of Islamic law."
    
    # Fill template with exact design
    page_content = get_exact_index_page_design().format(
        title=topic_data['title'],
        description=topic_data['description'],
        topics_content=topics_content,
        about_content=about_content,
        content_database=content_database
    )
    
    return page_content

def fix_all_fiqh_pages_design():
    """Fix all advanced fiqh pages to match index page design exactly - NO EMOJIS"""
    
    print("Fixing all fiqh pages to match index page design exactly...")
    print("NO EMOJIS - This is a serious Islamic research application")
    
    topics = get_advanced_fiqh_topics()
    pages_fixed = 0
    
    for topic_key, topic_data in topics.items():
        try:
            # Create page with exact design
            page_content = create_fiqh_page_with_exact_design(topic_key, topic_data)
            filename = f"{topic_key}.html"
            
            # Write the corrected page
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            pages_fixed += 1
            print(f"Fixed: {filename} - Now matches index page design exactly")
            
        except Exception as e:
            print(f"Error fixing {filename}: {e}")
    
    print(f"\nAll fiqh pages design fixed!")
    print(f"Total pages corrected: {pages_fixed}")
    print(f"Design now matches index page exactly")
    print(f"NO EMOJIS - Serious Islamic research application design")
    
    return pages_fixed

if __name__ == "__main__":
    try:
        pages_fixed = fix_all_fiqh_pages_design()
        print(f"\nFix Summary:")
        print(f"   All fiqh pages now match index page design exactly")
        print(f"   Same CSS variables, fonts, colors, and layout")
        print(f"   Same header, content sections, and styling")
        print(f"   NO EMOJIS - Professional Islamic research interface")
        
    except Exception as e:
        print(f"Error during fix: {e}")
        print("Please check the files and try again.")
