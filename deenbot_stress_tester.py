#!/usr/bin/env python3
"""
DeenBot Stress Tester - Comprehensive 5-Minute Stability Test
Tests all variations of user text to ensure DeenBot won't crash
"""

import time
import json
import random
import threading
import requests
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('deenbot_stress_test.log'),
        logging.StreamHandler()
    ]
)

class DeenBotStressTester:
    """Comprehensive stress testing for DeenBot stability"""
    
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.test_duration = 300  # 5 minutes in seconds
        self.test_interval = 0.5  # Test every 0.5 seconds
        self.running = False
        self.test_results = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'errors': [],
            'start_time': None,
            'end_time': None,
            'crash_detected': False
        }
        
        # Comprehensive test data covering all Islamic topics
        self.test_queries = [
            # Basic Islamic questions
            "What is Islam?",
            "Who is Prophet Muhammad?",
            "What are the five pillars?",
            "How to pray?",
            "What is halal?",
            "What is haram?",
            
            # Quran related
            "Tell me about Surah Al-Fatiha",
            "What does the Quran say about charity?",
            "Quran verses about patience",
            "Quran on family values",
            "Quran teachings on honesty",
            "What does the Quran say about knowledge?",
            
            # Hadith related
            "Hadith about kindness",
            "Hadith about prayer",
            "Hadith about honesty",
            "Hadith about parents",
            "Hadith about neighbors",
            "Hadith about learning",
            
            # Islamic practices
            "How to perform wudu?",
            "How to fast during Ramadan?",
            "How to give zakat?",
            "How to perform Hajj?",
            "How to read Quran?",
            "How to make dua?",
            
            # Islamic ethics
            "Islamic view on lying",
            "Islamic view on stealing",
            "Islamic view on helping others",
            "Islamic view on education",
            "Islamic view on business",
            "Islamic view on marriage",
            
            # Complex queries
            "What is the difference between Sunnah and Hadith?",
            "Explain the concept of Taqwa in Islam",
            "What are the conditions for a valid marriage in Islam?",
            "How does Islam view modern technology?",
            "What is the Islamic perspective on environmental protection?",
            "How to deal with non-Muslims according to Islam?",
            
            # Edge cases and stress tests
            "A" * 1000,  # Very long text
            "1234567890" * 100,  # Numbers
            "!@#$%^&*()" * 50,  # Special characters
            "مرحبا بالعالم",  # Arabic text
            "Hello World 你好世界 مرحبا بالعالم",  # Mixed languages
            "",  # Empty string
            
            # Religious variations
            "What is the meaning of Bismillah?",
            "Explain the concept of Barakah",
            "What is the significance of the number 786?",
            "How to seek forgiveness in Islam?",
            "What is the importance of Friday prayer?",
            "How to deal with grief in Islam?",
            
            # Practical life questions
            "Islamic way to greet someone",
            "How to eat according to Sunnah?",
            "Islamic etiquette for visiting",
            "How to dress modestly?",
            "Islamic rules for social media",
            "How to be a good Muslim neighbor?",
            
            # Historical questions
            "Tell me about the Battle of Badr",
            "What happened during the Hijra?",
            "Who were the first Muslims?",
            "History of the Kaaba",
            "Story of Prophet Ibrahim",
            "Life of Prophet Muhammad's family",
            
            # Contemporary issues
            "Islam and modern science",
            "Islamic banking principles",
            "Islam and social justice",
            "Islamic view on democracy",
            "Islam and human rights",
            "Islamic perspective on climate change"
        ]
        
        # Additional random variations
        self.random_prefixes = ["Please", "Can you", "I need to know", "Tell me", "Explain", "What is", "How to"]
        self.random_suffixes = ["?", "!", "...", " please", " thank you", " in detail", " briefly"]
        
        logging.info("🚀 DeenBot Stress Tester initialized")
        logging.info(f"📊 Will test {len(self.test_queries)} base queries for {self.test_duration} seconds")
    
    def generate_variation(self, base_query):
        """Generate variations of a base query"""
        variations = []
        
        # Original query
        variations.append(base_query)
        
        # Add random prefixes and suffixes
        for prefix in random.sample(self.random_prefixes, 3):
            for suffix in random.sample(self.random_suffixes, 2):
                variations.append(f"{prefix} {base_query}{suffix}")
        
        # Add case variations
        variations.append(base_query.upper())
        variations.append(base_query.lower())
        variations.append(base_query.title())
        
        # Add spacing variations
        variations.append(base_query.replace(" ", "  "))  # Double spaces
        variations.append(base_query.replace(" ", ""))    # No spaces
        
        # Add punctuation variations
        variations.append(base_query + "??")
        variations.append(base_query + "!!!")
        variations.append(base_query + "...")
        
        return variations
    
    def test_query(self, query):
        """Test a single query against DeenBot"""
        try:
            # Prepare request
            payload = {"message": query}
            headers = {"Content-Type": "application/json"}
            
            # Make request with timeout
            response = requests.post(
                f"{self.base_url}/chat",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                self.test_results['successful_requests'] += 1
                logging.debug(f"✅ Query successful: '{query[:50]}...'")
                return True
            else:
                self.test_results['failed_requests'] += 1
                error_msg = f"HTTP {response.status_code}: {query[:50]}..."
                self.test_results['errors'].append(error_msg)
                logging.warning(f"❌ Query failed: {error_msg}")
                return False
                
        except requests.exceptions.Timeout:
            self.test_results['failed_requests'] += 1
            error_msg = f"Timeout: {query[:50]}..."
            self.test_results['errors'].append(error_msg)
            logging.error(f"⏰ Query timeout: {error_msg}")
            return False
            
        except requests.exceptions.ConnectionError:
            self.test_results['crash_detected'] = True
            error_msg = f"Connection error - DeenBot may have crashed: {query[:50]}..."
            self.test_results['errors'].append(error_msg)
            logging.critical(f"💥 CRASH DETECTED: {error_msg}")
            return False
            
        except Exception as e:
            self.test_results['failed_requests'] += 1
            error_msg = f"Exception {type(e).__name__}: {query[:50]}..."
            self.test_results['errors'].append(error_msg)
            logging.error(f"❌ Query exception: {error_msg}")
            return False
    
    def health_check(self):
        """Check if DeenBot is still responding"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def run_stress_test(self):
        """Run the comprehensive 5-minute stress test"""
        logging.info("🔥 Starting DeenBot Stress Test - 5 Minutes of Continuous Testing")
        logging.info("=" * 70)
        
        self.test_results['start_time'] = datetime.now()
        self.running = True
        
        start_time = time.time()
        last_health_check = start_time
        
        while self.running and (time.time() - start_time) < self.test_duration:
            try:
                # Health check every 10 seconds
                if time.time() - last_health_check >= 10:
                    if not self.health_check():
                        logging.critical("💥 DeenBot has crashed during stress test!")
                        self.test_results['crash_detected'] = True
                        break
                    last_health_check = time.time()
                
                # Test random queries
                base_query = random.choice(self.test_queries)
                variations = self.generate_variation(base_query)
                
                for variation in variations:
                    if not self.running or (time.time() - start_time) >= self.test_duration:
                        break
                    
                    self.test_results['total_requests'] += 1
                    success = self.test_query(variation)
                    
                    # Log progress every 50 requests
                    if self.test_results['total_requests'] % 50 == 0:
                        elapsed = time.time() - start_time
                        remaining = self.test_duration - elapsed
                        success_rate = (self.test_results['successful_requests'] / self.test_results['total_requests']) * 100
                        
                        logging.info(f"📊 Progress: {self.test_results['total_requests']} requests, "
                                   f"{success_rate:.1f}% success, {remaining:.1f}s remaining")
                    
                    # Small delay between requests
                    time.sleep(self.test_interval)
                
            except KeyboardInterrupt:
                logging.info("🛑 Stress test interrupted by user")
                break
            except Exception as e:
                logging.error(f"❌ Error in stress test loop: {e}")
                time.sleep(1)
        
        self.test_results['end_time'] = datetime.now()
        self.running = False
        
        # Final health check
        if self.health_check():
            logging.info("✅ DeenBot survived the stress test!")
        else:
            logging.critical("💥 DeenBot crashed during stress test!")
            self.test_results['crash_detected'] = True
    
    def generate_report(self):
        """Generate comprehensive test report"""
        if not self.test_results['start_time']:
            return "No test results available"
        
        duration = (self.test_results['end_time'] - self.test_results['start_time']).total_seconds()
        success_rate = (self.test_results['successful_requests'] / max(self.test_results['total_requests'], 1)) * 100
        
        report = f"""
🕌 DEENBOT STRESS TEST REPORT
{'=' * 50}

📅 Test Date: {self.test_results['start_time'].strftime('%Y-%m-%d %H:%M:%S')}
⏱️  Duration: {duration:.1f} seconds ({duration/60:.1f} minutes)
📊 Total Requests: {self.test_results['total_requests']:,}
✅ Successful: {self.test_results['successful_requests']:,}
❌ Failed: {self.test_results['failed_requests']:,}
📈 Success Rate: {success_rate:.1f}%

🚨 CRASH STATUS: {'💥 CRASHED' if self.test_results['crash_detected'] else '✅ STABLE'}

📋 ERROR SUMMARY:
"""
        
        if self.test_results['errors']:
            error_counts = {}
            for error in self.test_results['errors']:
                error_type = error.split(':')[0]
                error_counts[error_type] = error_counts.get(error_type, 0) + 1
            
            for error_type, count in error_counts.items():
                report += f"   {error_type}: {count} occurrences\n"
        else:
            report += "   No errors recorded\n"
        
        report += f"""

🎯 RECOMMENDATION: {'❌ FAILED - DeenBot needs fixing' if self.test_results['crash_detected'] else '✅ PASSED - DeenBot is stable'}

📁 Detailed logs saved to: deenbot_stress_test.log
"""
        
        return report
    
    def save_results(self):
        """Save test results to JSON file"""
        results_file = f"deenbot_stress_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        # Convert datetime objects to strings for JSON serialization
        json_results = self.test_results.copy()
        if json_results['start_time']:
            json_results['start_time'] = json_results['start_time'].isoformat()
        if json_results['end_time']:
            json_results['end_time'] = json_results['end_time'].isoformat()
        
        with open(results_file, 'w') as f:
            json.dump(json_results, f, indent=2)
        
        logging.info(f"📁 Test results saved to: {results_file}")
        return results_file

def main():
    """Main function to run the stress test"""
    print("🕌 DeenBot Stress Tester - 5-Minute Stability Test")
    print("=" * 60)
    
    # Check if DeenBot is running
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        if response.status_code != 200:
            print("❌ DeenBot is not running on port 8080")
            print("   Please start DeenBot first using: ./start_deenbot_local.sh")
            return
    except:
        print("❌ Cannot connect to DeenBot on port 8080")
        print("   Please start DeenBot first using: ./start_deenbot_local.sh")
        return
    
    print("✅ DeenBot is running and ready for stress testing")
    print("🔥 This will test DeenBot continuously for 5 minutes")
    print("📊 Testing all variations of user text and edge cases")
    print("")
    
    # Confirm before starting
    response = input("🚀 Start the 5-minute stress test? (y/N): ").strip().lower()
    if response not in ['y', 'yes']:
        print("❌ Stress test cancelled")
        return
    
    print("")
    print("🔥 Starting comprehensive stress test...")
    print("⏳ This will take exactly 5 minutes")
    print("📊 Monitor progress in the logs below")
    print("")
    
    # Create and run stress tester
    tester = DeenBotStressTester()
    
    try:
        tester.run_stress_test()
    except KeyboardInterrupt:
        print("\n🛑 Stress test interrupted by user")
        tester.running = False
    
    # Generate and display report
    print("")
    print("📊 Generating test report...")
    print("")
    
    report = tester.generate_report()
    print(report)
    
    # Save results
    results_file = tester.save_results()
    print(f"📁 Full results saved to: {results_file}")
    
    # Final recommendation
    if tester.test_results['crash_detected']:
        print("\n🚨 RECOMMENDATION: DeenBot FAILED the stress test!")
        print("   The service crashed or became unresponsive.")
        print("   Please fix the issues before deploying to production.")
        return 1
    else:
        print("\n🎉 RECOMMENDATION: DeenBot PASSED the stress test!")
        print("   The service remained stable for 5 continuous minutes.")
        print("   It's ready for production deployment.")
        return 0

if __name__ == '__main__':
    exit(main())
