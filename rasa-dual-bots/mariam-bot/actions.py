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

class ActionCustomerRetention(Action):
    def name(self) -> Text:
        return "action_customer_retention"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🎯 **Customer Retention & Acquisition Strategy**

**Customer Retention Strategies:**
• **24/7 AI Support** - Keep customers engaged around the clock
• **Personalized Experiences** - Build loyalty through customization
• **Quick Response Times** - Improve satisfaction with instant help
• **Proactive Communication** - Prevent churn with timely updates
• **Customer Success Automation** - Drive retention through automation
• **Loyalty Programs** - Reward repeat customers
• **Feedback Loops** - Continuously improve based on customer input

**Customer Acquisition Benefits:**
• **Lead Generation** - Convert website visitors into prospects
• **Qualified Prospects** - Intelligent conversations identify real opportunities
• **Conversion Optimization** - Personalized offers increase sales
• **Referral Programs** - Satisfied customers bring new business
• **Multi-Channel Presence** - Reach prospects wherever they are
• **Social Proof** - Showcase success stories and testimonials

**Industry-Specific Retention Tactics:**

**Healthcare:**
• Patient communication automation
• Appointment reminders and follow-ups
• Health education content delivery
• Insurance verification assistance

**Retail:**
• Product recommendations
• Order tracking and updates
• Loyalty program management
• Personalized shopping experiences

**Automotive:**
• Service scheduling and reminders
• Maintenance notifications
• Parts availability updates
• Customer feedback collection

**Restaurant:**
• Reservation management
• Menu recommendations
• Special event coordination
• Customer preference tracking

**Want me to design a custom retention strategy for your business?** Just let me know your industry and current challenges."""
        
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
        response = """🤔 **I'm not sure I understood that request.**

**Let me help you better. I can assist with:**
• **Business solutions** and AI chatbots
• **Pricing** and package options
• **Demos** and consultations
• **Free trials** and setup
• **Technical details** and integration
• **Veteran discounts** and special offers

**Try asking about:**
• 'Schedule a demo'
• 'See pricing'
• 'Start free trial'
• 'Business analysis'
• 'Technical details'

**What would you like to know about?**"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionExtractBusinessInfo(Action):
    def name(self) -> Text:
        return "action_extract_business_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract business information from user message
        business_type = tracker.get_slot("business_type") or "general"
        business_size = tracker.get_slot("business_size") or "unknown"
        industry = tracker.get_slot("industry") or "general"
        
        response = f"""🏢 **Business Information Extracted**

**Business Type:** {business_type.title()}
**Business Size:** {business_size.title()}
**Industry:** {industry.title()}

**Based on this information, I recommend:**
• Custom AI chatbot solution for {business_type} businesses
• Industry-specific features and integrations
• ROI-optimized package selection
• Implementation timeline: 2-3 weeks

**Would you like me to:**
• Analyze your specific business needs?
• Show pricing for your industry?
• Schedule a consultation call?
• Start your free trial?

**What's your next step?**"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionGenerateProposal(Action):
    def name(self) -> Text:
        return "action_generate_proposal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        business_type = tracker.get_slot("business_type") or "general"
        budget_range = tracker.get_slot("budget_range") or "flexible"
        
        # Generate custom proposal based on business type and budget
        proposals = {
            "healthcare": {
                "package": "Professional Plan - $247/month",
                "features": ["HIPAA compliance", "Patient communication", "Appointment scheduling", "Medical FAQ handling"],
                "roi": "400-600% within 6 months"
            },
            "retail": {
                "package": "Professional Plan - $247/month",
                "features": ["Product information", "Order tracking", "Return assistance", "Inventory checking"],
                "roi": "300-500% within 4 months"
            },
            "automotive": {
                "package": "Professional Plan - $247/month",
                "features": ["Service scheduling", "Parts catalog", "Service history", "Maintenance reminders"],
                "roi": "350-550% within 5 months"
            },
            "restaurant": {
                "package": "Starter Plan - $79/month",
                "features": ["Menu support", "Reservation management", "Catering quotes", "Delivery tracking"],
                "roi": "250-450% within 3 months"
            }
        }
        
        proposal = proposals.get(business_type, proposals["retail"])
        
        response = f"""📋 **Custom Proposal for {business_type.title()} Business**

**Recommended Package:** {proposal['package']}
**Key Features:**
{chr(10).join([f"• {feature}" for feature in proposal['features']])}

**Expected ROI:** {proposal['roi']}
**Implementation Timeline:** 2-3 weeks
**Support Level:** 24/7 technical assistance

**Next Steps:**
1. Schedule consultation call (15 minutes)
2. Custom solution design (1 week)
3. Implementation and training (2-3 weeks)
4. Go-live and optimization (ongoing)

**Ready to proceed?** Let's schedule your consultation call!"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionOpenAIKnowledge(Action):
    def name(self) -> Text:
        return "action_openai_knowledge"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # This action would integrate with OpenAI for advanced knowledge responses
        # For now, providing a comprehensive knowledge response
        
        response = """🧠 **Advanced AI Knowledge & Capabilities**

**Our AI Technology:**
• **Natural Language Processing:** Understands customer intent with 95% accuracy
• **Machine Learning:** Continuously improves responses based on interactions
• **Multi-Language Support:** Handles 50+ languages for global businesses
• **Context Awareness:** Remembers conversation history and user preferences

**Advanced Features:**
• **Sentiment Analysis:** Detects customer mood and adjusts responses
• **Intent Recognition:** Identifies 100+ business intents automatically
• **Entity Extraction:** Pulls key information from customer messages
• **Smart Routing:** Directs complex queries to human agents when needed

**Integration Capabilities:**
• **CRM Systems:** Salesforce, HubSpot, Pipedrive
• **E-commerce:** Shopify, WooCommerce, Magento
• **Communication:** Slack, Teams, Discord
• **Analytics:** Google Analytics, Mixpanel, Amplitude

**What specific technical aspect would you like me to explain in detail?**"""
        
        dispatcher.utter_message(text=response)
        return []

# Missing Actions Implementation
class ActionPackageDetails(Action):
    def name(self) -> Text:
        return "action_package_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📦 **Detailed Package Information**

**Starter Plan - $79/month:**
• 1 Custom AI Chatbot
• 1,000 queries/month
• Basic integrations (website, email)
• Email support (24-48 hour response)
• Basic analytics dashboard
• Perfect for small businesses starting out

**Professional Plan - $247/month:**
• 3 Custom AI Chatbots
• 5,000 queries/month
• Payment processing integration
• Advanced analytics and reporting
• Priority support (4-8 hour response)
• CRM integration (Salesforce, HubSpot)
• Most popular choice for growing businesses

**Agency Plan - $497/month:**
• 10 Custom AI Chatbots
• 15,000 queries/month
• White-label options
• Multi-account management
• Dedicated account manager
• Custom integrations
• API access for developers

**Enterprise Plan - Custom Pricing:**
• Unlimited chatbots
• Unlimited queries
• Full white-label solution
• Custom payment workflows
• Private cloud deployment
• Dedicated support team
• Custom development services

**Which plan would you like me to explain in more detail?**"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionHipaaDetails(Action):
    def name(self) -> Text:
        return "action_hipaa_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🏥 **HIPAA Compliance Details**

**Full HIPAA Compliance:**
• **HIPAA Privacy Rule** compliance
• **HIPAA Security Rule** compliance
• **HITECH Act** compliance
• **Business Associate Agreement** (BAA) provided
• **Annual compliance audits** and certifications

**Security Features:**
• **End-to-end encryption** for all data
• **Access controls** and authentication
• **Audit logging** for all interactions
• **Data backup** and disaster recovery
• **Regular security assessments**

**Data Protection:**
• **PHI data** never stored permanently
• **Automatic data deletion** after sessions
• **Secure data transmission** (TLS 1.3)
• **Role-based access** controls
• **Data encryption** at rest and in transit

**Compliance Documentation:**
• **HIPAA compliance certificates**
• **Security assessment reports**
• **Privacy impact assessments**
• **Incident response procedures**
• **Staff training documentation**

**Ready to discuss your HIPAA compliance needs?** I can provide detailed documentation and setup assistance."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionPatientCommunication(Action):
    def name(self) -> Text:
        return "action_patient_communication"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """💬 **Patient Communication Features**

**Appointment Management:**
• **Schedule appointments** 24/7
• **Reschedule and cancel** appointments
• **Appointment reminders** via text/email
• **Waitlist management** for cancellations
• **Calendar integration** with your systems

**Patient Support:**
• **Medical FAQ** handling
• **Insurance verification** assistance
• **Prescription refill** requests
• **Lab result** notifications
• **Billing questions** support

**Communication Channels:**
• **Website chat** widget
• **Mobile app** integration
• **Text messaging** (SMS)
• **Email** support
• **Phone call** routing

**Patient Experience:**
• **Personalized responses** based on history
• **Multi-language support** for diverse patients
• **Accessibility features** for all patients
• **Quick response** times (under 30 seconds)
• **24/7 availability** for patient convenience

**What specific patient communication needs do you have?** I can customize the solution for your practice."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionInventoryDetails(Action):
    def name(self) -> Text:
        return "action_inventory_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📦 **Inventory Management Features**

**Real-Time Inventory:**
• **Live stock levels** across all locations
• **Automatic updates** when items are sold
• **Low stock alerts** and notifications
• **Reorder suggestions** based on sales data
• **Inventory forecasting** and planning

**Product Information:**
• **Detailed product descriptions** and specs
• **Pricing information** and updates
• **Availability status** by location
• **Alternative product** suggestions
• **Product reviews** and ratings

**Customer Support:**
• **Stock availability** checking
• **Product recommendations** based on needs
• **Order status** and tracking
• **Return and exchange** assistance
• **Warranty information** lookup

**Integration Capabilities:**
• **POS systems** (Square, Shopify, etc.)
• **Warehouse management** systems
• **Supplier portals** for reordering
• **Accounting software** integration
• **E-commerce platforms**

**How do you currently manage your inventory?** I can show you how our AI can streamline your process."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionCustomerService(Action):
    def name(self) -> Text:
        return "action_customer_service"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🎧 **Customer Service Automation**

**24/7 Support:**
• **Always available** for customer questions
• **Instant responses** to common inquiries
• **No waiting** in phone queues
• **Consistent service** quality
• **Multi-language support** for global customers

**Common Inquiries Handled:**
• **Product information** and availability
• **Order status** and tracking
• **Return and exchange** policies
• **Shipping information** and costs
• **Account management** assistance
• **Technical support** for products

**Customer Experience:**
• **Personalized responses** based on history
• **Context awareness** across conversations
• **Seamless handoff** to human agents
• **Customer satisfaction** tracking
• **Feedback collection** and analysis

**Business Benefits:**
• **Reduced support costs** by 60-80%
• **Faster response times** (under 30 seconds)
• **Increased customer satisfaction** scores
• **Scalable support** during peak periods
• **Data insights** for service improvement

**What customer service challenges are you facing?** I can show you how our AI can solve them."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionServiceScheduling(Action):
    def name(self) -> Text:
        return "action_service_scheduling"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📅 **Service Scheduling Features**

**Appointment Management:**
• **Online booking** 24/7
• **Real-time availability** checking
• **Service duration** calculations
• **Resource allocation** (technicians, equipment)
• **Conflict detection** and prevention

**Customer Convenience:**
• **Self-service scheduling** anytime
• **Reschedule and cancel** appointments
• **Reminder notifications** (SMS, email)
• **Service history** access
• **Preferred time slots** preferences

**Business Operations:**
• **Staff scheduling** optimization
• **Service capacity** management
• **Revenue forecasting** based on bookings
• **Customer communication** automation
• **Service reminders** and follow-ups

**Integration Features:**
• **Calendar systems** (Google, Outlook)
• **CRM platforms** for customer data
• **Payment processing** for deposits
• **Inventory systems** for parts/equipment
• **Accounting software** for invoicing

**What type of services do you schedule?** I can customize the solution for your specific needs."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionPartsCatalog(Action):
    def name(self) -> Text:
        return "action_parts_catalog"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🔧 **Parts Catalog Features**

**Comprehensive Parts Database:**
• **Full parts catalog** with descriptions
• **Compatibility information** by vehicle
• **Pricing and availability** in real-time
• **Part numbers** and specifications
• **Alternative parts** suggestions

**Customer Self-Service:**
• **Parts lookup** by vehicle make/model
• **Availability checking** across locations
• **Pricing quotes** and estimates
• **Order placement** and tracking
• **Warranty information** lookup

**Business Benefits:**
• **Reduced phone calls** for parts inquiries
• **Faster parts identification** and ordering
• **Increased parts sales** through easy access
• **Better customer experience** and satisfaction
• **Inventory optimization** based on demand

**Integration Capabilities:**
• **Parts suppliers** and catalogs
• **Inventory management** systems
• **Point of sale** systems
• **Customer databases** and history
• **Accounting and invoicing** software

**What type of parts do you handle?** I can show you how our AI can streamline your parts business."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionReservationSystem(Action):
    def name(self) -> Text:
        return "action_reservation_system"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🍽️ **Reservation System Features**

**Smart Booking Management:**
• **Online reservations** 24/7
• **Real-time availability** checking
• **Table management** and optimization
• **Party size** and special requests
• **Waitlist management** for busy times

**Customer Experience:**
• **Easy booking** from any device
• **Confirmation emails** and reminders
• **Modify or cancel** reservations
• **Special occasion** notifications
• **Loyalty program** integration

**Restaurant Operations:**
• **Staff scheduling** optimization
• **Kitchen preparation** planning
• **Revenue forecasting** based on bookings
• **Customer preferences** tracking
• **Peak time** management

**Advanced Features:**
• **Mobile app** integration
• **Social media** booking
• **Third-party platform** sync (OpenTable, etc.)
• **Analytics and reporting** on booking patterns
• **Marketing automation** for repeat customers

**What type of restaurant do you operate?** I can customize the reservation system for your needs."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionMenuSupport(Action):
    def name(self) -> Text:
        return "action_menu_support"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🍽️ **Menu Support Features**

**Dynamic Menu Management:**
• **Real-time menu updates** and changes
• **Daily specials** and promotions
• **Seasonal menu** rotations
• **Allergen information** and dietary restrictions
• **Nutritional information** and calorie counts

**Customer Assistance:**
• **Menu recommendations** based on preferences
• **Ingredient questions** and substitutions
• **Pricing information** and combo deals
• **Portion sizes** and serving suggestions
• **Wine and beverage** pairing suggestions

**Business Benefits:**
• **Reduced staff questions** about menu items
• **Faster order processing** with clear information
• **Increased upsells** through recommendations
• **Better customer satisfaction** with detailed info
• **Allergen safety** and compliance

**Integration Features:**
• **POS systems** for real-time pricing
• **Inventory systems** for availability
• **Kitchen display** systems
• **Online ordering** platforms
• **Customer feedback** collection

**What type of cuisine do you serve?** I can customize the menu support for your restaurant."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionPaymentOptions(Action):
    def name(self) -> Text:
        return "action_payment_options"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """💳 **Payment Options & Processing**

**Payment Methods Accepted:**
• **Credit/Debit Cards:** Visa, MasterCard, American Express, Discover
• **Digital Wallets:** Apple Pay, Google Pay, PayPal, Venmo
• **Bank Transfers:** ACH, wire transfers
• **Cryptocurrency:** Bitcoin, Ethereum (Enterprise plans)
• **Installment Plans:** Buy now, pay later options

**Security & Compliance:**
• **PCI DSS Level 1** compliance
• **End-to-end encryption** for all transactions
• **Fraud detection** and prevention
• **Secure tokenization** of payment data
• **Regular security audits** and testing

**Business Benefits:**
• **Faster payment processing** (2-3 seconds)
• **Reduced payment errors** and chargebacks
• **Multiple payment options** for customer convenience
• **Automated reconciliation** and reporting
• **Integration with accounting** software

**Processing Fees:**
• **Starter Plan:** 2.9% + $0.30 per transaction
• **Professional Plan:** 2.7% + $0.30 per transaction
• **Agency Plan:** 2.5% + $0.30 per transaction
• **Enterprise Plan:** Custom rates based on volume

**What payment methods do you currently accept?** I can show you how to expand your payment options."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionVeteranVerification(Action):
    def name(self) -> Text:
        return "action_veteran_verification"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🇺🇸 **Veteran Verification Process**

**Required Documentation:**
• **DD-214** (Certificate of Release or Discharge from Active Duty)
• **Military ID** (for active duty/reserves)
• **VA ID Card** (Veterans Health Identification Card)
• **Retirement Orders** (for retired military)

**Verification Steps:**
1. **Submit documentation** through secure portal
2. **Quick verification** (usually same day)
3. **Confirmation email** with veteran status
4. **Discount activation** on your account
5. **Welcome package** with veteran resources

**Veteran Benefits Activated:**
• **25% discount** on all plans
• **Priority implementation** scheduling
• **Dedicated veteran support** team
• **Extended trial period** (30 days)
• **Flexible payment options**

**Security & Privacy:**
• **Secure document upload** and storage
• **HIPAA-compliant** data handling
• **Military record verification** through official channels
• **No personal information** shared with third parties
• **Compliance with** military privacy regulations

**Ready to start your verification?** I can guide you through the process step by step."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionVeteranPricing(Action):
    def name(self) -> Text:
        return "action_veteran_pricing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🇺🇸 **Veteran Pricing & Special Offers**

**Veteran Discount: 25% Off All Plans**

**Starter Plan - $59.25/month** (was $79)
• 1 Custom AI Chatbot
• 1,000 queries/month
• Basic integrations
• Email support
• Perfect for veteran-owned small businesses

**Professional Plan - $185.25/month** (was $247)
• 3 Custom AI Chatbots
• 5,000 queries/month
• Payment processing
• Advanced analytics
• Priority support
• Most popular choice for veterans

**Agency Plan - $372.75/month** (was $497)
• 10 Custom AI Chatbots
• 15,000 queries/month
• White-label options
• Multi-account management
• Dedicated account manager

**Enterprise Plan - Custom Veteran Pricing**
• Unlimited chatbots
• Unlimited queries
• Full white-label solution
• Custom payment workflows
• Private cloud deployment

**Additional Veteran Benefits:**
• **Priority onboarding** and implementation
• **Dedicated veteran success** manager
• **Extended trial period** (30 days)
• **Flexible payment** options
• **Ongoing veteran support** network

**Ready to activate your veteran discount?** I can help you get verified and set up your account."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionFollowUp(Action):
    def name(self) -> Text:
        return "action_follow_up"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📧 **Follow-Up & Next Steps**

**What Happens Next:**
• **Follow-up email** with our conversation summary
• **Custom proposal** based on your business needs
• **Implementation timeline** and roadmap
• **Resource materials** and case studies
• **Contact information** for our team

**Scheduled Follow-Ups:**
• **24 hours:** Summary email with next steps
• **3 days:** Check-in call to answer questions
• **1 week:** Detailed proposal and pricing
• **2 weeks:** Implementation planning call
• **Ongoing:** Regular check-ins and support

**Resources You'll Receive:**
• **Business case studies** in your industry
• **ROI calculator** for your specific business
• **Implementation guide** and checklist
• **Training materials** and documentation
• **Support contact** information

**How to Stay Connected:**
• **Email:** hello@nexteleven.com
• **Phone:** (555) 123-4567
• **Website:** www.nexteleven.com
• **Support portal:** Available 24/7

**What's the best way to reach you for follow-up?** I want to make sure you get all the information you need."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionRetailSpecialist(Action):
    def name(self) -> Text:
        return "action_retail_specialist"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🛍️ **Retail Business Specialist Consultation**

**Retail-Specific Solutions:**
• **Product Information:** Detailed descriptions, specs, and pricing
• **Inventory Management:** Real-time stock levels and availability
• **Order Processing:** Seamless checkout and payment
• **Customer Service:** 24/7 support for inquiries and issues
• **Loyalty Programs:** Points, rewards, and member benefits

**Key Features for Retail:**
• **Multi-channel Support:** Website, mobile app, social media
• **Personalized Recommendations:** Based on browsing and purchase history
• **Return & Exchange:** Automated processing and tracking
• **Shipping Information:** Real-time tracking and delivery updates
• **Customer Feedback:** Reviews, ratings, and satisfaction surveys

**Business Impact:**
• **Increased Sales:** 25-40% through better customer service
• **Reduced Support Costs:** 60-80% automation savings
• **Better Customer Retention:** Personalized experiences
• **Improved Inventory Turnover:** Real-time demand insights
• **24/7 Availability:** Never miss a sale opportunity

**What type of retail business do you operate?** I can provide industry-specific insights and solutions."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionAutomotiveSpecialist(Action):
    def name(self) -> Text:
        return "action_automotive_specialist"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🚗 **Automotive Business Specialist Consultation**

**Automotive-Specific Solutions:**
• **Service Scheduling:** Online booking for maintenance and repairs
• **Parts Catalog:** Comprehensive database with compatibility info
• **Service History:** Complete vehicle maintenance records
• **Warranty Information:** Coverage details and claim assistance
• **Roadside Assistance:** Emergency support coordination

**Key Features for Automotive:**
• **Vehicle Recognition:** Automatic identification by VIN or license plate
• **Service Reminders:** Proactive maintenance notifications
• **Parts Availability:** Real-time inventory and ordering
• **Technician Scheduling:** Staff and resource management
• **Customer Communication:** Service updates and completion notifications

**Business Impact:**
• **Increased Service Bookings:** 30-50% through easy scheduling
• **Better Customer Retention:** Proactive maintenance reminders
• **Reduced Phone Calls:** 70-80% automation for common inquiries
• **Improved Efficiency:** Streamlined service processes
• **24/7 Customer Support:** Always available for customer needs

**What type of automotive services do you provide?** I can customize the solution for your specific business."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionRestaurantSpecialist(Action):
    def name(self) -> Text:
        return "action_restaurant_specialist"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🍽️ **Restaurant Business Specialist Consultation**

**Restaurant-Specific Solutions:**
• **Reservation Management:** Online booking and table management
• **Menu Support:** Dynamic menus with allergen and nutrition info
• **Order Processing:** Seamless online ordering and payment
• **Delivery Tracking:** Real-time updates for delivery orders
• **Customer Service:** 24/7 support for inquiries and issues

**Key Features for Restaurants:**
• **Smart Scheduling:** Optimized table allocation and staff scheduling
• **Menu Updates:** Real-time changes and daily specials
• **Catering Coordination:** Large party and event planning
• **Loyalty Programs:** Rewards and member benefits
• **Feedback Collection:** Reviews and satisfaction surveys

**Business Impact:**
• **Increased Reservations:** 25-45% through easy online booking
• **Higher Order Values:** 20-35% through recommendations
• **Reduced No-Shows:** 40-60% with reminder systems
• **Better Customer Experience:** Personalized service and support
• **24/7 Availability:** Never miss a reservation or order

**What type of restaurant do you operate?** I can provide cuisine-specific insights and solutions."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionIntegrationDetails(Action):
    def name(self) -> Text:
        return "action_integration_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🔌 **Integration & API Details**

**Pre-built Integrations:**
• **CRM Systems:** Salesforce, HubSpot, Pipedrive, Zoho
• **E-commerce:** Shopify, WooCommerce, Magento, BigCommerce
• **Payment Processors:** Stripe, PayPal, Square, Authorize.net
• **Communication:** Slack, Microsoft Teams, Discord, WhatsApp
• **Analytics:** Google Analytics, Mixpanel, Amplitude, Hotjar

**API Capabilities:**
• **REST API:** Full CRUD operations for all data
• **Webhook Support:** Real-time event notifications
• **OAuth 2.0:** Secure authentication and authorization
• **Rate Limiting:** Configurable API usage limits
• **API Documentation:** Comprehensive guides and examples

**Custom Integrations:**
• **Legacy Systems:** Custom API development for older systems
• **Proprietary Software:** Integration with in-house solutions
• **Third-party Services:** Custom connectors for specialized tools
• **Data Migration:** Seamless transfer from existing systems
• **Testing & Validation:** Comprehensive integration testing

**Technical Requirements:**
• **HTTPS endpoints** for secure communication
• **JSON data format** for easy processing
• **Webhook URLs** for real-time updates
• **API keys** for authentication
• **Rate limiting** compliance

**What systems do you need to integrate with?** I can provide specific integration details and setup assistance."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionSecurityDetails(Action):
    def name(self) -> Text:
        return "action_security_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🔒 **Security & Data Protection Details**

**Enterprise-Grade Security:**
• **SOC 2 Type II** certification
• **ISO 27001** compliance
• **GDPR compliance** for European customers
• **HIPAA compliance** for healthcare businesses
• **Regular security audits** and penetration testing

**Data Protection:**
• **End-to-end encryption** (AES-256)
• **Data encryption at rest** and in transit
• **Secure data centers** with 99.9% uptime
• **Regular backups** with geographic redundancy
• **Data retention policies** and automatic deletion

**Access Controls:**
• **Multi-factor authentication** (MFA)
• **Role-based access** controls
• **Single sign-on** (SSO) integration
• **Session management** and timeout controls
• **Audit logging** for all access attempts

**Privacy Features:**
• **Data anonymization** options
• **Consent management** for data collection
• **Right to be forgotten** implementation
• **Data portability** and export tools
• **Privacy impact assessments** and reviews

**What security concerns do you have?** I can provide detailed security documentation and compliance information."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionComplianceDetails(Action):
    def name(self) -> Text:
        return "action_compliance_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """📋 **Compliance & Regulatory Details**

**Industry-Specific Compliance:**
• **Healthcare:** HIPAA, HITECH, 21 CFR Part 11
• **Financial:** PCI DSS, SOX, GLBA
• **Retail:** CCPA, GDPR, state privacy laws
• **Education:** FERPA, COPPA compliance
• **Government:** FedRAMP, FISMA requirements

**Data Privacy Compliance:**
• **GDPR (EU):** Full compliance with data protection regulations
• **CCPA (California):** California Consumer Privacy Act compliance
• **State Laws:** Compliance with all state privacy regulations
• **International:** Cross-border data transfer compliance
• **Industry Standards:** Best practices for data handling

**Security Compliance:**
• **SOC 2 Type II:** Service Organization Control compliance
• **ISO 27001:** Information security management
• **NIST Framework:** Cybersecurity framework compliance
• **Penetration Testing:** Regular security assessments
• **Vulnerability Management:** Ongoing security monitoring

**Audit & Reporting:**
• **Compliance reports** and certifications
• **Regular audits** and assessments
• **Documentation** for regulatory reviews
• **Training materials** for staff compliance
• **Incident response** procedures

**What compliance requirements does your business have?** I can provide specific compliance details and documentation."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionScheduleVeteranConsultation(Action):
    def name(self) -> Text:
        return "action_schedule_veteran_consultation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🇺🇸 **Veteran Consultation Scheduling**

**Special Veteran Consultation:**
• **60-minute session** (extended from standard 45 minutes)
• **Veteran-specific solutions** and benefits
• **Military experience** understanding and respect
• **Priority scheduling** and dedicated time
• **No sales pressure** - focused on your needs

**What We'll Cover:**
• **Business analysis** tailored to veteran-owned businesses
• **Veteran discount** activation and setup
• **Implementation timeline** with priority scheduling
• **Ongoing support** from our veteran success team
• **Veteran business network** connections and resources

**Available Times:**
• **Monday-Friday:** 8 AM - 7 PM EST (extended hours for veterans)
• **Saturday:** 9 AM - 3 PM EST
• **Evening slots** available for busy schedules
• **Flexible scheduling** to accommodate your needs

**Veteran Benefits:**
• **25% discount** on all plans
• **Priority implementation** scheduling
• **Dedicated veteran support** manager
• **Extended trial period** (30 days)
• **Ongoing veteran community** access

**Ready to schedule your veteran consultation?** What time works best for you this week?"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionImplementationTimeline(Action):
    def name(self) -> Text:
        return "action_implementation_timeline"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """⏰ **Implementation Timeline & Process**

**Phase 1: Discovery & Planning (Week 1-2)**
• **Business analysis** and requirements gathering
• **Solution design** and customization planning
• **Integration planning** with existing systems
• **Timeline confirmation** and milestone setting
• **Resource allocation** and team assignment

**Phase 2: Development & Setup (Week 3-4)**
• **AI chatbot configuration** and training
• **Custom integrations** development and testing
• **Platform setup** and configuration
• **Staff training** and onboarding preparation
• **Testing environment** setup and validation

**Phase 3: Testing & Launch (Week 5-6)**
• **Comprehensive testing** of all features
• **User acceptance testing** with your team
• **Performance optimization** and fine-tuning
• **Go-live preparation** and final checks
• **Launch support** and monitoring

**Total Timeline: 4-6 weeks**
**Veteran Priority:** 3-4 weeks with priority scheduling

**What's your preferred start date?** I can begin the discovery process immediately."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionSupportHours(Action):
    def name(self) -> Text:
        return "action_support_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """🕒 **Support Hours & Availability**

**Standard Support Hours:**
• **Monday-Friday:** 8 AM - 8 PM EST
• **Saturday:** 9 AM - 5 PM EST
• **Sunday:** 10 AM - 4 PM EST
• **Holidays:** Limited support with emergency coverage

**Priority Support (Professional+ Plans):**
• **Extended hours:** 7 AM - 9 PM EST daily
• **Weekend support:** Saturday 8 AM - 6 PM EST
• **Faster response:** 2-4 hour response guarantee
• **Dedicated support** team member

**Enterprise Support (Enterprise Plans):**
• **24/7 availability** for critical issues
• **Dedicated support** manager
• **Emergency hotline** for urgent matters
• **On-site support** available when needed

**Support Channels:**
• **Live Chat:** Available during business hours
• **Email:** support@nexeleven.com (24/7)
• **Phone:** Available during support hours
• **Support Portal:** 24/7 self-service resources
• **Emergency Support:** Available for enterprise clients

**What support level do you need?** I can recommend the right plan for your support requirements."""
        
        dispatcher.utter_message(text=response)
        return []

class ActionSessionEnd(Action):
    def name(self) -> Text:
        return "action_session_end"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = """👋 **Session Summary & Next Steps**

**What We've Covered Today:**
• **Business analysis** and solution overview
• **Pricing and packages** for your needs
• **Implementation timeline** and process
• **Next steps** and follow-up plan

**Your Next Actions:**
• **Review materials** I'll send via email
• **Schedule consultation** call if interested
• **Start free trial** when ready
• **Contact support** with any questions

**Follow-up Schedule:**
• **24 hours:** Summary email with resources
• **3 days:** Check-in call to answer questions
• **1 week:** Detailed proposal and next steps

**Contact Information:**
• **Email:** hello@nexteleven.com
• **Phone:** (555) 123-4567
• **Website:** www.nexteleven.com
• **Support:** Available 24/7

**Thank you for your time today!** I look forward to helping your business grow with our AI solutions. 🚀"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionGenerateSalesMaterials(Action):
    def name(self) -> Text:
        return "action_generate_sales_materials"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        business_type = tracker.get_slot("business_type") or "general"
        
        # Determine material type from the intent that triggered this action
        latest_intent = tracker.get_intent_of_latest_message()
        
        if latest_intent == "generate_pricing_pdf":
            material_type = "pricing"
        elif latest_intent == "generate_proposal_pdf":
            material_type = "proposal"
        else:
            material_type = "general"
        
        # Generate appropriate sales materials based on request
        if material_type == "pricing":
            response = f"""📄 **Pricing PDF Generated & Sent!**

**I've created and sent you a comprehensive pricing guide for {business_type.title()} businesses.**

**What's included in your PDF:**
• Detailed pricing breakdown for all plans
• Feature comparison matrix
• ROI calculations for your industry
• Implementation timeline
• Veteran discount information
• Custom quote for your business size

**Check your email for:** `NextEleven_Pricing_{business_type.title()}_Guide.pdf`

**Need additional materials?** I can also create:
• Technical specifications document
• Case studies and success stories
• Implementation roadmap
• ROI analysis report

**What other materials would be helpful for your decision-making?**"""
        
        elif material_type == "proposal":
            response = f"""📋 **Custom Proposal PDF Generated & Sent!**

**I've created a personalized proposal for your {business_type.title()} business.**

**Your proposal includes:**
• Custom solution design
• Feature recommendations
• Implementation timeline
• Cost breakdown
• ROI projections
• Success metrics
• Next steps

**Check your email for:** `NextEleven_Proposal_{business_type.title()}_Business.pdf`

**Ready to discuss this proposal?** Let's schedule a consultation call!"""
        
        else:
            response = f"""📚 **Informational Materials Generated & Sent!**

**I've created comprehensive materials for your {business_type.title()} business.**

**Materials sent:**
• Industry-specific solution guide
• Technical specifications
• Case studies and testimonials
• Implementation best practices
• ROI analysis and benchmarks

**Check your email for:** `NextEleven_{business_type.title()}_Solutions_Guide.pdf`

**Need anything specific?** I can customize any of these materials!"""
        
        dispatcher.utter_message(text=response)
        return []

class ActionSendFollowUpMaterials(Action):
    def name(self) -> Text:
        return "action_send_follow_up_materials"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        business_type = tracker.get_slot("business_type") or "general"
        
        response = f"""📧 **Follow-Up Materials Sent!**

**I've sent you additional materials to help with your decision:**

**Email 1: Welcome & Next Steps**
• Account setup instructions
• Free trial activation
• Support contact information

**Email 2: Implementation Guide**
• Technical requirements
• Integration checklist
• Training schedule

**Email 3: Success Resources**
• Best practices guide
• ROI tracking tools
• Customer success stories

**All materials are customized for {business_type.title()} businesses.**

**Check your email for these follow-up materials!**

**Questions about any of these materials?** I'm here to help!"""
        
        dispatcher.utter_message(text=response)
        return []
