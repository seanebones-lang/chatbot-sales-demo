#!/bin/bash

echo "🚀 Setting up AI Integration for Mariam Bot..."

# Check if we're in the right directory
if [ ! -f "ai_integration.py" ]; then
    echo "❌ Error: Please run this script from the mariam-bot directory"
    exit 1
fi

# Check if Python and pip are available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed"
    exit 1
fi

echo "✅ Python and pip are available"

# Create virtual environment if it doesn't exist
if [ ! -d "ai-env" ]; then
    echo "🔧 Creating AI integration virtual environment..."
    python3 -m venv ai-env
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source ai-env/bin/activate

# Upgrade pip
echo "🔧 Upgrading pip..."
pip install --upgrade pip

# Install AI integration requirements
echo "🔧 Installing AI integration dependencies..."
pip install -r ai-requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ AI integration dependencies installed successfully"
else
    echo "❌ Error installing dependencies"
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "🔧 Creating environment configuration file..."
    cp ai.env.example .env
    echo "✅ Environment file created from template"
    echo ""
    echo "⚠️  IMPORTANT: You need to configure your OpenAI API key in the .env file"
    echo "   1. Get your API key from: https://platform.openai.com/api-keys"
    echo "   2. Edit the .env file and set OPENAI_API_KEY=your_key_here"
    echo "   3. Optionally adjust other settings like model and confidence thresholds"
    echo ""
else
    echo "✅ Environment file already exists"
fi

# Test AI integration
echo "🧪 Testing AI integration..."
python3 -c "
from ai_integration import get_ai_integration
ai = get_ai_integration()
health = ai.health_check()
print(f'AI Integration Health Check:')
print(f'  AI Enabled: {health[\"ai_enabled\"]}')
print(f'  OpenAI Configured: {health[\"openai_configured\"]}')
print(f'  Model: {health[\"model\"]}')
"

if [ $? -eq 0 ]; then
    echo "✅ AI integration test successful"
else
    echo "⚠️  AI integration test failed (this is normal if no API key is configured)"
fi

echo ""
echo "🎉 AI Integration Setup Complete!"
echo ""
echo "📋 Next Steps:"
echo "   1. Configure your OpenAI API key in the .env file"
echo "   2. Test the integration with: python3 -c 'from ai_integration import get_ai_integration; print(\"Working!\")'"
echo "   3. Restart Mariam bot to enable AI features"
echo ""
echo "🔧 To activate the environment in the future:"
echo "   source ai-env/bin/activate"
echo ""
echo "📚 For more information, check the AI integration documentation"
