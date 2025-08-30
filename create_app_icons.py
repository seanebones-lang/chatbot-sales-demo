#!/usr/bin/env python3

"""
Create Simple App Icons for Islamic Study Guide PWA
Generates basic icon files for PWA installation
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, filename):
    """Create a simple icon with Islamic theme"""
    
    # Create image with dark background
    img = Image.new('RGB', (size, size), color='#0a0f0f')
    draw = ImageDraw.Draw(img)
    
    # Calculate center
    center = size // 2
    
    # Draw outer circle (border)
    border_width = size // 20
    draw.ellipse([border_width, border_width, size - border_width, size - border_width], 
                 outline='#10b981', width=border_width)
    
    # Draw inner circle (accent)
    inner_size = size // 3
    inner_start = center - inner_size // 2
    inner_end = center + inner_size // 2
    draw.ellipse([inner_start, inner_start, inner_end, inner_end], 
                 fill='#10b981')
    
    # Add text (simplified for small sizes)
    if size >= 192:
        try:
            # Try to use a font
            font_size = size // 8
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
            text = "ISLAMIC"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            text_x = center - text_width // 2
            text_y = center + inner_size // 2 + 10
            draw.text((text_x, text_y), text, fill='#ffffff', font=font)
        except:
            # Fallback if font not available
            pass
    
    # Save icon
    img.save(filename, 'PNG')
    print(f"Created: {filename} ({size}x{size})")

def main():
    """Create all required app icons"""
    
    print("Creating app icons for Islamic Study Guide PWA...")
    
    # Create icons directory if it doesn't exist
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    # Create different icon sizes
    icon_sizes = [
        (192, 'icon-192x192.png'),
        (512, 'icon-512x512.png')
    ]
    
    for size, filename in icon_sizes:
        create_icon(size, filename)
    
    print("\nApp icons created successfully!")
    print("Your team can now install the app to their home screen!")
    print("\nTo share with your team:")
    print("1. Deploy to a web server")
    print("2. Send them the URL")
    print("3. They click 'Install App' button")
    print("4. App appears on their home screen!")

if __name__ == "__main__":
    main()
