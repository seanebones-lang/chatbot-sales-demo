#!/usr/bin/env python3
"""
DeenBot Fix Verification Test - Verify that previously failing topics now work
"""

import requests
import json

def test_topic(topic):
    """Test a single topic"""
    try:
        payload = {"message": topic}
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(
            "http://localhost:8080/chat",
            json=payload,
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            source = data.get('source', 'Unknown')
            response_text = data.get('response', '')[:100] + "..."
            print(f"✅ {topic:25} -> {source:30} | {response_text}")
            return True
        else:
            print(f"❌ {topic:25} -> HTTP {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ {topic:25} -> ERROR: {type(e).__name__}")
        return False

def main():
    """Test all previously failing topics"""
    print("🔧 DeenBot Fix Verification Test")
    print("=" * 60)
    print("Testing previously failing topics to verify the fix...")
    print("")
    
    # Topics that were failing before the fix
    previously_failing_topics = [
        "aqeedah",
        "fiqh", 
        "seerah",
        "sufism",
        "golden age",
        "ottoman empire",
        "modern challenges",
        "interfaith dialogue",
        "halal banking",
        "environmental protection",
        "emotional intelligence",
        "goal setting",
        "advanced dhikr",
        "dua collections",
        "quran memorization",
        "hadith collections",
        "fasting",
        "pilgrimage",
        "sunnah",
        "hadith"
    ]
    
    print(f"📊 Testing {len(previously_failing_topics)} previously failing topics...")
    print("")
    
    successful = 0
    failed = 0
    
    for topic in previously_failing_topics:
        if test_topic(topic):
            successful += 1
        else:
            failed += 1
    
    print("")
    print("=" * 60)
    print("🎯 FIX VERIFICATION RESULTS:")
    print(f"   Previously Failing Topics: {len(previously_failing_topics)}")
    print(f"   Now Working: {successful} ✅")
    print(f"   Still Failing: {failed} ❌")
    print(f"   Success Rate: {(successful/len(previously_failing_topics)*100):.1f}%")
    
    if failed == 0:
        print("\n🎉 PERFECT! All previously failing topics are now working!")
        print("   DeenBot enhanced knowledge base is fully functional!")
    elif failed <= 2:
        print("\n✅ EXCELLENT! Almost all topics are working!")
        print("   DeenBot enhanced knowledge base is highly functional!")
    elif failed <= 5:
        print("\n⚠️ GOOD! Most topics are working with minor issues.")
        print("   DeenBot enhanced knowledge base is mostly functional!")
    else:
        print("\n❌ NEEDS MORE WORK! Several topics are still failing.")
        print("   DeenBot enhanced knowledge base needs more fixing!")
    
    return successful, failed

if __name__ == '__main__':
    main()
