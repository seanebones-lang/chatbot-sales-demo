import React, { useState, useRef, useEffect } from 'react';
import { Send, BookOpen, Heart, Globe, MessageCircle, Bot, User, Sparkles } from 'lucide-react';

const QuickActions = ({ onActionClick }) => {
  const actions = [
    {
      icon: <BookOpen className="w-6 h-6" />,
      title: "Quran Study",
      description: "Complete Quran with translations and tafsir",
      color: "from-teal-600 to-teal-700"
    },
    {
      icon: <Heart className="w-6 h-6" />,
      title: "Hadith Collection",
      description: "Explore authentic Hadith from major collections",
      color: "from-green-600 to-green-700"
    },
    {
      icon: <Globe className="w-6 h-6" />,
      title: "Islamic Resources",
      description: "Prayer times, halal guides, and more",
      color: "from-teal-700 to-teal-800"
    }
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      {actions.map((action, index) => (
        <div
          key={index}
          onClick={() => onActionClick(action.title)}
          className="bg-calm-card border border-calm-border rounded-xl p-6 cursor-pointer transition-all duration-300 hover:scale-105 hover:shadow-calm-lg group"
        >
          <div className={`w-12 h-12 rounded-lg bg-gradient-to-br ${action.color} flex items-center justify-center text-white mb-4 group-hover:shadow-lg transition-shadow duration-300`}>
            {action.icon}
          </div>
          <h3 className="text-xl font-semibold text-teal-200 mb-2">{action.title}</h3>
          <p className="text-slate-300 text-sm leading-relaxed">{action.description}</p>
        </div>
      ))}
    </div>
  );
};

const IslamicChatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showWelcome, setShowWelcome] = useState(true);
  const messagesEndRef = useRef(null);

  // Get the server URL based on environment
  const getServerUrl = () => {
    const hostname = window.location.hostname;
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
      return 'http://localhost:8080';
    } else {
      return 'http://165.232.155.246:8080';
    }
  };

  useEffect(() => {
    // Show welcome message after 2 seconds
    const timer = setTimeout(() => {
      setShowWelcome(false);
    }, 2000);

    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Connect to the real DeenBot backend
      const response = await fetch(`${getServerUrl()}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: inputValue,
          user_id: 'islamic_study_guide_user'
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      const botMessage = {
        id: Date.now() + 1,
        text: data.response || "I apologize, but I didn't receive a proper response. Please try again.",
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error connecting to DeenBot:', error);
      
      // Fallback response if backend is not available
      const fallbackResponse = getFallbackResponse(inputValue);
      
      const errorMessage = {
        id: Date.now() + 1,
        text: fallbackResponse,
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const getFallbackResponse = (userInput) => {
    const lowerInput = userInput.toLowerCase();
    
    if (lowerInput.includes('alcohol') || lowerInput.includes('drink') || lowerInput.includes('wine')) {
      return "In Islam, alcohol and intoxicants are strictly prohibited (haram). The Quran clearly states in Surah Al-Ma'idah (5:90): 'O you who have believed, indeed, intoxicants, gambling, [sacrificing on] stone alters [to other than Allah], and divining arrows are but defilement from the work of Satan, so avoid it that you may be successful.' The Prophet Muhammad sallallahu alayhi wa sallam also said: 'Every intoxicant is khamr (wine) and every khamr is haram (forbidden).' This prohibition extends to all forms of alcohol, drugs, and mind-altering substances. The wisdom behind this prohibition includes protecting one's health, maintaining clear judgment, avoiding harm to oneself and others, and preserving the dignity and respect of individuals and society.";
    }
    
    if (lowerInput.includes('quran') || lowerInput.includes('surah') || lowerInput.includes('ayah')) {
      return "The Quran is the holy book of Islam, revealed to Prophet Muhammad sallallahu alayhi wa sallam over 23 years through Angel Jibreel. It contains 114 surahs (chapters) and over 6,000 ayahs (verses). The Quran is the literal word of Allah, preserved exactly as revealed, and serves as the primary source of Islamic law and guidance. It covers all aspects of human life including faith, worship, morality, social justice, family life, business ethics, and spiritual development. The Quran is recited in Arabic during prayers and is memorized by millions of Muslims worldwide. Its teachings emphasize monotheism, compassion, justice, and the importance of good character. The Quran also contains stories of previous prophets, lessons from history, and guidance for building a just and peaceful society.";
    }
    
    if (lowerInput.includes('hadith') || lowerInput.includes('sunnah')) {
      return "Hadith are the sayings, actions, and approvals of Prophet Muhammad sallallahu alayhi wa sallam, collected and preserved by his companions and later scholars. They complement the Quran and provide detailed guidance on how to implement Islamic teachings in daily life. The most authentic collections include Sahih Bukhari, Sahih Muslim, Sunan Abu Dawud, Sunan Tirmidhi, Sunan Nasai, and Sunan Ibn Majah. Hadith cover topics like prayer, fasting, business ethics, family relations, social conduct, and spiritual development. Scholars classify hadith based on their authenticity (sahih, hasan, da'if) and transmission chains. The Prophet's life serves as the perfect example (uswa hasana) for Muslims to follow. His teachings emphasize kindness, honesty, justice, and compassion in all aspects of life.";
    }
    
    if (lowerInput.includes('prayer') || lowerInput.includes('salah') || lowerInput.includes('namaz')) {
      return "Salah (prayer) is one of the five pillars of Islam and is obligatory for all adult Muslims. Muslims pray five times daily: Fajr (dawn, before sunrise), Dhuhr (noon, after the sun passes its zenith), Asr (afternoon, mid-afternoon), Maghrib (sunset, immediately after sunset), and Isha (night, after twilight). Each prayer consists of specific movements and recitations in Arabic, including standing (qiyam), bowing (ruku), prostration (sujood), and sitting (jalsa). Prayer serves as a direct connection with Allah, provides spiritual discipline, and reminds Muslims of their purpose in life. The Prophet Muhammad sallallahu alayhi wa sallam said: 'The prayer is the pillar of religion, and whoever abandons it has destroyed his religion.' Prayer times vary by location and season, and Muslims use prayer time tables or apps to determine the correct times. The Friday prayer (Jumu'ah) is congregational and includes a sermon (khutbah).";
    }
    
    if (lowerInput.includes('ramadan') || lowerInput.includes('fasting')) {
      return "Ramadan is the ninth month of the Islamic lunar calendar and is considered the holiest month for Muslims. During Ramadan, Muslims fast from dawn (Fajr) to sunset (Maghrib), abstaining from food, drink, and marital relations. Fasting is one of the five pillars of Islam and is obligatory for all adult Muslims who are physically and mentally capable. The fast begins with suhoor (pre-dawn meal) and ends with iftar (breaking of the fast). Ramadan is a time of increased spiritual devotion, self-discipline, and community bonding. Muslims increase their prayers, recitation of the Quran, and acts of charity during this month. The Night of Power (Laylat al-Qadr) occurs during the last ten nights of Ramadan and is considered better than a thousand months of worship. The month ends with the celebration of Eid al-Fitr, a joyous festival of breaking the fast. Fasting teaches patience, gratitude, empathy for the less fortunate, and strengthens one's relationship with Allah.";
    }
    
    if (lowerInput.includes('charity') || lowerInput.includes('zakat') || lowerInput.includes('sadaqah')) {
      return "Charity in Islam takes several forms, with Zakat being the third pillar of Islam. Zakat is obligatory charity, typically 2.5% of one's wealth above the nisab (minimum threshold) that has been held for one lunar year. It is distributed to eight categories of recipients including the poor, needy, debtors, travelers, and those working to collect and distribute Zakat. Sadaqah is voluntary charity that can be given at any time and in any amount. The Prophet Muhammad sallallahu alayhi wa sallam emphasized the importance of charity, saying: 'Charity does not decrease wealth.' Charity purifies wealth, helps those in need, and strengthens community bonds. Muslims are encouraged to give charity secretly when possible, as this is more virtuous. The Quran states: 'If you disclose your charitable expenditures, they are good; but if you conceal them and give them to the poor, it is better for you.' Charity is not limited to money but can include time, skills, knowledge, and kind words.";
    }
    
    if (lowerInput.includes('prophet') || lowerInput.includes('muhammad')) {
      return "Prophet Muhammad sallallahu alayhi wa sallam is the final messenger of Allah, born in Makkah in 570 CE. He received the first revelation of the Quran at age 40 in the Cave of Hira and spent 23 years spreading the message of Islam. His life serves as the perfect example (uswa hasana) for Muslims to follow. The Prophet was known for his excellent character, honesty (earning the title 'Al-Amin' - the trustworthy), compassion, justice, and wisdom. He established the first Islamic community in Madinah, creating a constitution that guaranteed rights for all citizens regardless of religion. His teachings emphasize monotheism, social justice, women's rights, education, and care for the environment. The Prophet's final sermon at Mount Arafat during his last Hajj emphasized equality, justice, and the rights of women. He passed away in 632 CE in Madinah and is buried in the Prophet's Mosque. His life and teachings continue to guide over 1.8 billion Muslims worldwide, providing a comprehensive framework for living a righteous and fulfilling life.";
    }
    
    if (lowerInput.includes('islam') || lowerInput.includes('muslim')) {
      return "Islam means 'submission to Allah' and is a monotheistic Abrahamic religion that emphasizes peace, justice, and compassion. Muslims believe in one God (Allah) and follow the teachings of Prophet Muhammad sallallahu alayhi wa sallam. The five pillars of Islam are: Shahada (declaration of faith), Salah (prayer), Zakat (charity), Sawm (fasting during Ramadan), and Hajj (pilgrimage to Makkah). Islam teaches that all humans are equal before Allah and emphasizes the importance of good character, honesty, justice, and kindness. The religion promotes education, scientific inquiry, and social responsibility. Muslims believe in the Day of Judgment and accountability for one's actions. Islam encourages moderation in all aspects of life and teaches that the purpose of human existence is to worship Allah and serve humanity. The religion has contributed significantly to art, architecture, science, medicine, and philosophy throughout history. Islam promotes family values, community service, and environmental stewardship.";
    }
    
    return "I'm DeenBot, your Islamic AI assistant. I can help you with comprehensive knowledge about Islam, including Quran, Hadith, Islamic rulings, prayer, fasting, charity, and much more. Please ask me a specific question about any Islamic topic, and I'll provide you with detailed, authentic information based on Islamic sources. For example, you could ask about prayer times, halal food, Islamic ethics, the life of Prophet Muhammad sallallahu alayhi wa sallam, or any other aspect of Islamic faith and practice.";
  };

  const handleActionClick = (action) => {
    const actionMessage = {
      id: Date.now(),
      text: `I'd be happy to help you with ${action}! What specific aspect would you like to learn about? I can provide comprehensive information about Quran study, Hadith collections, Islamic resources, prayer guides, and much more. Just ask me a detailed question and I'll give you a complete answer based on authentic Islamic sources.`,
      sender: 'bot',
      timestamp: new Date().toLocaleTimeString()
    };
    setMessages(prev => [...prev, actionMessage]);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  if (showWelcome) {
    return (
      <div className="min-h-screen bg-calm-bg flex items-center justify-center">
        <div className="text-center animate-fade-in">
          <div className="w-24 h-24 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-6 animate-float">
            <Sparkles className="w-12 h-12 text-white" />
          </div>
          <h1 className="text-4xl font-bold text-teal-300 mb-4 font-islamic">
            As-salamu alaykum
          </h1>
          <p className="text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Welcome to your Islamic Study Guide. I'm DeenBot, your AI assistant, here to help you learn about Islam, 
            answer your questions, and guide you through the beautiful teachings of our faith.
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-calm-bg">
      <div className="max-w-4xl mx-auto p-6">
        {/* Header */}
        <div className="text-center mb-8 animate-fade-in">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <Bot className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            DeenBot - Islamic AI Assistant
          </h1>
          <p className="text-slate-300 text-lg">
            Ask me anything about Islam, Quran, Hadith, or Islamic practices
          </p>
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
                <Bot className="w-12 h-12 mx-auto mb-3 text-slate-500" />
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
                      <Bot className="w-4 h-4 text-white" />
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
                  <Bot className="w-4 h-4 text-white" />
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
            {[
              "What does the Quran say about charity?",
              "How do I perform wudu?",
              "What are the five pillars of Islam?",
              "Tell me about Prophet Muhammad's life",
              "What is the significance of Ramadan?",
              "How should I treat my neighbors in Islam?"
            ].map((question, index) => (
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
      </div>
    </div>
  );
};

export default IslamicChatbot;
