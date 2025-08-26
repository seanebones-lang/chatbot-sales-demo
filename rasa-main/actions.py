import os
import logging
import openai
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActionOpenAIKnowledge(Action):
    def name(self) -> Text:
        return "action_openai_knowledge"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            # Get user message
            user_message = tracker.latest_message.get('text', '')
            
            # Get business context from slots
            business_type = tracker.get_slot('business_type') or 'general business'
            package_type = tracker.get_slot('package_type') or 'professional'
            industry = tracker.get_slot('industry') or 'general'
            
            # Create context-aware system prompt
            system_prompt = f"""You are Mariam, a senior AI consultant for NextEleven, a leading provider of enterprise-grade AI chatbot solutions.

Business Context: 
- Business Type: {business_type}
- Package Interest: {package_type}
- Industry: {industry}

You provide expert consultation on:
- AI chatbot solutions for business automation
- Customer service optimization
- Sales and lead generation
- ROI analysis and business case development
- Technical implementation and integration
- Industry-specific solutions and case studies

Always be:
- Professional, knowledgeable, and friendly
- Specific to their business context
- Focused on measurable business outcomes
- Clear about next steps and implementation
- Confident in NextEleven's capabilities

If you don't know something specific, suggest they schedule a consultation call or demo."""

            # Check if OpenAI API key is configured
            if not openai.api_key:
                logger.error("OpenAI API key not configured")
                dispatcher.utter_message(text="I'm sorry, but I'm currently experiencing technical difficulties. Please try again later or contact our team directly.")
                return []

            try:
                # Call OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_message}
                    ],
                    max_tokens=400,
                    temperature=0.7,
                    timeout=30
                )
                
                # Extract the response
                ai_reply = response.choices[0].message.content.strip()
                
                logger.info(f"OpenAI response generated successfully for: {user_message[:100]}...")
                
                # Send the response
                dispatcher.utter_message(text=ai_reply)
                
                # Add context-specific follow-up suggestions
                self._add_follow_up_suggestions(dispatcher, user_message, business_type)
                
            except openai.error.RateLimitError:
                logger.warning("OpenAI rate limit exceeded")
                dispatcher.utter_message(text="I'm receiving too many requests right now. Please wait a moment and try again, or contact our team directly.")
                
            except openai.error.InvalidRequestError as e:
                logger.error(f"OpenAI invalid request: {e}")
                dispatcher.utter_message(text="I'm sorry, but I couldn't process your request. Please try rephrasing your question or contact our team directly.")
                
            except openai.error.APIError as e:
                logger.error(f"OpenAI API error: {e}")
                dispatcher.utter_message(text="I'm experiencing technical difficulties with my AI service. Please try again in a few minutes or contact our team directly.")
                
            except Exception as e:
                logger.error(f"Unexpected OpenAI error: {e}")
                dispatcher.utter_message(text="I'm sorry, but something unexpected happened. Please try again later or contact our team directly.")
                
        except Exception as e:
            logger.error(f"Unexpected error in action_openai_knowledge: {e}")
            dispatcher.utter_message(text="I'm experiencing technical difficulties. Please try again later or contact our team directly.")
        
        return []

    def _add_follow_up_suggestions(self, dispatcher, user_message, business_type):
        """Add context-specific follow-up suggestions"""
        message_lower = user_message.lower()
        
        if any(word in message_lower for word in ['pricing', 'cost', 'price', 'investment']):
            dispatcher.utter_message(text="Would you like me to send you detailed pricing information with ROI calculations for your business type? Just provide your email address!")
        elif any(word in message_lower for word in ['demo', 'show', 'demonstrate', 'presentation']):
            dispatcher.utter_message(text="I'd be happy to schedule a personalized demo for your business. What time works best - morning, afternoon, or evening?")
        elif any(word in message_lower for word in ['trial', 'try', 'test', 'sample']):
            dispatcher.utter_message(text="Great! To get your free trial started, I'll need to know what type of business you have so I can customize the solution for you.")
        elif any(word in message_lower for word in ['technical', 'integration', 'implementation']):
            dispatcher.utter_message(text="I can provide detailed technical specifications and integration guides. Would you like me to send you our technical documentation?")
        elif any(word in message_lower for word in ['roi', 'return', 'investment', 'benefits']):
            dispatcher.utter_message(text="I can calculate the specific ROI for your business. What industry are you in and what are your current customer service costs?")

class ActionBusinessAnalysis(Action):
    def name(self) -> Text:
        return "action_business_analysis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        business_type = tracker.get_slot('business_type') or 'general business'
        
        # Provide industry-specific analysis
        analysis = self._get_business_analysis(business_type)
        dispatcher.utter_message(text=analysis)
        
        # Ask for more specific information
        dispatcher.utter_message(text="To give you the most accurate analysis, could you tell me more about your current customer service challenges and goals?")
        
        return []

    def _get_business_analysis(self, business_type):
        """Get industry-specific business analysis"""
        business_type_lower = business_type.lower()
        
        if any(word in business_type_lower for word in ['healthcare', 'medical', 'dental']):
            return """Healthcare businesses face unique challenges that NextEleven solves perfectly:
• HIPAA-compliant patient communication
• Appointment scheduling and reminders
• Insurance and billing questions
• Medical FAQ and resources
• 24/7 patient support

Typical results: 50-70% improvement in patient communication within 2 months."""
        
        elif any(word in business_type_lower for word in ['retail', 'ecommerce', 'shop']):
            return """Retail businesses benefit tremendously from NextEleven:
• 24/7 product information and support
• Order tracking and status updates
• Return and exchange assistance
• Inventory and availability checking
• Personalized recommendations

Typical results: 35-55% increase in sales conversion within 3 months."""
        
        elif any(word in business_type_lower for word in ['automotive', 'auto', 'car']):
            return """Automotive businesses see excellent results with NextEleven:
• Service appointment scheduling
• Parts catalog and pricing
• Service history tracking
• Maintenance reminders
• Technical support and FAQ

Typical results: 40-60% increase in service bookings within 2 months."""
        
        else:
            return f"""For {business_type}, NextEleven provides:
• 24/7 customer service automation
• Lead capture and qualification
• FAQ and knowledge base management
• Multi-platform integration
• Performance analytics and optimization

Typical results: 30-50% improvement in customer service efficiency within 3 months."""

class ActionPackageRecommendation(Action):
    def name(self) -> Text:
        return "action_package_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        business_type = tracker.get_slot('business_type') or 'general business'
        company_size = tracker.get_slot('company_size') or 'medium'
        
        # Recommend package based on business context
        recommendation = self._get_package_recommendation(business_type, company_size)
        dispatcher.utter_message(text=recommendation)
        
        return []

    def _get_package_recommendation(self, business_type, company_size):
        """Get package recommendation based on business context"""
        business_type_lower = business_type.lower()
        company_size_lower = company_size.lower()
        
        if any(word in company_size_lower for word in ['startup', 'small', 'new']):
            return """Based on your business size, I recommend our **Starter Plan** ($79/month):
• Perfect for small businesses and startups
• 1 Custom AI Chatbot with 1,000 queries/month
• Quick setup and essential features
• Great for testing and getting started

This gives you everything you need to begin automating customer service while keeping costs low."""
        
        elif any(word in company_size_lower for word in ['enterprise', 'large', 'corporate']):
            return """For your business scale, I recommend our **Enterprise Plan** (custom pricing):
• Unlimited chatbots and queries
• Full white-label solution
• Custom payment workflows
• Private cloud deployment
• 24/7 dedicated engineer support

This provides the scalability and customization enterprise businesses require."""
        
        else:
            return """I recommend our **Professional Plan** ($247/month) - our most popular choice:
• 3 Custom AI Chatbots with 5,000 queries/month
• Payment processing integration
• Advanced analytics and lead capture
• Priority support and training
• Perfect balance of features and value

This plan handles most business needs while providing room for growth."""

class ActionROICalculation(Action):
    def name(self) -> Text:
        return "action_roi_calculation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        business_type = tracker.get_slot('business_type') or 'general business'
        
        # Calculate ROI based on business type
        roi_analysis = self._calculate_roi(business_type)
        dispatcher.utter_message(text=roi_analysis)
        
        return []

    def _calculate_roi(self, business_type):
        """Calculate ROI based on business type"""
        business_type_lower = business_type.lower()
        
        if any(word in business_type_lower for word in ['healthcare', 'medical']):
            return """**ROI Analysis for Healthcare Businesses:**

Current Costs (monthly):
• Staff time on phone calls: $2,000-4,000
• After-hours missed opportunities: $1,500-3,000
• Patient communication inefficiencies: $1,000-2,000

With NextEleven (Professional Plan - $247/month):
• 60% reduction in phone calls: Save $1,200-2,400/month
• 24/7 patient support: Capture $1,500-3,000/month
• Improved efficiency: Save $600-1,200/month

**Monthly Savings: $3,300-6,600**
**ROI: 1,336-2,672%**
**Break-even: 2-4 weeks**"""
        
        elif any(word in business_type_lower for word in ['retail', 'ecommerce']):
            return """**ROI Analysis for Retail Businesses:**

Current Costs (monthly):
• Customer service staff: $3,000-6,000
• Lost sales from wait times: $2,000-5,000
• After-hours missed sales: $1,500-3,000

With NextEleven (Professional Plan - $247/month):
• 40% increase in sales conversion: Generate $2,000-5,000/month
• 24/7 customer support: Capture $1,500-3,000/month
• Reduced staff costs: Save $1,500-3,000/month

**Monthly Benefits: $5,000-11,000**
**ROI: 2,025-4,453%**
**Break-even: 1-2 weeks**"""
        
        else:
            return """**ROI Analysis for General Businesses:**

Current Costs (monthly):
• Customer service staff: $2,500-5,000
• Phone system and tools: $200-500
• Lost opportunities: $1,000-3,000

With NextEleven (Professional Plan - $247/month):
• 50% reduction in support costs: Save $1,250-2,500/month
• 24/7 lead capture: Generate $1,000-3,000/month
• Improved efficiency: Save $500-1,000/month

**Monthly Benefits: $2,750-6,500**
**ROI: 1,114-2,633%**
**Break-even: 2-3 weeks**"""

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="I'm not sure I understand. Could you rephrase that or ask me something about NextEleven's AI chatbot solutions, pricing, demos, or how to get started?")
        return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Let's start fresh! How can I help you today?")
        return [SlotSet("business_type", None), SlotSet("package_type", None)]
