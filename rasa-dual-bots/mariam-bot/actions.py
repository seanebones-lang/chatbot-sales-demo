from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted
import requests
import json
import os
from datetime import datetime, timedelta

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        events = [SessionStarted()]
        events.append(ActionExecuted("action_listen"))
        return events

class ActionBusinessAnalysis(Action):
    def name(self) -> Text:
        return "action_business_analysis"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        business_type = tracker.get_slot("business_type") or "general"
        
        analysis = {
            "healthcare": "🏥 **Healthcare Business Analysis**\n\n**Key Challenges:**\n• HIPAA compliance requirements\n• Patient communication complexity\n• Appointment scheduling management\n• Insurance verification processes\n\n**Our Solution Benefits:**\n• HIPAA-compliant AI chatbot\n• Automated patient communication\n• Smart appointment scheduling\n• Insurance verification automation\n\n**Expected ROI:** 400-600% within 6 months",
            "retail": "🛍️ **Retail Business Analysis**\n\n**Key Challenges:**\n• Inventory management complexity\n• Customer service scaling\n• Order processing efficiency\n• Return handling processes\n\n**Our Solution Benefits:**\n• Real-time inventory checking\n• 24/7 customer service\n• Automated order processing\n• Streamlined returns management\n\n**Expected ROI:** 300-500% within 4 months",
            "automotive": "🚗 **Automotive Business Analysis**\n\n**Key Challenges:**\n• Service scheduling complexity\n• Parts catalog management\n• Customer communication\n• Maintenance reminders\n\n**Our Solution Benefits:**\n• Automated service scheduling\n• Intelligent parts catalog\n• Customer communication hub\n• Proactive maintenance alerts\n\n**Expected ROI:** 350-550% within 5 months",
            "restaurant": "🍽️ **Restaurant Business Analysis**\n\n**Key Challenges:**\n• Reservation management\n• Menu updates and changes\n• Customer service scaling\n• Order processing efficiency\n\n**Our Solution Benefits:**\n• Smart reservation system\n• Dynamic menu support\n• 24/7 customer service\n• Automated order processing\n\n**Expected ROI:** 250-450% within 3 months"
        }
        
        response = analysis.get(business_type, analysis["retail"])
        dispatcher.utter_message(text=response)
        return []

class ActionPricingInquiry(Action):
    def name(self) -> Text:
        return "action_pricing_inquiry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
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
        return []

class ActionVeteranDiscounts(Action):
    def name(self) -> Text:
        return "action_veteran_discounts"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🇺🇸 **Veteran Discounts & Special Programs**

**25% Off All Plans**
• Available to all verified veterans
• Active duty, reserves, and retired
• No expiration date
• Applies to all plan levels

**Veteran Verification Process:**
• DD-214 or military ID
• Quick verification (usually same day)
• Secure and confidential
• No additional paperwork

**Special Veteran Benefits:**
• Priority onboarding support
• Dedicated veteran success manager
• Extended trial period (30 days)
• Flexible payment options

**Veteran Success Stories:**
• 500+ veteran-owned businesses served
• Average ROI: 450% within 6 months
• 98% satisfaction rating
• Ongoing support and training

**Ready to get started?** I can help you with verification and set up your veteran discount right away."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionScheduleDemo(Action):
    def name(self) -> Text:
        return "action_schedule_demo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📅 **Schedule Your Professional Demo**

**Demo Details:**
• 45-minute personalized session
• Live AI chatbot demonstration
• Industry-specific examples
• ROI calculation for your business
• Q&A session
• No sales pressure

**Available Times:**
• Monday-Friday: 9 AM - 6 PM EST
• Saturday: 10 AM - 2 PM EST
• Flexible scheduling available

**What to Expect:**
• Custom solution overview
• Live chatbot interaction
• Pricing discussion
• Implementation timeline
• Next steps planning

**To schedule your demo:**
• Reply with your preferred date/time
• Include your business type
• Mention if you're a veteran
• I'll confirm and send calendar invite

**What's your preferred demo time?** I'll get you scheduled right away!"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionStartFreeTrial(Action):
    def name(self) -> Text:
        return "action_start_free_trial"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🚀 **Start Your Free Trial**

**14-Day Free Trial Includes:**
• Full access to Professional Plan
• 3 Custom AI Chatbots
• 5,000 queries/month
• All integrations and features
• No credit card required
• No setup fees

**Trial Setup Process:**
• Quick business assessment
• Custom chatbot configuration
• Integration setup assistance
• Training and onboarding
• Performance monitoring

**What Happens After Trial:**
• No automatic charges
• Easy upgrade to paid plan
• Keep all your data
• Seamless transition
• Ongoing support

**To start your trial:**
• Reply with your business type
• Include your website/social media
• Mention any specific needs
• I'll set everything up for you

**Ready to get started?** What type of business do you have?"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionROICalculation(Action):
    def name(self) -> Text:
        return "action_roi_calculation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📊 **ROI Calculation & Projections**

**Investment Breakdown:**
• Professional Plan: $247/month
• Annual Investment: $2,964
• Setup & Training: $500 (one-time)
• Total First Year: $3,464

**Expected Returns (Industry Averages):**

**Healthcare:**
• Month 1-2: Setup & training
• Month 3-4: 200-300% ROI
• Month 5-6: 400-600% ROI
• Annual ROI: 800-1200%

**Retail:**
• Month 1-2: Setup & training
• Month 3-4: 150-250% ROI
• Month 5-6: 300-500% ROI
• Annual ROI: 600-1000%

**Automotive:**
• Month 1-2: Setup & training
• Month 3-4: 200-350% ROI
• Month 5-6: 350-550% ROI
• Annual ROI: 700-1100%

**Restaurant:**
• Month 1-2: Setup & training
• Month 3-4: 100-200% ROI
• Month 5-6: 250-450% ROI
• Annual ROI: 500-900%

**Break-even typically achieved in 2-3 months!**

**Want me to calculate ROI for your specific business?** Just let me know your industry and current customer service costs."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionTechnicalDetails(Action):
    def name(self) -> Text:
        return "action_technical_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🔧 **Technical Details & Architecture**

**AI Technology Stack:**
• GPT-4 powered language models
• Custom-trained business intelligence
• Natural language understanding (NLU)
• Context-aware conversations
• Multi-language support

**Integration Capabilities:**
• REST API endpoints
• Webhook support
• CRM integrations (Salesforce, HubSpot)
• Payment processors (Stripe, PayPal)
• Social media platforms
• Website chat widgets

**Security & Compliance:**
• SOC 2 Type II certified
• GDPR compliant
• HIPAA compliant (healthcare)
• End-to-end encryption
• Regular security audits
• Data privacy controls

**Performance & Scalability:**
• 99.9% uptime guarantee
• Sub-second response times
• Handles 10,000+ concurrent users
• Auto-scaling infrastructure
• Global CDN deployment

**Deployment Options:**
• Cloud-hosted (recommended)
• On-premise deployment
• Hybrid solutions
• White-label options

**Need specific technical details?** I can dive deeper into any area you're interested in."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionHealthcareSpecialist(Action):
    def name(self) -> Text:
        return "action_healthcare_specialist"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🏥 **Healthcare AI Specialist Consultation**

**Healthcare-Specific Features:**
• HIPAA-compliant chatbot
• Patient appointment scheduling
• Insurance verification automation
• Medical FAQ handling
• Prescription refill requests
• Lab result notifications

**Compliance & Security:**
• HIPAA compliance built-in
• PHI data protection
• Audit trail logging
• Secure data transmission
• Regular compliance updates

**Integration Capabilities:**
• Epic, Cerner, Allscripts
• Practice management systems
• Insurance provider APIs
• Patient portal integration
• Telemedicine platforms

**Success Metrics:**
• 40% reduction in call volume
• 60% faster appointment booking
• 80% patient satisfaction
• 50% staff time savings

**Ready to discuss your healthcare needs?** I can provide a detailed consultation and demo."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionContactInfo(Action):
    def name(self) -> Text:
        return "action_contact_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📞 **Contact Information & Support**

**NextEleven Studios**
• **Phone:** (555) 123-4567
• **Email:** hello@nexteleven.com
• **Website:** www.nexteleven.com
• **Address:** 123 AI Boulevard, Tech City, TC 12345

**Support Hours:**
• **Monday-Friday:** 8 AM - 8 PM EST
• **Saturday:** 9 AM - 5 PM EST
• **Sunday:** 10 AM - 4 PM EST
• **24/7 Emergency Support** for enterprise clients

**Contact Methods:**
• **Live Chat:** Available on our website
• **Support Ticket:** support@nexeleven.com
• **Priority Support:** Available with Professional+ plans
• **Dedicated Manager:** Available with Agency+ plans

**Social Media:**
• **LinkedIn:** NextEleven Studios
• **Twitter:** @NextElevenAI
• **Facebook:** NextEleven Studios

**Need immediate assistance?** I can connect you with our support team right away."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🤔 **I didn't quite understand that request.**

**Let me help you better. I can assist with:**

**Business Solutions:**
• AI chatbot implementation
• Customer service automation
• Lead generation systems
• Payment processing setup

**Pricing & Plans:**
• Package recommendations
• ROI calculations
• Veteran discounts
• Custom pricing

**Demos & Trials:**
• Professional demos
• Free trial setup
• Implementation guidance
• Training and support

**Technical Details:**
• Integration options
• Security & compliance
• Performance metrics
• Deployment options

**Try asking about:**
• 'Schedule a demo'
• 'See pricing details'
• 'Start free trial'
• 'Business analysis'
• 'Technical specifications'

**What would you like to know about?**"""
        
        dispatcher.utter_message(text=response)
        return []
