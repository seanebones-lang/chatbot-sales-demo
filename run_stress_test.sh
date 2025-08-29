#!/bin/bash

echo "🕌 DeenBot 5-Minute Stress Test Runner"
echo "======================================"
echo ""

# Check if DeenBot is running
echo "🔍 Checking if DeenBot is running..."
if curl -s http://localhost:8080/health > /dev/null; then
    echo "✅ DeenBot is running and ready for testing"
else
    echo "❌ DeenBot is not running on port 8080"
    echo "   Please start DeenBot first using: ./start_deenbot_local.sh"
    exit 1
fi

echo ""
echo "🔥 This stress test will:"
echo "   • Run continuously for exactly 5 minutes"
echo "   • Test all variations of user text"
echo "   • Send requests every 0.5 seconds"
echo "   • Monitor for crashes or failures"
echo "   • Generate a comprehensive report"
echo ""

# Confirm before starting
read -p "🚀 Start the 5-minute stress test? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Stress test cancelled"
    exit 0
fi

echo ""
echo "🔥 Starting DeenBot Stress Test..."
echo "⏳ This will take exactly 5 minutes"
echo "📊 Monitor progress in the terminal"
echo ""

# Run the stress test
python3 deenbot_stress_tester.py

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 DeenBot PASSED the stress test!"
    echo "✅ The service is stable and ready for production"
else
    echo ""
    echo "🚨 DeenBot FAILED the stress test!"
    echo "❌ The service needs fixing before deployment"
    echo ""
    echo "📋 Check the logs for details:"
    echo "   • deenbot_stress_test.log - Detailed test logs"
    echo "   • deenbot_stress_test_results_*.json - Test results"
    echo "   • deenbot_service.log - Service logs"
fi
