#!/bin/bash

echo "========================================"
echo "   Islamic Study Guide - Auto Start"
echo "========================================"
echo ""
echo "Starting your Islamic Study Guide..."
echo ""
echo "This will open in your web browser automatically."
echo ""
echo "If it doesn't open automatically:"
echo "1. Copy this link: http://localhost:8080"
echo "2. Paste it into your browser"
echo ""

# Wait a moment for user to read
sleep 3

# Try to open the application in the default browser
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://localhost:8080
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost:8080
    elif command -v gnome-open &> /dev/null; then
        gnome-open http://localhost:8080
    else
        echo "Could not automatically open browser. Please manually open: http://localhost:8080"
    fi
else
    echo "Unknown operating system. Please manually open: http://localhost:8080"
fi

echo ""
echo "Application should now be opening in your browser!"
echo ""
echo "If you see any errors, please let me know."
echo ""
read -p "Press Enter to continue..."
