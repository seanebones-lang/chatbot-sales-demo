#!/usr/bin/env python3
"""
DeenBot Test Suite: 48 Random Questions from Young Muslim Men
Tests DeenBot's ability to handle questions relevant to young Muslim men's experiences
"""

import requests
import json
import time
import random
from datetime import datetime

class DeenBotYoungMenTest:
    def __init__(self):
        self.base_url = "http://localhost:8080"
        self.test_questions = [
            # Identity and Faith (8 questions)
            "How can I strengthen my iman as a young Muslim man?",
            "What should I do when I feel disconnected from my faith?",
            "How do I balance being Muslim with modern life?",
            "What are the most important duas for young men?",
            "How can I be a good role model for other young Muslims?",
            "What should I do when friends question my Islamic practices?",
            "How do I explain my faith to non-Muslim classmates?",
            "What are the signs of weak iman and how to fix them?",
            
            # Education and Career (8 questions)
            "How should I choose my career path as a Muslim?",
            "What does Islam say about pursuing higher education?",
            "How do I maintain Islamic values in a competitive work environment?",
            "What should I do if my job conflicts with prayer times?",
            "How can I be successful while staying true to Islamic principles?",
            "What does Islam say about entrepreneurship and business?",
            "How do I handle workplace discrimination as a Muslim?",
            "What are the Islamic guidelines for financial planning?",
            
            # Relationships and Marriage (8 questions)
            "What should I look for in a potential spouse?",
            "How do I approach marriage as a young Muslim man?",
            "What are my responsibilities towards my future wife?",
            "How do I handle family pressure about marriage?",
            "What does Islam say about dating before marriage?",
            "How should I interact with women in professional settings?",
            "What are the rights and duties in an Islamic marriage?",
            "How do I prepare financially for marriage?",
            
            # Social Life and Friendships (8 questions)
            "How do I make Muslim friends in a new city?",
            "What should I do when friends want to do haram activities?",
            "How do I handle peer pressure to drink or party?",
            "What are good social activities for young Muslim men?",
            "How do I maintain friendships with non-Muslims?",
            "What should I do if I'm the only Muslim in my group?",
            "How do I handle social media as a Muslim?",
            "What are Islamic guidelines for social gatherings?",
            
            # Physical and Mental Health (8 questions)
            "How should I take care of my physical health as a Muslim?",
            "What does Islam say about mental health and seeking help?",
            "How do I deal with stress and anxiety?",
            "What are the Islamic guidelines for exercise and sports?",
            "How should I handle anger and frustration?",
            "What does Islam say about depression and sadness?",
            "How do I maintain a healthy lifestyle while being busy?",
            "What are the benefits of fasting beyond Ramadan?",
            
            # Technology and Modern Life (8 questions)
            "How do I use technology responsibly as a Muslim?",
            "What are the Islamic guidelines for social media use?",
            "How do I avoid wasting time on the internet?",
            "What does Islam say about online relationships?",
            "How do I protect my privacy online as a Muslim?",
            "What are good apps for Islamic learning?",
            "How do I balance gaming with Islamic responsibilities?",
            "What does Islam say about artificial intelligence and automation?"
        ]
        self.results = []
        self.start_time = None
        self.end_time = None
        
    def test_query(self, question):
        """Test a single query and return the result"""
        try:
            response = requests.post(
                f"{self.base_url}/chat",
                json={"message": question},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "question": question,
                    "response": data.get("response", "No response"),
                    "status": "success",
                    "status_code": response.status_code,
                    "response_time": response.elapsed.total_seconds()
                }
            else:
                return {
                    "question": question,
                    "response": f"HTTP {response.status_code}",
                    "status": "error",
                    "status_code": response.status_code,
                    "response_time": response.elapsed.total_seconds()
                }
                
        except requests.exceptions.Timeout:
            return {
                "question": question,
                "response": "Request timeout",
                "status": "timeout",
                "status_code": None,
                "response_time": 30
            }
        except requests.exceptions.ConnectionError:
            return {
                "question": question,
                "response": "Connection error",
                "status": "connection_error",
                "status_code": None,
                "response_time": 0
            }
        except Exception as e:
            return {
                "question": question,
                "response": f"Error: {str(e)}",
                "status": "exception",
                "status_code": None,
                "response_time": 0
            }
    
    def run_test(self):
        """Run the complete test suite"""
        print("🚀 Starting DeenBot Test: 48 Questions from Young Muslim Men")
        print("=" * 70)
        
        self.start_time = time.time()
        
        # Shuffle questions for randomness
        random.shuffle(self.test_questions)
        
        for i, question in enumerate(self.test_questions, 1):
            print(f"\n📝 Question {i}/48: {question}")
            result = self.test_query(question)
            self.results.append(result)
            
            if result["status"] == "success":
                print(f"✅ Success - Response time: {result['response_time']:.2f}s")
                # Show first 100 characters of response
                response_preview = result["response"][:100] + "..." if len(result["response"]) > 100 else result["response"]
                print(f"📄 Response: {response_preview}")
            else:
                print(f"❌ {result['status'].upper()}: {result['response']}")
            
            # Small delay between requests
            time.sleep(0.5)
        
        self.end_time = time.time()
        self.generate_report()
    
    def generate_report(self):
        """Generate comprehensive test report"""
        print("\n" + "=" * 70)
        print("📊 TEST REPORT: 48 Questions from Young Muslim Men")
        print("=" * 70)
        
        total_questions = len(self.results)
        successful_responses = len([r for r in self.results if r["status"] == "success"])
        failed_responses = total_questions - successful_responses
        
        # Calculate response times
        response_times = [r["response_time"] for r in self.results if r["status"] == "success"]
        avg_response_time = sum(response_times) / len(response_times) if response_times else 0
        max_response_time = max(response_times) if response_times else 0
        min_response_time = min(response_times) if response_times else 0
        
        # Calculate success rate
        success_rate = (successful_responses / total_questions) * 100
        
        print(f"📈 Overall Results:")
        print(f"   Total Questions: {total_questions}")
        print(f"   Successful Responses: {successful_responses}")
        print(f"   Failed Responses: {failed_responses}")
        print(f"   Success Rate: {success_rate:.1f}%")
        
        print(f"\n⏱️ Performance Metrics:")
        print(f"   Average Response Time: {avg_response_time:.2f} seconds")
        print(f"   Fastest Response: {min_response_time:.2f} seconds")
        print(f"   Slowest Response: {max_response_time:.2f} seconds")
        print(f"   Total Test Duration: {self.end_time - self.start_time:.2f} seconds")
        
        # Status breakdown
        status_counts = {}
        for result in self.results:
            status = result["status"]
            status_counts[status] = status_counts.get(status, 0) + 1
        
        print(f"\n📊 Status Breakdown:")
        for status, count in status_counts.items():
            print(f"   {status.upper()}: {count}")
        
        # Error analysis
        if failed_responses > 0:
            print(f"\n❌ Error Analysis:")
            error_results = [r for r in self.results if r["status"] != "success"]
            for error in error_results[:5]:  # Show first 5 errors
                print(f"   Question: {error['question'][:50]}...")
                print(f"   Error: {error['response']}")
                print()
        
        # Success assessment
        if success_rate >= 95:
            assessment = "EXCELLENT"
            emoji = "🌟"
        elif success_rate >= 90:
            assessment = "VERY GOOD"
            emoji = "👍"
        elif success_rate >= 80:
            assessment = "GOOD"
            emoji = "✅"
        elif success_rate >= 70:
            assessment = "FAIR"
            emoji = "⚠️"
        else:
            assessment = "NEEDS IMPROVEMENT"
            emoji = "🔧"
        
        print(f"\n{emoji} FINAL ASSESSMENT: {assessment}")
        print(f"   DeenBot successfully handled {successful_responses} out of {total_questions} questions")
        print(f"   from young Muslim men's perspective with a {success_rate:.1f}% success rate.")
        
        # Save results to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"deenbot_48_young_muslim_men_test_{timestamp}.json"
        
        report_data = {
            "test_type": "48 Questions from Young Muslim Men",
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_questions": total_questions,
                "successful_responses": successful_responses,
                "failed_responses": failed_responses,
                "success_rate": success_rate,
                "avg_response_time": avg_response_time,
                "total_duration": self.end_time - self.start_time
            },
            "results": self.results
        }
        
        with open(filename, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\n💾 Detailed results saved to: {filename}")
        print("=" * 70)

def main():
    """Main function to run the test"""
    test = DeenBotYoungMenTest()
    test.run_test()

if __name__ == '__main__':
    main()
