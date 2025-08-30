#!/usr/bin/env python3
"""
Create PDF Instructions for iOS Mobile App Installation
Converts markdown guide to PDF for team members and beta testers
"""

import os
import subprocess
import sys
from datetime import datetime

def check_dependencies():
    """Check if required tools are available"""
    print("🔍 Checking dependencies...")
    
    # Check for pandoc
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        print("✅ Pandoc found")
        pandoc_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Pandoc not found - will use alternative method")
        pandoc_available = False
    
    # Check for wkhtmltopdf
    try:
        subprocess.run(['wkhtmltopdf', '--version'], capture_output=True, check=True)
        print("✅ wkhtmltopdf found")
        wkhtmltopdf_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  wkhtmltopdf not found")
        wkhtmltopdf_available = False
    
    return pandoc_available, wkhtmltopdf_available

def create_html_version():
    """Create an HTML version of the installation guide"""
    print("📝 Creating HTML version...")
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iOS Mobile App Installation Guide - Islamic Study Guide</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #10b981;
            text-align: center;
            border-bottom: 3px solid #10b981;
            padding-bottom: 20px;
        }
        h2 {
            color: #059669;
            margin-top: 30px;
            border-left: 4px solid #10b981;
            padding-left: 15px;
        }
        h3 {
            color: #047857;
            margin-top: 25px;
        }
        .quick-start {
            background: #f0f9ff;
            border: 2px solid #10b981;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .troubleshooting {
            background: #fef3c7;
            border: 2px solid #f59e0b;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .pro-tips {
            background: #ecfdf5;
            border: 2px solid #10b981;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        .feedback-form {
            background: #f3e8ff;
            border: 2px solid #8b5cf6;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background: #10b981;
            color: white;
        }
        tr:nth-child(even) {
            background: #f9f9f9;
        }
        .checklist {
            list-style: none;
            padding: 0;
        }
        .checklist li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }
        .checklist li:before {
            content: "☐ ";
            color: #10b981;
            font-weight: bold;
        }
        .success {
            color: #059669;
            font-weight: bold;
        }
        .warning {
            color: #d97706;
            font-weight: bold;
        }
        .info {
            color: #0891b2;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #666;
        }
        @media print {
            body { background: white; }
            .container { box-shadow: none; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📱 iOS Mobile App Installation Guide</h1>
        <h2>Complete Islamic Study Guide Extended Edition</h2>
        <p><strong>For Team Members & Beta Testers</strong></p>
        
        <div class="quick-start">
            <h3>🚀 QUICK START (2 Minutes)</h3>
            <ol>
                <li><strong>Download</strong> the iOS app package from your team leader</li>
                <li><strong>Extract</strong> the ZIP file on your iPhone/iPad</li>
                <li><strong>Open Safari</strong> and navigate to the HTML file</li>
                <li><strong>Tap Share</strong> button → "Add to Home Screen"</li>
                <li><strong>Tap "Add"</strong> to confirm installation</li>
            </ol>
            <p class="success">Your Islamic Study Guide is now installed as a native iOS app! 🎉</p>
        </div>

        <h2>🎯 What You're Getting</h2>
        <ul>
            <li><strong>📚 Complete Islamic Knowledge Base</strong> - Quran, Hadith, Fiqh, Sunnah, Aqeedah, Seerah</li>
            <li><strong>🤖 DeenBot AI Assistant</strong> - Instant answers to Islamic questions</li>
            <li><strong>📱 Native iOS App Experience</strong> - Looks and feels like a real app</li>
            <li><strong>🔌 Full Offline Access</strong> - Works without internet connection</li>
        </ul>

        <h2>📱 Device Compatibility</h2>
        <table>
            <tr>
                <th>Device</th>
                <th>iOS Version</th>
                <th>Status</th>
            </tr>
            <tr>
                <td>iPhone 6s+</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 7+</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 8+</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone X+</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 11+</td>
                <td>iOS 13.0+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 12+</td>
                <td>iOS 14.0+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 13+</td>
                <td>iOS 15.0+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 14+</td>
                <td>iOS 16.0+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPhone 15+</td>
                <td>iOS 17.0+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPad Air</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPad Pro</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
            <tr>
                <td>iPad Mini</td>
                <td>iOS 11.3+</td>
                <td class="success">✅ Full Support</td>
            </tr>
        </table>

        <h2>🔧 Detailed Installation Steps</h2>
        
        <h3>For iPhone Users:</h3>
        <ol>
            <li><strong>Prepare Your Device</strong>
                <ul>
                    <li>Ensure iOS 11.3 or later</li>
                    <li>Have at least 50MB free storage</li>
                    <li>Use Safari browser (not Chrome, Firefox, etc.)</li>
                </ul>
            </li>
            <li><strong>Access the App Package</strong>
                <ul>
                    <li>Download the ZIP file from your team leader</li>
                    <li>Extract it using Files app or transfer to device</li>
                    <li>Locate islamic-study-guide-mobile.html</li>
                </ul>
            </li>
            <li><strong>Install the App</strong>
                <ul>
                    <li>Open Safari on your iPhone</li>
                    <li>Navigate to the HTML file</li>
                    <li>Wait for the page to fully load</li>
                    <li>Tap the Share button (square with arrow up) at bottom</li>
                    <li>Scroll down to find "Add to Home Screen"</li>
                    <li>Tap "Add to Home Screen"</li>
                    <li>Customize the app name if desired</li>
                    <li>Tap "Add" to confirm installation</li>
                </ul>
            </li>
            <li><strong>Launch Your App</strong>
                <ul>
                    <li>Go to Home Screen</li>
                    <li>Find your Islamic Study Guide app icon</li>
                    <li>Tap to launch</li>
                    <li>Enjoy your Islamic research tool!</li>
                </ul>
            </li>
        </ol>

        <h3>For iPad Users:</h3>
        <ol>
            <li><strong>Prepare Your Device</strong>
                <ul>
                    <li>Ensure iOS 11.3 or later</li>
                    <li>Have at least 50MB free storage</li>
                    <li>Use Safari browser</li>
                </ul>
            </li>
            <li><strong>Access the App Package</strong>
                <ul>
                    <li>Download the ZIP file from your team leader</li>
                    <li>Extract it using Files app</li>
                    <li>Locate islamic-study-guide-mobile.html</li>
                </ul>
            </li>
            <li><strong>Install the App</strong>
                <ul>
                    <li>Open Safari on your iPad</li>
                    <li>Navigate to the HTML file</li>
                    <li>Wait for the page to fully load</li>
                    <li>Tap the Share button (square with arrow) at top right</li>
                    <li>Select "Add to Home Screen"</li>
                    <li>Tap "Add" to confirm installation</li>
                </ul>
            </li>
            <li><strong>Launch Your App</strong>
                <ul>
                    <li>Go to Home Screen</li>
                    <li>Find your Islamic Study Guide app icon</li>
                    <li>Tap to launch</li>
                    <li>Enjoy your Islamic research tool!</li>
                </ul>
            </li>
        </ol>

        <div class="troubleshooting">
            <h2>🔍 Troubleshooting Guide</h2>
            
            <h3>"Add to Home Screen" Not Showing?</h3>
            <ul>
                <li><strong>Wrong Browser</strong> - Use Safari only (iOS requirement)</li>
                <li><strong>iOS Version Too Old</strong> - Update to iOS 11.3 or later</li>
                <li><strong>Page Not Fully Loaded</strong> - Wait for complete loading</li>
                <li><strong>Safari Cache Issues</strong> - Clear Safari cache and data</li>
                <li><strong>Private Browsing Mode</strong> - Exit private browsing</li>
            </ul>

            <h3>App Not Working Offline?</h3>
            <ul>
                <li><strong>Wait for First Load</strong> - App needs to cache content first (1-2 minutes)</li>
                <li><strong>Check Storage Space</strong> - Need at least 50MB free storage</li>
                <li><strong>Reinstall App</strong> - Delete and reinstall if needed</li>
            </ul>

            <h3>Icon Not Appearing on Home Screen?</h3>
            <ul>
                <li><strong>Check Home Screen Pages</strong> - Swipe left/right to check all pages</li>
                <li><strong>Check App Library</strong> - Icon might be in App Library</li>
                <li><strong>Restart Device</strong> - iOS system issue resolution</li>
            </ul>
        </div>

        <div class="pro-tips">
            <h2>🌟 Pro Tips for Beta Testers</h2>
            
            <h3>1. Test All Features</h3>
            <ul>
                <li><strong>Quran Search</strong> - Try different Surah names</li>
                <li><strong>Hadith Search</strong> - Test various topics</li>
                <li><strong>Fiqh Topics</strong> - Explore different categories</li>
                <li><strong>DeenBot</strong> - Ask various Islamic questions</li>
            </ul>

            <h3>2. Test Offline Functionality</h3>
            <ul>
                <li>Turn off WiFi after first load</li>
                <li>Test all sections without internet</li>
                <li>Verify content is accessible offline</li>
                <li>Check performance in offline mode</li>
            </ul>

            <h3>3. Test Different Devices</h3>
            <ul>
                <li>iPhone - Test on various screen sizes</li>
                <li>iPad - Test landscape and portrait modes</li>
                <li>iOS Versions - Test on different iOS versions if possible</li>
            </ul>

            <h3>4. Performance Testing</h3>
            <ul>
                <li>Loading Speed - Time how fast pages load</li>
                <li>Touch Response - Test touch interactions</li>
                <li>Memory Usage - Check if app uses too much memory</li>
                <li>Battery Impact - Monitor battery usage</li>
            </ul>

            <h3>5. User Experience Testing</h3>
            <ul>
                <li>Navigation - Test all navigation paths</li>
                <li>Search - Test search functionality</li>
                <li>Content - Verify content accuracy</li>
                <li>Design - Check visual consistency</li>
            </ul>
        </div>

        <div class="feedback-form">
            <h2>📋 Feedback Form</h2>
            
            <h3>Please Report:</h3>
            
            <h4>Installation Experience</h4>
            <ul class="checklist">
                <li>Installation successful on first try</li>
                <li>Installation required troubleshooting</li>
                <li>Installation failed completely</li>
                <li>Device model and iOS version</li>
            </ul>

            <h4>App Performance</h4>
            <ul class="checklist">
                <li>Fast and responsive</li>
                <li>Slow but functional</li>
                <li>Laggy or unresponsive</li>
                <li>Crashes or freezes</li>
            </ul>

            <h4>Content Quality</h4>
            <ul class="checklist">
                <li>All content loads correctly</li>
                <li>Some content missing</li>
                <li>Content errors found</li>
                <li>DeenBot working properly</li>
            </ul>

            <h4>User Experience</h4>
            <ul class="checklist">
                <li>Easy to navigate</li>
                <li>Confusing navigation</li>
                <li>Beautiful design</li>
                <li>Design issues found</li>
            </ul>

            <h4>Offline Functionality</h4>
            <ul class="checklist">
                <li>Works perfectly offline</li>
                <li>Some features don't work offline</li>
                <li>Completely broken offline</li>
                <li>Offline performance issues</li>
            </ul>

            <h4>Additional Comments:</h4>
            <p><em>[Please write any additional feedback, suggestions, or issues you encounter]</em></p>
        </div>

        <h2>🎉 You're All Set!</h2>
        <p>Your iPhone/iPad now has a <strong>professional Islamic research app</strong> that:</p>
        <ul>
            <li class="success">✅ <strong>Works offline</strong> - No internet needed</li>
            <li class="success">✅ <strong>Looks native</strong> - Feels like a real iOS app</li>
            <li class="success">✅ <strong>Updates automatically</strong> - Always current content</li>
            <li class="success">✅ <strong>Integrates perfectly</strong> - Works with iOS features</li>
        </ul>

        <h2>📞 Need Help?</h2>
        <ul>
            <li><strong>Installation Issues</strong> - Check troubleshooting section above</li>
            <li><strong>Technical Problems</strong> - Contact your team leader</li>
            <li><strong>Content Questions</strong> - Use DeenBot AI assistant</li>
            <li><strong>General Support</strong> - Refer to team documentation</li>
        </ul>

        <div class="footer">
            <p><strong>Installation Guide v1.0.0 - Complete Islamic Study Guide Extended Edition</strong></p>
            <p><em>For Team Members & Beta Testers</em> 📱</p>
            <p>Generated on: """ + datetime.now().strftime("%B %d, %Y at %I:%M %p") + """</p>
        </div>
    </div>
</body>
</html>"""
    
    with open('ios-installation-guide.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ HTML version created: ios-installation-guide.html")
    return 'ios-installation-guide.html'

def convert_to_pdf_with_pandoc(html_file):
    """Convert HTML to PDF using pandoc"""
    print("📄 Converting to PDF using Pandoc...")
    
    output_file = 'iOS-Mobile-App-Installation-Guide.pdf'
    
    try:
        cmd = [
            'pandoc',
            html_file,
            '-o', output_file,
            '--pdf-engine=wkhtmltopdf',
            '--standalone',
            '--css=style.css'
        ]
        
        subprocess.run(cmd, check=True)
        print(f"✅ PDF created successfully: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"❌ Pandoc conversion failed: {e}")
        return None

def convert_to_pdf_with_wkhtmltopdf(html_file):
    """Convert HTML to PDF using wkhtmltopdf"""
    print("📄 Converting to PDF using wkhtmltopdf...")
    
    output_file = 'iOS-Mobile-App-Installation-Guide.pdf'
    
    try:
        cmd = [
            'wkhtmltopdf',
            '--page-size', 'A4',
            '--margin-top', '20mm',
            '--margin-right', '20mm',
            '--margin-bottom', '20mm',
            '--margin-left', '20mm',
            '--encoding', 'UTF-8',
            '--print-media-type',
            html_file,
            output_file
        ]
        
        subprocess.run(cmd, check=True)
        print(f"✅ PDF created successfully: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"❌ wkhtmltopdf conversion failed: {e}")
        return None

def create_simple_pdf_instructions():
    """Create a simple text-based instruction file"""
    print("📝 Creating simple text instructions...")
    
    simple_content = """iOS MOBILE APP INSTALLATION GUIDE
Complete Islamic Study Guide Extended Edition
For Team Members & Beta Testers

QUICK START (2 Minutes):
1. Download the iOS app package from your team leader
2. Extract the ZIP file on your iPhone/iPad
3. Open Safari and navigate to islamic-study-guide-mobile.html
4. Tap Share button → "Add to Home Screen"
5. Tap "Add" to confirm installation

REQUIREMENTS:
- iOS 11.3 or later
- Safari browser (not Chrome/Firefox)
- 50MB free storage
- Internet for initial setup only

SUPPORTED DEVICES:
- iPhone 6s+ (iOS 11.3+)
- iPhone 7+ (iOS 11.3+)
- iPhone 8+ (iOS 11.3+)
- iPhone X+ (iOS 11.3+)
- iPhone 11+ (iOS 13.0+)
- iPhone 12+ (iOS 14.0+)
- iPhone 13+ (iOS 15.0+)
- iPhone 14+ (iOS 16.0+)
- iPhone 15+ (iOS 17.0+)
- iPad Air (iOS 11.3+)
- iPad Pro (iOS 11.3+)
- iPad Mini (iOS 11.3+)

TROUBLESHOOTING:
- Use Safari browser only
- Ensure iOS version is 11.3+
- Wait for page to fully load
- Clear Safari cache if needed
- Check storage space (50MB minimum)

FEATURES:
- Complete Islamic knowledge base
- DeenBot AI assistant
- Full offline access
- Native iOS app experience
- Touch-optimized interface

BETA TESTING TIPS:
- Test all features thoroughly
- Test offline functionality
- Test on different devices
- Monitor performance
- Report any issues found

NEED HELP?
- Check troubleshooting section
- Contact team leader
- Use DeenBot for content questions
- Refer to team documentation

Generated on: """ + datetime.now().strftime("%B %d, %Y at %I:%M %p") + """

For complete instructions, see the HTML version or contact your team leader.
"""
    
    with open('iOS-Installation-Guide-Simple.txt', 'w', encoding='utf-8') as f:
        f.write(simple_content)
    
    print("✅ Simple text guide created: iOS-Installation-Guide-Simple.txt")
    return 'iOS-Installation-Guide-Simple.txt'

def main():
    """Main function to create PDF instructions"""
    print("📱 Creating iOS Mobile App Installation Guide PDF")
    print("=" * 60)
    
    # Check dependencies
    pandoc_available, wkhtmltopdf_available = check_dependencies()
    
    # Create HTML version
    html_file = create_html_version()
    
    # Try to convert to PDF
    pdf_file = None
    
    if pandoc_available and wkhtmltopdf_available:
        pdf_file = convert_to_pdf_with_pandoc(html_file)
    elif wkhtmltopdf_available:
        pdf_file = convert_to_pdf_with_wkhtmltopdf(html_file)
    
    # Create simple text version as backup
    simple_file = create_simple_pdf_instructions()
    
    print("\n" + "=" * 60)
    print("🎉 Installation Guide Creation Complete!")
    
    if pdf_file:
        print(f"📄 PDF Guide: {pdf_file}")
        print("   - Ready for distribution to team members")
        print("   - Professional format for printing")
        print("   - Easy to share via email or file sharing")
    else:
        print("⚠️  PDF creation failed - using alternative formats")
    
    print(f"🌐 HTML Guide: {html_file}")
    print("   - Can be opened in any web browser")
    print("   - Professional formatting and styling")
    print("   - Easy to convert to PDF manually")
    
    print(f"📝 Text Guide: {simple_file}")
    print("   - Simple text format for quick reference")
    print("   - Easy to copy/paste into other documents")
    print("   - Universal compatibility")
    
    print("\n🚀 Next Steps:")
    print("   1. Share the guide with your team members")
    print("   2. Distribute the iOS app package")
    print("   3. Collect feedback from beta testers")
    print("   4. Iterate and improve based on feedback")
    
    print("\n📱 Your team can now install the Islamic Study Guide as a native iOS app!")

if __name__ == "__main__":
    main()
