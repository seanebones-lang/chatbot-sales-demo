#!/usr/bin/env python3
"""
Enhanced Actions for Mariam Bot with AI Integration
Provides fallback responses, hybrid mode, and context management
"""

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted
import requests
import json
import os
import logging
from datetime import datetime, timedelta

# Import AI integration
try:
    from ai_integration import get_ai_integration
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False
    logging.warning("⚠️ AI integration not available - using fallback mode only")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        events = [SessionStarted()]
        events.append(ActionExecuted("action_listen"))
        return events

class ActionAIFallback(Action):
    """AI fallback action when knowledge bot can't provide good answers"""
    
    def name(self) -> Text:
        return "action_ai_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not AI_AVAILABLE:
            dispatcher.utter_message(text="I'm sorry, but I'm having trouble understanding your request. Could you please rephrase your question?")
            return []
        
        user_message = tracker.latest_message.get('text', '')
        user_id = tracker.sender_id
        
        # Get AI integration instance
        ai_integration = get_ai_integration()
        
        # Build context
        context = self._build_context(tracker)
        
        # Get AI response
        ai_response = ai_integration.get_ai_response(user_message, context, 'fallback')
        
        # Update conversation context
        ai_integration.update_conversation_context(user_id, user_message, ai_response, 'ai_fallback')
        
        # Send response
        dispatcher.utter_message(text=ai_response)
        
        logger.info(f"🤖 AI Fallback used for user {user_id}: {user_message[:50]}...")
        return []

class ActionHybridResponse(Action):
    """Hybrid response combining knowledge bot and AI enhancement"""
    
    def name(self) -> Text:
        return "action_hybrid_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not AI_AVAILABLE:
            # Fall back to regular response
            dispatcher.utter_message(text="I understand your question. Let me provide you with the information I have.")
            return []
        
        user_message = tracker.latest_message.get('text', '')
        user_id = tracker.sender_id
        
        # Get AI integration instance
        ai_integration = get_ai_integration()
        
        # Build context
        context = self._build_context(tracker)
        
        # Get base knowledge response (you can customize this based on intent)
        base_response = self._get_base_knowledge_response(tracker)
        
        # Enhance with AI
        enhanced_response = ai_integration.enhance_knowledge_response(
            base_response, user_message, context
        )
        
        # Update conversation context
        ai_integration.update_conversation_context(user_id, user_message, enhanced_response, 'hybrid')
        
        # Send enhanced response
        dispatcher.utter_message(text=enhanced_response)
        
        logger.info(f"🔄 Hybrid response used for user {user_id}: {user_message[:50]}...")
        return []

class ActionConfidenceBasedResponse(Action):
    """Main action that decides response mode based on confidence"""
    
    def name(self) -> Text:
        return "action_confidence_based_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not AI_AVAILABLE:
            # Use regular knowledge bot response
            self._send_knowledge_response(dispatcher, tracker)
            return []
        
        # Get confidence scores
        intent_confidence = tracker.latest_message.get('intent', {}).get('confidence', 0.0)
        entity_confidence = self._calculate_entity_confidence(tracker)
        response_quality = self._assess_response_quality(tracker)
        
        # Get AI integration instance
        ai_integration = get_ai_integration()
        
        # Calculate overall confidence
        confidence_score = ai_integration.calculate_confidence_score(
            intent_confidence, entity_confidence, response_quality
        )
        
        # Determine response mode
        response_mode = ai_integration.determine_response_mode(
            confidence_score, tracker.latest_message.get('text', ''), 
            self._build_context(tracker)
        )
        
        # Execute appropriate response
        if response_mode == 'knowledge_bot':
            self._send_knowledge_response(dispatcher, tracker)
        elif response_mode == 'hybrid':
            self._execute_hybrid_response(dispatcher, tracker)
        else:  # ai_fallback
            self._execute_ai_fallback(dispatcher, tracker)
        
        return []

class ActionGetAIStats(Action):
    """Action to get AI integration statistics"""
    
    def name(self) -> Text:
        return "action_get_ai_stats"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not AI_AVAILABLE:
            dispatcher.utter_message(text="AI integration is not available.")
            return []
        
        ai_integration = get_ai_integration()
        stats = ai_integration.get_usage_statistics()
        health = ai_integration.health_check()
        
        stats_message = f"""📊 **AI Integration Statistics**

**Usage Breakdown:**
• Knowledge Bot Only: {stats['knowledge_bot_only']} ({stats.get('knowledge_bot_only_pct', 0):.1f}%)
• Hybrid Mode: {stats['hybrid_mode']} ({stats.get('hybrid_mode_pct', 0):.1f}%)
• AI Fallback: {stats['ai_fallback']} ({stats.get('ai_fallback_pct', 0):.1f}%)
• Total Requests: {stats['total_requests']}

**System Health:**
• AI Enabled: {'✅' if health['ai_enabled'] else '❌'}
• OpenAI Connection: {health['openai_connection']}
• Model: {health['model']}
• Active Contexts: {health['conversation_contexts']}"""
        
        dispatcher.utter_message(text=stats_message)
        return []

class ActionResetAIStats(Action):
    """Action to reset AI integration statistics"""
    
    def name(self) -> Text:
        return "action_reset_ai_stats"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if not AI_AVAILABLE:
            dispatcher.utter_message(text="AI integration is not available.")
            return []
        
        ai_integration = get_ai_integration()
        ai_integration.reset_usage_statistics()
        
        dispatcher.utter_message(text="📊 AI integration statistics have been reset.")
        return []

    def _build_context(self, tracker: Tracker) -> Dict:
        """Build conversation context for AI integration"""
        context = {
            'user_id': tracker.sender_id,
            'session_id': tracker.session_id,
            'conversation_history': [],
            'current_intent': tracker.latest_message.get('intent', {}).get('name', ''),
            'entities': [entity.get('entity') for entity in tracker.latest_message.get('entities', [])],
            'slots': {slot: value for slot, value in tracker.slots.items() if value is not None}
        }
        
        # Add conversation history
        for event in tracker.events:
            if event.get('event') == 'user':
                context['conversation_history'].append({
                    'user': event.get('text', ''),
                    'timestamp': event.get('timestamp', '')
                })
            elif event.get('event') == 'bot':
                context['conversation_history'].append({
                    'bot': event.get('text', ''),
                    'timestamp': event.get('timestamp', '')
                })
        
        return context

    def _calculate_entity_confidence(self, tracker: Tracker) -> float:
        """Calculate confidence in entity extraction"""
        entities = tracker.latest_message.get('entities', [])
        if not entities:
            return 0.0
        
        # Simple confidence calculation based on entity count and quality
        total_confidence = sum(entity.get('confidence', 0.5) for entity in entities)
        return min(total_confidence / len(entities), 1.0)

    def _assess_response_quality(self, tracker: Tracker) -> float:
        """Assess the quality of available responses"""
        # This is a simplified assessment - you can make this more sophisticated
        intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        # High-quality intents
        high_quality_intents = ['pricing_inquiry', 'business_analysis', 'technical_details']
        if intent in high_quality_intents:
            return 0.9
        
        # Medium-quality intents
        medium_quality_intents = ['greet', 'bot_capabilities', 'about_me']
        if intent in medium_quality_intents:
            return 0.7
        
        # Default quality
        return 0.5

    def _get_base_knowledge_response(self, tracker: Tracker) -> str:
        """Get base knowledge response based on intent"""
        intent = tracker.latest_message.get('intent', {}).get('name', '')
        
        base_responses = {
            'pricing_inquiry': "I can provide you with detailed pricing information for our AI chatbot solutions.",
            'business_analysis': "I'm here to help analyze your business needs and recommend the best AI solutions.",
            'technical_details': "Let me explain the technical aspects of our AI chatbot platform.",
            'default': "I have information that might be helpful for your question."
        }
        
        return base_responses.get(intent, base_responses['default'])

    def _send_knowledge_response(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        """Send regular knowledge bot response"""
        # This would typically call the appropriate action based on intent
        # For now, we'll send a generic message
        dispatcher.utter_message(text="I have information that should help answer your question.")

    def _execute_hybrid_response(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        """Execute hybrid response combining knowledge and AI"""
        action = ActionHybridResponse()
        action.run(dispatcher, tracker, {})

    def _execute_ai_fallback(self, dispatcher: CollectingDispatcher, tracker: Tracker):
        """Execute AI fallback response"""
        action = ActionAIFallback()
        action.run(dispatcher, tracker, {})

# Enhanced versions of existing actions
class ActionEnhancedPricingInquiry(Action):
    """Enhanced pricing inquiry with AI fallback capability"""
    
    def name(self) -> Text:
        return "action_enhanced_pricing_inquiry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # First, try to provide the standard pricing response
        try:
            response = """💰 **NextEleven AI Chatbot Pricing**

**Starter Plan - $79/month**
• 1 Custom AI Chatbot
• 1,000 queries/month
• Basic integrations
• Email support
• Perfect for small businesses

**Professional Plan - $247/month**
• 3 Custom AI Chatbots
• 5,000 queries/month
• Payment processing
• Advanced analytics
• Priority support
• Most popular choice

**Agency Plan - $497/month**
• 10 Custom AI Chatbots
• 15,000 queries/month
• White-label options
• Multi-account management
• Dedicated account manager

**Enterprise Plan - Custom Pricing**
• Unlimited chatbots
• Unlimited queries
• Full white-label solution
• Custom payment workflows
• Private cloud deployment

**Veteran Discount:** 25% off all plans for verified veterans

**What size business are you managing?** I can recommend the perfect plan for your needs."""
            
            dispatcher.utter_message(text=response)
            
            # If AI is available, offer enhancement
            if AI_AVAILABLE:
                ai_integration = get_ai_integration()
                user_message = tracker.latest_message.get('text', '')
                context = self._build_context(tracker)
                
                # Offer AI enhancement
                enhancement_offer = "\n\n🤖 **Would you like me to enhance this with AI insights?** I can provide industry-specific examples and personalized recommendations."
                dispatcher.utter_message(text=enhancement_offer)
                
        except Exception as e:
            logger.error(f"❌ Error in enhanced pricing inquiry: {str(e)}")
            # Fall back to AI if available
            if AI_AVAILABLE:
                action = ActionAIFallback()
                action.run(dispatcher, tracker, domain)
            else:
                dispatcher.utter_message(text="I'm having trouble accessing pricing information. Please try again or contact us directly.")
        
        return []

    def _build_context(self, tracker: Tracker) -> Dict:
        """Build context for AI integration"""
        return {
            'user_id': tracker.sender_id,
            'session_id': tracker.session_id,
            'current_intent': 'pricing_inquiry',
            'entities': [entity.get('entity') for entity in tracker.latest_message.get('entities', [])]
        }
