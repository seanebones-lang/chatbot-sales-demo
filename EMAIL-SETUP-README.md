# 📧 NextEleven Email Service Setup

This service automatically sends lead information from your website forms to **nexeleven@icloud.com**.

## 🚀 Quick Start

1. **Run the setup script:**
   ```bash
   ./setup-email.sh
   ```

2. **Configure your email credentials** (first time only)
3. **Start the service** (second time running the script)

## 🔧 Email Configuration

### Option 1: Gmail (Recommended for testing)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password:**
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
3. **Update `.env` file:**
   ```bash
   SENDER_EMAIL=your-email@gmail.com
   SENDER_PASSWORD=your-16-digit-app-password
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

### Option 2: iCloud Mail

```bash
SENDER_EMAIL=your-email@icloud.com
SENDER_PASSWORD=your-icloud-app-password
SMTP_SERVER=smtp.mail.me.com
SMTP_PORT=587
```

### Option 3: Outlook/Hotmail

```bash
SENDER_EMAIL=your-email@outlook.com
SENDER_PASSWORD=your-outlook-password
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

## 📁 Files Created

- `email-service.py` - Core email sending functionality
- `email-api.py` - Flask API server
- `email-requirements.txt` - Python dependencies
- `email.env.example` - Environment configuration template
- `setup-email.sh` - Automated setup script

## 🌐 API Endpoints

- **Health Check:** `GET /health`
- **Send Lead:** `POST /api/send-lead`
- **Test Email:** `POST /api/test-email`

## 🧪 Testing

1. **Start the service:**
   ```bash
   ./setup-email.sh
   ```

2. **Test the API:**
   ```bash
   curl -X POST http://localhost:5001/api/test-email
   ```

3. **Check health:**
   ```bash
   curl http://localhost:5001/health
   ```

## 📧 What Gets Sent

Every lead form submission sends an email to **nexeleven@icloud.com** with:

- **Lead Information:** Name, email, industry, interest
- **Additional Details:** Any specific needs mentioned
- **Timestamp:** When the lead was captured
- **Source:** Where the lead came from
- **Professional Formatting:** HTML email with NextEleven branding

## 🔒 Security Features

- **Environment Variables:** Credentials stored securely
- **Input Validation:** All form data validated before sending
- **Error Handling:** Comprehensive error logging and user feedback
- **CORS Protection:** API protected against unauthorized access

## 🚨 Troubleshooting

### Common Issues:

1. **"Authentication failed"**
   - Check your email/password in `.env`
   - For Gmail, ensure you're using an App Password

2. **"Connection refused"**
   - Check if port 5001 is available
   - Ensure firewall allows the connection

3. **"SMTP error"**
   - Verify SMTP server and port settings
   - Check if your email provider allows SMTP access

### Debug Mode:

The API runs in debug mode by default. Check the console for detailed error messages.

## 📱 Frontend Integration

The frontend automatically sends leads to `http://localhost:5001/api/send-lead` when the form is submitted.

## 🔄 Updating

To update the service:

1. Stop the current service (Ctrl+C)
2. Pull latest changes
3. Run `./setup-email.sh` again

## 📞 Support

If you encounter issues:

1. Check the console logs for error messages
2. Verify your email credentials in `.env`
3. Test the API endpoints manually
4. Ensure all dependencies are installed

---

**🎯 Goal:** Every lead from your website will now be automatically emailed to **nexeleven@icloud.com** with professional formatting and complete information!
