# NextEleven Main Rasa Chatbot System

🚀 **Enterprise-Grade AI Chatbot for Business Consultation**

A sophisticated Rasa-based chatbot system designed specifically for NextEleven's business consultation services. This system provides intelligent, context-aware responses for enterprise AI solutions, pricing, demos, trials, and business analysis.

## ✨ Features

### **🤖 Advanced AI Capabilities**
- **Rasa NLU**: State-of-the-art natural language understanding
- **OpenAI Integration**: GPT-3.5-turbo for intelligent knowledge responses
- **Context Awareness**: Business-specific responses based on industry and company size
- **Multi-Intent Recognition**: 25+ business consultation intents

### **💼 Business Intelligence**
- **Industry-Specific Analysis**: Healthcare, retail, automotive, and general business
- **ROI Calculations**: Detailed return on investment analysis by business type
- **Package Recommendations**: Smart suggestions based on business context
- **Lead Qualification**: Automated business needs assessment

### **🎯 Specialized Intents**
- Business analysis and consultation
- Pricing and package comparison
- Demo scheduling and trial setup
- Technical details and implementation
- Veteran discounts and special offers
- Industry-specific solutions
- ROI calculations and business case development

### **🔧 Technical Features**
- **REST API**: Webhook integration for frontend communication
- **Custom Actions**: Business logic for complex consultations
- **Session Management**: Conversation continuity and context
- **Error Handling**: Graceful fallbacks and user guidance
- **Rate Limiting**: OpenAI API protection and optimization

## 🏗️ Architecture

```
rasa-main/
├── config.yml          # Rasa configuration with DIETClassifier
├── domain.yml          # Intents, entities, slots, and responses
├── data/
│   ├── nlu.yml        # Training examples for all intents
│   ├── stories.yml    # Conversation flows and paths
│   └── rules.yml      # Direct intent-action mappings
├── actions.py          # Custom actions with OpenAI integration
├── endpoints.yml       # Action server configuration
├── credentials.yml     # REST channel configuration
├── frontend/           # React TypeScript frontend
│   ├── src/
│   │   ├── App.tsx    # Main chat interface
│   │   ├── App.css    # Styling with black theme
│   │   └── index.tsx  # React entry point
│   └── package.json   # Frontend dependencies
├── requirements.txt    # Python dependencies
├── train.sh           # Automated training script
├── run_actions.sh     # Action server startup
├── run_rasa.sh        # Rasa server startup
└── README.md          # This file
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Node.js 16+
- OpenAI API key

### **1. Setup Environment**
```bash
cd rasa-main
cp env.example .env
# Edit .env with your OpenAI API key
```

### **2. Train the Model**
```bash
./train.sh
```

### **3. Start the System**
```bash
# Terminal 1: Start action server
./run_actions.sh

# Terminal 2: Start Rasa server
./run_rasa.sh

# Terminal 3: Start frontend
cd frontend
npm install
npm start
```

### **4. Access the Chatbot**
- Frontend: http://localhost:3000
- Rasa API: http://localhost:5005
- Action Server: http://localhost:5055

## 📊 Training Data

### **Intents Covered**
- **Greeting & Farewell**: greet, goodbye, thank_you
- **Business Consultation**: business_analysis, industry_specific
- **Sales & Pricing**: get_pricing, see_pricing, package_comparison
- **Demo & Trials**: schedule_demo, start_trial
- **Technical**: technical_details, how_it_works, integration_details
- **Support**: support_questions, contact_sales
- **Special Offers**: veteran_discounts
- **Analysis**: roi_calculation, implementation_timeline

### **Training Examples**
- **25+ intents** with **15+ examples each**
- **Industry-specific** business scenarios
- **Real-world** consultation conversations
- **Comprehensive** fallback handling

## 🔧 Configuration

### **Rasa Configuration**
- **NLU Pipeline**: DIETClassifier with BERT embeddings
- **Policies**: TEDPolicy, RulePolicy, MemoizationPolicy
- **Training**: 100 epochs with optimized hyperparameters
- **Fallback**: 30% confidence threshold with custom actions

### **OpenAI Integration**
- **Model**: GPT-3.5-turbo
- **Context**: Business-aware system prompts
- **Rate Limiting**: Comprehensive error handling
- **Fallbacks**: Graceful degradation on API issues

## 🎨 Frontend Features

### **User Interface**
- **Dark Theme**: Consistent black background across platforms
- **Responsive Design**: Mobile-first approach
- **Quick Actions**: Pre-defined business consultation options
- **Real-time Chat**: Live conversation with typing indicators
- **Session Management**: Conversation continuity

### **Quick Action Buttons**
- Schedule Demo
- See Pricing
- Start Free Trial
- Business Analysis
- Technical Details
- Veteran Discounts

## 📈 Business Intelligence

### **Industry-Specific Analysis**
- **Healthcare**: HIPAA compliance, patient communication
- **Retail**: Sales conversion, inventory management
- **Automotive**: Service scheduling, parts catalog
- **General**: Customer service automation, lead capture

### **ROI Calculations**
- **Healthcare**: 1,336-2,672% ROI, 2-4 week break-even
- **Retail**: 2,025-4,453% ROI, 1-2 week break-even
- **General**: 1,114-2,633% ROI, 2-3 week break-even

### **Package Recommendations**
- **Starter**: $79/month for small businesses
- **Professional**: $247/month for growing companies
- **Enterprise**: Custom pricing for large organizations

## 🔒 Security & Compliance

- **Environment Variables**: Secure API key management
- **CORS Configuration**: Controlled cross-origin access
- **Rate Limiting**: API protection and abuse prevention
- **Error Handling**: No sensitive information exposure
- **Session Isolation**: User conversation privacy

## 🚀 Deployment

### **Development**
```bash
# Local development setup
./train.sh
./run_actions.sh &
./run_rasa.sh &
cd frontend && npm start
```

### **Production**
```bash
# Production deployment
export RASA_ENV=production
./train.sh
./run_actions.sh &
./run_rasa.sh &
cd frontend && npm run build
```

### **Docker (Optional)**
```dockerfile
# Dockerfile example
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5005
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "5005"]
```

## 📊 Monitoring & Analytics

### **Performance Metrics**
- Response time tracking
- Intent recognition accuracy
- User satisfaction scores
- Conversation completion rates
- Business conversion tracking

### **Logging**
- Comprehensive error logging
- OpenAI API usage tracking
- User interaction analytics
- Performance monitoring
- Business intelligence insights

## 🛠️ Troubleshooting

### **Common Issues**
1. **Training Failures**: Check Python version and dependencies
2. **Action Server Errors**: Verify OpenAI API key and connectivity
3. **Frontend Connection**: Ensure Rasa server is running on port 5005
4. **Model Performance**: Retrain with additional examples

### **Debug Commands**
```bash
# Check Rasa status
rasa shell

# Test actions
rasa run actions --debug

# Validate training data
rasa data validate

# Interactive training
rasa interactive
```

## 🔄 Development Workflow

### **Adding New Intents**
1. Add intent to `domain.yml`
2. Add examples to `data/nlu.yml`
3. Create stories in `data/stories.yml`
4. Add responses to `domain.yml`
5. Retrain model: `./train.sh`

### **Custom Actions**
1. Implement action in `actions.py`
2. Add to `domain.yml` actions list
3. Create training examples
4. Test with `rasa shell`

### **Frontend Updates**
1. Modify React components in `frontend/src/`
2. Update styling in `App.css`
3. Test responsiveness
4. Deploy with `npm run build`

## 📚 API Reference

### **Rasa Webhook Endpoint**
```
POST /webhooks/rest/webhook
Content-Type: application/json

{
  "sender": "user_session_id",
  "message": "user_message_text"
}
```

### **Response Format**
```json
[
  {
    "recipient_id": "user_session_id",
    "text": "bot_response_text"
  }
]
```

## 🌟 Performance Optimization

### **Training Optimization**
- **Epochs**: 100 for optimal accuracy
- **Learning Rate**: 0.001 for stable convergence
- **Model Confidence**: Linear normalization
- **Embedding Dimension**: 20 for efficiency

### **Runtime Optimization**
- **Session Management**: Efficient slot tracking
- **Response Caching**: Intelligent fallback handling
- **API Optimization**: OpenAI rate limit management
- **Memory Usage**: Optimized model loading

## 🔮 Future Enhancements

### **Planned Features**
- Multi-language support
- Voice integration
- Advanced analytics dashboard
- CRM integration
- Payment processing
- White-label solutions

### **Scalability Improvements**
- Horizontal scaling
- Load balancing
- Database integration
- Advanced caching
- Microservices architecture

## 📄 License

This project is proprietary software developed by NextEleven. All rights reserved.

## 🤝 Support

For technical support or business inquiries:
- **Email**: support@nexteleven.com
- **Documentation**: https://docs.nexteleven.com
- **Community**: https://community.nexteleven.com

---

**Happy Chatting with NextEleven! 🤖💼✨**
