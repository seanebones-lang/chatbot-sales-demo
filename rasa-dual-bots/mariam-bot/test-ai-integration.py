#!/usr/bin/env python3
"""
Test script for AI Integration System
Run this to verify everything is working correctly
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import openai
        print("✅ OpenAI module imported successfully")
    except ImportError as e:
        print(f"❌ OpenAI module import failed: {e}")
        return False
    
    try:
        from ai_integration import get_ai_integration
        print("✅ AI integration module imported successfully")
    except ImportError as e:
        print(f"❌ AI integration module import failed: {e}")
        return False
    
    return True

def test_ai_integration():
    """Test the AI integration system"""
    print("\n🤖 Testing AI integration system...")
    
    try:
        from ai_integration import get_ai_integration
        ai = get_ai_integration()
        
        # Test health check
        health = ai.health_check()
        print(f"✅ Health check completed")
        print(f"   AI Enabled: {health['ai_enabled']}")
        print(f"   OpenAI Configured: {health['openai_connection']}")
        print(f"   Model: {health['model']}")
        
        # Test usage stats
        stats = ai.get_usage_statistics()
        print(f"✅ Usage statistics retrieved")
        print(f"   Total Requests: {stats['total_requests']}")
        
        return True
        
    except Exception as e:
        print(f"❌ AI integration test failed: {e}")
        return False

def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🔌 Testing OpenAI connection...")
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("⚠️  OpenAI API key not configured")
        print("   Set OPENAI_API_KEY in your .env file to test API connection")
        return False
    
    try:
        import openai
        
        # Test with a simple request (using new API format)
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        
        print("✅ OpenAI API connection successful")
        print(f"   Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API connection failed: {e}")
        return False

def test_confidence_scoring():
    """Test confidence scoring system"""
    print("\n🎯 Testing confidence scoring...")
    
    try:
        from ai_integration import get_ai_integration
        ai = get_ai_integration()
        
        # Test confidence calculation
        confidence = ai.calculate_confidence_score(0.8, 0.7, 0.9)
        print(f"✅ Confidence scoring working")
        print(f"   Sample confidence: {confidence:.3f}")
        
        # Test response mode determination
        mode = ai.determine_response_mode(confidence, "test message", {})
        print(f"   Response mode: {mode}")
        
        return True
        
    except Exception as e:
        print(f"❌ Confidence scoring test failed: {e}")
        return False

def test_context_management():
    """Test conversation context management"""
    print("\n📝 Testing context management...")
    
    try:
        from ai_integration import get_ai_integration
        ai = get_ai_integration()
        
        # Test context update
        ai.update_conversation_context(
            user_id="test_user",
            user_message="Hello",
            bot_response="Hi there!",
            mode="knowledge_bot"
        )
        
        print("✅ Context management working")
        print(f"   Active contexts: {len(ai.conversation_contexts)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Context management test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 AI Integration System Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("AI Integration Test", test_ai_integration),
        ("OpenAI Connection Test", test_openai_connection),
        ("Confidence Scoring Test", test_confidence_scoring),
        ("Context Management Test", test_context_management)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! AI integration is working correctly.")
    elif passed >= total - 1:
        print("⚠️  Most tests passed. Check configuration for minor issues.")
    else:
        print("❌ Several tests failed. Review the errors above.")
    
    print("\n📋 Next Steps:")
    if passed >= 3:
        print("✅ Basic AI integration is working")
        print("   You can now use Mariam with AI capabilities")
    else:
        print("❌ Basic setup issues detected")
        print("   1. Check your .env file configuration")
        print("   2. Verify OpenAI API key is valid")
        print("   3. Ensure all dependencies are installed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
