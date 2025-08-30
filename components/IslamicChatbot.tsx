import React, { useState, useRef, useEffect } from 'react';
import { Send, BookOpen, Heart, Star, Moon, Sun, Users, Globe } from 'lucide-react';

const IslamicChatbot = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Assalamu alaikum! I'm your Islamic AI assistant. I can help you with Quran, Hadith, Islamic rulings, and general Islamic knowledge. How may I assist you today?",
      sender: 'bot',
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showQuickActions, setShowQuickActions] = useState(true);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const addMessage = (text: string, sender: 'user' | 'bot' = 'user') => {
    const newMessage = {
      id: messages.length + 1,
      text,
      sender,
      timestamp: new Date()
    };
    setMessages(prev => [...prev, newMessage]);
  };

  const handleSendMessage = async () => {
    if (input.trim()) {
      const userMessage = input;
      addMessage(userMessage);
      setInput('');
      setIsLoading(true);

      try {
        // Simulate API call to deenbot backend
        const response = await processUserMessage(userMessage);
        addMessage(response, 'bot');
      } catch (error) {
        addMessage("I apologize, but I'm experiencing some technical difficulties. Please try again or contact support.", 'bot');
      } finally {
        setIsLoading(false);
      }
    }
  };

  const processUserMessage = async (message: string): Promise<string> => {
    // Simulate processing delay
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    const lowerMessage = message.toLowerCase();
    
    if (lowerMessage.includes('quran') || lowerMessage.includes('surah') || lowerMessage.includes('ayah')) {
      return "The Quran is the holy book of Islam, revealed to Prophet Muhammad (ﷺ) over 23 years. I can help you find specific surahs, ayahs, or explain meanings. What would you like to know about the Quran?";
    } else if (lowerMessage.includes('hadith') || lowerMessage.includes('sunnah')) {
      return "Hadith are the sayings, actions, and approvals of Prophet Muhammad (ﷺ). They complement the Quran and provide guidance for daily life. Which aspect of Hadith would you like to explore?";
    } else if (lowerMessage.includes('prayer') || lowerMessage.includes('salah') || lowerMessage.includes('namaz')) {
      return "Salah (prayer) is one of the five pillars of Islam. Muslims pray five times daily: Fajr (dawn), Dhuhr (noon), Asr (afternoon), Maghrib (sunset), and Isha (night). Would you like to learn about prayer times or how to pray?";
    } else if (lowerMessage.includes('ramadan') || lowerMessage.includes('fasting')) {
      return "Ramadan is the ninth month of the Islamic calendar when Muslims fast from dawn to sunset. It's a time of spiritual reflection, increased devotion, and community. Would you like to know more about fasting or Ramadan traditions?";
    } else if (lowerMessage.includes('halal') || lowerMessage.includes('haram')) {
      return "Halal means 'permissible' and Haram means 'forbidden' in Islam. These terms apply to food, business practices, and daily activities. What specific area would you like to learn about?";
    } else if (lowerMessage.includes('zakat') || lowerMessage.includes('charity')) {
      return "Zakat is the third pillar of Islam - obligatory charity given annually to those in need. It's typically 2.5% of one's wealth above the nisab (minimum threshold). Would you like to learn about Zakat calculation or distribution?";
    } else if (lowerMessage.includes('hajj') || lowerMessage.includes('umrah')) {
      return "Hajj is the annual pilgrimage to Makkah, one of the five pillars of Islam. Umrah is a lesser pilgrimage that can be performed anytime. Both involve visiting the Kaaba and performing specific rituals. What would you like to know?";
    } else if (lowerMessage.includes('prophet') || lowerMessage.includes('muhammad')) {
      return "Prophet Muhammad (ﷺ) is the final messenger of Allah, born in Makkah in 570 CE. He received the Quran and established Islam. His life serves as a perfect example for Muslims. What aspect of his life would you like to learn about?";
    } else if (lowerMessage.includes('islam') || lowerMessage.includes('muslim')) {
      return "Islam means 'submission to Allah' and is a monotheistic Abrahamic religion. Muslims believe in one God (Allah) and follow the teachings of Prophet Muhammad (ﷺ). What would you like to know about Islamic beliefs or practices?";
    } else {
      return "I can help you with various Islamic topics including Quran, Hadith, prayer, fasting, halal/haram rulings, Islamic history, and more. Please ask a specific question or choose from the quick actions below.";
    }
  };

  const handleQuickAction = (action: string) => {
    let message = '';
    switch (action) {
      case 'quran':
        message = "Tell me about the Quran";
        break;
      case 'hadith':
        message = "What are Hadith?";
        break;
      case 'prayer':
        message = "How do Muslims pray?";
        break;
      case 'ramadan':
        message = "Tell me about Ramadan";
        break;
      case 'halal':
        message = "What is halal and haram?";
        break;
      case 'zakat':
        message = "Explain Zakat";
        break;
      case 'hajj':
        message = "What is Hajj?";
        break;
      case 'prophet':
        message = "Tell me about Prophet Muhammad";
        break;
    }
    
    if (message) {
      addMessage(message);
      processUserMessage(message).then(response => {
        addMessage(response, 'bot');
      });
    }
  };

  const QuickActions = () => (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
      <button
        onClick={() => handleQuickAction('quran')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <BookOpen size={24} />
        <span className="text-sm font-medium">Quran</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('hadith')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Heart size={24} />
        <span className="text-sm font-medium">Hadith</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('prayer')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-purple-600 to-purple-700 hover:from-purple-700 hover:to-purple-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Moon size={24} />
        <span className="text-sm font-medium">Prayer</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('ramadan')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-orange-600 to-orange-700 hover:from-orange-700 hover:to-orange-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Sun size={24} />
        <span className="text-sm font-medium">Ramadan</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('halal')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-teal-600 to-teal-700 hover:from-teal-700 hover:to-teal-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Star size={24} />
        <span className="text-sm font-medium">Halal/Haram</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('zakat')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-emerald-600 to-emerald-700 hover:from-emerald-700 hover:to-emerald-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Users size={24} />
        <span className="text-sm font-medium">Zakat</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('hajj')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-indigo-600 to-indigo-700 hover:from-indigo-700 hover:to-indigo-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Globe size={24} />
        <span className="text-sm font-medium">Hajj</span>
      </button>
      
      <button
        onClick={() => handleQuickAction('prophet')}
        className="flex flex-col items-center gap-2 bg-gradient-to-br from-rose-600 to-rose-700 hover:from-rose-700 hover:to-rose-800 text-white p-4 rounded-lg transition-all duration-200 hover:scale-105"
      >
        <Heart size={24} />
        <span className="text-sm font-medium">Prophet</span>
      </button>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      <div className="max-w-6xl mx-auto p-4">
        {/* Header */}
        <header className="text-center mb-8">
          <div className="bg-gradient-to-r from-green-600/20 to-blue-600/20 backdrop-blur-sm border border-green-500/30 rounded-2xl p-8 mb-6">
            <h1 className="text-4xl md:text-6xl font-bold bg-gradient-to-r from-green-400 to-blue-400 bg-clip-text text-transparent mb-4">
              Islamic AI Assistant
            </h1>
            <p className="text-xl text-gray-300 max-w-2xl mx-auto">
              Your knowledgeable companion for Islamic learning, Quran study, Hadith exploration, and religious guidance
            </p>
            <div className="flex justify-center items-center gap-4 mt-4 text-sm text-gray-400">
              <span className="flex items-center gap-2">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                Online 24/7
              </span>
              <span>•</span>
              <span>Powered by Islamic Knowledge Base</span>
              <span>•</span>
              <span>Multilingual Support</span>
            </div>
          </div>
        </header>

        {/* Main Chat Interface */}
        <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-2xl p-6 shadow-2xl">
          {/* Quick Actions */}
          {showQuickActions && (
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-300 mb-4 text-center">
                Quick Actions - Choose a Topic
              </h3>
              <QuickActions />
            </div>
          )}

          {/* Chat Messages */}
          <div className="space-y-4 mb-6 max-h-96 overflow-y-auto">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-xs md:max-w-md lg:max-w-lg px-4 py-3 rounded-2xl ${
                    message.sender === 'user'
                      ? 'bg-gradient-to-r from-green-600 to-green-700 text-white'
                      : 'bg-slate-700/80 text-gray-100 border border-slate-600/50'
                  }`}
                >
                  <p className="text-sm md:text-base">{message.text}</p>
                  <p className="text-xs opacity-70 mt-2 text-right">
                    {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </p>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-slate-700/80 text-gray-100 border border-slate-600/50 px-4 py-3 rounded-2xl">
                  <div className="flex items-center gap-2">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-green-400"></div>
                    <span className="text-sm">Thinking...</span>
                  </div>
                </div>
              </div>
            )}
            
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="flex gap-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder="Ask about Islamic topics, Quran, Hadith, prayer, or any religious question..."
              className="flex-1 bg-slate-700/80 text-white p-4 rounded-xl border border-slate-600/50 focus:border-green-500 focus:outline-none focus:ring-2 focus:ring-green-500/20 transition-all duration-200"
            />
            <button
              onClick={handleSendMessage}
              disabled={isLoading || !input.trim()}
              className="bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 disabled:opacity-50 disabled:cursor-not-allowed text-white p-4 rounded-xl font-medium transition-all duration-200 hover:scale-105"
            >
              <Send size={20} />
            </button>
          </div>

          {/* Footer */}
          <div className="mt-6 text-center">
            <p className="text-sm text-gray-400">
              💡 <span className="text-green-400">Tip:</span> Ask specific questions for better answers. 
              Try: "What does the Quran say about charity?" or "How do I perform wudu?"
            </p>
          </div>
        </div>

        {/* Additional Resources */}
        <div className="mt-8 grid md:grid-cols-3 gap-6">
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6 text-center">
            <BookOpen size={32} className="mx-auto mb-3 text-green-400" />
            <h3 className="font-semibold mb-2">Quran Study</h3>
            <p className="text-sm text-gray-400">Access complete Quran with translations and tafsir</p>
          </div>
          
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6 text-center">
            <Heart size={32} className="mx-auto mb-3 text-blue-400" />
            <h3 className="font-semibold mb-2">Hadith Collection</h3>
            <p className="text-sm text-gray-400">Explore authentic Hadith from major collections</p>
          </div>
          
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6 text-center">
            <Globe size={32} className="mx-auto mb-3 text-purple-400" />
            <h3 className="font-semibold mb-2">Islamic Resources</h3>
            <p className="text-sm text-gray-400">Prayer times, halal guides, and more</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default IslamicChatbot;

