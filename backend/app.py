from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
import uuid

app = Flask(__name__)
CORS(app)

# In-memory storage (replace with database in production)
appointments = []
clients = {}

# Artist configuration
ARTIST_INFO = {
    "name": "Artist Name",
    "specialties": ["Traditional", "Neo-Traditional", "Black & Grey", "Color Realism"],
    "hourlyRate": "$150-200",
    "minDeposit": "$100",
    "contact": {
        "phone": "(555) 123-4567",
        "email": "artist@studio.com",
        "instagram": "@artisthandle"
    },
    "availability": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
}

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Tattoo Assistant Backend Running"})

@app.route('/api/artist-info', methods=['GET'])
def get_artist_info():
    return jsonify(ARTIST_INFO)

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    try:
        data = request.json
        
        # Generate unique appointment ID
        appointment_id = str(uuid.uuid4())
        
        # Create appointment object
        appointment = {
            "id": appointment_id,
            "clientName": data.get('clientName'),
            "clientPhone": data.get('clientPhone'),
            "serviceType": data.get('serviceType'),
            "preferredDate": data.get('preferredDate'),
            "designDescription": data.get('designDescription'),
            "status": "pending",
            "createdAt": datetime.now().isoformat(),
            "estimatedDuration": get_estimated_duration(data.get('serviceType')),
            "estimatedCost": get_estimated_cost(data.get('serviceType'))
        }
        
        # Store appointment
        appointments.append(appointment)
        
        # Store client info
        clients[data.get('clientPhone')] = {
            "name": data.get('clientName'),
            "phone": data.get('clientPhone'),
            "appointments": [appointment_id]
        }
        
        return jsonify({
            "success": True,
            "appointmentId": appointment_id,
            "message": "Appointment request created successfully! We'll contact you within 24 hours to confirm."
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    return jsonify(appointments)

@app.route('/api/availability/<date>', methods=['GET'])
def check_availability(date):
    try:
        # Parse date
        check_date = datetime.strptime(date, '%Y-%m-%d')
        day_name = check_date.strftime('%A')
        
        # Check if day is available
        is_available = day_name in ARTIST_INFO['availability']
        
        # Check existing appointments (simple logic)
        existing_appointments = [apt for apt in appointments if apt['preferredDate'] == date]
        slots_available = 3 - len(existing_appointments) if is_available else 0
        
        return jsonify({
            "date": date,
            "dayName": day_name,
            "isAvailable": is_available,
            "slotsAvailable": max(0, slots_available),
            "existingAppointments": len(existing_appointments)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/generate-portfolio-pdf', methods=['POST'])
def generate_portfolio_pdf():
    try:
        # Create PDF in memory
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.darkblue
        )
        story.append(Paragraph(f"{ARTIST_INFO['name']} - Portfolio", title_style))
        story.append(Spacer(1, 20))
        
        # Contact Info
        contact_style = ParagraphStyle(
            'Contact',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=20
        )
        story.append(Paragraph(f"Phone: {ARTIST_INFO['contact']['phone']}", contact_style))
        story.append(Paragraph(f"Email: {ARTIST_INFO['contact']['email']}", contact_style))
        story.append(Paragraph(f"Instagram: {ARTIST_INFO['contact']['instagram']}", contact_style))
        story.append(Spacer(1, 20))
        
        # Specialties
        story.append(Paragraph("Specialties:", styles['Heading2']))
        for specialty in ARTIST_INFO['specialties']:
            story.append(Paragraph(f"• {specialty}", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Pricing
        story.append(Paragraph("Pricing:", styles['Heading2']))
        story.append(Paragraph(f"Hourly Rate: {ARTIST_INFO['hourlyRate']}", styles['Normal']))
        story.append(Paragraph(f"Minimum Deposit: {ARTIST_INFO['minDeposit']}", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Availability
        story.append(Paragraph("Available Days:", styles['Heading2']))
        story.append(Paragraph(", ".join(ARTIST_INFO['availability']), styles['Normal']))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"{ARTIST_INFO['name']}_Portfolio.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-aftercare-pdf', methods=['POST'])
def generate_aftercare_pdf():
    try:
        # Create PDF in memory
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.darkred
        )
        story.append(Paragraph("Tattoo Aftercare Instructions", title_style))
        story.append(Spacer(1, 20))
        
        # First 24 Hours
        story.append(Paragraph("First 24 Hours:", styles['Heading2']))
        first_24 = [
            "Keep bandage on for 2-4 hours",
            "Gently wash with antibacterial soap and lukewarm water",
            "Pat dry with clean paper towel",
            "Apply thin layer of recommended ointment"
        ]
        for instruction in first_24:
            story.append(Paragraph(f"• {instruction}", styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Days 2-14
        story.append(Paragraph("Days 2-14:", styles['Heading2']))
        days_2_14 = [
            "Wash 2-3 times daily with mild soap",
            "Apply fragrance-free moisturizer when dry",
            "Do not pick, scratch, or rub the tattoo",
            "Avoid soaking in water (pools, baths, hot tubs)"
        ]
        for instruction in days_2_14:
            story.append(Paragraph(f"• {instruction}", styles['Normal']))
        story.append(Spacer(1, 15))
        
        # Ongoing Care
        story.append(Paragraph("Ongoing Care:", styles['Heading2']))
        ongoing = [
            "Use SPF 30+ sunscreen once healed",
            "Keep moisturized to prevent fading",
            f"Contact {ARTIST_INFO['name']} with any concerns"
        ]
        for instruction in ongoing:
            story.append(Paragraph(f"• {instruction}", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Contact Info
        story.append(Paragraph("Contact Information:", styles['Heading2']))
        story.append(Paragraph(f"Artist: {ARTIST_INFO['name']}", styles['Normal']))
        story.append(Paragraph(f"Phone: {ARTIST_INFO['contact']['phone']}", styles['Normal']))
        story.append(Paragraph(f"Email: {ARTIST_INFO['contact']['email']}", styles['Normal']))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name="Tattoo_Aftercare_Instructions.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/process-deposit', methods=['POST'])
def process_deposit():
    try:
        data = request.json
        
        # In a real app, you'd integrate with Stripe/PayPal here
        deposit = {
            "id": str(uuid.uuid4()),
            "amount": data.get('amount'),
            "paymentMethod": data.get('paymentMethod'),
            "clientPhone": data.get('clientPhone'),
            "status": "pending",
            "createdAt": datetime.now().isoformat()
        }
        
        # Simulate payment processing
        if deposit['amount'] and deposit['paymentMethod']:
            deposit['status'] = 'completed'
            deposit['processedAt'] = datetime.now().isoformat()
            
            return jsonify({
                "success": True,
                "depositId": deposit['id'],
                "message": f"Deposit of {deposit['amount']} processed successfully!",
                "status": "completed"
            })
        else:
            return jsonify({
                "success": False,
                "error": "Invalid deposit information"
            }), 400
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

def get_estimated_duration(service_type):
    durations = {
        "Consultation": "1 hour",
        "Small Tattoo (2-3 hrs)": "2-3 hours",
        "Medium Tattoo (4-6 hrs)": "4-6 hours",
        "Large Tattoo (Full Day)": "6-8 hours",
        "Touch-up": "1-2 hours"
    }
    return durations.get(service_type, "TBD")

def get_estimated_cost(service_type):
    costs = {
        "Consultation": "$50",
        "Small Tattoo (2-3 hrs)": "$300-450",
        "Medium Tattoo (4-6 hrs)": "$600-1200",
        "Large Tattoo (Full Day)": "$900-1600",
        "Touch-up": "$100-200"
    }
    return costs.get(service_type, "TBD")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
