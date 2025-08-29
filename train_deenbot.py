#!/usr/bin/env python3
"""
DeenBot Training Script - Improve AI responses through supervised learning
This script helps train the DeenBot by collecting feedback and improving responses
"""

import json
import sqlite3
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DeenBotTrainer:
    """Trainer class for improving DeenBot responses"""
    
    def __init__(self, db_path: str = "deenbot_learning.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_training_tables()
    
    def _create_training_tables(self):
        """Create tables for training data"""
        # Training examples table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS training_examples (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                input_message TEXT NOT NULL,
                expected_response TEXT NOT NULL,
                response_type TEXT NOT NULL,
                category TEXT NOT NULL,
                difficulty_level INTEGER DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                usage_count INTEGER DEFAULT 0,
                success_rate REAL DEFAULT 0.0
            )
        ''')
        
        # Feedback table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                conversation_id INTEGER,
                user_rating INTEGER CHECK (user_rating >= 1 AND user_rating <= 5),
                feedback_text TEXT,
                improvement_suggestions TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id)
            )
        ''')
        
        # Response improvements table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS response_improvements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_response TEXT,
                improved_response TEXT,
                improvement_reason TEXT,
                applied_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                effectiveness_improvement REAL
            )
        ''')
        
        self.conn.commit()
        logging.info("✅ Training tables created")
    
    def add_training_example(self, input_message: str, expected_response: str, 
                           response_type: str, category: str, difficulty_level: int = 1):
        """Add a new training example"""
        try:
            self.cursor.execute('''
                INSERT INTO training_examples 
                (input_message, expected_response, response_type, category, difficulty_level)
                VALUES (?, ?, ?, ?, ?)
            ''', (input_message, expected_response, response_type, category, difficulty_level))
            
            self.conn.commit()
            logging.info(f"✅ Added training example for category: {category}")
            return True
        except Exception as e:
            logging.error(f"❌ Failed to add training example: {e}")
            return False
    
    def add_user_feedback(self, conversation_id: int, rating: int, 
                         feedback_text: str = "", improvement_suggestions: str = ""):
        """Add user feedback for a conversation"""
        try:
            self.cursor.execute('''
                INSERT INTO user_feedback 
                (conversation_id, user_rating, feedback_text, improvement_suggestions)
                VALUES (?, ?, ?, ?)
            ''', (conversation_id, rating, feedback_text, improvement_suggestions))
            
            self.conn.commit()
            logging.info(f"✅ Added user feedback with rating: {rating}/5")
            return True
        except Exception as e:
            logging.error(f"❌ Failed to add user feedback: {e}")
            return False
    
    def improve_response(self, original_response: str, improved_response: str, 
                        improvement_reason: str, effectiveness_improvement: float = 0.0):
        """Record a response improvement"""
        try:
            self.cursor.execute('''
                INSERT INTO response_improvements 
                (original_response, improved_response, improvement_reason, effectiveness_improvement)
                VALUES (?, ?, ?, ?)
            ''', (original_response, improved_response, improvement_reason, effectiveness_improvement))
            
            self.conn.commit()
            logging.info(f"✅ Recorded response improvement with {effectiveness_improvement:.2f} improvement")
            return True
        except Exception as e:
            logging.error(f"❌ Failed to record response improvement: {e}")
            return False
    
    def get_training_data(self, category: str = None, limit: int = 100) -> List[Dict]:
        """Get training data for a specific category"""
        try:
            if category:
                self.cursor.execute('''
                    SELECT * FROM training_examples 
                    WHERE category = ? 
                    ORDER BY success_rate DESC, usage_count DESC 
                    LIMIT ?
                ''', (category, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM training_examples 
                    ORDER BY success_rate DESC, usage_count DESC 
                    LIMIT ?
                ''', (limit,))
            
            columns = [description[0] for description in self.cursor.description]
            results = []
            
            for row in self.cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            return results
        except Exception as e:
            logging.error(f"❌ Failed to get training data: {e}")
            return []
    
    def get_feedback_analysis(self) -> Dict:
        """Analyze user feedback to identify improvement areas"""
        try:
            # Overall rating statistics
            self.cursor.execute('''
                SELECT 
                    AVG(user_rating) as avg_rating,
                    COUNT(*) as total_feedback,
                    COUNT(CASE WHEN user_rating >= 4 THEN 1 END) as positive_feedback,
                    COUNT(CASE WHEN user_rating <= 2 THEN 1 END) as negative_feedback
                FROM user_feedback
            ''')
            
            rating_stats = self.cursor.fetchone()
            
            # Common improvement suggestions
            self.cursor.execute('''
                SELECT improvement_suggestions, COUNT(*) as count
                FROM user_feedback 
                WHERE improvement_suggestions IS NOT NULL AND improvement_suggestions != ''
                GROUP BY improvement_suggestions
                ORDER BY count DESC
                LIMIT 10
            ''')
            
            improvement_suggestions = self.cursor.fetchall()
            
            return {
                "average_rating": round(rating_stats[0] or 0, 2),
                "total_feedback": rating_stats[1],
                "positive_feedback_percentage": round((rating_stats[2] / rating_stats[1] * 100) if rating_stats[1] > 0 else 0, 1),
                "negative_feedback_percentage": round((rating_stats[3] / rating_stats[1] * 100) if rating_stats[1] > 0 else 0, 1),
                "top_improvement_suggestions": improvement_suggestions
            }
        except Exception as e:
            logging.error(f"❌ Failed to analyze feedback: {e}")
            return {"error": str(e)}
    
    def generate_training_examples(self):
        """Generate comprehensive training examples for common scenarios"""
        training_data = [
            # Emotional Support Examples
            {
                "input": "I'm feeling really down today",
                "response": "I understand you're going through a difficult time. Remember that Allah is with you and this feeling will pass. Let me share some Islamic guidance to help lift your spirits...",
                "type": "emotional_support",
                "category": "grief_and_sadness",
                "difficulty": 1
            },
            {
                "input": "I had an amazing day alhamdulillah!",
                "response": "Alhamdulillah! It's wonderful to hear about your great day. Your gratitude reflects the beautiful teachings of Islam. Let me share some ways to build on this positive energy...",
                "type": "positive_reinforcement",
                "category": "motivation_and_encouragement",
                "difficulty": 1
            },
            {
                "input": "I'm worried about my future",
                "response": "It's natural to feel concerned about the future. In Islam, we're taught to trust in Allah's plan while doing our best. Let me share some Islamic wisdom about dealing with uncertainty...",
                "type": "guidance",
                "category": "anxiety_and_worry",
                "difficulty": 2
            },
            
            # Question-Based Examples
            {
                "input": "How do I become a better Muslim?",
                "response": "Becoming a better Muslim is a beautiful journey of continuous improvement. Here are some practical steps based on Islamic teachings: 1) Strengthen your prayer routine, 2) Read Quran daily, 3) Practice gratitude...",
                "type": "educational",
                "category": "self_improvement",
                "difficulty": 2
            },
            {
                "input": "What does Islam say about helping others?",
                "response": "Islam places great emphasis on helping others. The Prophet (PBUH) said: 'The best of people are those who are most beneficial to people.' Here are some ways to help others according to Islamic teachings...",
                "type": "educational",
                "category": "charity_and_service",
                "difficulty": 2
            },
            
            # Context-Aware Examples
            {
                "input": "I lost my job and I'm scared",
                "response": "I'm sorry to hear about your job loss. This is undoubtedly a challenging time, but remember that Allah tests us to make us stronger. Let me share some Islamic guidance for dealing with financial difficulties...",
                "type": "emotional_support",
                "category": "financial_struggles",
                "difficulty": 3
            },
            {
                "input": "My family is going through a hard time",
                "response": "Family difficulties can be especially challenging. In Islam, family bonds are sacred and we're taught to support each other through difficult times. Let me share some Islamic wisdom about family relationships...",
                "type": "guidance",
                "category": "family_issues",
                "difficulty": 3
            }
        ]
        
        for example in training_data:
            self.add_training_example(
                example["input"],
                example["response"],
                example["type"],
                example["category"],
                example["difficulty"]
            )
        
        logging.info(f"✅ Generated {len(training_data)} training examples")
    
    def analyze_response_quality(self) -> Dict:
        """Analyze the quality of responses based on training data"""
        try:
            # Get response effectiveness from conversations
            self.cursor.execute('''
                SELECT 
                    COUNT(*) as total_responses,
                    AVG(effectiveness_score) as avg_effectiveness,
                    COUNT(CASE WHEN effectiveness_score >= 0.8 THEN 1 END) as high_quality,
                    COUNT(CASE WHEN effectiveness_score <= 0.5 THEN 1 END) as low_quality
                FROM conversations 
                WHERE effectiveness_score IS NOT NULL
            ''')
            
            quality_stats = self.cursor.fetchone()
            
            # Get pattern usage statistics
            self.cursor.execute('''
                SELECT 
                    response_type,
                    AVG(effectiveness) as avg_effectiveness,
                    COUNT(*) as usage_count
                FROM learned_patterns 
                GROUP BY response_type
                ORDER BY avg_effectiveness DESC
            ''')
            
            pattern_stats = self.cursor.fetchall()
            
            return {
                "total_responses": quality_stats[0],
                "average_effectiveness": round(quality_stats[1] or 0, 2),
                "high_quality_percentage": round((quality_stats[2] / quality_stats[0] * 100) if quality_stats[0] > 0 else 0, 1),
                "low_quality_percentage": round((quality_stats[3] / quality_stats[0] * 100) if quality_stats[0] > 0 else 0, 1),
                "pattern_effectiveness": [
                    {
                        "type": row[0],
                        "avg_effectiveness": round(row[1], 2),
                        "usage_count": row[2]
                    }
                    for row in pattern_stats
                ]
            }
        except Exception as e:
            logging.error(f"❌ Failed to analyze response quality: {e}")
            return {"error": str(e)}
    
    def export_training_data(self, filename: str = "deenbot_training_data.json"):
        """Export training data for external analysis"""
        try:
            training_data = self.get_training_data(limit=1000)
            feedback_analysis = self.get_feedback_analysis()
            quality_analysis = self.analyze_response_quality()
            
            export_data = {
                "export_timestamp": datetime.now().isoformat(),
                "training_examples": training_data,
                "feedback_analysis": feedback_analysis,
                "quality_analysis": quality_analysis
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            logging.info(f"✅ Training data exported to {filename}")
            return True
        except Exception as e:
            logging.error(f"❌ Failed to export training data: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        self.conn.close()

def main():
    """Main training function"""
    print("🚀 DeenBot Training System")
    print("=" * 50)
    
    trainer = DeenBotTrainer()
    
    try:
        # Generate training examples
        print("📚 Generating training examples...")
        trainer.generate_training_examples()
        
        # Analyze current performance
        print("📊 Analyzing current performance...")
        feedback_analysis = trainer.get_feedback_analysis()
        quality_analysis = trainer.analyze_response_quality()
        
        print(f"\n📈 Performance Summary:")
        print(f"• Average User Rating: {feedback_analysis.get('average_rating', 'N/A')}/5")
        print(f"• Total Responses: {quality_analysis.get('total_responses', 'N/A')}")
        print(f"• Average Effectiveness: {quality_analysis.get('average_effectiveness', 'N/A')}")
        
        # Export data for analysis
        print("\n💾 Exporting training data...")
        trainer.export_training_data()
        
        print("\n✅ Training session completed successfully!")
        print("\n💡 Next Steps:")
        print("1. Review the exported training data")
        print("2. Add more specific training examples")
        print("3. Collect user feedback to improve responses")
        print("4. Use the feedback analysis to identify weak areas")
        
    except Exception as e:
        logging.error(f"❌ Training session failed: {e}")
        print(f"\n❌ Training failed: {e}")
    
    finally:
        trainer.close()

if __name__ == '__main__':
    main()
