#!/usr/bin/env python3

# Test script to debug Quran search
from comprehensive_islamic_knowledge import ComprehensiveIslamicKnowledge

def test_quran_search():
    print("🔍 Testing Quran search methods...")
    
    # Initialize the knowledge base
    kb = ComprehensiveIslamicKnowledge()
    
    print(f"📚 Quran database entries: {len(kb.quran_database)}")
    
    # Test search_quran_comprehensive
    print("\n🔍 Testing search_quran_comprehensive('Al-Fatiha')...")
    results = kb.search_quran_comprehensive("Al-Fatiha")
    print(f"Results: {len(results)}")
    for i, result in enumerate(results):
        print(f"  {i+1}. {result}")
    
    # Test search_quran_comprehensive with "Quran"
    print("\n🔍 Testing search_quran_comprehensive('Quran')...")
    results = kb.search_quran_comprehensive("Quran")
    print(f"Results: {len(results)}")
    for i, result in enumerate(results):
        print(f"  {i+1}. {result}")
    
    # Test the main search method
    print("\n🔍 Testing search_comprehensive_knowledge('Al-Fatiha')...")
    results = kb.search_comprehensive_knowledge("Al-Fatiha")
    print(f"Results: {len(results)}")
    for i, result in enumerate(results):
        print(f"  {i+1}. Type: {result.get('type')}, Title: {result.get('title')}")
    
    # Test with "Quran"
    print("\n🔍 Testing search_comprehensive_knowledge('Quran')...")
    results = kb.search_comprehensive_knowledge("Quran")
    print(f"Results: {len(results)}")
    for i, result in enumerate(results):
        print(f"  {i+1}. Type: {result.get('type')}, Title: {result.get('title')}")

if __name__ == "__main__":
    test_quran_search()
