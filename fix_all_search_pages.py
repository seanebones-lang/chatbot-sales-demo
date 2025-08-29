#!/usr/bin/env python3
import os
import re

def fix_html_file(filepath):
    """Fix hardcoded localhost:8080 URLs in HTML files"""
    print(f"🔧 Fixing: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains localhost:8080
        if 'localhost:8080' in content:
            print(f"  📍 Found localhost:8080 in {filepath}")
            
            # Add the auto-detection function before the first script tag
            auto_detect_function = '''
        // Auto-detect server URL (local vs DigitalOcean)
        function getServerUrl() {
            const hostname = window.location.hostname;
            if (hostname === 'localhost' || hostname === '127.0.0.1') {
                return 'http://localhost:8080';
            } else {
                // On DigitalOcean, use the same hostname but port 8080
                return `http://${hostname}:8080`;
            }
        }
        
'''
            
            # Find the first <script> tag and add the function before it
            script_pattern = r'(<script[^>]*>)'
            if re.search(script_pattern, content):
                content = re.sub(script_pattern, auto_detect_function + r'\1', content, count=1)
                print(f"  ✅ Added auto-detection function")
            
            # Replace all hardcoded localhost:8080 URLs
            old_pattern = r'fetch\("http://localhost:8080/chat"'
            new_pattern = r'const serverUrl = getServerUrl();\n            fetch(`${serverUrl}/chat`'
            
            if re.search(old_pattern, content):
                content = re.sub(old_pattern, new_pattern, content)
                print(f"  ✅ Fixed fetch calls")
            
            # Also fix any remaining localhost:8080 references
            content = re.sub(r'http://localhost:8080', '${serverUrl}', content)
            
            # Write the fixed content back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  🎉 File fixed successfully")
            return True
        else:
            print(f"  ✅ No localhost:8080 found - skipping")
            return False
            
    except Exception as e:
        print(f"  ❌ Error fixing {filepath}: {e}")
        return False

def main():
    """Main function to fix all HTML files"""
    print("🚀 Starting to fix all search pages...")
    print("=" * 50)
    
    # Get all HTML files in current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    fixed_count = 0
    total_count = len(html_files)
    
    for html_file in html_files:
        if fix_html_file(html_file):
            fixed_count += 1
        print()
    
    print("=" * 50)
    print(f"🎉 Fix complete! Fixed {fixed_count} out of {total_count} HTML files")
    
    if fixed_count > 0:
        print("\n📋 Files that were fixed:")
        for html_file in html_files:
            if 'localhost:8080' in open(html_file, 'r').read():
                print(f"  ❌ {html_file} - Still has issues")
            else:
                print(f"  ✅ {html_file} - Fixed")

if __name__ == '__main__':
    main()
