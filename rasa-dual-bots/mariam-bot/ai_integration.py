#!/usr/bin/env python3
"""
AI Integration Module for Mariam Bot
Provides fallback AI responses, confidence scoring, and hybrid enhancement
"""

import openai
import json
import logging
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIIntegration:
    def __init__(self):
        """Initialize AI integration with OpenAI"""
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        self.max_tokens = int(os.getenv('OPENAI_MAX_TOKENS', '500'))
        self.temperature = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
        
        if self.api_key:
            openai.api_key = self.api_key
            self.enabled = True
            logger.info("✅ OpenAI API configured successfully")
        else:
            self.enabled = False
            logger.warning("⚠️ OpenAI API key not found - AI features disabled")
        
        # Conversation context storage
        self.conversation_contexts = {}
        
        # Confidence thresholds
        self.confidence_thresholds = {
            'high': 0.8,      # Use knowledge bot only
            'medium': 0.6,    # Use hybrid mode
            'low': 0.4        # Use AI fallback
        }
        
        # Usage tracking
        self.usage_stats = {
            'knowledge_bot_only': 0,
            'hybrid_mode': 0,
            'ai_fallback': 0,
            'total_requests': 0
        }

    def calculate_confidence_score(self, intent_confidence: float, entity_confidence: float, 
                                 response_quality: float) -> float:
        """
        Calculate overall confidence score for response quality
        
        Args:
            intent_confidence: Rasa's intent confidence (0-1)
            entity_confidence: Entity extraction confidence (0-1)
            response_quality: Quality of the response match (0-1)
        
        Returns:
            float: Overall confidence score (0-1)
        """
        # Weighted average of different confidence factors
        weights = {
            'intent': 0.4,
            'entity': 0.3,
            'response': 0.3
        }
        
        confidence_score = (
            intent_confidence * weights['intent'] +
            entity_confidence * weights['entity'] +
            response_quality * weights['response']
        )
        
        logger.info(f"🎯 Confidence Score: {confidence_score:.3f} "
                   f"(Intent: {intent_confidence:.3f}, Entity: {entity_confidence:.3f}, "
                   f"Response: {response_quality:.3f})")
        
        return confidence_score

    def determine_response_mode(self, confidence_score: float, 
                             user_message: str, context: Dict) -> str:
        """
        Determine which response mode to use based on confidence
        
        Args:
            confidence_score: Calculated confidence score
            user_message: User's input message
            context: Conversation context
            
        Returns:
            str: Response mode ('knowledge_bot', 'hybrid', 'ai_fallback')
        """
        if confidence_score >= self.confidence_thresholds['high']:
            mode = 'knowledge_bot'
            self.usage_stats['knowledge_bot_only'] += 1
            logger.info(f"🎯 Using KNOWLEDGE BOT mode (Confidence: {confidence_score:.3f})")
            
        elif confidence_score >= self.confidence_thresholds['medium']:
            mode = 'hybrid'
            self.usage_stats['hybrid_mode'] += 1
            logger.info(f"🔄 Using HYBRID mode (Confidence: {confidence_score:.3f})")
            
        else:
            mode = 'ai_fallback'
            self.usage_stats['ai_fallback'] += 1
            logger.info(f"🤖 Using AI FALLBACK mode (Confidence: {confidence_score:.3f})")
        
        self.usage_stats['total_requests'] += 1
        return mode

    def get_ai_response(self, user_message: str, context: Dict, 
                       mode: str = 'fallback') -> str:
        """
        Get AI-generated response from OpenAI
        
        Args:
            user_message: User's input message
            context: Conversation context
            mode: Response mode ('fallback', 'enhance', 'hybrid')
            
        Returns:
            str: AI-generated response
        """
        if not self.enabled:
            return "I'm sorry, but I'm currently unable to access AI assistance. Please try rephrasing your question."
        
        try:
            # Build conversation context for OpenAI
            messages = self._build_openai_context(user_message, context, mode)
            
            # Generate response from OpenAI (using new API format)
            client = openai.OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            ai_response = response.choices[0].message.content.strip()
            
            # Log the AI interaction
            logger.info(f"🤖 AI Response Generated (Mode: {mode}): {ai_response[:100]}...")
            
            return ai_response
            
        except Exception as e:
            logger.error(f"❌ OpenAI API Error: {str(e)}")
            return "I'm experiencing technical difficulties with AI assistance. Please try again later."

    def enhance_knowledge_response(self, knowledge_response: str, user_message: str, 
                                 context: Dict) -> str:
        """
        Enhance knowledge bot response with AI insights
        
        Args:
            knowledge_response: Original knowledge bot response
            user_message: User's input message
            context: Conversation context
            
        Returns:
            str: Enhanced response
        """
        if not self.enabled:
            return knowledge_response
        
        try:
            enhancement_prompt = f"""
            You are Mariam, an AI business consultant at NextEleven Studios. 
            
            The user asked: "{user_message}"
            
            I provided this response: "{knowledge_response}"
            
            Please enhance this response by:
            1. Adding relevant examples or case studies
            2. Providing actionable next steps
            3. Including industry-specific insights
            4. Making it more engaging and professional
            
            Keep the enhanced response concise and focused on business value.
            """
            
            messages = [
                {"role": "system", "content": "You are Mariam, an expert AI business consultant helping businesses grow with AI solutions."},
                {"role": "user", "content": enhancement_prompt}
            ]
            
            client = openai.OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            enhanced_response = response.choices[0].message.content.strip()
            
            # Combine original and enhanced response
            final_response = f"{knowledge_response}\n\n🤖 **AI Enhancement:**\n{enhanced_response}"
            
            logger.info(f"🔄 Response Enhanced: {len(enhanced_response)} chars added")
            return final_response
            
        except Exception as e:
            logger.error(f"❌ Enhancement Error: {str(e)}")
            return knowledge_response

    def _build_openai_context(self, user_message: str, context: Dict, mode: str) -> List[Dict]:
        """
        Build conversation context for OpenAI API
        
        Args:
            user_message: Current user message
            context: Conversation context
            mode: Response mode
            
        Returns:
            List[Dict]: Messages for OpenAI API
        """
        # Base system message
        system_message = """You are Mariam, an AI business consultant at NextEleven Studios. 
        
        Your expertise includes:
        - AI chatbot solutions for businesses
        - Business process automation
        - Customer retention strategies
        - Industry-specific solutions (healthcare, retail, automotive, restaurant)
        - Veteran business support
        
        Always be professional, helpful, and focused on providing business value.
        Keep responses concise but informative."""
        
        messages = [{"role": "system", "content": system_message}]
        
        # Add conversation history if available
        if context.get('conversation_history'):
            for msg in context['conversation_history'][-5:]:  # Last 5 messages
                if msg.get('user'):
                    messages.append({"role": "user", "content": msg['user']})
                if msg.get('bot'):
                    messages.append({"role": "assistant", "content": msg['bot']})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        return messages

    def update_conversation_context(self, user_id: str, user_message: str, 
                                 bot_response: str, mode: str):
        """
        Update conversation context for future AI interactions
        
        Args:
            user_id: Unique identifier for the user
            user_message: User's message
            bot_response: Bot's response
            mode: Response mode used
        """
        if user_id not in self.conversation_contexts:
            self.conversation_contexts[user_id] = {
                'conversation_history': [],
                'last_interaction': None,
                'preferred_mode': 'knowledge_bot',
                'topics_discussed': set()
            }
        
        context = self.conversation_contexts[user_id]
        
        # Add to conversation history
        context['conversation_history'].append({
            'user': user_message,
            'bot': bot_response,
            'mode': mode,
            'timestamp': datetime.now().isoformat()
        })
        
        # Keep only last 10 messages
        if len(context['conversation_history']) > 10:
            context['conversation_history'] = context['conversation_history'][-10:]
        
        # Update last interaction
        context['last_interaction'] = datetime.now().isoformat()
        
        # Update preferred mode based on usage
        if mode == 'ai_fallback':
            context['preferred_mode'] = 'ai_fallback'
        elif mode == 'hybrid':
            context['preferred_mode'] = 'hybrid'
        
        logger.info(f"📝 Context updated for user {user_id} (Mode: {mode})")

    def get_usage_statistics(self) -> Dict:
        """
        Get current usage statistics
        
        Returns:
            Dict: Usage statistics
        """
        total = self.usage_stats['total_requests']
        if total == 0:
            return self.usage_stats
        
        percentages = {
            'knowledge_bot_only_pct': (self.usage_stats['knowledge_bot_only'] / total) * 100,
            'hybrid_mode_pct': (self.usage_stats['hybrid_mode'] / total) * 100,
            'ai_fallback_pct': (self.usage_stats['ai_fallback'] / total) * 100
        }
        
        return {**self.usage_stats, **percentages}

    def reset_usage_statistics(self):
        """Reset usage statistics"""
        self.usage_stats = {
            'knowledge_bot_only': 0,
            'hybrid_mode': 0,
            'ai_fallback': 0,
            'total_requests': 0
        }
        logger.info("📊 Usage statistics reset")

    def health_check(self) -> Dict:
        """
        Check AI integration health
        
        Returns:
            Dict: Health status
        """
        health_status = {
            'ai_enabled': self.enabled,
            'openai_configured': bool(self.api_key),
            'model': self.model,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
            'conversation_contexts': len(self.conversation_contexts),
            'usage_stats': self.usage_stats
        }
        
        if self.enabled:
            try:
                # Test OpenAI connection
                client = openai.OpenAI(api_key=self.api_key)
                test_response = client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": "Hello"}],
                    max_tokens=10
                )
                health_status['openai_connection'] = '✅ Working'
            except Exception as e:
                health_status['openai_connection'] = f'❌ Error: {str(e)}'
        else:
            health_status['openai_connection'] = '⚠️ Disabled'
        
        return health_status

# Global AI integration instance
ai_integration = AIIntegration()

def get_ai_integration() -> AIIntegration:
    """Get the global AI integration instance"""
    return ai_integration
