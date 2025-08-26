from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted
import logging
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ActionSessionStart(Action):
    """Action to start a new session."""
    
    def name(self) -> Text:
        return "action_session_start"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        dispatcher.utter_message(text="🎨 **Welcome to Alternative Tattoo Studio!** I'm Ozzy, your AI tattoo assistant. How can I help you today?")
        return [SessionStarted(), ActionExecuted("action_listen")]

class ActionTattooConsultation(Action):
    """Action to handle tattoo consultation requests."""
    
    def name(self) -> Text:
        return "action_tattoo_consultation"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        # Extract slots if available
        tattoo_style = tracker.get_slot("tattoo_style")
        tattoo_placement = tracker.get_slot("tattoo_placement")
        tattoo_size = tracker.get_slot("tattoo_size")
        budget_range = tracker.get_slot("budget_range")
        
        response = "💬 **Great! Let's plan your perfect tattoo!**\n\n"
        
        if tattoo_style:
            response += f"**Style:** {tattoo_style}\n"
        if tattoo_placement:
            response += f"**Placement:** {tattoo_placement}\n"
        if tattoo_size:
            response += f"**Size:** {tattoo_size}\n"
        if budget_range:
            response += f"**Budget:** {budget_range}\n"
        
        response += "\n**Next Steps:**\n• Schedule a consultation (free)\n• See artist portfolios\n• Get pricing estimates\n• Discuss design options\n\n**What would you like to do next?**"
        
        dispatcher.utter_message(text=response)
        return []

class ActionBookAppointment(Action):
    """Action to handle appointment booking."""
    
    def name(self) -> Text:
        return "action_book_appointment"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        # Extract appointment details if available
        appointment_date = tracker.get_slot("appointment_date")
        appointment_time = tracker.get_slot("appointment_time")
        artist_name = tracker.get_slot("artist_name")
        
        response = "📅 **Perfect! Let's get you booked!**\n\n"
        
        if appointment_date:
            response += f"**Date:** {appointment_date}\n"
        if appointment_time:
            response += f"**Time:** {appointment_time}\n"
        if artist_name:
            response += f"**Artist:** {artist_name}\n"
        
        response += "\n**Available Times:**\n• Tuesday-Thursday: 11 AM - 8 PM\n• Friday-Saturday: 11 AM - 9 PM\n• Sunday-Monday: Closed\n\n**To complete your booking, I need:**\n• Your name\n• Phone number\n• Preferred date/time\n• Type of appointment\n\n**Ready to book?** Just provide your details!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionArtistRecommendation(Action):
    """Action to recommend artists based on style and requirements."""
    
    def name(self) -> Text:
        return "action_artist_recommendation"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        # Extract style preference if available
        tattoo_style = tracker.get_slot("tattoo_style")
        
        response = "👨‍🎨 **Here are our amazing artists and their specialties:**\n\n"
        
        if tattoo_style:
            response += f"**For {tattoo_style} style, I recommend:**\n\n"
        
        response += "**Mike - Traditional Master**\n• American traditional & Japanese styles\n• Bold lines & bright colors\n• 15+ years experience\n• Available: Tue-Thu, Fri-Sat\n\n"
        response += "**Sarah - Fine Line Specialist**\n• Minimalist & geometric designs\n• Delicate linework\n• 8+ years experience\n• Available: Tue-Thu, Fri-Sat\n\n"
        response += "**Jake - Realism Expert**\n• Black & grey realism\n• Portrait & wildlife\n• 12+ years experience\n• Available: Tue-Thu, Fri-Sat\n\n"
        response += "**Emma - Creative Artist**\n• Watercolor & abstract\n• Color blending\n• 6+ years experience\n• Available: Tue-Thu, Fri-Sat\n\n"
        response += "**Alex - Tribal Specialist**\n• Polynesian & Celtic tribal\n• Geometric patterns\n• 10+ years experience\n• Available: Tue-Thu, Fri-Sat\n\n"
        response += "**Want to see their portfolios or check availability?** Just ask!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionPricingEstimate(Action):
    """Action to provide pricing estimates."""
    
    def name(self) -> Text:
        return "action_pricing_estimate"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        # Extract design details if available
        design_complexity = tracker.get_slot("design_complexity")
        session_duration = tracker.get_slot("session_duration")
        budget_range = tracker.get_slot("budget_range")
        
        response = "💰 **Here's a detailed pricing breakdown:**\n\n"
        
        if design_complexity:
            response += f"**For {design_complexity} designs:**\n\n"
        
        response += "**Size & Complexity:**\n• Small (1-2 hours): $100-200\n• Medium (2-4 hours): $200-400\n• Large (4+ hours): $400+\n• Custom designs: +$50-100\n\n"
        response += "**Artist Experience:**\n• Junior artists: 10% discount\n• Senior artists: Standard rates\n• Master artists: +20% premium\n\n"
        response += "**Placement & Detail:**\n• Simple designs: Base rate\n• Complex details: +25-50%\n• Cover-ups: +30-50%\n\n"
        response += "**Additional Services:**\n• Consultation: Free\n• Design fee: $50-200\n• Touch-ups: $50-200\n• Aftercare kit: $25\n\n"
        
        if budget_range:
            response += f"**For your {budget_range} budget, you can get:**\n"
            if "100-200" in budget_range:
                response += "• Small simple designs\n• Basic flash tattoos\n• Minimalist linework\n"
            elif "200-400" in budget_range:
                response += "• Medium detailed designs\n• Custom simple tattoos\n• Color work\n"
            elif "400-800" in budget_range:
                response += "• Large custom designs\n• Complex artwork\n• Multiple colors\n"
            elif "800+" in budget_range:
                response += "• Sleeve work\n• Full back pieces\n• Complex custom designs\n"
        
        response += "\n**Want a specific quote?** Schedule a consultation and I'll give you an exact price!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionDesignConsultation(Action):
    """Action to handle design consultation requests."""
    
    def name(self) -> Text:
        return "action_design_consultation"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🎨 **Design consultation is where the magic happens!**\n\n"
        response += "**What we'll discuss:**\n• Your design concept and inspiration\n• Placement and sizing options\n• Style and technique choices\n• Color vs. black & grey\n• Custom vs. flash designs\n• Timeline and sessions needed\n\n"
        response += "**Consultation Process:**\n1. **Initial Meeting** (30 min, free)\n2. **Concept Discussion** - Share your ideas\n3. **Artist Selection** - Based on style\n4. **Design Creation** - Artist sketches\n5. **Revisions** - Up to 2 free revisions\n6. **Final Approval** - You approve design\n7. **Scheduling** - Book your session\n\n"
        response += "**Design Fees:**\n• Simple custom: $50-100\n• Complex custom: $100-200\n• Multiple revisions: +$25 each\n\n"
        response += "**Timeline:**\n• Simple designs: 1-2 weeks\n• Complex designs: 2-4 weeks\n• Rush orders: +$50 fee\n\n"
        response += "**Ready to start your design?** Schedule a consultation and let's create something amazing!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionContactInfo(Action):
    """Action to provide contact information."""
    
    def name(self) -> Text:
        return "action_contact_information"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📞 **Alternative Tattoo Studio Contact Information:**\n\n"
        response += "**Phone:** (555) 987-6543\n**Text:** (555) 987-6543\n**Email:** hello@alternativetattoo.com\n\n"
        response += "**Address:** 456 Ink Street, Art District, AD 54321\n\n"
        response += "**Social Media:**\n• Instagram: @AlternativeTattoo\n• Facebook: Alternative Tattoo Studio\n• TikTok: @AlternativeTattoo\n\n"
        response += "**Support Hours:**\n• Tuesday-Thursday: 11 AM - 8 PM\n• Friday-Saturday: 11 AM - 9 PM\n• Sunday-Monday: Closed\n\n"
        response += "**Emergency Contact:** For urgent matters, text us directly!\n\n"
        response += "**Need to reach us quickly?** Text is usually fastest! 📱💬"
        
        dispatcher.utter_message(text=response)
        return []

class ActionDefaultFallback(Action):
    """Action to handle default fallback responses."""
    
    def name(self) -> Text:
        return "action_default_fallback"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        fallback_responses = [
            "🤷‍♂️ **I'm not quite sure what you're asking about.** Can you rephrase that? I'm here to help with tattoo appointments, artists, designs, pricing, and studio information.",
            "🎯 **That's outside my tattoo expertise!** I'm focused on helping you with tattoo appointments, artist portfolios, pricing, services, and studio information. What tattoo-related question can I help with?",
            "💬 **I want to make sure I understand you correctly.** Could you try asking that in a different way? I'm here to help with all things tattoo-related!",
            "🎨 **Let me help you with tattoo studio questions!** I can assist with appointments, artists, designs, pricing, services, and studio information. What would you like to know?",
            "🤔 **I'm not following that question.** Can you ask about something tattoo-related? I'm great with appointments, artists, designs, and studio info!"
        ]
        
        response = random.choice(fallback_responses)
        dispatcher.utter_message(text=response)
        return []

# Additional specialized actions for Ozzy

class ActionTattooStyleRecommendation(Action):
    """Action to recommend tattoo styles based on preferences."""
    
    def name(self) -> Text:
        return "action_tattoo_style_recommendation"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🎨 **Here are the most popular tattoo styles we offer:**\n\n"
        response += "**Traditional Styles:**\n• American Traditional - Bold colors, thick lines\n• Japanese Traditional - Detailed, symbolic\n• Neo-Traditional - Modern twist on classic\n\n"
        response += "**Modern Styles:**\n• Minimalist - Simple, clean lines\n• Geometric - Mathematical precision\n• Watercolor - Soft, flowing colors\n• Black & Grey - Shading and depth\n\n"
        response += "**Specialty Styles:**\n• Realism - Photo-like detail\n• Tribal - Cultural patterns\n• Script - Text and lettering\n• Abstract - Artistic expression\n\n"
        response += "**What style interests you most?** I can show you examples and recommend the perfect artist!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionPlacementAdvice(Action):
    """Action to provide tattoo placement advice."""
    
    def name(self) -> Text:
        return "action_placement_advice"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📍 **Tattoo placement is crucial! Here's what to consider:**\n\n"
        response += "**Pain Level (Low to High):**\n• Upper arm/forearm - Low pain\n• Shoulder/back - Low-medium pain\n• Calf/thigh - Medium pain\n• Ribs/ankle - High pain\n• Hand/foot - Very high pain\n\n"
        response += "**Visibility & Work:**\n• **Always visible:** Face, neck, hands\n• **Sometimes visible:** Arms, lower legs\n• **Usually hidden:** Back, chest, upper thighs\n\n"
        response += "**Healing Considerations:**\n• Areas that bend (elbows, knees) - Slower healing\n• Areas with movement - May need touch-ups\n• Areas with sun exposure - Fade faster\n\n"
        response += "**Size & Placement:**\n• Small designs - Wrist, ankle, behind ear\n• Medium designs - Forearm, calf, shoulder\n• Large designs - Back, chest, full sleeve\n\n"
        response += "**What area are you thinking?** I can give you specific advice!"
        
        dispatcher.utter_message(text=response)
        return []

class ActionAftercareDetailed(Action):
    """Action to provide detailed aftercare instructions."""
    
    def name(self) -> Text:
        return "action_aftercare_detailed"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🩹 **Complete Tattoo Aftercare Guide:**\n\n"
        response += "**First 24-48 Hours:**\n• Keep bandage on for 2-4 hours\n• Wash gently with mild, fragrance-free soap\n• Pat dry with clean paper towel\n• Apply thin layer of healing ointment\n• Wear loose, clean clothing\n\n"
        response += "**Days 3-7 (Scabbing Phase):**\n• Wash 2-3 times daily\n• Apply ointment 2-3 times daily\n• Don't pick or scratch scabs\n• Avoid swimming, hot tubs, saunas\n• Stay out of direct sunlight\n\n"
        response += "**Days 8-14 (Peeling Phase):**\n• Continue washing 2-3 times daily\n• Apply lotion when skin feels dry\n• Don't peel off skin flakes\n• Avoid tight clothing on tattoo\n• No swimming or soaking\n\n"
        response += "**Weeks 3-4 (Healing Phase):**\n• Tattoo should look healed\n• Continue moisturizing\n• Can resume normal activities\n• Sun protection is crucial\n• Schedule touch-up if needed\n\n"
        response += "**Long-term Care:**\n• Always use sunscreen (SPF 30+)\n• Moisturize regularly\n• Avoid excessive sun exposure\n• Touch-ups every 5-10 years\n\n"
        response += "**Red Flags (Call us immediately):**\n• Excessive redness or swelling\n• Pus or foul odor\n• Fever or chills\n• Severe pain\n\n"
        response += "**Questions about aftercare?** I'm here to help! 🧴✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionStudioPolicies(Action):
    """Action to explain studio policies."""
    
    def name(self) -> Text:
        return "action_studio_policies"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📋 **Alternative Tattoo Studio Policies:**\n\n"
        response += "**Appointment Policies:**\n• 24-hour notice for cancellations\n• No-shows may require deposit for future bookings\n• Late arrivals may lose appointment time\n• Rescheduling available with notice\n\n"
        response += "**Payment Policies:**\n• Deposits required for all appointments\n• Deposits are non-refundable\n• Payment plans available for $300+ tattoos\n• Cash preferred, cards accepted\n• No refunds after work begins\n\n"
        response += "**Health & Safety:**\n• Must be 18+ with valid ID\n• No tattoos if pregnant\n• Inform us of medical conditions\n• No alcohol 24 hours before\n• No blood thinners without doctor approval\n\n"
        response += "**Design Policies:**\n• 2 free revisions included\n• Additional revisions: $25 each\n• Rush orders: +$50 fee\n• Design fees non-refundable\n• Copyright remains with artist\n\n"
        response += "**Studio Rules:**\n• No smoking inside\n• No food or drinks in work areas\n• One guest per client\n• Children must be supervised\n• Respect other clients' privacy\n\n"
        response += "**Questions about any policy?** I'm happy to clarify!"
        
        dispatcher.utter_message(text=response)
        return []
