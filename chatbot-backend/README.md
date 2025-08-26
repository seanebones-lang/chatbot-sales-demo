# AI Chatbot Backend

A robust Flask backend that provides AI-powered chat functionality using OpenAI's GPT models.

## Features

- 🤖 **OpenAI Integration**: Powered by GPT-3.5-turbo
- 🔒 **Rate Limiting**: Built-in protection against abuse
- 🌐 **CORS Support**: Configured for React frontend
- 📝 **Comprehensive Logging**: Detailed request/response logging
- ⚡ **Error Handling**: Graceful error handling with user-friendly messages
- 🔧 **Environment Configuration**: Easy setup with environment variables
- 📊 **Health Monitoring**: Health check endpoints
- 🚀 **Production Ready**: Includes Gunicorn for production deployment

## Tech Stack

- **Python 3.8+**
- **Flask 2.3+** - Web framework
- **OpenAI Python SDK** - AI model integration
- **Flask-CORS** - Cross-origin resource sharing
- **Flask-Limiter** - Rate limiting
- **Python-dotenv** - Environment variable management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key
- Virtual environment (recommended)

## Installation

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv chatbot-env

# Activate virtual environment
# On macOS/Linux:
source chatbot-env/bin/activate

# On Windows:
chatbot-env\Scripts\activate
```

### 2. Install Dependencies

```bash
cd chatbot-backend
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
# Copy the example environment file
cp env.example .env

# Edit .env file with your OpenAI API key
nano .env
```

**Required Environment Variables:**
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**Optional Environment Variables:**
```env
FLASK_ENV=development  # or production
PORT=5000              # default port
```

### 4. Get OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Create a new API key
4. Copy the key to your `.env` file

## Running the Backend

### Development Mode

```bash
# Make sure virtual environment is activated
python app.py
```

The server will start on `http://localhost:5000`

### Production Mode

```bash
# Set environment
export FLASK_ENV=production

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### POST /chat
Main chat endpoint that processes user messages.

**Request:**
```json
{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "reply": "Hello! I'm doing well, thank you for asking. How can I help you today?",
  "model": "gpt-3.5-turbo",
  "tokens_used": 25
}
```

### GET /health
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Chatbot Backend",
  "version": "1.0.0"
}
```

### GET /models
Get available OpenAI models (requires API key).

**Response:**
```json
{
  "models": ["gpt-3.5-turbo", "gpt-4", "text-davinci-003"],
  "available": true
}
```

## Configuration

### Rate Limiting
- **Default**: 200 requests per day, 50 per hour
- **Chat endpoint**: 30 requests per minute per IP
- **Configurable**: Modify limits in `app.py`

### CORS Settings
- **Frontend origin**: `http://localhost:3000`
- **Configurable**: Update origins in `app.py`

### OpenAI Settings
- **Model**: GPT-3.5-turbo (configurable)
- **Max tokens**: 500 per response
- **Temperature**: 0.7 (balanced creativity)
- **Timeout**: 30 seconds

## Project Structure

```
chatbot-backend/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── env.example        # Environment variables template
├── README.md          # This file
└── .env               # Your environment variables (create this)
```

## Development

### Adding New Endpoints

1. Add new route functions to `app.py`
2. Include proper error handling
3. Add logging for debugging
4. Update documentation

### Customizing AI Behavior

Modify the `SYSTEM_PROMPT` in `app.py`:

```python
SYSTEM_PROMPT = """You are a specialized AI assistant for [your domain].
You have expertise in [specific areas].
You always [specific behavior]."""
```

### Adding Middleware

```python
from flask import request

@app.before_request
def log_request():
    logger.info(f"{request.method} {request.path}")
```

## Testing

### Manual Testing with curl

```bash
# Test health endpoint
curl http://localhost:5000/health

# Test chat endpoint
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how are you?"}'
```

### Testing with Postman

1. Import the endpoints
2. Set base URL to `http://localhost:5000`
3. Test each endpoint individually

## Troubleshooting

### Common Issues

**"OpenAI API key not configured"**
- Check your `.env` file
- Ensure `OPENAI_API_KEY` is set
- Restart the server after changing environment variables

**"Module not found" errors**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**CORS errors from frontend**
- Verify CORS origins in `app.py`
- Check frontend is running on correct port
- Ensure backend is accessible

**Rate limiting errors**
- Wait for rate limit to reset
- Check your IP address
- Consider increasing limits for development

### Logs

The application logs to console by default. For production:

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[
        logging.FileHandler('chatbot.log'),
        logging.StreamHandler()
    ]
)
```

## Deployment

### Using Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run production server
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Environment Variables for Production

```env
FLASK_ENV=production
PORT=5000
OPENAI_API_KEY=your_production_api_key
```

## Security Considerations

- **API Key Protection**: Never commit API keys to version control
- **Rate Limiting**: Prevents abuse and controls costs
- **Input Validation**: Sanitizes user input
- **Error Handling**: Doesn't expose sensitive information
- **CORS**: Restricts access to authorized origins

## Monitoring

### Health Checks
- Monitor `/health` endpoint
- Set up alerts for unhealthy status
- Track response times

### OpenAI Usage
- Monitor token usage
- Track API costs
- Set up usage alerts

### Application Metrics
- Request/response counts
- Error rates
- Response times

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs
3. Check OpenAI API status
4. Open an issue in the repository
