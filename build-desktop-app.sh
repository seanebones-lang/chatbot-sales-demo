#!/bin/bash

# Build Desktop App Script for Islamic Study Guide Extended Edition
echo "🏗️  Building Complete Islamic Study Guide Extended Edition Desktop App..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    echo "   Download from: https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed. Please install npm first."
    exit 1
fi

echo "✅ Node.js and npm found"

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Create build directory if it doesn't exist
mkdir -p build

# Create simple app icon if it doesn't exist
if [ ! -f "build/icon.png" ]; then
    echo "🎨 Creating app icon..."
    python3 create_app_icons.py
    # Copy the generated icon to build directory
    cp icon-192x192.png build/icon.png
fi

# Build the desktop app
echo "🔨 Building desktop application..."

# Build for current platform
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 Building for macOS..."
    npm run build:mac
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    echo "🪟 Building for Windows..."
    npm run build:win
else
    echo "🐧 Building for Linux..."
    npm run build:linux
fi

# Check if build was successful
if [ -d "dist" ]; then
    echo "✅ Desktop app built successfully!"
    echo ""
    echo "📁 Build output location: dist/"
    echo ""
    
    # List build outputs
    echo "📦 Build outputs:"
    ls -la dist/
    echo ""
    
    echo "🚀 Your desktop app is ready!"
    echo ""
    echo "📱 To install on your Mac:"
    echo "   1. Go to dist/ folder"
    echo "   2. Double-click the .dmg file"
    echo "   3. Drag Islamic Study Guide to Applications"
    echo "   4. Launch from Applications folder"
    echo ""
    echo "🔄 To run in development mode:"
    echo "   npm start"
    
else
    echo "❌ Build failed. Please check the error messages above."
    exit 1
fi
