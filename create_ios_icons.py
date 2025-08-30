#!/usr/bin/env python3
"""
Create iOS-specific app icons for Islamic Study Guide Mobile App
Generates all required icon sizes for iOS PWA installation
"""

import os
from PIL import Image, ImageDraw, ImageFont
import math

def create_ios_icon(size, filename, text="ISLAMIC"):
    """Create an iOS app icon with the specified size"""
    
    # Create new image with dark green background
    img = Image.new('RGB', (size, size), color='#0a0f0f')
    draw = ImageDraw.Draw(img)
    
    # Calculate circle dimensions
    margin = size // 8
    circle_size = size - (2 * margin)
    circle_x = margin
    circle_y = margin
    
    # Draw main circle (dark green)
    draw.ellipse([circle_x, circle_y, circle_x + circle_size, circle_y + circle_size], 
                 fill='#0a0f0f', outline='#10b981', width=max(2, size//50))
    
    # Draw inner circle (lighter green)
    inner_margin = size // 6
    inner_circle_size = size - (2 * inner_margin)
    inner_circle_x = inner_margin
    inner_circle_y = inner_margin
    
    draw.ellipse([inner_circle_x, inner_circle_y, 
                  inner_circle_x + inner_circle_size, inner_circle_y + inner_circle_size], 
                 fill='#065f46', outline='#10b981', width=max(1, size//100))
    
    # Draw Islamic symbols
    # Crescent moon
    moon_center_x = size // 2
    moon_center_y = size // 3
    moon_radius = size // 8
    
    # Draw crescent using two circles
    outer_circle = (moon_center_x - moon_radius, moon_center_y - moon_radius,
                    moon_center_x + moon_radius, moon_center_y + moon_radius)
    inner_circle = (moon_center_x - moon_radius + moon_radius//3, moon_center_y - moon_radius,
                    moon_center_x + moon_radius - moon_radius//3, moon_center_y + moon_radius)
    
    draw.ellipse(outer_circle, fill='#fbbf24')
    draw.ellipse(inner_circle, fill='#065f46')
    
    # Draw book symbol
    book_width = size // 4
    book_height = size // 6
    book_x = size // 2 - book_width // 2
    book_y = size * 2 // 3
    
    # Book cover
    draw.rectangle([book_x, book_y, book_x + book_width, book_y + book_height], 
                  fill='#fbbf24', outline='#d97706', width=max(1, size//100))
    
    # Book pages
    page_margin = max(1, size//100)
    draw.rectangle([book_x + page_margin, book_y + page_margin, 
                    book_x + book_width - page_margin, book_y + book_height - page_margin], 
                  fill='#fef3c7')
    
    # Add text if size allows
    if size >= 120:
        try:
            # Try to use a system font
            font_size = max(8, size // 15)
            font = ImageFont.load_default()
            
            # Calculate text position
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            text_x = (size - text_width) // 2
            text_y = size - text_height - size//20
            
            # Draw text with outline
            draw.text((text_x, text_y), text, fill='#ffffff', font=font)
        except:
            pass
    
    # Save the icon
    img.save(filename, 'PNG')
    print(f"✅ Created: {filename} ({size}x{size})")

def main():
    """Create all iOS app icons"""
    
    # Create icons directory if it doesn't exist
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    # iOS icon sizes (in pixels)
    ios_icon_sizes = [
        20,   # iPhone notification
        29,   # iPhone settings
        40,   # iPhone spotlight
        58,   # iPhone settings (@2x)
        60,   # iPhone app (@2x)
        76,   # iPad app
        80,   # iPhone spotlight (@2x)
        87,   # iPhone settings (@3x)
        120,  # iPhone app (@3x)
        152,  # iPad app (@2x)
        167,  # iPad Pro app (@2x)
        180,  # iPhone app (@3x)
        192,  # PWA standard
        512   # PWA standard
    ]
    
    print("🎨 Creating iOS App Icons for Islamic Study Guide...")
    print("=" * 60)
    
    # Create each icon size
    for size in ios_icon_sizes:
        filename = f"icons/icon-{size}x{size}.png"
        create_ios_icon(size, filename)
    
    # Create additional sizes for manifest
    additional_sizes = [96, 144, 168, 192, 512]
    for size in additional_sizes:
        if size not in ios_icon_sizes:
            filename = f"icons/icon-{size}x{size}.png"
            create_ios_icon(size, filename)
    
    print("=" * 60)
    print("🎉 All iOS app icons created successfully!")
    print("\n📱 Icon files created:")
    
    # List all created files
    icon_files = [f for f in os.listdir('icons') if f.startswith('icon-') and f.endswith('.png')]
    icon_files.sort(key=lambda x: int(x.split('-')[1].split('x')[0]))
    
    for icon_file in icon_files:
        print(f"   • {icon_file}")
    
    print(f"\n📁 Icons saved in: {os.path.abspath('icons')}")
    print("\n🚀 Next steps:")
    print("   1. Copy icons to your project root")
    print("   2. Update manifest.json with new icon paths")
    print("   3. Test PWA installation on iOS devices")

if __name__ == "__main__":
    main()
