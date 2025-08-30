#!/usr/bin/env python3
"""
Content Scanner for DeenBot
Scans all HTML content files to provide comprehensive Islamic knowledge access
"""

import os
import re
import json
from datetime import datetime
from bs4 import BeautifulSoup
import logging
import threading
import time

class IslamicContentScanner:
    """Comprehensive scanner for all Islamic knowledge content files"""
    
    def __init__(self):
        self.content_index = {}
        self.file_paths = []
        self.scan_complete = False
        self.scan_thread = None
        # Start with immediate scan for testing
        self.scan_all_content_sync()
    
    def start_background_scan(self):
        """Start background content scanning"""
        self.scan_thread = threading.Thread(target=self.scan_all_content, daemon=True)
        self.scan_thread.start()
        logging.info("🔍 Islamic content scanner started in background")
    
    def scan_all_content_sync(self):
        """Synchronous scan for immediate testing"""
        try:
            logging.info("📚 Starting synchronous Islamic content scan...")
            
            # Get all HTML files in the current directory
            html_files = []
            for file in os.listdir('.'):
                if file.endswith('.html') and not file.startswith('test-') and not file.startswith('deenbot-'):
                    html_files.append(file)
            
            logging.info(f"📖 Found {len(html_files)} content files to scan")
            
            for file_path in html_files:
                try:
                    self.scan_file_content(file_path)
                except Exception as e:
                    logging.warning(f"⚠️ Error scanning {file_path}: {e}")
            
            self.scan_complete = True
            logging.info(f"✅ Islamic content scan complete! Indexed {len(self.content_index)} knowledge sources")
            
        except Exception as e:
            logging.error(f"❌ Content scan failed: {e}")
    
    def scan_all_content(self):
        """Background scan method"""
        self.scan_all_content_sync()
    
    def scan_file_content(self, file_path):
        """Scan individual HTML file for Islamic knowledge content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse HTML content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract text content
            text_content = soup.get_text()
            
            # Extract headings and sections
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            
            # Create knowledge sections
            sections = []
            
            for heading in headings:
                if heading.get_text().strip():
                    section_title = heading.get_text().strip()
                    section_content = self.extract_section_content(heading, soup)
                    
                    if section_content:
                        sections.append({
                            'title': section_title,
                            'content': section_content,
                            'source': file_path
                        })
            
            # Also add full text as a searchable section
            if text_content.strip():
                sections.append({
                    'title': f'Full Content - {file_path}',
                    'content': text_content,
                    'source': file_path
                })
            
            # Store in index
            self.content_index[file_path] = {
                'sections': sections,
                'full_text': text_content,
                'last_updated': datetime.now().isoformat()
            }
            
            logging.info(f"📖 Scanned {file_path}: {len(sections)} sections found")
            
        except Exception as e:
            logging.warning(f"⚠️ Error scanning {file_path}: {e}")
    
    def extract_section_content(self, heading, soup):
        """Extract content for a specific section"""
        try:
            content = []
            current = heading.find_next_sibling()
            
            # Collect content until next heading
            while current and current.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                if current.name in ['p', 'div', 'li', 'span'] and current.get_text().strip():
                    content.append(current.get_text().strip())
                current = current.find_next_sibling()
            
            return ' '.join(content) if content else ""
            
        except Exception as e:
            return ""
    
    def search_content(self, query, max_results=5):
        """Search through all scanned content for relevant Islamic knowledge"""
        if not self.scan_complete:
            return []
        
        query_lower = query.lower()
        results = []
        
        for file_path, file_data in self.content_index.items():
            for section in file_data['sections']:
                relevance_score = self.calculate_relevance(query_lower, section)
                
                if relevance_score > 0.1:  # Lower threshold for better results
                    results.append({
                        'title': section['title'],
                        'content': section['content'][:500] + "..." if len(section['content']) > 500 else section['content'],
                        'source': section['source'],
                        'relevance': relevance_score
                    })
        
        # Sort by relevance and return top results
        results.sort(key=lambda x: x['relevance'], reverse=True)
        return results[:max_results]
    
    def calculate_relevance(self, query, section):
        """Calculate relevance score for a section"""
        try:
            title_score = 0
            content_score = 0
            
            # Check title relevance
            title_lower = section['title'].lower()
            for word in query.split():
                if word in title_lower:
                    title_score += 0.5
            
            # Check content relevance
            content_lower = section['content'].lower()
            for word in query.split():
                if word in content_lower:
                    content_score += 0.1
            
            # Bonus for exact phrase matches
            if query in content_lower:
                content_score += 0.3
            
            # Bonus for Islamic terms
            islamic_terms = ['hadith', 'sunnah', 'quran', 'fiqh', 'islam', 'muslim', 'prayer', 'fasting', 'charity']
            for term in islamic_terms:
                if term in content_lower and term in query_lower:
                    content_score += 0.2
            
            return title_score + content_score
            
        except Exception as e:
            return 0
    
    def get_comprehensive_response(self, query):
        """Get comprehensive response from scanned Islamic content"""
        try:
            # Search through local content first
            local_results = self.search_content(query)
            
            if local_results:
                # Format response from local content
                response = f"**Found in Islamic Knowledge Base:**\n\n"
                
                for i, result in enumerate(local_results, 1):
                    response += f"**{i}. {result['title']}**\n"
                    response += f"{result['content']}\n"
                    response += f"*Source: {result['source']}*\n\n"
                
                return response, local_results[0]['source']
            
            return None, None
            
        except Exception as e:
            logging.error(f"❌ Content search error: {e}")
            return None, None
    
    def get_status(self):
        """Get scanner status"""
        return {
            'scan_complete': self.scan_complete,
            'files_indexed': len(self.content_index),
            'total_sections': sum(len(data['sections']) for data in self.content_index.values()),
            'last_updated': datetime.now().isoformat()
        }

# Global instance
content_scanner = IslamicContentScanner()

if __name__ == "__main__":
    # Test the scanner
    print("Content Scanner Status:", content_scanner.get_status())
    print("\nTesting search for 'hadith':")
    results = content_scanner.search_content('hadith', max_results=3)
    print(f"Found {len(results)} results")
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']} - {result['source']}")
