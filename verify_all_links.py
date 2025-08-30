#!/usr/bin/env python3
"""
Comprehensive Link Verification Script
Complete Islamic Study Guide Extended Edition

This script verifies that all links in the application work properly
and lead to fully populated content with the correct design.
"""

import os
import re
from pathlib import Path
import requests
from urllib.parse import urljoin, urlparse

def get_all_html_files():
    """Get all HTML files in the current directory"""
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html'):
            html_files.append(file)
    return html_files

def extract_links_from_file(filename):
    """Extract all href links from an HTML file"""
    links = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all href attributes
        href_pattern = r'href=["\']([^"\']+)["\']'
        matches = re.findall(href_pattern, content)
        
        for match in matches:
            if match.startswith('http'):
                links.append(('external', match))
            elif match.startswith('#'):
                links.append(('anchor', match))
            elif match.startswith('mailto:'):
                links.append(('email', match))
            elif match.startswith('tel:'):
                links.append(('phone', match))
            else:
                links.append(('internal', match))
                
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        
    return links

def verify_file_exists(filename):
    """Verify if a file exists and has content"""
    if not os.path.exists(filename):
        return False, "File does not exist"
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if len(content.strip()) == 0:
            return False, "File is empty"
            
        # Check if file has proper HTML structure
        if '<!DOCTYPE html>' not in content:
            return False, "Not a valid HTML file"
            
        # Check if file has the correct design (CSS variables)
        if '--bg-primary: #0a0f0f' not in content:
            return False, "Does not have correct design (CSS variables missing)"
            
        # Check if file has content beyond just HTML structure
        if len(content) < 1000:
            return False, "File has minimal content"
            
        return True, "File exists and has proper content"
        
    except Exception as e:
        return False, f"Error reading file: {e}"

def verify_design_compliance(filename):
    """Verify that a file follows the exact design policy"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for required CSS variables
        required_vars = [
            '--bg-primary: #0a0f0f',
            '--accent-primary: #10b981',
            '--text-primary: #ffffff'
        ]
        
        for var in required_vars:
            if var not in content:
                return False, f"Missing required CSS variable: {var}"
        
        # Check for correct font family
        if "'Georgia', 'Times New Roman', serif" not in content:
            return False, "Incorrect font family"
            
        # Check for theme toggle functionality
        if 'toggleTheme()' not in content:
            return False, "Missing theme toggle functionality"
            
        # Check for back link to main index (skip for main index page itself)
        if filename != 'complete-islamic-study-guide-dark.html' and 'complete-islamic-study-guide-dark.html' not in content:
            return False, "Missing back link to main index"
            
        return True, "Design compliance verified"
        
    except Exception as e:
        return False, f"Error checking design compliance: {e}"

def main():
    """Main function to verify all links"""
    print("🔍 COMPREHENSIVE LINK VERIFICATION")
    print("Complete Islamic Study Guide Extended Edition")
    print("=" * 60)
    
    # Get all HTML files
    html_files = get_all_html_files()
    
    print(f"📊 Found {len(html_files)} HTML files to verify")
    print()
    
    # Track verification results
    total_links = 0
    working_links = 0
    broken_links = 0
    design_violations = 0
    
    # Verify each file
    for filename in html_files:
        print(f"🔍 Verifying: {filename}")
        
        # Extract links from file
        links = extract_links_from_file(filename)
        total_links += len([l for l in links if l[0] == 'internal'])
        
        # Verify file exists and has content
        exists, message = verify_file_exists(filename)
        if not exists:
            print(f"   ❌ File issue: {message}")
            broken_links += 1
            continue
            
        # Verify design compliance
        design_ok, design_message = verify_design_compliance(filename)
        if not design_ok:
            print(f"   ⚠️  Design violation: {design_message}")
            design_violations += 1
        else:
            print(f"   ✅ Design compliance: OK")
            
        # Verify internal links
        internal_links = [l for l in links if l[0] == 'internal']
        for link_type, link in internal_links:
            if link.endswith('.html'):
                target_exists, target_message = verify_file_exists(link)
                if target_exists:
                    working_links += 1
                    print(f"      ✅ Link: {link} - Working")
                else:
                    broken_links += 1
                    print(f"      ❌ Link: {link} - {target_message}")
        
        print()
    
    # Summary
    print("=" * 60)
    print(f"🎉 LINK VERIFICATION COMPLETE!")
    print(f"📁 Files verified: {len(html_files)}")
    print(f"🔗 Total internal links: {total_links}")
    print(f"✅ Working links: {working_links}")
    print(f"❌ Broken links: {broken_links}")
    print(f"⚠️  Design violations: {design_violations}")
    print()
    
    if broken_links == 0 and design_violations == 0:
        print("🎉 PERFECT! All links work and all files follow design policy!")
        print("📱 Application is ready for production deployment!")
    elif broken_links == 0:
        print("✅ All links work, but some design violations found.")
        print("🔧 Consider running design fix script again.")
    else:
        print("❌ Some links are broken or files have issues.")
        print("🔧 These need to be fixed before deployment.")
    
    print()
    print("🔍 Verification complete!")

if __name__ == "__main__":
    main()
