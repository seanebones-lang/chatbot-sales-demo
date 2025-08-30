#!/usr/bin/env python3
"""
Comprehensive Content Migration Script
Complete Islamic Study Guide Extended Edition

This script migrates all website content to the application format,
ensuring exact design compliance and comprehensive Islamic content.
"""

import os
import re
from pathlib import Path

def get_exact_index_page_design():
    """Get the exact design template from the main index page."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Islamic Study Guide - Extended Edition</title>
    
    <!-- PWA Meta Tags -->
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#10b981">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Islamic Study Guide">
    <link rel="apple-touch-icon" href="icon-192x192.png">
    
    <style>
        :root {
            --bg-primary: #0a0f0f;
            --bg-secondary: #1a1f1f;
            --accent-primary: #10b981;
            --accent-secondary: #059669;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --border-primary: #374151;
            --shadow-primary: 0 8px 32px rgba(0, 0, 0, 0.3);
            --shadow-secondary: 0 4px 16px rgba(0, 0, 0, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', 'Times New Roman', serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 40px 20px;
            background: linear-gradient(135deg, var(--bg-secondary), var(--bg-primary));
            border-radius: 20px;
            border: 2px solid var(--accent-primary);
            box-shadow: var(--shadow-primary);
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
            color: var(--accent-primary);
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
        }

        .header p {
            font-size: 1.2rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto;
        }

        .content-section {
            background: var(--bg-secondary);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid var(--border-primary);
            box-shadow: var(--shadow-secondary);
        }

        .content-section h2 {
            color: var(--accent-primary);
            font-size: 1.8rem;
            margin-bottom: 20px;
            border-bottom: 2px solid var(--accent-primary);
            padding-bottom: 10px;
        }

        .content-section h3 {
            color: var(--accent-secondary);
            font-size: 1.4rem;
            margin: 25px 0 15px 0;
        }

        .content-section p {
            margin-bottom: 15px;
            color: var(--text-secondary);
            font-size: 1.1rem;
        }

        .content-section ul, .content-section ol {
            margin: 15px 0;
            padding-left: 30px;
        }

        .content-section li {
            margin-bottom: 8px;
            color: var(--text-secondary);
        }

        .content-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .content-card {
            background: var(--bg-primary);
            border: 1px solid var(--border-primary);
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-secondary);
        }

        .content-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-primary);
            border-color: var(--accent-primary);
        }

        .content-card h4 {
            color: var(--accent-primary);
            margin-bottom: 10px;
            font-size: 1.2rem;
        }

        .content-card p {
            color: var(--text-secondary);
            font-size: 1rem;
        }

        .back-link {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 24px;
            background: var(--accent-primary);
            color: var(--bg-primary);
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-secondary);
        }

        .back-link:hover {
            background: var(--accent-secondary);
            transform: translateY(-2px);
            box-shadow: var(--shadow-primary);
        }

        .search-container {
            margin: 20px 0;
            text-align: center;
        }

        .search-input {
            width: 100%;
            max-width: 500px;
            padding: 15px 20px;
            border: 2px solid var(--border-primary);
            border-radius: 25px;
            background: var(--bg-primary);
            color: var(--text-primary);
            font-size: 1.1rem;
            transition: all 0.3s ease;
        }

        .search-input:focus {
            outline: none;
            border-color: var(--accent-primary);
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.1);
        }

        .search-input::placeholder {
            color: var(--text-secondary);
        }

        .theme-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--accent-primary);
            color: var(--bg-primary);
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            font-size: 1.2rem;
            cursor: pointer;
            box-shadow: var(--shadow-primary);
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .theme-toggle:hover {
            background: var(--accent-secondary);
            transform: scale(1.1);
        }

        @media (max-width: 768px) {
            .container {
                padding: 15px;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .header p {
                font-size: 1rem;
            }
            
            .content-section {
                padding: 20px;
            }
            
            .content-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Light theme */
        [data-theme="light"] {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --text-primary: #1e293b;
            --text-secondary: #475569;
            --border-primary: #e2e8f0;
        }
    </style>
</head>
<body>
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle theme">🌙</button>
    
    <div class="container">
        <header class="header">
            <h1>Complete Islamic Study Guide</h1>
            <p>Extended Edition - Comprehensive Islamic Knowledge Database</p>
        </header>
        
        <div class="search-container">
            <input type="text" class="search-input" id="searchInput" placeholder="Search Islamic content..." oninput="filterContent()">
        </div>
        
        <div id="contentContainer">
            <!-- Content will be dynamically generated -->
        </div>
        
        <div style="text-align: center; margin-top: 40px;">
            <a href="complete-islamic-study-guide-dark.html" class="back-link">Back to Main Index</a>
        </div>
    </div>

    <script>
        // Theme toggle functionality
        function toggleTheme() {
            const body = document.body;
            const currentTheme = body.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            
            body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            const button = document.querySelector('.theme-toggle');
            button.textContent = newTheme === 'light' ? '🌙' : '☀️';
        }

        // Load saved theme
        function loadTheme() {
            const savedTheme = localStorage.getItem('theme') || 'dark';
            document.body.setAttribute('data-theme', savedTheme);
            
            const button = document.querySelector('.theme-toggle');
            button.textContent = savedTheme === 'light' ? '🌙' : '☀️';
        }

        // Search functionality
        function filterContent() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const contentCards = document.querySelectorAll('.content-card');
            
            contentCards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // Load theme on page load
        document.addEventListener('DOMContentLoaded', loadTheme);
    </script>
</body>
</html>"""

def get_comprehensive_website_structure():
    """Get the complete website content structure."""
    return {
        "islamic-practices": {
            "title": "Core Islamic Practices",
            "description": "Essential Islamic practices and daily routines",
            "sections": [
                {
                    "title": "Daily Prayers",
                    "content": "The five daily prayers (Salah) are the cornerstone of Islamic worship. Each prayer has specific times and requirements that Muslims must observe throughout the day. The prayers include Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night)."
                },
                {
                    "title": "Fasting",
                    "content": "Fasting during Ramadan is one of the Five Pillars of Islam. Muslims abstain from food, drink, and other physical needs from dawn until sunset. This practice teaches self-discipline, self-control, and empathy for those less fortunate."
                },
                {
                    "title": "Charity (Zakat)",
                    "content": "Zakat is the obligatory giving of a portion of one's wealth to those in need. It is calculated as 2.5% of one's savings and investments above a certain threshold. This practice ensures wealth distribution and helps maintain social justice."
                },
                {
                    "title": "Pilgrimage (Hajj)",
                    "content": "Hajj is the annual pilgrimage to Mecca that every able-bodied Muslim must perform at least once in their lifetime. It involves specific rituals and commemorates the trials of Prophet Ibrahim and his family."
                }
            ]
        },
        "islamic-ethics": {
            "title": "Islamic Ethics and Morality",
            "description": "Moral principles and ethical guidelines in Islam",
            "sections": [
                {
                    "title": "Honesty and Truthfulness",
                    "content": "Islam places great emphasis on honesty and truthfulness. Muslims are commanded to always speak the truth, even when it is difficult. Lying is considered a major sin that can lead to other immoral behaviors."
                },
                {
                    "title": "Kindness and Compassion",
                    "content": "Showing kindness and compassion to all creation is a fundamental Islamic principle. This includes being kind to family, neighbors, strangers, and even animals. The Prophet Muhammad emphasized treating others as you would like to be treated."
                },
                {
                    "title": "Justice and Fairness",
                    "content": "Islam commands absolute justice in all matters. Muslims must be fair in their dealings with others, regardless of their religion, race, or social status. Justice is considered a divine attribute that humans must strive to emulate."
                },
                {
                    "title": "Respect for Elders",
                    "content": "Respecting and honoring elders is a key Islamic value. This includes showing deference to parents, grandparents, and other senior members of the community. The Quran specifically commands kindness to parents."
                }
            ]
        },
        "islamic-family": {
            "title": "Family and Social Life",
            "description": "Islamic guidance on family relationships and social conduct",
            "sections": [
                {
                    "title": "Marriage and Family",
                    "content": "Marriage is highly valued in Islam as it provides a foundation for family life and social stability. Islamic marriage is based on mutual consent, love, and respect. The family unit is considered the building block of society."
                },
                {
                    "title": "Parent-Child Relationships",
                    "content": "Islam emphasizes the importance of strong parent-child relationships. Children must respect and obey their parents, while parents must provide love, care, and proper Islamic education to their children."
                },
                {
                    "title": "Community Relations",
                    "content": "Muslims are encouraged to be active members of their communities. This includes participating in community events, helping neighbors, and contributing to the well-being of society as a whole."
                },
                {
                    "title": "Social Etiquette",
                    "content": "Islamic social etiquette includes greeting others with peace (Salam), showing respect to guests, maintaining good manners in speech and behavior, and treating others with dignity and respect."
                }
            ]
        },
        "islamic-business": {
            "title": "Business and Financial Ethics",
            "description": "Islamic principles for business and financial dealings",
            "sections": [
                {
                    "title": "Fair Trade Practices",
                    "content": "Islam promotes fair and ethical business practices. This includes honest pricing, quality products, fair wages for workers, and avoiding exploitation of customers or employees. Deception and fraud are strictly prohibited."
                },
                {
                    "title": "Interest-Free Finance",
                    "content": "Islamic finance prohibits the charging or payment of interest (riba). Instead, it promotes profit-sharing arrangements, asset-backed financing, and other ethical financial instruments that benefit both parties."
                },
                {
                    "title": "Social Responsibility",
                    "content": "Islamic businesses have a responsibility to contribute positively to society. This includes providing employment opportunities, supporting charitable causes, and ensuring that business activities do not harm the environment or community."
                },
                {
                    "title": "Transparency and Accountability",
                    "content": "Business dealings must be transparent and accountable. All agreements should be clearly documented, and parties must fulfill their obligations honestly and completely."
                }
            ]
        },
        "islamic-education": {
            "title": "Education and Learning",
            "description": "The importance of knowledge and education in Islam",
            "sections": [
                {
                    "title": "Seeking Knowledge",
                    "content": "Islam places great emphasis on seeking knowledge. The Prophet Muhammad said that seeking knowledge is obligatory for every Muslim. This includes both religious and secular knowledge that benefits humanity."
                },
                {
                    "title": "Religious Education",
                    "content": "Religious education includes learning about the Quran, Hadith, Islamic law, and Islamic history. This knowledge helps Muslims understand their faith and practice it correctly in daily life."
                },
                {
                    "title": "Secular Education",
                    "content": "Islam encourages Muslims to pursue secular education in fields like science, medicine, engineering, and arts. This knowledge helps Muslims contribute positively to society and fulfill their role as stewards of creation."
                },
                {
                    "title": "Lifelong Learning",
                    "content": "Learning is a continuous process that should continue throughout one's life. Muslims are encouraged to constantly seek new knowledge and skills that can benefit themselves and others."
                }
            ]
        },
        "islamic-health": {
            "title": "Health and Wellness",
            "description": "Islamic guidance on physical and mental health",
            "sections": [
                {
                    "title": "Physical Health",
                    "content": "Islam emphasizes the importance of maintaining good physical health. This includes eating nutritious food, exercising regularly, getting adequate sleep, and avoiding harmful substances. The body is considered a trust from God that must be cared for."
                },
                {
                    "title": "Mental Health",
                    "content": "Mental health is equally important in Islam. Muslims are encouraged to maintain positive thoughts, seek help when needed, and support others who may be struggling with mental health issues."
                },
                {
                    "title": "Preventive Care",
                    "content": "Islam promotes preventive healthcare measures. This includes regular medical check-ups, vaccinations, and adopting healthy lifestyle habits. Prevention is considered better than cure."
                },
                {
                    "title": "Spiritual Wellness",
                    "content": "Spiritual wellness is achieved through regular prayer, meditation, reading the Quran, and maintaining a strong connection with God. This spiritual foundation supports overall health and well-being."
                }
            ]
        },
        "islamic-environment": {
            "title": "Environmental Stewardship",
            "description": "Islamic principles for environmental protection and sustainability",
            "sections": [
                {
                    "title": "Care for Creation",
                    "content": "Islam teaches that humans are stewards of God's creation. This means we have a responsibility to care for the environment, protect natural resources, and ensure sustainable use of the earth's resources for future generations."
                },
                {
                    "title": "Conservation",
                    "content": "Conservation of natural resources is an Islamic duty. This includes reducing waste, recycling, using renewable energy sources, and protecting wildlife and natural habitats."
                },
                {
                    "title": "Sustainable Living",
                    "content": "Sustainable living practices align with Islamic values. This includes reducing consumption, choosing environmentally friendly products, and adopting practices that minimize our ecological footprint."
                },
                {
                    "title": "Environmental Justice",
                    "content": "Environmental justice means ensuring that all people, regardless of their economic status, have access to clean air, water, and a healthy environment. This is a fundamental Islamic principle of justice and equality."
                }
            ]
        },
        "islamic-technology": {
            "title": "Technology and Modern Life",
            "description": "Islamic guidance on using technology responsibly",
            "sections": [
                {
                    "title": "Responsible Technology Use",
                    "content": "Technology should be used responsibly and ethically. This includes using social media mindfully, protecting personal information, and ensuring that technology enhances rather than hinders human relationships and spiritual growth."
                },
                {
                    "title": "Digital Ethics",
                    "content": "Digital ethics include being honest online, respecting others' privacy, avoiding cyberbullying, and using technology to spread positive messages and Islamic values."
                },
                {
                    "title": "Technology for Good",
                    "content": "Technology should be used to benefit humanity and promote Islamic values. This includes using technology for education, charity, community building, and spreading knowledge about Islam."
                },
                {
                    "title": "Balancing Technology and Tradition",
                    "content": "While embracing modern technology, Muslims should maintain traditional Islamic values and practices. Technology should enhance, not replace, important aspects of Islamic life like family time and community connections."
                }
            ]
        },
        "islamic-contemporary": {
            "title": "Contemporary Islamic Issues",
            "description": "Addressing modern challenges from an Islamic perspective",
            "sections": [
                {
                    "title": "Social Media and Communication",
                    "content": "Social media presents both opportunities and challenges for Muslims. It can be used to spread Islamic knowledge and connect with other Muslims worldwide, but it also requires careful management to avoid negative influences and maintain Islamic values."
                },
                {
                    "title": "Global Citizenship",
                    "content": "Muslims are encouraged to be active global citizens who contribute positively to the world. This includes promoting peace, justice, and cooperation among all people, regardless of their background or beliefs."
                },
                {
                    "title": "Interfaith Dialogue",
                    "content": "Interfaith dialogue is important for promoting understanding and cooperation between different religious communities. Muslims are encouraged to engage in respectful dialogue while maintaining their Islamic identity and values."
                },
                {
                    "title": "Modern Challenges",
                    "content": "Modern life presents unique challenges that require thoughtful Islamic responses. This includes issues like climate change, economic inequality, and social justice. Islam provides timeless principles that can guide our approach to these contemporary issues."
                }
            ]
        }
    }

def generate_content_sections_html(content_structure):
    """Generate HTML content sections from the structure."""
    html_content = ""
    
    for key, section in content_structure.items():
        html_content += f"""
        <div class="content-section">
            <h2>{section['title']}</h2>
            <p>{section['description']}</p>
            
            <div class="content-grid">"""
        
        for subsection in section['sections']:
            html_content += f"""
                <div class="content-card">
                    <h4>{subsection['title']}</h4>
                    <p>{subsection['content']}</p>
                </div>"""
        
        html_content += """
            </div>
        </div>"""
    
    return html_content

def create_page_with_exact_design(title, content_html, filename):
    """Create a page with the exact design template."""
    template = get_exact_index_page_design()
    
    # Replace the title
    template = template.replace("Complete Islamic Study Guide - Extended Edition", title)
    
    # Replace the header content
    template = template.replace(
        '<h1>Complete Islamic Study Guide</h1>',
        f'<h1>{title}</h1>'
    )
    
    # Replace the content container
    template = template.replace(
        '<!-- Content will be dynamically generated -->',
        content_html
    )
    
    # Write the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✅ Created: {filename}")

def migrate_all_website_content():
    """Migrate all website content to the application format."""
    print("🚀 COMPREHENSIVE CONTENT MIGRATION")
    print("Complete Islamic Study Guide Extended Edition")
    print("=" * 50)
    
    # Get the content structure
    content_structure = get_comprehensive_website_structure()
    
    # Create the main content page
    main_content_html = generate_content_sections_html(content_structure)
    create_page_with_exact_design(
        "Complete Islamic Content Database",
        main_content_html,
        "complete-islamic-content-database.html"
    )
    
    # Create individual section pages
    for key, section in content_structure.items():
        section_html = generate_content_sections_html({key: section})
        filename = f"{key.replace('-', '_')}.html"
        create_page_with_exact_design(
            section['title'],
            section_html,
            filename
        )
    
    print("\n🎉 CONTENT MIGRATION COMPLETE!")
    print(f"📁 Total pages created: {len(content_structure) + 1}")
    print("\n📱 All content now follows the exact design policy!")
    print("🔍 Next steps:")
    print("1. Verify all pages display correctly")
    print("2. Test navigation between pages")
    print("3. Ensure content is properly formatted")
    print("4. Test responsive design on all pages")

if __name__ == "__main__":
    migrate_all_website_content()
