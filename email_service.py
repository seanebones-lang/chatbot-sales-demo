#!/usr/bin/env python3
"""
Email Service for NextEleven Lead Capture System
Sends lead information to nexteleven@icloud.com
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import json
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        # Email configuration - you'll need to set these environment variables
        self.sender_email = os.getenv('SENDER_EMAIL', 'your-email@gmail.com')
        self.sender_password = os.getenv('SENDER_PASSWORD', 'your-app-password')
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.recipient_email = 'nexteleven@icloud.com'
        
    def send_lead_email(self, lead_data):
        """Send lead information to nexteleven@icloud.com"""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = f"🎯 New Lead: {lead_data.get('name', 'Unknown')} - {lead_data.get('interest', 'General')}"
            
            # Create email body
            body = self._create_lead_email_body(lead_data)
            msg.attach(MIMEText(body, 'html'))
            
            # Send email
            self._send_email(msg)
            
            logger.info(f"✅ Lead email sent successfully for {lead_data.get('name', 'Unknown')}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to send lead email: {str(e)}")
            return False
    
    def _create_lead_email_body(self, lead_data):
        """Create HTML email body with lead information"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .header {{ background: linear-gradient(135deg, #1E90FF, #00CED1); color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; }}
                .lead-info {{ background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 15px 0; }}
                .field {{ margin: 10px 0; }}
                .label {{ font-weight: bold; color: #1E90FF; }}
                .value {{ color: #333; }}
                .footer {{ background: #f8f9fa; padding: 15px; text-align: center; color: #666; font-size: 12px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🎯 New Lead Captured!</h1>
                <p>NextEleven AI Chatbot Solutions</p>
            </div>
            
            <div class="content">
                <h2>Lead Information</h2>
                <div class="lead-info">
                    <div class="field">
                        <span class="label">Name:</span>
                        <span class="value">{lead_data.get('name', 'Not provided')}</span>
                    </div>
                    <div class="field">
                        <span class="label">Email:</span>
                        <span class="value">{lead_data.get('email', 'Not provided')}</span>
                    </div>
                    <div class="field">
                        <span class="label">Industry:</span>
                        <span class="value">{lead_data.get('business', 'Not specified')}</span>
                    </div>
                    <div class="field">
                        <span class="label">Primary Interest:</span>
                        <span class="value">{lead_data.get('interest', 'Not specified')}</span>
                    </div>
                    <div class="field">
                        <span class="label">Additional Details:</span>
                        <span class="value">{lead_data.get('message', 'None provided')}</span>
                    </div>
                    <div class="field">
                        <span class="label">Timestamp:</span>
                        <span class="value">{timestamp}</span>
                    </div>
                    <div class="field">
                        <span class="label">Source:</span>
                        <span class="value">{lead_data.get('source', 'Landing Page')}</span>
                    </div>
                </div>
                
                <h3>Next Steps</h3>
                <ul>
                    <li>Review lead information</li>
                    <li>Send personalized follow-up email</li>
                    <li>Schedule consultation call if appropriate</li>
                    <li>Add to CRM system</li>
                </ul>
            </div>
            
            <div class="footer">
                <p>This email was automatically generated by the NextEleven Lead Capture System</p>
                <p>Timestamp: {timestamp}</p>
            </div>
        </body>
        </html>
        """
        
        return html_body
    
    def _send_email(self, msg):
        """Send email using SMTP"""
        try:
            # Create secure SSL context
            context = ssl.create_default_context()
            
            # Connect to SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender_email, self.sender_password)
                
                # Send email
                text = msg.as_string()
                server.sendmail(self.sender_email, self.recipient_email, text)
                
        except Exception as e:
            logger.error(f"SMTP error: {str(e)}")
            raise

def main():
    """Test the email service"""
    email_service = EmailService()
    
    # Test lead data
    test_lead = {
        'name': 'Test User',
        'email': 'test@example.com',
        'business': 'Healthcare',
        'interest': 'Customer Service Bot',
        'message': 'Looking for HIPAA-compliant chatbot solution',
        'source': 'Test Form',
        'timestamp': datetime.now().isoformat()
    }
    
    print("🧪 Testing email service...")
    success = email_service.send_lead_email(test_lead)
    
    if success:
        print("✅ Test email sent successfully!")
    else:
        print("❌ Test email failed!")

if __name__ == "__main__":
    main()
