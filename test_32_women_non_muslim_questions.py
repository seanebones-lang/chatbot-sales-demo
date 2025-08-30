#!/usr/bin/env python3
"""
DeenBot Test: 32 Questions About Islam from Non-Muslim Women's Perspective
Specialized testing of DeenBot's ability to handle gender-specific questions and concerns
"""

import requests
import json
import time
from datetime import datetime

class DeenBotWomenNonMuslimTester:
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
        
        # 32 specialized questions from non-Muslim women's perspective
        self.test_questions = [
            # Women's Rights and Status in Islam (8 questions)
            "What rights do women have in Islam?",
            "Is it true that Islam oppresses women?",
            "How does Islam view women's education?",
            "Can Muslim women work and have careers?",
            "What is the Islamic view on women's leadership?",
            "Do Muslim women have property rights?",
            "How does Islam protect women's dignity?",
            "What is the Islamic perspective on women's independence?",
            
            # Dress Code and Modesty (6 questions)
            "Why do Muslim women wear hijab?",
            "Is hijab mandatory for all Muslim women?",
            "What is the Islamic dress code for women?",
            "Can Muslim women wear makeup and jewelry?",
            "What should I wear when visiting Muslim women?",
            "How do Muslim women dress for different occasions?",
            
            # Family and Relationships (6 questions)
            "What is the Islamic view on marriage?",
            "Can Muslim women choose their own husbands?",
            "What are the rights of Muslim wives?",
            "How does Islam view divorce for women?",
            "What is the Islamic perspective on motherhood?",
            "How do Muslim women handle family conflicts?",
            
            # Social Interactions (6 questions)
            "How should I interact with Muslim women?",
            "Can I hug or shake hands with Muslim women?",
            "What topics are appropriate to discuss with Muslim women?",
            "How do Muslim women socialize with non-Muslims?",
            "What should I know about Muslim women's privacy?",
            "How do Muslim women participate in community activities?",
            
            # Modern Women's Issues (6 questions)
            "How does Islam address women's mental health?",
            "What is the Islamic view on women's sports and fitness?",
            "How do Muslim women balance work and family?",
            "What is the Islamic perspective on women's social media use?",
            "How does Islam address women's financial independence?",
            "What is the Islamic view on women's travel and mobility?"
        ]
        
        print("🕌 DeenBot Women's Non-Muslim Question Tester")
        print("=" * 60)
        print(f"👩 Testing {len(self.test_questions)} specialized questions about Islam")
        print(f"🌐 DeenBot URL: {self.base_url}")
        print("🎯 Focus: Women's rights, dress code, family, and modern issues")
        print()
    
    def test_question(self, question, question_number):
        """Test a single question and record results"""
        try:
            print(f"🔍 Question {question_number:2d}: {question}")
            
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
                
                # Show first 120 characters of response
                response_preview = response_text[:120].replace('\n', ' ').strip()
                if len(response_text) > 120:
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
        print("🚀 Starting specialized women's perspective DeenBot test...")
        print()
        
        self.test_results['start_time'] = datetime.now()
        self.test_results['total_questions'] = len(self.test_questions)
        
        # Test each question
        for i, question in enumerate(self.test_questions, 1):
            self.test_question(question, i)
            time.sleep(0.5)  # Small delay between requests
        
        self.test_results['end_time'] = datetime.now()
        
        # Generate comprehensive report
        self.generate_report()
    
    def generate_report(self):
        """Generate detailed test report"""
        print("📊 GENERATING WOMEN'S PERSPECTIVE TEST REPORT")
        print("=" * 60)
        
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
            print("   🎉 EXCELLENT: DeenBot handles women's questions exceptionally well!")
        elif success_rate >= 90:
            print("   ✅ VERY GOOD: DeenBot handles women's questions very well!")
        elif success_rate >= 80:
            print("   👍 GOOD: DeenBot handles women's questions well with minor issues.")
        elif success_rate >= 70:
            print("   ⚠️  FAIR: DeenBot has some issues with women's questions.")
        else:
            print("   ❌ POOR: DeenBot has significant issues with women's questions.")
        
        print()
        print("📁 Detailed results saved to: deenbot_women_non_muslim_test_results.json")
        
        # Save detailed results
        self.save_results()
    
    def save_results(self):
        """Save test results to JSON file"""
        results_file = f"deenbot_women_non_muslim_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
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
    print("🕌 DeenBot Women's Non-Muslim Question Tester")
    print("=" * 70)
    
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
    
    print("✅ DeenBot is running and ready for specialized testing")
    print("👩 This will test 32 questions about Islam from non-Muslim women's perspective")
    print("⏳ This will take approximately 3-5 minutes")
    print("")
    
    # Auto-authorize and start the test
    print("🚀 Auto-authorizing and starting the specialized women's perspective test...")
    print("")
    print("🔥 Starting specialized DeenBot test...")
    print("📊 Testing 32 women-focused questions about Islam")
    print("⏳ This will take several minutes")
    print("📈 Monitoring progress and response quality...")
    print("")
    
    # Create and run tester
    tester = DeenBotWomenNonMuslimTester()
    
    try:
        tester.run_comprehensive_test()
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
    
    print("\n🎯 Test completed!")

if __name__ == '__main__':
    main()
