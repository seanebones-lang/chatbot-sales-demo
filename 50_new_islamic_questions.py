#!/usr/bin/env python3
"""
50 New Islamic Questions Test - Realistic User Queries
Tests with authentic questions that Muslims actually ask in real life
"""

import requests
import json
import time
from datetime import datetime

class RealisticIslamicQuestionTester:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.test_results = {
            'total_questions': 0,
            'successful': 0,
            'failed': 0,
            'errors': [],
            'start_time': None,
            'end_time': None,
            'question_details': []
        }
        
        # 50 realistic Islamic questions that Muslims actually ask
        self.realistic_questions = [
            # Prayer & Worship
            "Can I pray if I'm bleeding from a cut?",
            "What if I miss Fajr prayer?",
            "How do I know which direction to pray?",
            "Can I pray in my work clothes?",
            "What should I do if I forget how many rakats I prayed?",
            "Is it okay to pray with nail polish?",
            "Can I pray if I have makeup on?",
            "What if I'm traveling and can't find a clean place to pray?",
            
            # Fasting & Ramadan
            "What if I accidentally eat during fasting?",
            "Can I take medicine while fasting?",
            "What if I forget I'm fasting and drink water?",
            "Do I need to make up missed fasts from last year?",
            "Can I brush my teeth while fasting?",
            "What if I'm sick during Ramadan?",
            "Is it okay to exercise while fasting?",
            "What if I break my fast early by mistake?",
            
            # Family & Relationships
            "How should I treat my non-Muslim family?",
            "What if my parents don't approve of my Islamic practices?",
            "Can I marry someone from a different culture?",
            "How do I explain Islam to my children?",
            "What if my spouse doesn't pray?",
            "How should I handle family conflicts?",
            "Can I attend non-Muslim family celebrations?",
            "What if my family doesn't understand my hijab?",
            
            # Work & Business
            "How do I handle riba in my job?",
            "Can I work in a bank?",
            "What if my boss asks me to lie?",
            "How do I maintain Islamic values at work?",
            "Can I shake hands with the opposite gender?",
            "What if my company serves alcohol at events?",
            "How do I handle interest-based loans?",
            "Can I work on Fridays?",
            
            # Modern Life
            "Is it okay to use social media?",
            "How do I deal with Islamophobia online?",
            "Can I listen to music?",
            "What if my friends drink alcohol?",
            "How do I maintain modesty in modern society?",
            "Can I watch movies and TV shows?",
            "How do I handle dating apps?",
            "What if I'm invited to a party with alcohol?",
            
            # Health & Medical
            "Can I get a tattoo for medical reasons?",
            "What if I need a blood transfusion?",
            "How do I handle medical procedures during Ramadan?",
            "Can I take birth control?",
            "What if I need surgery?",
            "How do I maintain health while fasting?",
            "Can I use pain medication?",
            "What if I'm pregnant during Ramadan?",
            
            # Education & Learning
            "How do I study Islam while in school?",
            "Can I attend a non-Muslim university?",
            "What if my teacher says something against Islam?",
            "How do I handle exams during Ramadan?",
            "Can I study with the opposite gender?",
            "What if my school serves non-halal food?",
            "How do I balance Islamic studies with other subjects?",
            "Can I participate in school sports?",
            
            # Community & Society
            "How do I find a good mosque?",
            "What if there's no mosque in my area?",
            "How do I deal with cultural differences in Islam?",
            "Can I participate in community events?",
            "What if my neighbors are Islamophobic?",
            "How do I help new Muslims?",
            "Can I volunteer at non-Muslim organizations?",
            "What if my community doesn't understand Islam?"
        ]
    
    def run_realistic_test(self):
        """Run the realistic Islamic questions test"""
        print("🎯 DeenBot 50 Realistic Islamic Questions Test")
        print("📊 Total Questions:", len(self.realistic_questions))
        print("🌐 Testing URL:", self.base_url)
        print("=" * 60)
        
        self.test_results['start_time'] = datetime.now()
        print(f"🎯 Starting realistic questions test at {self.test_results['start_time'].strftime('%H:%M:%S')}")
        print("=" * 60)
        
        for i, question in enumerate(self.realistic_questions, 1):
            try:
                # Send question to DeenBot
                response = requests.post(
                    f"{self.base_url}/chat",
                    json={"message": question},
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    source = data.get('source', 'Unknown')
                    
                    # Record successful response
                    self.test_results['successful'] += 1
                    self.test_results['question_details'].append({
                        'question': question,
                        'response_length': len(data.get('response', '')),
                        'source': source,
                        'status': 'success'
                    })
                    
                    print(f"✅ Q {i:2d}: SUCCESS - {question[:50]}... -> {source}")
                    
                else:
                    # Record failed response
                    self.test_results['failed'] += 1
                    error_msg = f"HTTP {response.status_code}"
                    self.test_results['errors'].append(error_msg)
                    self.test_results['question_details'].append({
                        'question': question,
                        'error': error_msg,
                        'status': 'failed'
                    })
                    
                    print(f"❌ Q {i:2d}: FAILED - {question[:50]}... -> {error_msg}")
                
                self.test_results['total_questions'] += 1
                
                # Show progress every 10 questions
                if i % 10 == 0:
                    success_rate = (self.test_results['successful'] / self.test_results['total_questions']) * 100
                    print(f"📊 Progress: {i}/{len(self.realistic_questions)} questions, {success_rate:.1f}% success rate")
                    print("-" * 40)
                
                # Small delay to be respectful to the server
                time.sleep(0.1)
                
            except requests.exceptions.Timeout:
                error_msg = "Timeout"
                self.test_results['failed'] += 1
                self.test_results['errors'].append(error_msg)
                self.test_results['question_details'].append({
                    'question': question,
                    'error': error_msg,
                    'status': 'failed'
                })
                print(f"⏰ Q {i:2d}: TIMEOUT - {question[:50]}...")
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                self.test_results['failed'] += 1
                self.test_results['errors'].append(error_msg)
                self.test_results['question_details'].append({
                    'question': question,
                    'error': error_msg,
                    'status': 'failed'
                })
                print(f"💥 Q {i:2d}: ERROR - {question[:50]}... -> {error_msg}")
        
        # Calculate final results
        self.test_results['end_time'] = datetime.now()
        duration = (self.test_results['end_time'] - self.test_results['start_time']).total_seconds()
        success_rate = (self.test_results['successful'] / self.test_results['total_questions']) * 100
        
        print("=" * 60)
        print("🎯 REALISTIC ISLAMIC QUESTIONS TEST COMPLETE!")
        print("=" * 60)
        
        print("📊 FINAL RESULTS:")
        print(f"   Total Questions: {self.test_results['total_questions']}")
        print(f"   Successful: {self.test_results['successful']}")
        print(f"   Failed: {self.test_results['failed']}")
        print(f"   Success Rate: {success_rate:.1f}%")
        print(f"   Duration: {duration:.1f} seconds")
        print(f"   Questions per second: {self.test_results['total_questions']/duration:.1f}")
        
        if self.test_results['errors']:
            print(f"\n❌ ERRORS ENCOUNTERED:")
            error_counts = {}
            for error in self.test_results['errors']:
                error_type = error.split(':')[0] if ':' in error else error
                error_counts[error_type] = error_counts.get(error_type, 0) + 1
            
            for error_type, count in error_counts.items():
                print(f"   {error_type}: {count} occurrences")
        
        print(f"\n🎯 RECOMMENDATION:")
        if success_rate >= 95:
            print("   🎉 EXCELLENT! DeenBot handles realistic questions perfectly!")
        elif success_rate >= 80:
            print("   ✅ GOOD! DeenBot handles most realistic questions well.")
        elif success_rate >= 60:
            print("   ⚠️ FAIR! DeenBot has some issues with realistic questions.")
        else:
            print("   ❌ POOR! DeenBot struggles with realistic questions.")
        
        return success_rate
    
    def save_results(self):
        """Save test results to file"""
        results_file = f"deenbot_50_realistic_questions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convert datetime objects to strings for JSON serialization
        json_results = self.test_results.copy()
        if json_results['start_time']:
            json_results['start_time'] = json_results['start_time'].isoformat()
        if json_results['end_time']:
            json_results['end_time'] = json_results['end_time'].isoformat()
        
        with open(results_file, 'w') as f:
            json.dump(json_results, f, indent=2)
        
        print(f"\n📁 Test results saved to: {results_file}")
        return results_file

def main():
    """Main function to run the realistic Islamic questions test"""
    print("🎯 DeenBot 50 Realistic Islamic Questions Test")
    print("=" * 60)
    
    # Check if DeenBot is running
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        if response.status_code != 200:
            print("❌ DeenBot is not running on port 8080")
            print("   Please start DeenBot first")
            return
    except:
        print("❌ Cannot connect to DeenBot on port 8080")
        print("   Please start DeenBot first")
        return
    
    print("✅ DeenBot is running and ready for realistic questions testing")
    print("🎯 This will test 50 realistic questions that Muslims actually ask")
    print("")
    
    # Confirm before starting
    response = input("🎯 Start the 50 realistic Islamic questions test? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Realistic questions test cancelled")
        return
    
    print("")
    print("🎯 Starting realistic Islamic questions test...")
    print("📊 This will test practical knowledge with real-world scenarios")
    print("")
    
    # Create and run tester
    tester = RealisticIslamicQuestionTester()
    
    try:
        success_rate = tester.run_realistic_test()
    except KeyboardInterrupt:
        print("\n🛑 Realistic questions test interrupted by user")
        return
    
    # Save results
    results_file = tester.save_results()
    
    # Final recommendation
    if success_rate >= 95:
        print("\n🎉 DeenBot handles realistic questions EXCELLENTLY!")
        print("   Ready for real-world use with authentic Muslim queries!")
        print("   Perfect for daily Islamic guidance!")
    elif success_rate >= 80:
        print("\n✅ DeenBot handles realistic questions well!")
        print("   Good for general use with some areas needing attention.")
        print("   Suitable for most real-world scenarios.")
    else:
        print("\n❌ DeenBot has issues with realistic questions!")
        print("   Needs more work before handling real-world queries.")
        print("   Focus on practical Islamic knowledge areas.")
    
    return 0

if __name__ == '__main__':
    exit(main())
