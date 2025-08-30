#!/usr/bin/env python3
"""
Create iOS App Package for Islamic Study Guide
Packages all necessary files for iOS PWA installation
"""

import os
import shutil
import zipfile
from datetime import datetime

def create_ios_app_package():
    """Create a complete iOS app package for distribution"""
    
    # Package name and version
    package_name = "Islamic-Study-Guide-iOS-App"
    version = "1.0.0"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create package directory
    package_dir = f"{package_name}-v{version}-{timestamp}"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    os.makedirs(package_dir)
    
    print(f"📦 Creating iOS App Package: {package_dir}")
    print("=" * 60)
    
    # Files to include in the package
    essential_files = [
        "islamic-study-guide-mobile.html",
        "manifest.json",
        "sw.js",
        "complete-islamic-study-guide-dark.html",
        "quran-index.html",
        "hadith-index.html",
        "fiqh-index.html",
        "sunnah-index.html",
        "aqeedah-index.html",
        "seerah-index.html",
        "duas-index.html",
        "ethics-index.html",
        "history-index.html",
        "science-index.html"
    ]
    
    # Copy essential HTML files
    print("📁 Copying essential HTML files...")
    for file in essential_files:
        if os.path.exists(file):
            shutil.copy2(file, package_dir)
            print(f"   ✅ {file}")
        else:
            print(f"   ⚠️  {file} (not found)")
    
    # Copy all icon files
    print("\n🎨 Copying iOS app icons...")
    icon_files = [f for f in os.listdir('.') if f.startswith('icon-') and f.endswith('.png')]
    for icon in icon_files:
        shutil.copy2(icon, package_dir)
        print(f"   ✅ {icon}")
    
    # Copy additional content pages
    print("\n📚 Copying content pages...")
    content_pages = [
        "prayer-worship.html",
        "ramadan-fasting.html",
        "hajj-umrah.html",
        "zakat-charity.html",
        "family-marriage.html",
        "business-finance.html",
        "health-medicine.html",
        "education-learning.html",
        "social-community.html"
    ]
    
    for page in content_pages:
        if os.path.exists(page):
            shutil.copy2(page, package_dir)
            print(f"   ✅ {page}")
    
    # Copy advanced fiqh pages
    print("\n⚖️  Copying advanced Fiqh pages...")
    fiqh_pages = [
        "business_financial.html",
        "medical_health.html",
        "technology_modern.html",
        "environmental_social.html",
        "contemporary_issues.html"
    ]
    
    for page in fiqh_pages:
        if os.path.exists(page):
            shutil.copy2(page, package_dir)
            print(f"   ✅ {page}")
    
    # Copy documentation
    print("\n📖 Copying documentation...")
    docs = [
        "IOS_INSTALLATION_GUIDE.md",
        "README.md",
        "DESIGN_POLICY.md"
    ]
    
    for doc in docs:
        if os.path.exists(doc):
            shutil.copy2(doc, package_dir)
            print(f"   ✅ {doc}")
    
    # Create README for the package
    create_package_readme(package_dir, version, timestamp)
    
    # Create installation script
    create_installation_script(package_dir)
    
    # Create ZIP archive
    zip_filename = f"{package_dir}.zip"
    print(f"\n🗜️  Creating ZIP archive: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arcname)
    
    print(f"   ✅ {zip_filename} created successfully!")
    
    # Clean up package directory
    shutil.rmtree(package_dir)
    
    print("\n" + "=" * 60)
    print("🎉 iOS App Package Created Successfully!")
    print(f"📦 Package: {zip_filename}")
    print(f"📱 Ready for iOS installation")
    print("\n🚀 Next steps:")
    print("   1. Share the ZIP file with your team")
    print("   2. Extract on iOS devices")
    print("   3. Open islamic-study-guide-mobile.html in Safari")
    print("   4. Install as PWA app")
    
    return zip_filename

def create_package_readme(package_dir, version, timestamp):
    """Create a README file for the iOS app package"""
    
    readme_content = f"""# 📱 Islamic Study Guide iOS App Package
## Version {version} - {timestamp}

**Complete Islamic Study Guide Extended Edition for iOS Devices**

---

## 🚀 **Quick Start**

1. **Extract** this package on your iOS device
2. **Open** `islamic-study-guide-mobile.html` in Safari
3. **Install** as a native iOS app
4. **Enjoy** your Islamic research tool!

---

## 📋 **What's Included**

✅ **Mobile-Optimized Interface** - Touch-friendly design  
✅ **Complete Islamic Content** - Quran, Hadith, Fiqh, Sunnah  
✅ **DeenBot AI Assistant** - Instant Islamic answers  
✅ **iOS App Icons** - All required sizes  
✅ **Offline Capability** - Works without internet  
✅ **Installation Guide** - Step-by-step instructions  

---

## 📱 **Installation Steps**

### **Step 1: Extract Package**
- Unzip this package on your iOS device
- Or extract on computer and transfer to device

### **Step 2: Open in Safari**
- Open **Safari** (not Chrome or other browsers)
- Navigate to `islamic-study-guide-mobile.html`
- Wait for page to fully load

### **Step 3: Install as App**
- Tap the **Share button** (square with arrow)
- Scroll down and tap **"Add to Home Screen"**
- Tap **"Add"** to confirm
- Your app is now installed! 🎉

---

## 🔧 **Troubleshooting**

- **Use Safari only** - Other browsers won't work
- **Check iOS version** - iOS 11.3+ required
- **Clear cache** if installation fails
- **Restart Safari** if needed

---

## 📚 **Content Overview**

- **Quran**: All 114 Surahs with Tafsir
- **Hadith**: Authentic collections
- **Fiqh**: Islamic jurisprudence
- **Sunnah**: Prophetic traditions
- **Aqeedah**: Islamic beliefs
- **Seerah**: Prophet's life
- **Advanced Topics**: Modern Islamic issues

---

## 🤖 **DeenBot AI Features**

- **Instant Answers** to any Islamic question
- **Multi-source Responses** with authenticity ratings
- **Follow-up Questions** for deeper learning
- **Offline Knowledge** base

---

## 📞 **Support**

For technical support or questions:
- Check the installation guide
- Review troubleshooting section
- Contact your development team

---

**Package Version**: {version}  
**Created**: {timestamp}  
**Compatibility**: iOS 11.3+ (iPhone 6s+, iPad Air+)  

**Enjoy your Complete Islamic Study Guide on iOS!** 📱✨
"""
    
    with open(os.path.join(package_dir, "README.md"), 'w') as f:
        f.write(readme_content)

def create_installation_script(package_dir):
    """Create a simple installation script for the package"""
    
    script_content = """#!/bin/bash
# Islamic Study Guide iOS App - Installation Helper
# Run this script to set up the app on your iOS device

echo "📱 Islamic Study Guide iOS App Installation Helper"
echo "=================================================="
echo ""

# Check if we're on macOS
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "✅ Detected macOS"
    echo ""
    echo "📋 Installation Steps:"
    echo "1. Open Safari on your iOS device"
    echo "2. Navigate to: islamic-study-guide-mobile.html"
    echo "3. Tap Share button → Add to Home Screen"
    echo "4. Tap 'Add' to confirm"
    echo ""
    echo "🚀 Quick Launch:"
    echo "   open islamic-study-guide-mobile.html"
    echo ""
    
    # Offer to open the file
    read -p "Would you like to open the mobile app now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open islamic-study-guide-mobile.html
        echo "✅ Opened in default browser"
    fi
else
    echo "⚠️  This script is designed for macOS"
    echo "📱 For iOS installation, transfer files to your device"
    echo "   and follow the installation guide"
fi

echo ""
echo "📖 For detailed instructions, see: IOS_INSTALLATION_GUIDE.md"
echo "🎉 Installation complete!"
"""
    
    script_path = os.path.join(package_dir, "install.sh")
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    # Make script executable
    os.chmod(script_path, 0o755)

if __name__ == "__main__":
    try:
        package_file = create_ios_app_package()
        print(f"\n🎯 Package ready: {package_file}")
        print("📱 Share this file with your team for iOS installation!")
    except Exception as e:
        print(f"❌ Error creating package: {e}")
        import traceback
        traceback.print_exc()
