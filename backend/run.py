#!/usr/bin/env python3
"""
Tattoo Assistant Backend Startup Script
"""

import os
import sys
from app import app

if __name__ == '__main__':
    print("🎨 Starting Tattoo Assistant Backend...")
    print("📍 Server will run on: http://localhost:5000")
    print("🔗 API endpoints available at: http://localhost:5000/api/")
    print("📖 API Documentation:")
    print("   GET  /api/health - Health check")
    print("   GET  /api/artist-info - Get artist information")
    print("   POST /api/appointments - Create appointment")
    print("   GET  /api/appointments - List appointments")
    print("   GET  /api/availability/<date> - Check availability")
    print("   POST /api/generate-portfolio-pdf - Generate portfolio PDF")
    print("   POST /api/generate-aftercare-pdf - Generate aftercare PDF")
    print("   POST /api/process-deposit - Process deposit")
    print("\n🚀 Starting server...\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
