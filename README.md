# 🤖 AI Chatbot System

A complete, production-ready AI chatbot system built with **React + TypeScript** frontend and **Flask + OpenAI** backend.

## 🚀 Quick Start

### Prerequisites
- **Node.js 16+** and **npm**
- **Python 3.8+** and **pip**
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### 1. Start the Backend (Flask)
```bash
# Terminal 1: Backend
cd chatbot-backend

# Create virtual environment
python3 -m venv chatbot-env
source chatbot-env/bin/activate  # On Windows: chatbot-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
cp env.example .env
# Edit .env and add your OPENAI_API_KEY

# Start the server
python app.py
```

### 2. Start the Frontend (React)
```bash
# Terminal 2: Frontend
cd chatbot-frontend

# Install dependencies
npm install

# Start the app
npm start
```

### 3. Open Your Browser
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000

## 🏗️ Architecture

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐
│   React App     │ ◄──────────────► │   Flask API     │
│  (Port 3000)    │                 │  (Port 5000)    │
└─────────────────┘                 └─────────────────┘
                                              │
                                              ▼
                                    ┌─────────────────┐
                                    │   OpenAI API    │
                                    │  (GPT-3.5-turbo)│
                                    └─────────────────┘
```

## ✨ Features

### Frontend (React + TypeScript)
- 🎨 **Modern Dark UI** with responsive design
- 💬 **Real-time Chat** with message history
- ⏱️ **Timestamps** on all messages
- 🔄 **Auto-scroll** to latest messages
- 📱 **Mobile-first** responsive design
- ⚡ **Loading States** with animated spinners
- 🚨 **Error Handling** with user-friendly messages

### Backend (Flask + OpenAI)
- 🤖 **GPT-3.5-turbo** integration
- 🔒 **Rate Limiting** (30 requests/minute)
- 🌐 **CORS Support** for frontend
- 📝 **Comprehensive Logging**
- ⚡ **Error Handling** with fallbacks
- 🔧 **Environment Configuration**
- 📊 **Health Monitoring** endpoints

## 📁 Project Structure

```
├── chatbot-frontend/          # React TypeScript app
│   ├── public/
│   ├── src/
│   │   ├── App.tsx           # Main chat component
│   │   ├── App.css           # Chat styling
│   │   └── index.tsx         # App entry point
│   ├── package.json
│   └── README.md
│
├── chatbot-backend/           # Flask Python API
│   ├── app.py                # Main Flask app
│   ├── requirements.txt      # Python dependencies
│   ├── env.example          # Environment template
│   └── README.md
│
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables
Create `.env` file in `chatbot-backend/`:

```env
OPENAI_API_KEY=your_actual_api_key_here
FLASK_ENV=development
PORT=5000
```

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST | Send message, get AI response |
| `/health` | GET | Backend health check |
| `/models` | GET | Available OpenAI models |

## 🧪 Testing

### Test Backend
```bash
# Health check
curl http://localhost:5000/health

# Send a message
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

### Test Frontend
- Open http://localhost:3000
- Type a message and press Enter
- Verify AI response appears

## 🚀 Deployment

### Frontend (React)
```bash
cd chatbot-frontend
npm run build
# Deploy 'build' folder to Netlify/Vercel/S3
```

### Backend (Flask)
```bash
cd chatbot-backend
pip install gunicorn
gunicorn -w 4 -b 0.00.0:5000 app:app
```

## 🔒 Security Features

- **Rate Limiting**: Prevents API abuse
- **Input Validation**: Sanitizes user messages
- **CORS Protection**: Restricts cross-origin requests
- **Error Handling**: No sensitive data exposure
- **Environment Variables**: Secure API key storage

## 📱 Responsive Design

The frontend automatically adapts to:
- **Desktop**: Full-width chat interface
- **Tablet**: Optimized for medium screens
- **Mobile**: Touch-friendly mobile interface

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
- Check Python version (3.8+)
- Verify virtual environment is activated
- Ensure OpenAI API key is set

**Frontend can't connect:**
- Verify backend is running on port 5000
- Check CORS settings
- Ensure no firewall blocking

**OpenAI errors:**
- Verify API key is correct
- Check OpenAI account status
- Monitor rate limits

### Debug Mode
```bash
# Backend debug
export FLASK_ENV=development
python app.py

# Frontend debug
npm start
# Check browser console for errors
```

## 🔄 Development Workflow

1. **Backend changes**: Restart Flask server
2. **Frontend changes**: Hot reload (automatic)
3. **Environment changes**: Restart both services
4. **New dependencies**: Update requirements.txt/package.json

## 📊 Monitoring

### Health Checks
- Backend: http://localhost:5000/health
- Frontend: Check browser console
- OpenAI: Monitor API usage

### Logs
- Backend: Console output
- Frontend: Browser console
- OpenAI: Platform dashboard

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

- **Documentation**: Check individual README files
- **Issues**: Open GitHub issues
- **Questions**: Check troubleshooting section

---

**Happy Chatting! 🤖💬**
