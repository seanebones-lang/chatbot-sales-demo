#!/usr/bin/env python3

"""
Generate Individual Content Pages - Application Format
Creates individual content pages for all topics with exact index page design
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

        .content-text {{
            color: var(--text-secondary);
            line-height: 1.8;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }}

        .content-text h2 {{
            color: var(--accent-primary);
            font-size: 1.6rem;
            margin: 2rem 0 1rem 0;
            border-bottom: 2px solid var(--accent-primary);
            padding-bottom: 0.5rem;
        }}

        .content-text h3 {{
            color: var(--accent-secondary);
            font-size: 1.3rem;
            margin: 1.5rem 0 1rem 0;
        }}

        .content-text p {{
            margin-bottom: 1rem;
        }}

        .content-text ul, .content-text ol {{
            margin: 1rem 0 1rem 2rem;
        }}

        .content-text li {{
            margin-bottom: 0.5rem;
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

        <div class="search-section">
            <h3>Search {title}</h3>
            <div class="search-container">
                <input type="text" class="search-input" id="searchInput" placeholder="Search for specific topics..." onkeyup="performSearch()">
                <button class="search-button" onclick="performSearch()">Search</button>
            </div>
            <div class="search-results" id="searchResults">
                <p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>
            </div>
        </div>

        <div class="content-section">
            <h3>{content_title}</h3>
            <div class="content-text">
                {content_body}
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

        function performSearch() {{
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const resultsContainer = document.getElementById('searchResults');
            
            if (searchTerm.length < 2) {{
                resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Search results will appear here...</p>';
                return;
            }}
            
            // Placeholder search functionality
            resultsContainer.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">Search functionality will be implemented with comprehensive Islamic content database.</p>';
        }}
    </script>
</body>
</html>"""

def get_content_pages_structure():
    """Get the structure of all individual content pages to generate"""
    return {
        # Sunnah & Prophetic Traditions
        "daily-sunnah-practices": {
            "title": "Daily Sunnah Practices",
            "description": "Essential daily practices from the Prophet's life and teachings",
            "back_link": "sunnah-index.html",
            "back_text": "Sunnah Index",
            "content_title": "Daily Sunnah Practices",
            "content_body": """
                <h2>Essential Daily Practices from the Prophet's Life</h2>
                
                <h3>Morning Practices</h3>
                <p>The Prophet Muhammad (PBUH) began each day with specific practices that set the tone for the entire day. These practices are not only acts of worship but also contribute to physical and mental well-being.</p>
                
                <ul>
                    <li><strong>Fajr Prayer:</strong> The Prophet emphasized the importance of praying Fajr at its earliest time and staying in the mosque until sunrise.</li>
                    <li><strong>Morning Supplications:</strong> Reciting specific duas upon waking up and beginning the day.</li>
                    <li><strong>Miswak:</strong> Using the tooth stick (miswak) for oral hygiene, which the Prophet described as purifying for the mouth and pleasing to Allah.</li>
                </ul>
                
                <h3>Throughout the Day</h3>
                <p>During the day, the Prophet maintained several consistent practices that demonstrate his character and provide guidance for Muslims.</p>
                
                <ul>
                    <li><strong>Kindness to All:</strong> The Prophet was always kind to children, elderly, and animals, showing compassion in all interactions.</li>
                    <li><strong>Truthfulness:</strong> Maintaining honesty in all dealings, even in difficult situations.</li>
                    <li><strong>Patience:</strong> Demonstrating patience in adversity and with difficult people.</li>
                    <li><strong>Gratitude:</strong> Expressing thanks to Allah for blessings and to people for their kindness.</li>
                </ul>
                
                <h3>Evening Practices</h3>
                <p>As the day concluded, the Prophet had specific practices for reflection and preparation for the next day.</p>
                
                <ul>
                    <li><strong>Maghrib Prayer:</strong> Praying Maghrib at its proper time and making dua for the day's completion.</li>
                    <li><strong>Evening Supplications:</strong> Reciting protective duas before sleeping.</li>
                    <li><strong>Reflection:</strong> Taking time to reflect on the day's actions and seeking forgiveness for any mistakes.</li>
                </ul>
                
                <h3>Weekly Practices</h3>
                <p>Certain practices were performed weekly, contributing to community building and spiritual growth.</p>
                
                <ul>
                    <li><strong>Friday Prayer:</strong> Attending the congregational Friday prayer and listening to the khutbah.</li>
                    <li><strong>Family Time:</strong> Spending quality time with family members and showing them love and care.</li>
                    <li><strong>Charity:</strong> Giving in charity regularly, even if it's a small amount.</li>
                </ul>
                
                <h3>Benefits of Following Sunnah</h3>
                <p>Following these daily practices brings numerous benefits:</p>
                
                <ul>
                    <li><strong>Spiritual Growth:</strong> Regular connection with Allah through worship and remembrance.</li>
                    <li><strong>Character Development:</strong> Building positive character traits through consistent practice.</li>
                    <li><strong>Community Building:</strong> Strengthening relationships with family and community members.</li>
                    <li><strong>Mental Well-being:</strong> Creating structure and purpose in daily life.</li>
                </ul>
                
                <p>These practices are not meant to be burdensome but rather to enhance the quality of life and bring one closer to Allah. The Prophet's example shows that a balanced life includes worship, work, family, and community service.</p>
            """
        },
        
        "prophetic-character": {
            "title": "Prophetic Character",
            "description": "Moral qualities and character traits of Prophet Muhammad (PBUH)",
            "back_link": "sunnah-index.html",
            "back_text": "Sunnah Index",
            "content_title": "Prophetic Character",
            "content_body": """
                <h2>The Noble Character of Prophet Muhammad (PBUH)</h2>
                
                <h3>Truthfulness and Honesty</h3>
                <p>Prophet Muhammad (PBUH) was known as "Al-Amin" (the trustworthy) even before his prophethood. His honesty was so well-known that people would entrust him with their valuables. The Prophet said: "Truthfulness leads to righteousness, and righteousness leads to Paradise."</p>
                
                <h3>Kindness and Compassion</h3>
                <p>The Prophet showed extraordinary kindness to all creation. He was gentle with children, respectful to the elderly, and kind to animals. He said: "The merciful will be shown mercy by the Most Merciful. Be merciful to those on earth, and the One above the heavens will be merciful to you."</p>
                
                <h3>Patience and Perseverance</h3>
                <p>Throughout his mission, the Prophet demonstrated remarkable patience in the face of persecution, loss, and difficulties. He endured years of hardship in Makkah with dignity and never retaliated against his persecutors. His patience serves as a model for all Muslims.</p>
                
                <h3>Humility and Modesty</h3>
                <p>Despite being the leader of a growing community and receiving divine revelation, the Prophet remained humble. He would sit on the ground, eat simple food, and never sought special treatment. He said: "Allah has revealed to me that you should be humble so that no one oppresses another."</p>
                
                <h3>Justice and Fairness</h3>
                <p>The Prophet was known for his absolute fairness in all matters. He would judge between people impartially, regardless of their status or relationship to him. He said: "If my daughter Fatima were to steal, I would cut off her hand." This demonstrates his commitment to justice above all personal considerations.</p>
                
                <h3>Forgiveness and Mercy</h3>
                <p>One of the most remarkable aspects of the Prophet's character was his ability to forgive. When he conquered Makkah, he forgave those who had persecuted him and his followers. He said: "The best among you are those who have the best character."</p>
                
                <h3>Generosity and Charity</h3>
                <p>The Prophet was extremely generous and would give away whatever he had to help others. He never kept wealth for himself and lived a simple life. His generosity extended beyond material things to include his time, knowledge, and compassion.</p>
                
                <h3>Respect for Women</h3>
                <p>The Prophet showed great respect for women and elevated their status in society. He said: "The best of you are those who are best to their wives." He treated women with dignity and respect, setting an example for all men to follow.</p>
                
                <h3>Environmental Consciousness</h3>
                <p>The Prophet taught respect for the environment and all living creatures. He said: "If the Hour (Day of Judgment) is about to be established and one of you was holding a palm seedling, let him take advantage of even one second before the Hour is established to plant it."</p>
                
                <h3>Community Service</h3>
                <p>The Prophet actively served his community, helping the poor, visiting the sick, and participating in community activities. He said: "The believer is like a building, each part supporting the other."</p>
                
                <h3>Learning and Teaching</h3>
                <p>The Prophet was a lifelong learner and teacher. He encouraged seeking knowledge and said: "Seeking knowledge is obligatory for every Muslim." He would teach people of all ages and backgrounds, adapting his teaching style to their needs.</p>
                
                <p>The character of Prophet Muhammad (PBUH) serves as the perfect example for all Muslims. His life demonstrates that it is possible to achieve spiritual greatness while maintaining excellent character and serving humanity. Following his example leads to personal fulfillment and contributes to building a better society.</p>
            """
        },
        
        # Islamic Beliefs & Theology
        "six-articles-of-faith": {
            "title": "Six Articles of Faith",
            "description": "Belief in Allah, angels, books, messengers, Day of Judgment, and divine decree",
            "back_link": "aqeedah-index.html",
            "back_text": "Aqeedah Index",
            "content_title": "The Six Articles of Faith",
            "content_body": """
                <h2>The Six Articles of Faith in Islam</h2>
                
                <p>The six articles of faith (Arkan al-Iman) form the foundation of Islamic belief. These are the core beliefs that every Muslim must accept and believe in with certainty.</p>
                
                <h3>1. Belief in Allah (Tawheed)</h3>
                <p>Belief in Allah is the most fundamental article of faith. Muslims believe in:</p>
                <ul>
                    <li><strong>Oneness of Allah:</strong> There is no god but Allah, and He has no partners or equals.</li>
                    <li><strong>Divine Attributes:</strong> Allah possesses perfect attributes such as knowledge, power, mercy, and wisdom.</li>
                    <li><strong>Worship:</strong> Only Allah deserves to be worshipped, and no one else should be associated with Him in worship.</li>
                </ul>
                
                <h3>2. Belief in Angels (Malaika)</h3>
                <p>Angels are spiritual beings created by Allah from light. Muslims believe in:</p>
                <ul>
                    <li><strong>Existence:</strong> Angels are real beings, not metaphorical or symbolic.</li>
                    <li><strong>Functions:</strong> Angels have specific duties assigned by Allah, such as recording deeds, delivering messages, and managing natural phenomena.</li>
                    <li><strong>Names:</strong> Some angels are known by name, such as Jibreel (Gabriel), Mikail (Michael), and Israfil.</li>
                </ul>
                
                <h3>3. Belief in Divine Books (Kutub)</h3>
                <p>Allah has revealed books to guide humanity. Muslims believe in:</p>
                <ul>
                    <li><strong>Previous Books:</strong> The Torah (Tawrat), Psalms (Zabur), and Gospel (Injeel) were revealed to previous prophets.</li>
                    <li><strong>The Quran:</strong> The final and complete revelation to Prophet Muhammad (PBUH), which confirms and supersedes previous revelations.</li>
                    <li><strong>Preservation:</strong> The Quran is perfectly preserved in its original form, unlike previous books that have been altered.</li>
                </ul>
                
                <h3>4. Belief in Prophets and Messengers (Rusul)</h3>
                <p>Allah has sent prophets and messengers to guide humanity. Muslims believe in:</p>
                <ul>
                    <li><strong>All Prophets:</strong> All prophets sent by Allah, including Adam, Noah, Abraham, Moses, Jesus, and Muhammad (PBUH).</li>
                    <li><strong>Finality:</strong> Prophet Muhammad (PBUH) is the final prophet, and no prophet will come after him.</li>
                    <li><strong>Infallibility:</strong> Prophets are protected from major sins and errors in conveying Allah's message.</li>
                </ul>
                
                <h3>5. Belief in the Day of Judgment (Yawm al-Qiyamah)</h3>
                <p>There will be a day when all people will be resurrected and judged. Muslims believe in:</p>
                <ul>
                    <li><strong>Resurrection:</strong> All people will be brought back to life on the Day of Judgment.</li>
                    <li><strong>Accountability:</strong> Every person will be held accountable for their beliefs and actions.</li>
                    <li><strong>Reward and Punishment:</strong> People will be rewarded for good deeds and punished for bad deeds, with Allah's mercy and justice.</li>
                </ul>
                
                <h3>6. Belief in Divine Decree (Qadr)</h3>
                <p>Everything that happens is according to Allah's knowledge and will. Muslims believe in:</p>
                <ul>
                    <li><strong>Allah's Knowledge:</strong> Allah knows everything that has happened, is happening, and will happen.</li>
                    <li><strong>Allah's Will:</strong> Nothing happens except by Allah's permission and will.</li>
                    <li><strong>Human Choice:</strong> While Allah knows our choices, humans have free will and are responsible for their actions.</li>
                </ul>
                
                <h3>Importance of These Beliefs</h3>
                <p>These six articles of faith are essential because:</p>
                <ul>
                    <li>They provide a complete worldview that explains the purpose of life and existence.</li>
                    <li>They establish the relationship between Allah and His creation.</li>
                    <li>They guide moral and ethical behavior.</li>
                    <li>They provide comfort and hope in difficult times.</li>
                    <li>They unite Muslims around common beliefs and values.</li>
                </ul>
                
                <p>Understanding and believing in these articles of faith is the foundation of Islamic practice. They are not just intellectual concepts but living beliefs that should influence every aspect of a Muslim's life.</p>
            """
        },
        
        # Islamic Supplications
        "morning-evening-duas": {
            "title": "Morning and Evening Duas",
            "description": "Essential supplications for beginning and ending the day",
            "back_link": "duas-index.html",
            "back_text": "Duas Index",
            "content_title": "Morning and Evening Supplications",
            "content_body": """
                <h2>Essential Morning and Evening Supplications</h2>
                
                <p>Morning and evening supplications are an important part of a Muslim's daily routine. These duas help protect us throughout the day and night and keep us connected to Allah.</p>
                
                <h3>Morning Supplications</h3>
                <p>Upon waking up in the morning, Muslims should recite these supplications:</p>
                
                <h4>1. Dua upon Waking Up</h4>
                <p><strong>Arabic:</strong> الحمد لله الذي أحيانا بعد ما أماتنا وإليه النشور</p>
                <p><strong>Transliteration:</strong> Alhamdu lillahil-lathee ahyana ba'da ma amatana wa ilayhin-nushoor</p>
                <p><strong>Translation:</strong> "All praise is for Allah who gave us life after causing us to die (sleep) and unto Him is the resurrection."</p>
                
                <h4>2. Dua for Morning Protection</h4>
                <p><strong>Arabic:</strong> أصبحنا وأصبح الملك لله والحمد لله لا إله إلا الله وحده لا شريك له</p>
                <p><strong>Transliteration:</strong> Asbahna wa asbahal-mulku lillah, walhamdu lillah, la ilaha illallahu wahdahu la shareeka lah</p>
                <p><strong>Translation:</strong> "We have reached the morning and at this very time all sovereignty belongs to Allah. All praise is for Allah. None has the right to be worshipped except Allah, alone, without any partner."</p>
                
                <h4>3. Ayat al-Kursi</h4>
                <p>Reciting Ayat al-Kursi (Quran 2:255) in the morning provides protection throughout the day.</p>
                
                <h3>Evening Supplications</h3>
                <p>In the evening, before sleeping, Muslims should recite these supplications:</p>
                
                <h4>1. Dua for Evening Protection</h4>
                <p><strong>Arabic:</strong> أمسينا وأمسى الملك لله والحمد لله لا إله إلا الله وحده لا شريك له</p>
                <p><strong>Transliteration:</strong> Amsayna wa amsal-mulku lillah, walhamdu lillah, la ilaha illallahu wahdahu la shareeka lah</p>
                <p><strong>Translation:</strong> "We have reached the evening and at this very time all sovereignty belongs to Allah. All praise is for Allah. None has the right to be worshipped except Allah, alone, without any partner."</p>
                
                <h4>2. Dua before Sleeping</h4>
                <p><strong>Arabic:</strong> باسمك ربي وضعت جنبي وبك أرفعه فإن أمسكت نفسي فارحمها وإن أرسلتها فاحفظها بما تحفظ به عبادك الصالحين</p>
                <p><strong>Transliteration:</strong> Bismika rabbee wada'tu janbee wa bika arfa'uh, fa in amsakta nafsee farhamhaa, wa in arsaltahaa fahfadhhaa bimaa tahfadhu bihi 'ibaadakas-saaliheen</p>
                <p><strong>Translation:</strong> "In Your name, my Lord, I lay down my side, and in Your name I raise it. If You should take my soul, then have mercy upon it, and if You should return my soul, then protect it as You protect Your righteous servants."</p>
                
                <h4>3. The Three Quls</h4>
                <p>Recite Surah Al-Ikhlas, Al-Falaq, and An-Nas three times each for protection during sleep.</p>
                
                <h3>Benefits of Morning and Evening Duas</h3>
                <p>Reciting these supplications regularly provides numerous benefits:</p>
                <ul>
                    <li><strong>Protection:</strong> These duas protect us from harm and evil throughout the day and night.</li>
                    <li><strong>Connection with Allah:</strong> They keep us mindful of Allah and strengthen our relationship with Him.</li>
                    <li><strong>Gratitude:</strong> They help us express gratitude for Allah's blessings and protection.</li>
                    <li><strong>Discipline:</strong> They establish a daily routine of remembrance and worship.</li>
                    <li><strong>Peace of Mind:</strong> They provide comfort and reassurance in our daily lives.</li>
                </ul>
                
                <h3>When to Recite</h3>
                <p>These supplications should be recited:</p>
                <ul>
                    <li><strong>Morning:</strong> After Fajr prayer or when starting the day's activities.</li>
                    <li><strong>Evening:</strong> After Maghrib prayer or before going to sleep.</li>
                    <li><strong>Consistently:</strong> Make it a habit to recite them daily without fail.</li>
                </ul>
                
                <p>Making these supplications a regular part of your daily routine will bring blessings, protection, and spiritual growth. They are simple yet powerful ways to stay connected to Allah throughout the day.</p>
            """
        }
    }

def create_content_page_with_exact_design(page_key, page_data):
    """Create a content page with exact index page design - NO EMOJIS"""
    
    # Additional sections if needed
    additional_sections = ""
    
    # Fill template with exact design
    page_content = get_exact_index_page_design().format(
        title=page_data['title'],
        description=page_data['description'],
        back_link=page_data['back_link'],
        back_text=page_data['back_text'],
        content_title=page_data['content_title'],
        content_body=page_data['content_body'],
        additional_sections=additional_sections
    )
    
    return page_content

def generate_all_content_pages():
    """Generate all individual content pages with exact index page design"""
    
    print("Generating all individual content pages...")
    print("Using exact index page design - NO EMOJIS")
    print("This is a serious Islamic research application")
    
    structure = get_content_pages_structure()
    pages_generated = 0
    
    for page_key, page_data in structure.items():
        try:
            # Create page with exact design
            page_content = create_content_page_with_exact_design(page_key, page_data)
            filename = f"{page_key}.html"
            
            # Write the generated page
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(page_content)
            
            pages_generated += 1
            print(f"Generated: {filename} - Now matches index page design exactly")
            
        except Exception as e:
            print(f"Error generating {page_key}: {e}")
    
    print(f"\nAll content pages generated!")
    print(f"Total pages generated: {pages_generated}")
    print(f"Design now matches index page exactly")
    print(f"NO EMOJIS - Serious Islamic research application design")
    
    return pages_generated

if __name__ == "__main__":
    try:
        pages_generated = generate_all_content_pages()
        print(f"\nGeneration Summary:")
        print(f"   All content pages now generated in application format")
        print(f"   Same CSS variables, fonts, colors, and layout")
        print(f"   Same header, content sections, and styling")
        print(f"   NO EMOJIS - Professional Islamic research interface")
        
    except Exception as e:
        print(f"Error during generation: {e}")
        print("Please check the files and try again.")
