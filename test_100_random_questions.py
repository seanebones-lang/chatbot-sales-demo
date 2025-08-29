#!/usr/bin/env python3
"""
DeenBot 100 Random Questions Test - Ultimate Knowledge Base Stress Test
Tests with completely random questions to ensure robustness and comprehensive coverage
"""

import requests
import json
import time
import random
from datetime import datetime

class RandomQuestionTester:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.test_results = {
            'total_questions': 0,
            'successful': 0,
            'failed': 0,
            'errors': [],
            'start_time': None,
            'end_time': None
        }
        
        # 100 completely random questions covering various scenarios
        self.random_questions = [
            # Random Islamic concepts
            "What is the meaning of Bismillah?",
            "How to perform wudu correctly?",
            "What are the benefits of fasting?",
            "How to make dua for parents?",
            "What is the importance of charity?",
            "How to strengthen iman?",
            "What is the best time to pray?",
            "How to deal with anxiety?",
            "What is Islamic banking?",
            "How to raise children Islamically?",
            
            # Random daily life questions
            "How to be a good neighbor?",
            "What is halal food?",
            "How to dress modestly?",
            "What is Islamic etiquette?",
            "How to greet people?",
            "What is visiting etiquette?",
            "How to eat according to Sunnah?",
            "What is social media etiquette?",
            "How to be patient?",
            "What is gratitude in Islam?",
            
            # Random spiritual questions
            "How to purify the heart?",
            "What is dhikr?",
            "How to connect with Allah?",
            "What is spiritual growth?",
            "How to find inner peace?",
            "What is divine love?",
            "How to increase taqwa?",
            "What is the purpose of life?",
            "How to be closer to Allah?",
            "What is the best way to worship?",
            
            # Random family questions
            "How to treat parents?",
            "What is marriage in Islam?",
            "How to resolve conflicts?",
            "What are family rights?",
            "How to be a good spouse?",
            "What is parenting in Islam?",
            "How to raise children?",
            "What is family in Islam?",
            "How to deal with family problems?",
            "What is divorce in Islam?",
            
            # Random business questions
            "What is Islamic business?",
            "How to avoid riba?",
            "What is halal business?",
            "How to manage wealth?",
            "What is charity in Islam?",
            "How to give zakat?",
            "What is sadaqah?",
            "How to invest halal?",
            "What is Islamic finance?",
            "How to bank halal?",
            
            # Random health questions
            "What is health in Islam?",
            "How to seek medical treatment?",
            "What is hygiene in Islam?",
            "How to stay healthy?",
            "What is Islamic medicine?",
            "How to maintain health?",
            "What is exercise in Islam?",
            "How to cope with stress?",
            "What is mental health in Islam?",
            "How to manage emotions?",
            
            # Random education questions
            "What is education in Islam?",
            "How to seek knowledge?",
            "What is wisdom in Islam?",
            "How to understand Islam?",
            "What is learning in Islam?",
            "How to gain wisdom?",
            "What is Islamic education?",
            "How to study Islam?",
            "What is the importance of knowledge?",
            "How to memorize Quran?",
            
            # Random social questions
            "What is justice in Islam?",
            "How to build community?",
            "What is equality in Islam?",
            "How to serve others?",
            "What is social justice?",
            "How to help neighbors?",
            "What is community service?",
            "How to promote unity?",
            "What is the role of women?",
            "How to deal with non-Muslims?",
            
            # Random advanced topics
            "What is aqeedah?",
            "What is fiqh?",
            "What is seerah?",
            "What is sufism?",
            "What is Islamic history?",
            "What was the Golden Age?",
            "What is Al-Andalus?",
            "What is the Ottoman Empire?",
            "What is Islamic civilization?",
            "What are Muslim achievements?",
            
            # Random contemporary issues
            "What are modern challenges?",
            "How to deal with technology?",
            "What is interfaith dialogue?",
            "How to promote understanding?",
            "What is Islamic finance?",
            "How to bank halal?",
            "What is environmental protection?",
            "How to protect the environment?",
            "What is Islamic psychology?",
            "How to manage mental health?"
        ]
        
        print(f"🎲 DeenBot 100 Random Questions Test")
        print(f"📊 Total Questions: {len(self.random_questions)}")
        print(f"🌐 Testing URL: {self.base_url}")
        print("=" * 60)
    
    def test_question(self, question, question_number):
        """Test a single random question"""
        try:
            payload = {"message": question}
            headers = {"Content-Type": "application/json"}
            
            response = requests.post(
                f"{self.base_url}/chat",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('response') and len(data['response']) > 30:
                    self.test_results['successful'] += 1
                    source = data.get('source', 'Unknown')
                    print(f"✅ Q{question_number:3d}: SUCCESS - {question[:40]}... -> {source}")
                    return True
                else:
                    self.test_results['failed'] += 1
                    error_msg = f"Q{question_number}: Empty or short response"
                    self.test_results['errors'].append(error_msg)
                    print(f"❌ Q{question_number:3d}: FAILED - {question[:40]}... (Empty response)")
                    return False
            else:
                self.test_results['failed'] += 1
                error_msg = f"Q{question_number}: HTTP {response.status_code}"
                self.test_results['errors'].append(error_msg)
                print(f"❌ Q{question_number:3d}: FAILED - {question[:40]}... (HTTP {response.status_code})")
                return False
                
        except requests.exceptions.Timeout:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: Timeout"
            self.test_results['errors'].append(error_msg)
            print(f"⏰ Q{question_number:3d}: TIMEOUT - {question[:40]}...")
            return False
            
        except requests.exceptions.ConnectionError:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: Connection error"
            self.test_results['errors'].append(error_msg)
            print(f"🔌 Q{question_number:3d}: CONNECTION ERROR - {question[:40]}...")
            return False
            
        except Exception as e:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: {type(e).__name__} - {str(e)}"
            self.test_results['errors'].append(error_msg)
            print(f"❌ Q{question_number:3d}: ERROR - {question[:40]}... ({type(e).__name__})")
            return False
    
    def run_random_test(self):
        """Run the 100 random questions test"""
        self.test_results['start_time'] = datetime.now()
        self.test_results['total_questions'] = len(self.random_questions)
        
        print(f"🎲 Starting random questions test at {self.test_results['start_time'].strftime('%H:%M:%S')}")
        print("=" * 60)
        
        # Shuffle questions for true randomness
        random.shuffle(self.random_questions)
        
        for i, question in enumerate(self.random_questions, 1):
            self.test_question(question, i)
            
            # Progress update every 20 questions
            if i % 20 == 0:
                success_rate = (self.test_results['successful'] / i) * 100
                print(f"📊 Progress: {i}/{len(self.random_questions)} questions, {success_rate:.1f}% success rate")
                print("-" * 40)
            
            # Small delay to avoid overwhelming the server
            time.sleep(0.1)
        
        self.test_results['end_time'] = datetime.now()
        
        # Final results
        print("=" * 60)
        print("🎯 RANDOM QUESTIONS TEST COMPLETE!")
        print("=" * 60)
        
        duration = (self.test_results['end_time'] - self.test_results['start_time']).total_seconds()
        success_rate = (self.test_results['successful'] / self.test_results['total_questions']) * 100
        
        print(f"📊 FINAL RESULTS:")
        print(f"   Total Questions: {self.test_results['total_questions']}")
        print(f"   Successful: {self.test_results['successful']}")
        print(f"   Failed: {self.test_results['failed']}")
        print(f"   Success Rate: {success_rate:.1f}%")
        print(f"   Duration: {duration:.1f} seconds")
        print(f"   Questions per second: {self.test_results['total_questions']/duration:.1f}")
        
        if self.test_results['errors']:
            print(f"\n❌ ERROR SUMMARY:")
            error_counts = {}
            for error in self.test_results['errors']:
                error_type = error.split(':')[0]
                error_counts[error_type] = error_counts.get(error_type, 0) + 1
            
            for error_type, count in error_counts.items():
                print(f"   {error_type}: {count} occurrences")
        
        print(f"\n🎯 RECOMMENDATION:")
        if success_rate >= 95:
            print("   🎉 EXCELLENT! DeenBot handles random questions perfectly!")
        elif success_rate >= 80:
            print("   ✅ GOOD! DeenBot handles most random questions well.")
        elif success_rate >= 60:
            print("   ⚠️ FAIR! DeenBot has some issues with random questions.")
        else:
            print("   ❌ POOR! DeenBot struggles with random questions.")
        
        return success_rate
    
    def save_results(self):
        """Save test results to file"""
        results_file = f"deenbot_100_random_questions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
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
    """Main function to run the random questions test"""
    print("🎲 DeenBot 100 Random Questions Test")
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
    
    print("✅ DeenBot is running and ready for random questions testing")
    print("🎲 This will test 100 random questions to ensure knowledge base robustness")
    print("")
    
    # Confirm before starting
    response = input("🎲 Start the 100 random questions test? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Random questions test cancelled")
        return
    
    print("")
    print("🎲 Starting random questions knowledge base test...")
    print("📊 This will test robustness with unexpected and varied queries")
    print("")
    
    # Create and run tester
    tester = RandomQuestionTester()
    
    try:
        success_rate = tester.run_random_test()
    except KeyboardInterrupt:
        print("\n🛑 Random questions test interrupted by user")
        return
    
    # Save results
    results_file = tester.save_results()
    
    # Final recommendation
    if success_rate >= 95:
        print("\n🎉 DeenBot knowledge base is EXCELLENT!")
        print("   Handles random questions perfectly!")
        print("   Ready for production use with any type of query!")
    elif success_rate >= 80:
        print("\n✅ DeenBot knowledge base is working well!")
        print("   Handles most random questions with minor issues.")
        print("   Good for general use with some areas needing attention.")
    else:
        print("\n❌ DeenBot knowledge base has significant issues!")
        print("   Struggles with random questions.")
        print("   Needs more work before production use.")
    
    return 0

if __name__ == '__main__':
    exit(main())
