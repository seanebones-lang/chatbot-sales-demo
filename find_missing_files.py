#!/usr/bin/env python3
"""
Script to find missing HTML files referenced in the main guide
"""

import re
import os
from pathlib import Path

def extract_html_links(html_file):
    """Extract all HTML file links from the main guide"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all href="filename.html" patterns
    pattern = r'href="([^"]*\.html)"'
    matches = re.findall(pattern, content)
    
    # Remove duplicates and sort
    unique_links = sorted(list(set(matches)))
    return unique_links

def check_existing_files(links):
    """Check which files exist and which are missing"""
    existing = []
    missing = []
    
    for link in links:
        if os.path.exists(link):
            existing.append(link)
        else:
            missing.append(link)
    
    return existing, missing

def main():
    main_file = "complete-islamic-study-guide-dark.html"
    
    if not os.path.exists(main_file):
        print(f"Error: {main_file} not found!")
        return
    
    print("Analyzing missing HTML files...")
    print("=" * 50)
    
    # Extract all HTML links
    links = extract_html_links(main_file)
    print(f"Total HTML links found: {len(links)}")
    
    # Check which exist and which are missing
    existing, missing = check_existing_files(links)
    
    print(f"\nExisting files: {len(existing)}")
    print(f"Missing files: {len(missing)}")
    
    print("\n" + "=" * 50)
    print("MISSING FILES:")
    print("=" * 50)
    
    # Group missing files by category
    categories = {
        'Index Files': [f for f in missing if 'index' in f.lower()],
        'Quran Files': [f for f in missing if 'quran' in f.lower() or 'surah' in f.lower()],
        'Hadith Files': [f for f in missing if 'hadith' in f.lower() or any(x in f.lower() for x in ['bukhari', 'muslim', 'dawud', 'tirmidhi', 'nasai', 'majah'])],
        'Fiqh Files': [f for f in missing if 'fiqh' in f.lower()],
        'Sunnah Files': [f for f in missing if 'sunnah' in f.lower()],
        'Duas Files': [f for f in missing if 'duas' in f.lower()],
        'General Islamic': [f for f in missing if not any(x in f.lower() for x in ['index', 'quran', 'hadith', 'fiqh', 'sunnah', 'duas'])],
    }
    
    for category, files in categories.items():
        if files:
            print(f"\n{category}:")
            for file in sorted(files):
                print(f"  - {file}")
    
    # Save missing files list
    with open('missing_files_list.txt', 'w') as f:
        f.write("Missing HTML Files\n")
        f.write("=" * 30 + "\n\n")
        for category, files in categories.items():
            if files:
                f.write(f"{category}:\n")
                for file in sorted(files):
                    f.write(f"  - {file}\n")
                f.write("\n")
    
    print(f"\nMissing files list saved to: missing_files_list.txt")
    print(f"\nTotal missing files to create: {len(missing)}")

if __name__ == "__main__":
    main()
