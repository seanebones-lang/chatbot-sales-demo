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
            
            # Get business type from slots
            business_type = tracker.get_slot('business_type') or 'general business'
            
            # Create context-aware system prompt
            system_prompt = f"""You are a helpful AI assistant for NextEleven, a company that provides enterprise-grade AI chatbot solutions.

Business Context: The user is asking about {business_type} and our services.

You provide clear, accurate, and helpful responses about:
- NextEleven's chatbot solutions
- Business benefits and ROI
- Technical capabilities
- Pricing and packages
- Implementation process
- Industry-specific solutions

Always be:
- Professional and friendly
- Specific to their business type
- Focused on how NextEleven can help
- Clear about next steps

If you don't know something specific, suggest they contact our team or schedule a consultation."""

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
                    max_tokens=300,
                    temperature=0.7,
                    timeout=30
                )
                
                # Extract the response
                ai_reply = response.choices[0].message.content.strip()
                
                logger.info(f"OpenAI response generated successfully for: {user_message[:100]}...")
                
                # Send the response
                dispatcher.utter_message(text=ai_reply)
                
                # Add follow-up suggestions based on context
                if 'pricing' in user_message.lower() or 'cost' in user_message.lower():
                    dispatcher.utter_message(text="Would you like me to send you detailed pricing information? Just provide your email address!")
                elif 'demo' in user_message.lower() or 'show' in user_message.lower():
                    dispatcher.utter_message(text="I'd be happy to schedule a personalized demo for you. What time works best - morning, afternoon, or evening?")
                elif 'trial' in user_message.lower() or 'try' in user_message.lower():
                    dispatcher.utter_message(text="Great! To get your free trial started, I'll need to know what type of business you have so I can customize the solution for you.")
                
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

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="I'm not sure I understand. Could you rephrase that or ask me something about our services, pricing, or how to get started?")
        return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Let's start fresh! How can I help you today?")
        return [SlotSet("business_type", None), SlotSet("package_type", None)]
