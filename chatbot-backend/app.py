import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for frontend
CORS(app, origins=['http://localhost:3000'])

# Configure rate limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# System prompt for the AI assistant
SYSTEM_PROMPT = """You are a helpful, friendly, and knowledgeable AI assistant. 
You provide clear, accurate, and helpful responses to user questions. 
You are polite, professional, and always try to be as helpful as possible.
If you don't know something, you're honest about it and suggest where they might find the information."""

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'AI Chatbot Backend',
        'version': '1.0.0'
    })

@app.route('/chat', methods=['POST'])
@limiter.limit("30 per minute")  # Rate limit: 30 requests per minute per IP
def chat():
    """Main chat endpoint that processes user messages and returns AI responses"""
    try:
        # Get request data
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        user_message = data.get('message', '').strip()
        
        # Validate input
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if len(user_message) > 1000:
            return jsonify({'error': 'Message too long (max 1000 characters)'}), 400
        
        logger.info(f"Received message: {user_message[:100]}...")
        
        # Check if OpenAI API key is configured
        if not openai.api_key:
            logger.error("OpenAI API key not configured")
            return jsonify({
                'error': 'OpenAI API not configured',
                'reply': "I'm sorry, but I'm currently experiencing technical difficulties. Please try again later."
            }), 500
        
        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.7,
                timeout=30
            )
            
            # Extract the response
            ai_reply = response.choices[0].message.content.strip()
            
            logger.info(f"AI response generated successfully")
            
            return jsonify({
                'reply': ai_reply,
                'model': 'gpt-3.5-turbo',
                'tokens_used': response.usage.total_tokens if hasattr(response, 'usage') else None
            })
            
        except openai.error.RateLimitError:
            logger.warning("OpenAI rate limit exceeded")
            return jsonify({
                'error': 'Rate limit exceeded',
                'reply': "I'm receiving too many requests right now. Please wait a moment and try again."
            }), 429
            
        except openai.error.InvalidRequestError as e:
            logger.error(f"OpenAI invalid request: {e}")
            return jsonify({
                'error': 'Invalid request to AI service',
                'reply': "I'm sorry, but I couldn't process your request. Please try rephrasing your question."
            }), 400
            
        except openai.error.APIError as e:
            logger.error(f"OpenAI API error: {e}")
            return jsonify({
                'error': 'AI service error',
                'reply': "I'm experiencing technical difficulties with my AI service. Please try again in a few minutes."
            }), 500
            
        except Exception as e:
            logger.error(f"Unexpected OpenAI error: {e}")
            return jsonify({
                'error': 'Unexpected error',
                'reply': "I'm sorry, but something unexpected happened. Please try again later."
            }), 500
            
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {e}")
        return jsonify({
            'error': 'Internal server error',
            'reply': "I'm sorry, but I'm experiencing technical difficulties. Please try again later."
        }), 500

@app.route('/models', methods=['GET'])
def get_models():
    """Get available OpenAI models (if API key is configured)"""
    try:
        if not openai.api_key:
            return jsonify({'error': 'OpenAI API not configured'}), 500
        
        models = openai.Model.list()
        return jsonify({
            'models': [model.id for model in models.data],
            'available': True
        })
    except Exception as e:
        logger.error(f"Error fetching models: {e}")
        return jsonify({
            'error': 'Could not fetch models',
            'available': False
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(429)
def ratelimit_handler(error):
    """Handle rate limit errors"""
    return jsonify({
        'error': 'Rate limit exceeded',
        'reply': "You're sending messages too quickly. Please wait a moment before trying again."
    }), 429

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    return jsonify({
        'error': 'Internal server error',
        'reply': "I'm experiencing technical difficulties. Please try again later."
    }), 500

if __name__ == '__main__':
    # Check if OpenAI API key is set
    if not os.getenv('OPENAI_API_KEY'):
        logger.warning("OpenAI API key not found in environment variables")
        logger.warning("Set OPENAI_API_KEY environment variable to enable AI functionality")
    
    # Run the app
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f"Starting AI Chatbot Backend on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
