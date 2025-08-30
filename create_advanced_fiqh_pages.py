#!/usr/bin/env python3

"""
Advanced Fiqh Topics Page Generator
Creates comprehensive fiqh topic pages with search functionality
"""

import os

def get_advanced_fiqh_topics():
    """Get comprehensive list of advanced fiqh topics"""
    return {
        "business_financial": {
            "title": "Business & Financial Fiqh",
            "description": "Islamic rulings on business transactions, finance, and economic activities",
            "topics": [
                "Trade and Commerce", "Banking and Interest", "Investment and Stocks",
                "Insurance and Risk Management", "Partnership and Joint Ventures",
                "Real Estate and Property", "Employment and Labor", "Taxation and Zakat",
                "Cryptocurrency and Digital Assets", "Islamic Banking Products"
            ],
            "icon": "💼"
        },
        "medical_health": {
            "title": "Medical & Health Fiqh",
            "description": "Islamic rulings on medical treatment, health, and bioethics",
            "topics": [
                "Medical Treatment and Surgery", "Organ Transplantation", "Blood Donation",
                "Pregnancy and Abortion", "Mental Health Treatment", "Vaccination",
                "End of Life Care", "Medical Research Ethics", "Alternative Medicine",
                "Health Insurance and Coverage"
            ],
            "icon": "🏥"
        },
        "technology_modern": {
            "title": "Technology & Modern Life Fiqh",
            "description": "Islamic rulings on modern technology and contemporary issues",
            "topics": [
                "Social Media and Internet", "Artificial Intelligence", "Gaming and Entertainment",
                "Digital Privacy and Security", "Online Business", "Remote Work",
                "Virtual Reality and Augmented Reality", "Blockchain Technology",
                "Smart Devices and IoT", "Digital Content Creation"
            ],
            "icon": "💻"
        },
        "environmental_social": {
            "title": "Environmental & Social Fiqh",
            "description": "Islamic rulings on environmental protection and social responsibility",
            "topics": [
                "Environmental Conservation", "Climate Change", "Sustainable Living",
                "Animal Rights and Welfare", "Community Service", "Social Justice",
                "Charity and Philanthropy", "Education and Learning", "Public Health",
                "Disaster Relief and Emergency Response"
            ],
            "icon": "🌍"
        },
        "contemporary_issues": {
            "title": "Contemporary Issues Fiqh",
            "description": "Islamic rulings on modern challenges and current events",
            "topics": [
                "Globalization and Cultural Exchange", "Refugee and Immigration",
                "International Relations", "Media and Journalism", "Sports and Recreation",
                "Arts and Entertainment", "Travel and Tourism", "Consumer Rights",
                "Workplace Ethics", "Family in Modern Society"
            ],
            "icon": "🌐"
        }
    }

def create_fiqh_topic_page(topic_key, topic_data):
    """Create a comprehensive fiqh topic page with search functionality"""
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic_data['title']} - Advanced Fiqh</title>
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

        .search-section {{
            background: var(--secondary-color);
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 2px 4px var(--shadow-color);
        }}

        .search-container {{
            display: flex;
            gap: 15px;
            margin-bottom: 20px;
        }}

        .search-input {{
            flex: 1;
            padding: 12px 20px;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            background: var(--primary-color);
            color: var(--text-color);
            font-size: 1rem;
        }}

        .search-input:focus {{
            outline: none;
            border-color: var(--accent-color);
        }}

        .search-button {{
            padding: 12px 24px;
            background: var(--accent-color);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s;
        }}

        .search-button:hover {{
            background: #45a049;
        }}

        .search-results {{
            margin-top: 20px;
            min-height: 100px;
        }}

        .result-item {{
            background: var(--primary-color);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
            border-left: 4px solid var(--accent-color);
            display: none;
        }}

        .result-item.show {{
            display: block;
        }}

        .result-title {{
            color: var(--accent-color);
            font-size: 1.2rem;
            margin-bottom: 10px;
        }}

        .result-content {{
            opacity: 0.9;
            line-height: 1.7;
        }}

        .topics-section {{
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

        .topics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}

        .topic-card {{
            background: var(--primary-color);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid var(--accent-color);
            transition: transform 0.3s;
        }}

        .topic-card:hover {{
            transform: translateY(-5px);
        }}

        .topic-card h3 {{
            color: var(--accent-color);
            margin-bottom: 10px;
        }}

        .topic-card p {{
            opacity: 0.9;
            margin-bottom: 15px;
        }}

        .topic-link {{
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }}

        .topic-link:hover {{
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
            
            .search-container {{
                flex-direction: column;
            }}
            
            .topics-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <a href="fiqh-index.html" class="back-button">← Back</a>
    <button class="theme-toggle" onclick="toggleTheme()">🌙 Theme</button>
    
    <div class="container">
        <div class="header">
            <h1>{topic_data['icon']} {topic_data['title']}</h1>
            <p>{topic_data['description']}</p>
        </div>

        <div class="search-section">
            <h2 class="section-title">🔍 Search Fiqh Topics</h2>
            <div class="search-container">
                <input type="text" class="search-input" id="searchInput" placeholder="Search for specific fiqh topics..." onkeyup="performSearch()">
                <button class="search-button" onclick="performSearch()">Search</button>
            </div>
            <div class="search-results" id="searchResults">
                <p style="text-align: center; opacity: 0.7;">Search results will appear here...</p>
            </div>
        </div>

        <div class="topics-section">
            <h2 class="section-title">📚 Available Topics</h2>
            <div class="topics-grid">
                {generate_topic_cards(topic_data['topics'])}
            </div>
        </div>
    </div>

    <script>
        // Fiqh content database
        const fiqhContent = {{
            {generate_fiqh_content_database(topic_data['topics'])}
        }};

        function performSearch() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const resultsContainer = document.getElementById('searchResults');
            
            if (searchTerm.length < 2) {{
                resultsContainer.innerHTML = '<p style="text-align: center; opacity: 0.7;">Search results will appear here...</p>';
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
                resultsContainer.innerHTML = '<p style="text-align: center; opacity: 0.7;">No results found for "' + searchTerm + '"</p>';
            }} else {{
                let resultsHTML = '<h3 style="color: var(--accent-color); margin-bottom: 15px;">Search Results:</h3>';
                results.forEach(result => {{
                    resultsHTML += `
                        <div class="result-item show">
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

def generate_topic_cards(topics):
    """Generate HTML for topic cards"""
    cards_html = ""
    for topic in topics:
        topic_key = topic.lower().replace(" ", "-").replace("&", "and")
        cards_html += f"""
                <div class="topic-card">
                    <h3>{topic}</h3>
                    <p>Comprehensive Islamic rulings and guidance on {topic.lower()} according to Islamic jurisprudence.</p>
                    <a href="#" class="topic-link" onclick="searchForTopic('{topic}')">Learn More</a>
                </div>"""
    return cards_html

def generate_fiqh_content_database(topics):
    """Generate JavaScript content database for search functionality"""
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

def create_all_advanced_fiqh_pages():
    """Create all advanced fiqh topic pages"""
    
    print("🔄 Creating advanced fiqh topic pages...")
    
    topics = get_advanced_fiqh_topics()
    pages_created = 0
    
    for topic_key, topic_data in topics.items():
        try:
            page_content = create_fiqh_topic_page(topic_key, topic_data)
            filename = f"{topic_key}.html"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            pages_created += 1
            print(f"✅ Created: {filename}")
            
        except Exception as e:
            print(f"❌ Error creating {filename}: {e}")
    
    print(f"\n🎉 Advanced fiqh pages creation completed!")
    print(f"📊 Total pages created: {pages_created}")
    print(f"🔍 All pages include search functionality")
    print(f"📚 Comprehensive fiqh content coverage")
    
    return pages_created

if __name__ == "__main__":
    try:
        pages_created = create_all_advanced_fiqh_pages()
        print(f"\n🎯 Creation Summary:")
        print(f"   • Advanced fiqh topic pages created: {pages_created}")
        print(f"   • Search functionality implemented")
        print(f"   • Comprehensive content coverage")
        print(f"   • Professional design maintained")
        
    except Exception as e:
        print(f"❌ Error during creation: {e}")
        print("Please check the files and try again.")
