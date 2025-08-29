#!/usr/bin/env python3
"""
DeenBot 100+ Question Test - Comprehensive Knowledge Base Verification
Tests all expanded topics to ensure the 1000x knowledge expansion is working
"""

import requests
import json
import time
from datetime import datetime

class DeenBotTester:
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
        
        # 100+ comprehensive test questions covering all topics
        self.test_questions = [
            # Core Islamic Concepts
            "What is Islam?",
            "What is Taqwa?",
            "What are the five pillars of Islam?",
            "What is the Shahada?",
            "What is Salah?",
            "What is Zakat?",
            "What is Sawm?",
            "What is Hajj?",
            
            # Prayer and Worship
            "How to perform wudu?",
            "How to pray?",
            "What is dua?",
            "What is dhikr?",
            "What is tahajjud?",
            "What are prayer times?",
            "How to make dua?",
            "What is the importance of prayer?",
            
            # Islamic Ethics and Character
            "What is patience in Islam?",
            "What is gratitude in Islam?",
            "What is humility in Islam?",
            "What is honesty in Islam?",
            "How to control anger?",
            "What is sabr?",
            "What is shukr?",
            "What is tawadu?",
            
            # Family and Relationships
            "How to treat parents?",
            "What is marriage in Islam?",
            "How to raise children?",
            "What is family in Islam?",
            "How to be a good spouse?",
            "What are family rights?",
            "How to resolve family conflicts?",
            "What is parenting in Islam?",
            
            # Business and Finance
            "What is Islamic business?",
            "What is riba?",
            "What is charity in Islam?",
            "How to manage wealth?",
            "What is halal business?",
            "What is Islamic banking?",
            "How to give zakat?",
            "What is sadaqah?",
            
            # Health and Wellness
            "What is health in Islam?",
            "How to seek medical treatment?",
            "What is hygiene in Islam?",
            "What is exercise in Islam?",
            "How to maintain health?",
            "What is Islamic medicine?",
            "How to stay healthy?",
            "What is wellness in Islam?",
            
            # Education and Knowledge
            "What is education in Islam?",
            "How to seek knowledge?",
            "What is wisdom in Islam?",
            "How to understand Islam?",
            "What is learning in Islam?",
            "How to gain wisdom?",
            "What is Islamic education?",
            "How to study Islam?",
            
            # Social Justice and Community
            "What is justice in Islam?",
            "What is equality in Islam?",
            "How to build community?",
            "How to serve others?",
            "What is social justice?",
            "How to help neighbors?",
            "What is community service?",
            "How to promote unity?",
            
            # Advanced Islamic Topics
            "What is aqeedah?",
            "What is fiqh?",
            "What is seerah?",
            "What is sufism?",
            "What are Islamic beliefs?",
            "What is Islamic law?",
            "What is prophet biography?",
            "What is spirituality?",
            
            # Islamic History and Civilization
            "What is Islamic history?",
            "What was the Golden Age?",
            "What is Al-Andalus?",
            "What is the Ottoman Empire?",
            "What is Islamic civilization?",
            "What are Muslim achievements?",
            "What is Islamic Spain?",
            "What is Muslim history?",
            
            # Contemporary Issues
            "What are modern challenges?",
            "How to deal with technology?",
            "What is interfaith dialogue?",
            "How to promote understanding?",
            "What is Islamic finance?",
            "How to bank halal?",
            "What is environmental protection?",
            "How to protect the environment?",
            
            # Personal Development
            "What is Islamic psychology?",
            "How to manage mental health?",
            "What is emotional intelligence?",
            "How to control emotions?",
            "How to manage stress?",
            "How to cope with difficulties?",
            "How to set goals?",
            "How to achieve objectives?",
            
            # Advanced Worship
            "What is night prayer?",
            "How to do advanced dhikr?",
            "What are dhikr methods?",
            "What are dua collections?",
            "How to make supplications?",
            "How to memorize Quran?",
            "What is hifz?",
            "How to recite Quran?",
            
            # Islamic Culture
            "What is Islamic art?",
            "What is Muslim art?",
            "What is Islamic architecture?",
            "How to design mosques?",
            "What is Islamic literature?",
            "What is Muslim literature?",
            "What is Islamic music?",
            "What are nasheeds?",
            
            # Quranic Knowledge
            "What are important Quranic verses?",
            "What are essential verses?",
            "How to understand Quran?",
            "What are hadith collections?",
            "What are hadith books?",
            "How to verify hadith?",
            "What is authentic hadith?",
            "How to study hadith?",
            
            # Additional Topics
            "What is Ramadan?",
            "What is fasting?",
            "What is pilgrimage?",
            "What is the Kaaba?",
            "What is Mecca?",
            "What is Medina?",
            "What is the Prophet's Mosque?",
            "What is the Black Stone?",
            
            # Edge Cases and Variations
            "What is the meaning of Bismillah?",
            "How to become a better Muslim?",
            "What is the purpose of life?",
            "How to find peace?",
            "What is the best way to worship?",
            "How to strengthen faith?",
            "What is the most important thing in Islam?",
            "How to be closer to Allah?",
            
            # Complex Questions
            "What is the difference between Sunnah and Hadith?",
            "How does Islam view modern science?",
            "What is the Islamic perspective on democracy?",
            "How to balance tradition and modernity?",
            "What is the role of women in Islam?",
            "How to deal with non-Muslims?",
            "What is jihad in Islam?",
            "How to understand Islamic rulings?",
            
            # Practical Life
            "How to eat according to Sunnah?",
            "What is Islamic etiquette?",
            "How to dress modestly?",
            "What is halal food?",
            "How to greet people?",
            "What is visiting etiquette?",
            "How to be a good neighbor?",
            "What is social media etiquette?",
            
            # Spiritual Growth
            "How to increase iman?",
            "What is spiritual purification?",
            "How to develop taqwa?",
            "What is heart purification?",
            "How to find inner peace?",
            "What is spiritual growth?",
            "How to connect with Allah?",
            "What is divine love?",
            
            # Final Comprehensive Questions
            "What is the complete Islamic way of life?",
            "How to implement Islam in daily life?",
            "What is the ultimate goal of a Muslim?",
            "How to be successful in this life and the next?",
            "What is the comprehensive Islamic guidance?",
            "How to live as a true Muslim?",
            "What is the path to Paradise?",
            "How to achieve eternal happiness?"
        ]
        
        print(f"🚀 DeenBot 100+ Question Test")
        print(f"📊 Total Questions: {len(self.test_questions)}")
        print(f"🌐 Testing URL: {self.base_url}")
        print("=" * 60)
    
    def test_question(self, question, question_number):
        """Test a single question"""
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
                if data.get('response') and len(data['response']) > 50:
                    self.test_results['successful'] += 1
                    print(f"✅ Q{question_number:3d}: SUCCESS - {question[:50]}...")
                    return True
                else:
                    self.test_results['failed'] += 1
                    error_msg = f"Q{question_number}: Empty or short response"
                    self.test_results['errors'].append(error_msg)
                    print(f"❌ Q{question_number:3d}: FAILED - {question[:50]}... (Empty response)")
                    return False
            else:
                self.test_results['failed'] += 1
                error_msg = f"Q{question_number}: HTTP {response.status_code}"
                self.test_results['errors'].append(error_msg)
                print(f"❌ Q{question_number:3d}: FAILED - {question[:50]}... (HTTP {response.status_code})")
                return False
                
        except requests.exceptions.Timeout:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: Timeout"
            self.test_results['errors'].append(error_msg)
            print(f"⏰ Q{question_number:3d}: TIMEOUT - {question[:50]}...")
            return False
            
        except requests.exceptions.ConnectionError:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: Connection error"
            self.test_results['errors'].append(error_msg)
            print(f"🔌 Q{question_number:3d}: CONNECTION ERROR - {question[:50]}...")
            return False
            
        except Exception as e:
            self.test_results['failed'] += 1
            error_msg = f"Q{question_number}: {type(e).__name__} - {str(e)}"
            self.test_results['errors'].append(error_msg)
            print(f"❌ Q{question_number:3d}: ERROR - {question[:50]}... ({type(e).__name__})")
            return False
    
    def run_comprehensive_test(self):
        """Run the comprehensive 100+ question test"""
        self.test_results['start_time'] = datetime.now()
        self.test_results['total_questions'] = len(self.test_questions)
        
        print(f"🔥 Starting comprehensive test at {self.test_results['start_time'].strftime('%H:%M:%S')}")
        print("=" * 60)
        
        for i, question in enumerate(self.test_questions, 1):
            self.test_question(question, i)
            
            # Progress update every 20 questions
            if i % 20 == 0:
                success_rate = (self.test_results['successful'] / i) * 100
                print(f"📊 Progress: {i}/{len(self.test_questions)} questions, {success_rate:.1f}% success rate")
                print("-" * 40)
            
            # Small delay to avoid overwhelming the server
            time.sleep(0.1)
        
        self.test_results['end_time'] = datetime.now()
        
        # Final results
        print("=" * 60)
        print("🎯 COMPREHENSIVE TEST COMPLETE!")
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
            print("   🎉 EXCELLENT! DeenBot knowledge base is working perfectly!")
        elif success_rate >= 80:
            print("   ✅ GOOD! DeenBot knowledge base is working well with minor issues.")
        elif success_rate >= 60:
            print("   ⚠️ FAIR! DeenBot knowledge base has some issues that need fixing.")
        else:
            print("   ❌ POOR! DeenBot knowledge base has significant problems.")
        
        return success_rate
    
    def save_results(self):
        """Save test results to file"""
        results_file = f"deenbot_100_questions_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
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
    """Main function to run the comprehensive test"""
    print("🕌 DeenBot 100+ Question Comprehensive Test")
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
    
    print("✅ DeenBot is running and ready for comprehensive testing")
    print("🔥 This will test over 100 questions covering all knowledge base topics")
    print("")
    
    # Confirm before starting
    response = input("🚀 Start the comprehensive 100+ question test? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Comprehensive test cancelled")
        return
    
    print("")
    print("🔥 Starting comprehensive knowledge base test...")
    print("📊 This will test all expanded topics and knowledge areas")
    print("")
    
    # Create and run tester
    tester = DeenBotTester()
    
    try:
        success_rate = tester.run_comprehensive_test()
    except KeyboardInterrupt:
        print("\n🛑 Comprehensive test interrupted by user")
        return
    
    # Save results
    results_file = tester.save_results()
    
    # Final recommendation
    if success_rate >= 95:
        print("\n🎉 DeenBot knowledge base is EXCELLENT!")
        print("   The 1000x expansion is working perfectly!")
        print("   Ready for production use with comprehensive Islamic guidance!")
    elif success_rate >= 80:
        print("\n✅ DeenBot knowledge base is working well!")
        print("   Most topics are accessible with minor issues.")
        print("   Good for general use with some areas needing attention.")
    else:
        print("\n❌ DeenBot knowledge base has significant issues!")
        print("   Many topics are not accessible.")
        print("   Needs fixing before production use.")
    
    return 0

if __name__ == '__main__':
    exit(main())
