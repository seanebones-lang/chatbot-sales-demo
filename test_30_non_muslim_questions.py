#!/usr/bin/env python3
"""
DeenBot Test: 30 Random Questions About Islam from Non-Muslim Perspective
Tests DeenBot's ability to handle diverse, realistic questions from non-Muslims
"""

import requests
import json
import time
from datetime import datetime

class DeenBotNonMuslimTester:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.test_results = {
            'total_questions': 0,
            'successful_responses': 0,
            'failed_responses': 0,
            'response_times': [],
            'questions_tested': [],
            'start_time': None,
            'end_time': None
        }
        
        # 30 realistic questions from non-Muslim perspective
        self.test_questions = [
            # Basic Understanding Questions
            "What is Islam and what do Muslims believe?",
            "Who is Allah and how is He different from God in other religions?",
            "What is the Quran and how is it different from the Bible?",
            "Who is Prophet Muhammad and why is he important to Muslims?",
            "What are the main differences between Islam and Christianity?",
            "What are the main differences between Islam and Judaism?",
            
            # Cultural and Social Questions
            "Why do Muslim women wear hijab?",
            "What is halal food and why is it important?",
            "Why do Muslims pray five times a day?",
            "What is Ramadan and why do Muslims fast?",
            "Why do Muslims face Mecca when praying?",
            "What is the significance of the Kaaba?",
            
            # Practical Questions
            "How do Muslims greet each other?",
            "What should I do if I'm invited to a Muslim home?",
            "Can non-Muslims visit mosques?",
            "What are the rules for non-Muslims during Ramadan?",
            "How do Muslims celebrate their holidays?",
            "What is the proper way to interact with Muslim colleagues?",
            
            # Misconceptions and Clarifications
            "Is Islam a violent religion?",
            "Do Muslims believe in Jesus?",
            "What does Jihad really mean?",
            "Why do some Muslim countries have different laws?",
            "Is it true that Muslims can't eat pork?",
            "Why do some Muslims have multiple wives?",
            
            # Modern and Contemporary Issues
            "How does Islam view modern technology?",
            "What is the Islamic perspective on democracy?",
            "How do Muslims view other religions?",
            "What is the Islamic stance on human rights?",
            "How does Islam address environmental issues?",
            "What is the future of Islam in the modern world?"
        ]
        
        print("🕌 DeenBot Non-Muslim Question Tester")
        print("=" * 50)
        print(f"📝 Testing {len(self.test_questions)} questions about Islam")
        print(f"🌐 DeenBot URL: {self.base_url}")
        print()
    
    def test_question(self, question, question_number):
        """Test a single question and record results"""
        try:
            print(f"🔍 Question {question_number}: {question}")
            
            # Prepare request
            payload = {"message": question}
            headers = {"Content-Type": "application/json"}
            
            # Record start time
            start_time = time.time()
            
            # Make request
            response = requests.post(
                f"{self.base_url}/chat",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            # Calculate response time
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                self.test_results['successful_responses'] += 1
                self.test_results['response_times'].append(response_time)
                
                # Extract key information
                response_text = data.get('response', '')
                source = data.get('source', 'Unknown')
                references = data.get('references', [])
                
                print(f"✅ Response received in {response_time:.2f}s")
                print(f"📚 Source: {source}")
                print(f"📖 References: {len(references)} provided")
                
                # Show first 150 characters of response
                response_preview = response_text[:150].replace('\n', ' ').strip()
                if len(response_text) > 150:
                    response_preview += "..."
                print(f"💬 Response preview: {response_preview}")
                
                # Record question details
                self.test_results['questions_tested'].append({
                    'question': question,
                    'response_time': response_time,
                    'source': source,
                    'references_count': len(references),
                    'response_length': len(response_text)
                })
                
            else:
                self.test_results['failed_responses'] += 1
                print(f"❌ Failed with status {response.status_code}")
                print(f"📄 Response: {response.text}")
                
        except requests.exceptions.Timeout:
            self.test_results['failed_responses'] += 1
            print(f"⏰ Request timed out")
        except requests.exceptions.ConnectionError:
            self.test_results['failed_responses'] += 1
            print(f"🔌 Connection error")
        except Exception as e:
            self.test_results['failed_responses'] += 1
            print(f"❌ Error: {str(e)}")
        
        print("-" * 80)
        print()
    
    def run_comprehensive_test(self):
        """Run the complete test suite"""
        print("🚀 Starting comprehensive DeenBot test...")
        print()
        
        self.test_results['start_time'] = datetime.now()
        self.test_results['total_questions'] = len(self.test_questions)
        
        # Test each question
        for i, question in enumerate(self.test_questions, 1):
            self.test_question(question, i)
            time.sleep(1)  # Small delay between requests
        
        self.test_results['end_time'] = datetime.now()
        
        # Generate comprehensive report
        self.generate_report()
    
    def generate_report(self):
        """Generate detailed test report"""
        print("📊 GENERATING COMPREHENSIVE TEST REPORT")
        print("=" * 50)
        
        duration = (self.test_results['end_time'] - self.test_results['start_time']).total_seconds()
        success_rate = (self.test_results['successful_responses'] / self.test_results['total_questions']) * 100
        
        # Calculate response time statistics
        if self.test_results['response_times']:
            avg_response_time = sum(self.test_results['response_times']) / len(self.test_results['response_times'])
            min_response_time = min(self.test_results['response_times'])
            max_response_time = max(self.test_results['response_times'])
        else:
            avg_response_time = min_response_time = max_response_time = 0
        
        print(f"📅 Test Date: {self.test_results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)")
        print(f"📊 Total Questions: {self.test_results['total_questions']}")
        print(f"✅ Successful Responses: {self.test_results['successful_responses']}")
        print(f"❌ Failed Responses: {self.test_results['failed_responses']}")
        print(f"📈 Success Rate: {success_rate:.1f}%")
        print()
        
        print("⏱️  RESPONSE TIME ANALYSIS:")
        print(f"   Average: {avg_response_time:.2f} seconds")
        print(f"   Fastest: {min_response_time:.2f} seconds")
        print(f"   Slowest: {max_response_time:.2f} seconds")
        print()
        
        print("🎯 RESPONSE QUALITY ANALYSIS:")
        if self.test_results['questions_tested']:
            # Analyze response sources
            sources = {}
            total_references = 0
            total_response_length = 0
            
            for test in self.test_results['questions_tested']:
                source = test['source']
                sources[source] = sources.get(source, 0) + 1
                total_references += test['references_count']
                total_response_length += test['response_length']
            
            print("   Response Sources:")
            for source, count in sources.items():
                print(f"     {source}: {count} responses")
            
            avg_references = total_references / len(self.test_results['questions_tested'])
            avg_response_length = total_response_length / len(self.test_results['questions_tested'])
            
            print(f"   Average References per Response: {avg_references:.1f}")
            print(f"   Average Response Length: {avg_response_length:.0f} characters")
        
        print()
        print("🏆 FINAL ASSESSMENT:")
        if success_rate >= 95:
            print("   🎉 EXCELLENT: DeenBot is performing exceptionally well!")
        elif success_rate >= 90:
            print("   ✅ VERY GOOD: DeenBot is performing very well!")
        elif success_rate >= 80:
            print("   👍 GOOD: DeenBot is performing well with minor issues.")
        elif success_rate >= 70:
            print("   ⚠️  FAIR: DeenBot has some issues that need attention.")
        else:
            print("   ❌ POOR: DeenBot has significant issues that need immediate fixing.")
        
        print()
        print("📁 Detailed results saved to: deenbot_non_muslim_test_results.json")
        
        # Save detailed results
        self.save_results()
    
    def save_results(self):
        """Save test results to JSON file"""
        results_file = f"deenbot_non_muslim_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convert datetime objects to strings for JSON serialization
        json_results = self.test_results.copy()
        if json_results['start_time']:
            json_results['start_time'] = json_results['start_time'].isoformat()
        if json_results['end_time']:
            json_results['end_time'] = json_results['end_time'].isoformat()
        
        with open(results_file, 'w') as f:
            json.dump(json_results, f, indent=2)
        
        print(f"💾 Results saved to: {results_file}")

def main():
    """Main function to run the test"""
    print("🕌 DeenBot Non-Muslim Question Tester")
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
    
    print("✅ DeenBot is running and ready for testing")
    print("📝 This will test 30 realistic questions about Islam from non-Muslim perspective")
    print("")
    
    # Confirm before starting
    response = input("🚀 Start the comprehensive test? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Test cancelled")
        return
    
    print("")
    print("🔥 Starting comprehensive DeenBot test...")
    print("📊 Testing 30 diverse questions about Islam")
    print("⏳ This will take several minutes")
    print("")
    
    # Create and run tester
    tester = DeenBotNonMuslimTester()
    
    try:
        tester.run_comprehensive_test()
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
    
    print("\n🎯 Test completed!")

if __name__ == '__main__':
    main()
