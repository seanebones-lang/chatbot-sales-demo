import React, { useState, useRef, useEffect } from 'react';
import { Send, MessageCircle, BookOpen, Search, FileText, Info, CheckCircle, AlertCircle, Bookmark, Share2, Heart, Star, Clock, Users, MapPin, Globe, Bot, User } from 'lucide-react';
import Logo from './Logo';

const IslamicChatbot = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'bot',
      text: 'As-salamu alaykum! May I answer questions you have about Islam? I am DeenBot, your Islamic AI assistant, and I am here to help you learn about Islam, Quran, Hadith, and Islamic practices. Please ask me anything you would like to know.',
      timestamp: 'Just now'
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showQuickActions, setShowQuickActions] = useState(true);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      sender: 'user',
      text: inputValue.trim(),
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    // Simulate AI response
    setTimeout(() => {
      const botResponse = {
        id: Date.now() + 1,
        sender: 'bot',
        text: `Thank you for your question about "${inputValue.trim()}". I am DeenBot, designed to provide authentic Islamic knowledge. For this specific question, I would need to consult my knowledge base to give you an accurate answer backed by authentic sources from the Quran and Hadith. Please allow me a moment to provide you with a comprehensive response with proper citations.`,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, botResponse]);
      setIsLoading(false);
    }, 2000);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  const handleActionClick = (action) => {
    setInputValue(action);
    setShowQuickActions(false);
  };

  const quickActions = [
    'What are the Five Pillars of Islam?',
    'How do I perform wudu?',
    'What does the Quran say about charity?',
    'How do I pray the five daily prayers?',
    'What are the conditions for fasting in Ramadan?',
    'How do I find the Qibla direction?',
    'What are the benefits of reading the Quran?',
    'How do I greet other Muslims?'
  ];

  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8 animate-fade-in">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <Logo size={64} />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            DeenBot - Islamic AI Assistant
          </h1>
          <p className="text-slate-300 text-lg">
            Ask me anything about Islam, Quran, Hadith, or Islamic practices
          </p>
          
          {/* NextEleven Donation Credit */}
          <div className="mt-4 p-3 bg-calm-surface border border-calm-border rounded-lg inline-block">
            <p className="text-sm text-teal-400">
              DeenBot donated by <span className="font-semibold">NextEleven</span>
            </p>
          </div>
        </div>

        {/* Quick Actions */}
        <QuickActions onActionClick={handleActionClick} />

        {/* Chat Interface */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <MessageCircle className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Chat with DeenBot</h2>
          </div>
          
          {/* Messages - Fixed height and scrolling */}
          <div className="space-y-4 mb-4 h-96 overflow-y-auto pr-2">
            {messages.length === 0 ? (
              <div className="text-center py-8 text-slate-400">
                <MessageCircle className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Start a conversation by asking a question about Islam</p>
              </div>
            ) : (
              messages.map((message) => (
                <div
                  key={message.id}
                  className={`flex gap-3 ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  {message.sender === 'bot' && (
                    <div className="w-8 h-8 bg-teal-600 rounded-full flex items-center justify-center flex-shrink-0">
                      <MessageCircle className="w-4 h-4 text-white" />
                    </div>
                  )}
                  <div
                    className={`max-w-xs lg:max-w-md px-4 py-3 rounded-lg ${
                      message.sender === 'user'
                        ? 'bg-teal-600 text-white'
                        : 'bg-calm-surface border border-calm-border text-slate-200'
                    }`}
                  >
                    <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.text}</p>
                    <p className={`text-xs mt-2 ${
                      message.sender === 'user' ? 'text-teal-100' : 'text-slate-400'
                    }`}>
                      {message.timestamp}
                    </p>
                  </div>
                  {message.sender === 'user' && (
                    <div className="w-8 h-8 bg-green-600 rounded-full flex items-center justify-center flex-shrink-0">
                      <User className="w-4 h-4 text-white" />
                    </div>
                  )}
                </div>
              ))
            )}
            {isLoading && (
              <div className="flex gap-3 justify-start">
                <div className="w-8 h-8 bg-teal-600 rounded-full flex items-center justify-center">
                  <MessageCircle className="w-4 h-4 text-white" />
                </div>
                <div className="bg-calm-surface border border-calm-border px-4 py-3 rounded-lg">
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-teal-400 rounded-full animate-pulse"></div>
                    <div className="w-2 h-2 bg-teal-400 rounded-full animate-pulse animation-delay-200"></div>
                    <div className="w-2 h-2 bg-teal-400 rounded-full animate-pulse animation-delay-400"></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Verification Disclaimer */}
          <div className="mb-4 p-4 bg-gradient-to-r from-blue-600/20 to-teal-600/20 border border-blue-500/30 rounded-lg">
            <div className="flex items-start gap-3">
              <Info className="w-5 h-5 text-blue-400 mt-0.5 flex-shrink-0" />
              <div className="text-sm text-slate-300">
                <p className="mb-2">
                  <strong>Our intent Insha Allah, is for correct authenticated knowledge base.</strong> 
                  DeenBot can make mistakes, please verify the sources given.
                </p>
                <p>
                  <strong>DeenBot knowledge base must be able to answer modern questions from Muslims around the world.</strong> 
                  Every answer must be backed up with authentic source the user can verify.
                </p>
              </div>
            </div>
          </div>

          {/* Input */}
          <div className="flex gap-3">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask DeenBot about Quran, Hadith, prayer, or any religious question..."
              className="flex-1 bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
              disabled={isLoading}
            />
            <button
              onClick={handleSendMessage}
              disabled={isLoading || !inputValue.trim()}
              className="bg-gradient-to-r from-teal-600 to-green-600 hover:from-teal-700 hover:to-green-700 text-white px-6 py-3 rounded-lg font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-teal-glow"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Example Questions */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6">
          <h3 className="text-lg font-semibold text-teal-200 mb-4">Example Questions for DeenBot</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {quickActions.map((question, index) => (
              <button
                key={index}
                onClick={() => setInputValue(question)}
                className="text-left p-3 bg-calm-surface border border-calm-border rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm"
              >
                {question}
              </button>
            ))}
          </div>
        </div>

        {/* Features Overview */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <BookOpen className="w-12 h-12 text-teal-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Authentic Sources</h3>
            <p className="text-slate-300 text-sm">
              All answers backed by Quran, Hadith, and scholarly sources
            </p>
          </div>
          
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <Globe className="w-12 h-12 text-green-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Global Knowledge</h3>
            <p className="text-slate-300 text-sm">
              Answers questions from Muslims around the world
            </p>
          </div>
          
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <CheckCircle className="w-12 h-12 text-teal-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Verification Ready</h3>
            <p className="text-slate-300 text-sm">
              Sources provided for every answer to verify authenticity
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

const QuickActions = ({ onActionClick }) => {
  const actions = [
    {
      title: 'Islamic Basics',
      description: 'Learn fundamental Islamic concepts',
      icon: <BookOpen className="w-6 h-6" />,
      questions: [
        'What are the Five Pillars of Islam?',
        'What is the Shahada?',
        'How do I become a Muslim?'
      ]
    },
    {
      title: 'Prayer & Worship',
      description: 'Guidance on Islamic worship',
      icon: <Clock className="w-6 h-6" />,
      questions: [
        'How do I perform wudu?',
        'What are the prayer times?',
        'How do I pray correctly?'
      ]
    },
    {
      title: 'Quran & Hadith',
      description: 'Study Islamic texts',
      icon: <FileText className="w-6 h-6" />,
      questions: [
        'What does the Quran say about charity?',
        'How do I read the Quran?',
        'What are authentic Hadith sources?'
      ]
    },
    {
      title: 'Daily Life',
      description: 'Islamic guidance for daily activities',
      icon: <Users className="w-6 h-6" />,
      questions: [
        'How do I greet other Muslims?',
        'What is halal food?',
        'How do I dress modestly?'
      ]
    }
  ];

  return (
    <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
      <h3 className="text-lg font-semibold text-teal-200 mb-4">Quick Start - Choose a Topic</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {actions.map((action, index) => (
          <div key={index} className="bg-calm-surface border border-calm-border rounded-lg p-4">
            <div className="flex items-center gap-3 mb-3">
              <div className="w-10 h-10 bg-teal-600/20 rounded-lg flex items-center justify-center text-teal-400">
                {action.icon}
              </div>
              <div>
                <h4 className="font-semibold text-teal-200 text-sm">{action.title}</h4>
                <p className="text-xs text-slate-400">{action.description}</p>
              </div>
            </div>
            <div className="space-y-2">
              {action.questions.map((question, qIndex) => (
                <button
                  key={qIndex}
                  onClick={() => onActionClick(question)}
                  className="w-full text-left p-2 bg-calm-bg border border-calm-border rounded text-xs text-slate-300 hover:text-teal-200 hover:bg-calm-bg/80 transition-all duration-200"
                >
                  {question}
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default IslamicChatbot;
