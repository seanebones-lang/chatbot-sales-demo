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
    """Action to explain studio policies and procedures."""
    
    def name(self) -> Text:
        return "action_studio_policies"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📋 **Studio Policies & Procedures**\n\n**Appointment Policies:**\n• 24-hour cancellation notice required\n• No-shows may lose future booking privileges\n• Late arrivals may result in rescheduling\n• Deposits are non-refundable\n\n**Studio Rules:**\n• No smoking or vaping inside\n• No food or drinks near tattoo area\n• One guest per client maximum\n• Children must be supervised\n\n**Health & Safety:**\n• All artists are licensed and certified\n• Equipment is sterilized after each use\n• Single-use needles and tubes\n• Medical-grade disinfectants\n\n**Questions about any policy?** I'm here to clarify! 📋✅"
        
        dispatcher.utter_message(text=response)
        return []

class ActionAftercareInstructions(Action):
    """Action to provide detailed aftercare instructions."""
    
    def name(self) -> Text:
        return "action_aftercare_instructions"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🩹 **Complete Aftercare Instructions**\n\n**First 24-48 Hours:**\n• Keep bandage on for 2-4 hours\n• Wash gently with mild, fragrance-free soap\n• Pat dry with clean paper towel\n• Apply thin layer of healing ointment\n• Re-bandage if needed\n\n**First Week:**\n• Wash 2-3 times daily\n• Apply ointment 2-3 times daily\n• Avoid swimming, hot tubs, saunas\n• Avoid direct sunlight\n• Don't pick or scratch scabs\n\n**Healing Timeline:**\n• Days 1-3: Redness and swelling\n• Days 3-7: Scabbing begins\n• Days 7-14: Scabs fall off\n• Days 14-28: Peeling phase\n• Month 2-3: Tattoo settles\n\n**What to Avoid:**\n• Tight clothing over tattoo\n• Excessive sweating\n• Pools and hot tubs\n• Tanning beds\n• Picking at scabs\n\n**Need aftercare help?** I'm here 24/7! 🧴✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionArtistPortfolio(Action):
    """Action to showcase artist portfolios and styles."""
    
    def name(self) -> Text:
        return "action_artist_portfolio"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🖼️ **Artist Portfolios & Specialties**\n\n**Mike - Traditional Master (15+ years):**\n• American traditional style\n• Japanese traditional (Irezumi)\n• Bold lines and bright colors\n• Large-scale pieces\n• Available: Tue-Thu, Fri-Sat\n\n**Sarah - Fine Line Specialist (8+ years):**\n• Minimalist designs\n• Geometric patterns\n• Delicate linework\n• Small, detailed pieces\n• Available: Tue-Thu, Fri-Sat\n\n**Jake - Realism Expert (12+ years):**\n• Black & grey realism\n• Portrait tattoos\n• Wildlife and nature\n• Photorealistic style\n• Available: Tue-Thu, Fri-Sat\n\n**Emma - Creative Artist (6+ years):**\n• Watercolor style\n• Abstract designs\n• Color blending\n• Artistic expression\n• Available: Tue-Thu, Fri-Sat\n\n**Alex - Tribal Specialist (10+ years):**\n• Polynesian tribal\n• Celtic designs\n• Geometric tribal\n• Cultural patterns\n• Available: Tue-Thu, Fri-Sat\n\n**Want to see specific examples?** I can describe their work in detail! 🎨👨‍🎨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionBudgetRange(Action):
    """Action to discuss budget ranges and options."""
    
    def name(self) -> Text:
        return "action_budget_range"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "💰 **Budget-Friendly Tattoo Options**\n\n**$100-200 Budget:**\n• Small simple designs (1-2 hours)\n• Basic flash tattoos\n• Minimalist linework\n• Simple geometric shapes\n• Small text or symbols\n\n**$200-400 Budget:**\n• Medium detailed designs (2-4 hours)\n• Custom simple tattoos\n• Color work\n• Moderate complexity\n• Good size pieces\n\n**$400-800 Budget:**\n• Large custom designs (4-6 hours)\n• Complex artwork\n• Multiple colors\n• Detailed shading\n• Sleeve work\n\n**$800+ Budget:**\n• Full sleeve work\n• Large back pieces\n• Complex custom designs\n• Multiple sessions\n• Masterpiece level work\n\n**Budget Tips:**\n• Start small and add to it later\n• Choose simpler designs\n• Consider black & grey only\n• Ask about student/military discounts\n\n**What's your budget range?** I can suggest perfect options! 💸✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionContactInformation(Action):
    """Action to provide studio contact information."""
    
    def name(self) -> Text:
        return "action_contact_information"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📞 **Alternative Tattoo Studio Contact Info**\n\n**Primary Contact:**\n• **Phone:** (555) 987-6543\n• **Text:** (555) 987-6543 (fastest response)\n• **Email:** hello@alternativetattoo.com\n\n**Studio Address:**\n• 456 Ink Street, Art District\n• AD 54321\n• Free parking in back lot\n• Wheelchair accessible\n\n**Social Media:**\n• Instagram: @AlternativeTattoo\n• Facebook: Alternative Tattoo Studio\n• TikTok: @AlternativeTattoo\n• Twitter: @AltTattooStudio\n\n**Best Ways to Reach Us:**\n• **Text:** Usually responds within minutes\n• **Instagram DM:** Great for sharing design ideas\n• **Phone:** Best for urgent questions\n• **Email:** Perfect for detailed inquiries\n\n**Need to reach us quickly?** Text is usually fastest! 📱💬"
        
        dispatcher.utter_message(text=response)
        return []

class ActionCoverUpTattoo(Action):
    """Action to discuss cover-up tattoo options."""
    
    def name(self) -> Text:
        return "action_cover_up_tattoo"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🔄 **Cover-Up Tattoo Options**\n\n**Cover-Up Considerations:**\n• Original tattoo size and color\n• Skin condition and scarring\n• Desired new design\n• Placement options\n• Multiple sessions often needed\n\n**Cover-Up Process:**\n• Consultation and assessment\n• Design planning and strategy\n• Laser treatment (if needed)\n• Cover-up tattoo application\n• Touch-up sessions\n\n**Cover-Up Pricing:**\n• Small cover-up: $200-400\n• Medium cover-up: $400-800\n• Large cover-up: $800+\n• Laser treatment: $100-300 per session\n• Design fee: $50-100\n\n**Cover-Up Challenges:**\n• Dark colors are harder to cover\n• Large tattoos need strategic design\n• Scarring may affect results\n• Multiple sessions often required\n\n**Cover-Up Success Factors:**\n• Choose experienced artists\n• Be open to design flexibility\n• Consider laser treatment first\n• Realistic expectations\n\n**Ready to discuss your cover-up?** Let's see what we're working with! 🎨✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionCustomDesign(Action):
    """Action to explain custom design process."""
    
    def name(self) -> Text:
        return "action_custom_design"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🎨 **Custom Design Process**\n\n**Design Process Steps:**\n• Initial consultation (free)\n• Concept discussion and inspiration\n• Artist creates preliminary sketch\n• Revisions and refinements\n• Final design approval\n• Tattoo session scheduling\n\n**Design Fees:**\n• Simple custom: $50-100\n• Complex custom: $100-200\n• Multiple revisions: +$25 each\n• Rush orders: +$50 fee\n\n**Design Timeline:**\n• Simple designs: 1-2 weeks\n• Complex designs: 2-4 weeks\n• Rush orders: 3-5 days\n• Major revisions: +1 week\n\n**What to Bring:**\n• Reference images and ideas\n• Inspiration sources\n• Size and placement preferences\n• Color preferences\n• Budget considerations\n\n**Design Tips:**\n• Be specific about your vision\n• Bring multiple reference images\n• Consider placement carefully\n• Be open to artist suggestions\n• Allow time for revisions\n\n**Ready to start your custom design?** Let's talk about your vision! ✨🎨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionDesignComplexity(Action):
    """Action to explain design complexity factors."""
    
    def name(self) -> Text:
        return "action_design_complexity"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🎨 **Design Complexity Breakdown**\n\n**Simple Designs:**\n• Basic shapes and lines\n• Minimal detail work\n• Single color or black only\n• 1-2 hour sessions\n• $100-200 pricing\n• Good for first tattoos\n\n**Medium Designs:**\n• Moderate detail work\n• Multiple elements\n• Some color work\n• 2-4 hour sessions\n• $200-400 pricing\n• Most popular choice\n\n**Complex Designs:**\n• High detail work\n• Multiple colors\n• Shading and depth\n• 4-6 hour sessions\n• $400-800 pricing\n• Professional results\n\n**Masterpiece Level:**\n• Extreme detail work\n• Full color palette\n• Multiple techniques\n• 6+ hour sessions\n• $800+ pricing\n• Gallery-quality work\n\n**Complexity Factors:**\n• Line thickness and detail\n• Number of colors used\n• Shading and depth\n• Size and placement\n• Artist experience level\n• Time investment needed\n\n**What complexity are you thinking?** I can give you a better estimate! 🎨📏"
        
        dispatcher.utter_message(text=response)
        return []

class ActionDesignRevisions(Action):
    """Action to explain design revision process."""
    
    def name(self) -> Text:
        return "action_design_revisions"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "✏️ **Design Revision Process**\n\n**Revision Process:**\n• Initial design presentation\n• Feedback and suggestions\n• Artist makes changes\n• Review revised design\n• Additional revisions if needed\n• Final approval\n\n**Revision Limits:**\n• 2 free revisions included\n• Additional revisions: $25 each\n• Major design changes: $50\n• Complete redesign: $100\n• Rush revisions: +$25 fee\n\n**Revision Timeline:**\n• Minor changes: 1-2 days\n• Major changes: 3-5 days\n• Complete redesign: 1 week\n• Rush revisions: 2-3 days\n• Complex changes: 1-2 weeks\n\n**Revision Tips:**\n• Be specific about changes\n• Provide clear feedback\n• Consider all aspects\n• Don't rush the process\n• Trust your artist's expertise\n\n**We want you to love your design!** Revisions ensure perfect results.\n\n**Need design changes?** Let's make it perfect! ✨🎨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionHealthRequirements(Action):
    """Action to explain health and safety requirements."""
    
    def name(self) -> Text:
        return "action_health_requirements"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🏥 **Health & Safety Requirements**\n\n**Age Requirements:**\n• Must be 18+ with valid government ID\n• Parental consent not accepted\n• No exceptions to age policy\n• ID must be current and valid\n\n**Health Considerations:**\n• No tattoos if pregnant\n• Consult doctor if on blood thinners\n• Inform us of medical conditions\n• No tattoos over recent scars\n• No tattoos over skin conditions\n• Wait 6 months after major surgery\n\n**What to Bring:**\n• Valid government ID (driver's license, passport, state ID)\n• List of current medications\n• Medical history if relevant\n• Emergency contact information\n\n**Health Restrictions:**\n• No tattoos if sick or feverish\n• No tattoos over moles or birthmarks\n• No tattoos over areas with skin conditions\n• Consult doctor for chronic conditions\n\n**Health questions?** We can discuss them during consultation! 🩺✅"
        
        dispatcher.utter_message(text=response)
        return []

class ActionHealingTimeline(Action):
    """Action to explain tattoo healing timeline."""
    
    def name(self) -> Text:
        return "action_healing_timeline"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "⏰ **Tattoo Healing Timeline**\n\n**Week 1 - Initial Healing:**\n• Days 1-2: Redness and swelling\n• Days 3-4: Scabbing begins\n• Days 5-7: Scabbing continues\n• Keep bandage on for 2-4 hours\n\n**Week 2 - Scabbing Phase:**\n• Days 8-10: Heavy scabbing\n• Days 11-14: Scabs start falling\n• Don't pick at scabs\n• Apply ointment regularly\n\n**Week 3-4 - Peeling Phase:**\n• Days 15-21: Skin peeling\n• Days 22-28: Final healing\n• Moisturize frequently\n• Avoid sun exposure\n\n**Month 2-3 - Settling:**\n• Tattoo settles into skin\n• Colors become permanent\n• Texture normalizes\n• Full healing complete\n\n**Healing Factors:**\n• Placement affects healing time\n• Skin type matters\n• Aftercare is crucial\n• Individual healing varies\n• Health and lifestyle impact\n\n**Healing questions?** I'm here to help! 🩹⏱️"
        
        dispatcher.utter_message(text=response)
        return []

class ActionPaymentOptions(Action):
    """Action to explain payment options and policies."""
    
    def name(self) -> Text:
        return "action_payment_options"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "💳 **Payment Options & Policies**\n\n**Accepted Payment Methods:**\n• Cash (preferred)\n• Credit/Debit cards\n• Venmo\n• PayPal\n• Apple Pay\n• Google Pay\n• Cash App\n\n**Deposit Requirements:**\n• Consultations: No deposit\n• Small tattoos: $50 deposit\n• Medium tattoos: $100 deposit\n• Large tattoos: $200 deposit\n• Custom designs: $100 deposit\n• Sleeve work: $300 deposit\n\n**Payment Plans:**\n• Available for tattoos $300+\n• 50% down payment required\n• Balance due day of appointment\n• No interest or fees\n• Must be paid in full\n\n**Deposit Policies:**\n• Deposits are non-refundable\n• Deposits go toward final price\n• Deposits hold your appointment\n• Lost deposits if you no-show\n\n**Questions about payment?** I'm here to help! 💰✅"
        
        dispatcher.utter_message(text=response)
        return []

class ActionSessionDuration(Action):
    """Action to explain session duration factors."""
    
    def name(self) -> Text:
        return "action_session_duration"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "⏱️ **Session Duration Breakdown**\n\n**Short Sessions (1-2 hours):**\n• Small simple designs\n• Basic linework\n• Minimal color\n• Good for first tattoos\n• Less expensive\n• Quick healing\n\n**Medium Sessions (2-4 hours):**\n• Detailed designs\n• Color work\n• Moderate complexity\n• Most popular choice\n• Good value\n• Manageable pain\n\n**Long Sessions (4-6 hours):**\n• Complex designs\n• Full color work\n• Large pieces\n• Multiple techniques\n• Professional results\n• Requires endurance\n\n**Extended Sessions (6+ hours):**\n• Sleeve work\n• Full back pieces\n• Masterpiece level\n• Multiple sessions recommended\n• Premium pricing\n• Maximum comfort needed\n\n**Session Factors:**\n• Design complexity\n• Artist speed\n• Your pain tolerance\n• Studio scheduling\n• Placement sensitivity\n\n**How long can you sit?** This helps determine your options! 🪑⏰"
        
        dispatcher.utter_message(text=response)
        return []

class ActionSpecialOffers(Action):
    """Action to explain special offers and discounts."""
    
    def name(self) -> Text:
        return "action_special_offers"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🎉 **Current Special Offers**\n\n**Student Discounts:**\n• 15% off with valid student ID\n• Available year-round\n• Applies to all services\n• No expiration date\n\n**Military/Veteran Discounts:**\n• 20% off all services\n• Available to all veterans\n• Active duty and reserves\n• DD-214 or military ID required\n\n**Referral Rewards:**\n• $25 credit for each friend\n• Credit applied to your next tattoo\n• No limit on referrals\n• Both you and friend get credit\n\n**First Timer Special:**\n• 10% off first tattoo\n• Available to new clients only\n• Applies to any service\n• One-time use\n\n**Seasonal Promotions:**\n• Spring Cleaning: 20% off cover-ups\n• Summer Vibes: 15% off watercolor\n• Fall Colors: 10% off color tattoos\n• Winter Special: 25% off black & grey\n\n**Want to know more about any offer?** Just ask! 🎁✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionStudioInformation(Action):
    """Action to provide general studio information."""
    
    def name(self) -> Text:
        return "action_studio_information"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🏢 **Alternative Tattoo Studio Information**\n\n**Studio Hours:**\n• Tuesday - Thursday: 11 AM - 8 PM\n• Friday - Saturday: 11 AM - 9 PM\n• Sunday - Monday: Closed\n• Walk-ins welcome during business hours\n\n**Studio Features:**\n• Private tattoo rooms\n• Sterile equipment\n• Licensed artists\n• Professional atmosphere\n• Music and entertainment\n• Refreshments available\n\n**Services Offered:**\n• Custom tattoo designs\n• Cover-up tattoos\n• Touch-up work\n• Consultations\n• Design services\n• Aftercare products\n\n**Studio Policies:**\n• 18+ only with valid ID\n• No smoking inside\n• One guest per client\n• Children must be supervised\n• Professional conduct required\n\n**Need more studio info?** I'm here to help! 🏢✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionStudioLocation(Action):
    """Action to provide studio location and directions."""
    
    def name(self) -> Text:
        return "action_studio_location"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "📍 **Studio Location & Directions**\n\n**Studio Address:**\n• 456 Ink Street, Art District\n• AD 54321\n• Located in the heart of Art District\n• Easy to find and access\n\n**Getting Here:**\n• **By Car:** Free parking in back lot\n• **By Bus:** Routes 15, 22, 33 stop nearby\n• **By Train:** Art District Station (5 min walk)\n• **By Bike:** Bike racks available\n• **By Foot:** Central location\n\n**Nearby Landmarks:**\n• Art District Gallery (2 blocks)\n• Coffee Corner (next door)\n• Art Supply Store (across street)\n• Public Parking Garage (1 block)\n• Art District Park (3 blocks)\n\n**Studio Features:**\n• Street-level access\n• Wheelchair accessible\n• Well-lit entrance\n• Security cameras\n• Easy to find\n\n**Need directions?** I can give you turn-by-turn! 🗺️✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionTouchUpTattoo(Action):
    """Action to explain touch-up tattoo services."""
    
    def name(self) -> Text:
        return "action_touch_up_tattoo"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🔧 **Touch-Up Tattoo Services**\n\n**When Touch-Ups Are Needed:**\n• Color fading over time\n• Line blurring\n• Patchy areas\n• Healing issues\n• Normal wear and tear\n• Sun damage\n\n**Touch-Up Timing:**\n• Wait 4-6 weeks after healing\n• Best within 6 months\n• Can be done years later\n• Seasonal touch-ups recommended\n• Before special events\n\n**Touch-Up Pricing:**\n• Small touch-up: $50-100\n• Medium touch-up: $100-200\n• Large touch-up: $200+\n• Free touch-up within 3 months\n• Color refresh: +$25\n\n**Touch-Up Process:**\n• Quick consultation\n• Minor adjustments\n• Faster healing\n• Less expensive\n• Minimal discomfort\n\n**Touch-Up Tips:**\n• Schedule before important events\n• Consider seasonal timing\n• Bring original design reference\n• Allow healing time\n• Follow aftercare instructions\n\n**Need a touch-up?** I can check availability for you! 🎨✨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionUrgencyLevel(Action):
    """Action to discuss urgency and scheduling options."""
    
    def name(self) -> Text:
        return "action_urgency_level"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "⚡ **Scheduling & Urgency Options**\n\n**Same Day (Walk-in):**\n• Small simple designs\n• Flash tattoos\n• Touch-ups\n• Subject to availability\n• Limited artist choice\n• +$50 rush fee\n\n**This Week:**\n• Small custom designs\n• Simple consultations\n• Basic appointments\n• Limited artist choice\n• +$25 rush fee\n• Better availability\n\n**Next Week:**\n• Medium custom designs\n• Artist consultations\n• Better availability\n• More artist options\n• +$10 rush fee\n• Standard pricing\n\n**2+ Weeks:**\n• Large custom designs\n• Full consultations\n• All artists available\n• Best appointment times\n• No rush fees\n• Full artist selection\n\n**Rush Fee Breakdown:**\n• Same day: +$50\n• This week: +$25\n• Next week: +$10\n• 2+ weeks: No fee\n\n**What's your timeline?** I'll find the best option for you! ⏰🎨"
        
        dispatcher.utter_message(text=response)
        return []

class ActionWalkInAvailability(Action):
    """Action to explain walk-in availability and options."""
    
    def name(self) -> Text:
        return "action_walk_in_availability"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """Run the action."""
        response = "🚶‍♂️ **Walk-In Availability & Options**\n\n**Best Times for Walk-ins:**\n• Tuesday-Thursday: 2 PM - 6 PM\n• Friday-Saturday: 3 PM - 7 PM\n• Sunday-Monday: Closed\n• Avoid lunch hours (12-1 PM)\n\n**Walk-in Services Available:**\n• Small tattoos (under 2 hours)\n• Flash designs\n• Touch-ups\n• Consultations\n• Simple linework\n• Basic designs\n\n**Walk-in Limitations:**\n• Large tattoos need appointments\n• Custom designs need consultation\n• Popular artists may be booked\n• Subject to artist availability\n• Limited design options\n• Rush fees may apply\n\n**Walk-in Process:**\n• Check in at front desk\n• Discuss design options\n• Check artist availability\n• Get time estimate\n• Start when ready\n\n**Walk-in Tips:**\n• Come during slower hours\n• Be flexible with design\n• Have backup options\n• Bring reference images\n• Be patient with wait times\n\n**Want to try walking in?** I can check current availability! 🕐✨"
        
        dispatcher.utter_message(text=response)
        return []
