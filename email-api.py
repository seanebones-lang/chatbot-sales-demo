#!/usr/bin/env python3
"""
Flask API for NextEleven Email Service
Handles lead capture form submissions and sends emails to nexteleven@icloud.com
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import logging
from email_service import EmailService
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize email service
email_service = EmailService()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'NextEleven Email API',
        'timestamp': datetime.now().isoformat(),
        'recipient': email_service.recipient_email
    })

@app.route('/api/send-lead', methods=['POST'])
def send_lead():
    """Send lead information via email"""
    try:
        # Get lead data from request
        lead_data = request.json
        
        if not lead_data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'interest']
        for field in required_fields:
            if not lead_data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Add metadata
        lead_data['timestamp'] = datetime.now().isoformat()
        lead_data['source'] = lead_data.get('source', 'Landing Page Form')
        
        # Log the lead
        logger.info(f"📧 Processing lead from {lead_data['name']} ({lead_data['email']})")
        
        # Send email
        success = email_service.send_lead_email(lead_data)
        
        if success:
            logger.info(f"✅ Lead email sent successfully for {lead_data['name']}")
            return jsonify({
                'success': True,
                'message': 'Lead information sent successfully',
                'lead_id': f"LEAD_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                'timestamp': lead_data['timestamp']
            }), 200
        else:
            logger.error(f"❌ Failed to send lead email for {lead_data['name']}")
            return jsonify({
                'success': False,
                'error': 'Failed to send email'
            }), 500
            
    except Exception as e:
        logger.error(f"❌ Error processing lead: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

@app.route('/api/test-email', methods=['POST'])
def test_email():
    """Test email functionality"""
    try:
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'business': 'Test Industry',
            'interest': 'Test Interest',
            'message': 'This is a test email from the NextEleven system',
            'source': 'API Test',
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info("🧪 Testing email functionality...")
        success = email_service.send_lead_email(test_data)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Test email sent successfully',
                'recipient': email_service.recipient_email
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Test email failed'
            }), 500
            
    except Exception as e:
        logger.error(f"❌ Test email error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 5001))
    
    print(f"🚀 Starting NextEleven Email API on port {port}")
    print(f"📧 Emails will be sent to: {email_service.recipient_email}")
    print(f"🔧 Configure email settings with environment variables:")
    print(f"   - SENDER_EMAIL: Your Gmail address")
    print(f"   - SENDER_PASSWORD: Your Gmail app password")
    print(f"   - SMTP_SERVER: smtp.gmail.com (default)")
    print(f"   - SMTP_PORT: 587 (default)")
    
    app.run(host='0.0.0.0', port=port, debug=True)
