# 🤖 Rasa AI Chatbot System

A production-ready, trainable AI chatbot built with **Rasa** for NLU and dialogue management, integrated with **OpenAI** for knowledge responses, and a **React TypeScript** frontend.

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** and **pip**
- **Node.js 16+** and **npm**
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### 1. Setup Environment
```bash
# Clone and navigate to project
cd rasa-chatbot

# Set your OpenAI API key
cp env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### 2. Train the Model
```bash
# Make scripts executable
chmod +x *.sh

# Train the chatbot (creates virtual environment, installs dependencies, trains model)
./train.sh
```

### 3. Start All Services
```bash
# Terminal 1: Action Server (OpenAI integration)
./run_actions.sh

# Terminal 2: Rasa Server (NLU + Dialogue)
./run_rasa.sh

# Terminal 3: React Frontend
cd frontend
npm install
npm start
```

### 4. Open Your Browser
- **Frontend**: http://localhost:3000
- **Rasa Server**: http://localhost:5005
- **Action Server**: http://localhost:5055

## 🏗️ Architecture

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐    OpenAI API    ┌─────────────────┐
│   React App     │ ◄──────────────► │   Rasa Server   │ ◄──────────────► │   OpenAI GPT    │
│  (Port 3000)    │                 │  (Port 5005)    │                 │  (GPT-3.5-turbo)│
└─────────────────┘                 └─────────────────┘                 └─────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │ Action Server   │
                                    │  (Port 5055)   │
                                    └─────────────────┘
```

## ✨ Features

### **Rasa Core**
- 🧠 **Advanced NLU** with DIETClassifier
- 💬 **Dialogue Management** with TEDPolicy
- 🔄 **Conversation Flows** with stories and rules
- 📊 **Intent Recognition** for business queries
- 🎯 **Entity Extraction** for business types, packages

### **OpenAI Integration**
- 🤖 **GPT-3.5-turbo** for knowledge responses
- 🎭 **Context-Aware** system prompts
- ⚡ **Real-time** AI responses
- 🔒 **Rate Limiting** and error handling
- 💡 **Intelligent Fallbacks**

### **Frontend**
- 🎨 **Modern Dark UI** with black backgrounds
- 📱 **Mobile-Responsive** design
- ⚡ **Real-time Chat** with loading states
- 🔄 **Auto-scroll** to latest messages
- ⏱️ **Timestamps** on all messages

## 📁 Project Structure

```
rasa-chatbot/
├── data/                    # Training data
│   ├── nlu.yml             # Intent examples
│   ├── stories.yml         # Conversation flows
│   └── rules.yml           # Conversation rules
├── frontend/                # React TypeScript app
│   ├── src/App.tsx         # Main chat component
│   ├── src/App.css         # Styling
│   └── package.json        # Dependencies
├── actions.py               # Custom actions (OpenAI integration)
├── config.yml               # Rasa configuration
├── domain.yml               # Intents, entities, responses
├── endpoints.yml            # Server endpoints
├── credentials.yml          # Channel credentials
├── requirements.txt         # Python dependencies
├── train.sh                 # Training script
├── run_actions.sh           # Action server script
├── run_rasa.sh              # Rasa server script
└── README.md                # This file
```

## 🔧 Configuration

### Environment Variables
Create `.env` file:
```env
OPENAI_API_KEY=your_actual_api_key_here
```

### Rasa Configuration
- **NLU Pipeline**: DIETClassifier with BERT embeddings
- **Dialogue Policies**: TEDPolicy, RulePolicy, MemoizationPolicy
- **Training**: 100 epochs for fast, accurate training
- **API**: REST webhook enabled on port 5005

## 🧪 Training Data

### **Intents Covered**
- `greet` - Hello, hi, hey
- `get_pricing` - Cost, pricing, rates
- `schedule_demo` - Demo, show, demonstrate
- `start_trial` - Trial, try, test
- `business_analysis` - Business assessment, evaluation
- `technical_details` - Technical specs, how it works
- `veteran_discounts` - Military, veteran benefits
- `thank_you` - Thanks, appreciation
- `goodbye` - Bye, see you, farewell

### **Entities Extracted**
- `business_type` - Industry classification
- `package_type` - Service package selection
- `email` - Contact information
- `time_preference` - Scheduling preferences

## 🚀 Deployment

### **Development**
```bash
# All-in-one training
./train.sh

# Start services
./run_actions.sh    # Terminal 1
./run_rasa.sh       # Terminal 2
cd frontend && npm start  # Terminal 3
```

### **Production**
```bash
# Train model
./train.sh

# Start action server with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5055 rasa_sdk.executor:app

# Start Rasa server
rasa run --enable-api --cors "*" --port 5005 --host 0.0.0.0

# Build and serve frontend
cd frontend
npm run build
# Deploy 'build' folder to your hosting service
```

## 🔒 Security Features

- **Rate Limiting**: Built into Rasa policies
- **Input Validation**: Sanitized user messages
- **CORS Protection**: Configurable origins
- **Error Handling**: No sensitive data exposure
- **Environment Variables**: Secure API key storage

## 📊 Monitoring

### **Health Checks**
- **Rasa Server**: http://localhost:5005/status
- **Action Server**: Check logs for errors
- **Frontend**: Browser console monitoring

### **Logs**
- **Rasa**: Console output with detailed logging
- **Actions**: Custom action execution logs
- **OpenAI**: API call monitoring

## 🐛 Troubleshooting

### **Common Issues**

**"No trained models found"**
```bash
# Run training first
./train.sh
```

**"Action server connection failed"**
- Ensure action server is running on port 5055
- Check virtual environment activation
- Verify requirements installation

**"OpenAI API errors"**
- Check API key in `.env` file
- Verify OpenAI account status
- Monitor rate limits

**"Frontend can't connect"**
- Verify Rasa server on port 5005
- Check CORS settings
- Ensure no firewall blocking

### **Debug Mode**
```bash
# Rasa debug
rasa run --enable-api --debug --port 5005

# Action server debug
rasa run actions --debug --port 5055
```

## 🔄 Development Workflow

1. **Modify Training Data**: Edit `data/nlu.yml`, `stories.yml`
2. **Update Actions**: Modify `actions.py` for new functionality
3. **Retrain Model**: Run `./train.sh`
4. **Test Changes**: Restart servers and test in frontend
5. **Iterate**: Refine based on test results

## 📈 Performance Optimization

### **Fast Training**
- **Small Dataset**: Start with 10 examples per intent
- **Epochs**: 100 for balance of speed/accuracy
- **Model Size**: Optimized for production use

### **Scalability**
- **Horizontal Scaling**: Multiple action server instances
- **Load Balancing**: Nginx reverse proxy
- **Caching**: Redis for session storage

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

- **Documentation**: Check Rasa docs for advanced features
- **Issues**: Open GitHub issues
- **Questions**: Check troubleshooting section

---

**Happy Chatting with Rasa! 🤖💬**
