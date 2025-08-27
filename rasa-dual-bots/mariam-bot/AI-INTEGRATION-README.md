# 🤖 AI Integration System for Mariam Bot

## Overview

This AI integration system enhances Mariam Bot with intelligent fallback responses, hybrid mode capabilities, and context-aware conversations using OpenAI's GPT models. When Mariam's knowledge base can't provide satisfactory answers, the AI system seamlessly takes over to ensure users always get helpful responses.

## 🚀 Key Features

### 1. **AI Fallback Logic**
- Automatically detects when knowledge bot responses are insufficient
- Provides intelligent, context-aware responses using OpenAI
- Maintains conversation flow and business context

### 2. **Confidence Scoring System**
- **High Confidence (≥0.8)**: Uses knowledge bot only
- **Medium Confidence (0.6-0.8)**: Hybrid mode with AI enhancement
- **Low Confidence (<0.6)**: Full AI fallback response

### 3. **Seamless OpenAI Integration**
- Automatic API key management
- Configurable models (GPT-3.5-turbo, GPT-4)
- Error handling and rate limiting
- Cost optimization with token limits

### 4. **Conversation Context Management**
- Maintains conversation history across sessions
- Tracks user preferences and interaction patterns
- Provides personalized responses based on context

### 5. **Hybrid Mode**
- Combines knowledge bot responses with AI insights
- Adds examples, case studies, and actionable steps
- Enhances existing responses without replacing them

### 6. **Comprehensive Logging**
- Tracks AI vs. knowledge bot usage
- Monitors confidence scores and response quality
- Provides analytics and performance insights

## 🛠️ Installation

### Quick Setup
```bash
# Navigate to mariam-bot directory
cd rasa-dual-bots/mariam-bot

# Run the automated setup script
./setup-ai.sh
```

### Manual Setup
```bash
# Create virtual environment
python3 -m venv ai-env
source ai-env/bin/activate

# Install dependencies
pip install -r ai-requirements.txt

# Configure environment
cp ai.env.example .env
# Edit .env with your OpenAI API key
```

## ⚙️ Configuration

### Environment Variables (.env file)
```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=500
OPENAI_TEMPERATURE=0.7

# Confidence Thresholds
CONFIDENCE_HIGH_THRESHOLD=0.8
CONFIDENCE_MEDIUM_THRESHOLD=0.6
CONFIDENCE_LOW_THRESHOLD=0.4

# Logging
LOG_LEVEL=INFO
LOG_AI_INTERACTIONS=true
```

### Getting OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a new API key
3. Add it to your `.env` file
4. Set appropriate usage limits in OpenAI dashboard

## 🔧 Usage

### Basic Integration
The AI system automatically integrates with existing Mariam Bot actions:

```python
from ai_integration import get_ai_integration

# Get AI integration instance
ai = get_ai_integration()

# Check if AI is available
if ai.enabled:
    # Use AI features
    response = ai.get_ai_response(user_message, context)
```

### Response Modes

#### 1. **Knowledge Bot Only** (High Confidence)
- Uses existing Mariam responses
- No AI intervention
- Fastest response time

#### 2. **Hybrid Mode** (Medium Confidence)
- Combines knowledge bot + AI enhancement
- Adds examples and insights
- Balanced response quality

#### 3. **AI Fallback** (Low Confidence)
- Full AI-generated response
- Context-aware and personalized
- Highest response quality

### Context Management
```python
# Update conversation context
ai.update_conversation_context(
    user_id="user123",
    user_message="What are your prices?",
    bot_response="Here's our pricing...",
    mode="hybrid"
)

# Get context for future interactions
context = ai.conversation_contexts.get("user123", {})
```

## 📊 Monitoring & Analytics

### Usage Statistics
```python
# Get current usage stats
stats = ai.get_usage_statistics()
print(f"AI Fallback: {stats['ai_fallback']} ({stats['ai_fallback_pct']:.1f}%)")
print(f"Hybrid Mode: {stats['hybrid_mode']} ({stats['hybrid_mode_pct']:.1f}%)")
```

### Health Monitoring
```python
# Check system health
health = ai.health_check()
print(f"AI Enabled: {health['ai_enabled']}")
print(f"OpenAI Connection: {health['openai_connection']}")
```

### Logging
The system provides detailed logging for:
- Confidence score calculations
- Response mode decisions
- AI API interactions
- Error handling
- Performance metrics

## 🔄 Integration with Existing Actions

### Enhanced Actions
The system provides enhanced versions of existing actions:

- `ActionEnhancedPricingInquiry`: Pricing with AI enhancement
- `ActionAIFallback`: AI fallback responses
- `ActionHybridResponse`: Hybrid knowledge + AI responses
- `ActionConfidenceBasedResponse`: Automatic mode selection

### Adding AI to Custom Actions
```python
from ai_integration import get_ai_integration

class ActionCustomWithAI(Action):
    def run(self, dispatcher, tracker, domain):
        ai = get_ai_integration()
        
        if ai.enabled:
            # Get AI-enhanced response
            response = ai.enhance_knowledge_response(
                base_response="Your base response",
                user_message=tracker.latest_message.get('text'),
                context=self._build_context(tracker)
            )
        else:
            response = "Your base response"
        
        dispatcher.utter_message(text=response)
```

## 🚨 Error Handling

### Graceful Degradation
- If OpenAI API is unavailable, falls back to knowledge bot
- If API key is invalid, disables AI features gracefully
- Rate limiting and timeout handling

### Common Issues & Solutions

#### API Key Issues
```bash
# Check if API key is loaded
python3 -c "from ai_integration import get_ai_integration; print(get_ai_integration().enabled)"
```

#### Rate Limiting
```bash
# Adjust rate limits in .env
MAX_AI_REQUESTS_PER_MINUTE=30
MAX_AI_REQUESTS_PER_HOUR=500
```

#### Model Issues
```bash
# Try different models
OPENAI_MODEL=gpt-3.5-turbo-16k
OPENAI_MODEL=gpt-4
```

## 📈 Performance Optimization

### Token Management
- Configurable max tokens per response
- Automatic truncation for long conversations
- Cost optimization strategies

### Caching
- Conversation context caching
- Response pattern learning
- Reduced API calls for similar questions

### Async Support
- Optional async processing for high-volume scenarios
- Background AI response generation
- Non-blocking user interactions

## 🔒 Security & Privacy

### Data Handling
- No sensitive data sent to OpenAI
- Local conversation context storage
- Configurable data retention policies

### API Security
- Secure API key storage
- Rate limiting and abuse prevention
- Audit logging for compliance

## 🧪 Testing

### Unit Tests
```bash
# Test AI integration
python3 -c "
from ai_integration import get_ai_integration
ai = get_ai_integration()
print('AI Integration Test:', '✅ PASS' if ai.enabled else '❌ FAIL')
"
```

### Integration Tests
```bash
# Test with Mariam bot
rasa test --domain domain.yml --stories data/stories.yml
```

### Performance Tests
```bash
# Test response times
python3 -c "
import time
from ai_integration import get_ai_integration
ai = get_ai_integration()
start = time.time()
response = ai.get_ai_response('test message', {}, 'fallback')
print(f'Response time: {time.time() - start:.2f}s')
"
```

## 📚 Advanced Features

### Custom Models
- Support for different OpenAI models
- Fine-tuned model integration
- Local model alternatives

### Multi-Language Support
- Automatic language detection
- Localized AI responses
- Cultural context awareness

### Industry Specialization
- Healthcare-specific AI responses
- Retail optimization
- Automotive industry knowledge
- Restaurant management insights

## 🆘 Support & Troubleshooting

### Common Commands
```bash
# Check AI integration status
python3 -c "from ai_integration import get_ai_integration; print(get_ai_integration().health_check())"

# Reset usage statistics
python3 -c "from ai_integration import get_ai_integration; get_ai_integration().reset_usage_statistics()"

# Test OpenAI connection
python3 -c "from ai_integration import get_ai_integration; ai = get_ai_integration(); print(ai.health_check()['openai_connection'])"
```

### Debug Mode
```bash
# Enable debug logging
LOG_LEVEL=DEBUG
LOG_AI_INTERACTIONS=true
LOG_CONFIDENCE_SCORES=true
```

### Getting Help
1. Check the logs for error messages
2. Verify OpenAI API key and configuration
3. Test with simple queries first
4. Check rate limits and usage quotas

## 🎯 Best Practices

### 1. **Start Small**
- Begin with basic fallback responses
- Gradually add hybrid mode features
- Monitor performance and costs

### 2. **Monitor Usage**
- Track AI vs. knowledge bot usage
- Monitor confidence score distributions
- Optimize thresholds based on data

### 3. **Iterate and Improve**
- Collect user feedback on AI responses
- Adjust confidence thresholds
- Fine-tune prompts and context

### 4. **Cost Management**
- Set appropriate token limits
- Monitor API usage and costs
- Use caching to reduce API calls

## 🔮 Future Enhancements

### Planned Features
- **Multi-modal AI**: Image and document understanding
- **Voice Integration**: Speech-to-text and text-to-speech
- **Advanced Analytics**: Deep learning insights
- **Custom Training**: Domain-specific model fine-tuning

### Community Contributions
- Open-source prompt templates
- Industry-specific knowledge bases
- Performance optimization techniques
- Integration examples

---

## 📞 Support

For questions or issues with the AI integration system:

1. **Check the logs** for detailed error information
2. **Review this documentation** for common solutions
3. **Test the integration** with the provided test scripts
4. **Monitor system health** using the health check functions

---

**🎉 Congratulations!** You now have a powerful AI-enhanced chatbot that can handle any question with intelligence and grace.

