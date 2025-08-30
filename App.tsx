import React, { useState } from 'react';
import { Menu, X, BookOpen, MessageCircle, Calendar, Star, Clock, Users, Heart, Globe, Search, Home, ChevronRight } from 'lucide-react';
import IslamicChatbot from './src/components/IslamicChatbot';
import DailyMessage from './src/components/DailyMessage';
import NewMuslim from './src/components/NewMuslim';
import PrayerGuide from './src/components/PrayerGuide';
import FiqhBrowser from './src/components/FiqhBrowser';
import QuranContent from './src/components/QuranContent';
import HadithContent from './src/components/HadithContent';
import Logo from './src/components/Logo';

const App = () => {
  const [activeTab, setActiveTab] = useState('deenbot');
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Navigation structure with all available information
  const navigationItems = [
    {
      id: 'deenbot',
      title: 'DeenBot AI',
      subtitle: 'Islamic AI Assistant',
      icon: <MessageCircle className="w-5 h-5" />,
      description: 'Ask questions about Islam, Quran, Hadith, and Islamic practices'
    },
    {
      id: 'daily-messages',
      title: 'Daily Messages',
      subtitle: 'Daily Wisdom & Inspiration',
      icon: <Calendar className="w-5 h-5" />,
      description: 'Daily Islamic wisdom, Quran verses, and Hadiths for spiritual growth'
    },
    {
      id: 'new-muslim',
      title: 'New Muslim Guide',
      subtitle: 'Essential Guidance',
      icon: <Star className="w-5 h-5" />,
      description: 'Complete guide for new Muslims: Shahada, prayer, wudu, and essential knowledge'
    },
    {
      id: 'prayer-guide',
      title: 'Prayer Guide',
      subtitle: 'Complete Prayer Instructions',
      icon: <Clock className="w-5 h-5" />,
      description: 'How to pray, wudu guide, prayer times, duas, and Qibla direction'
    },
    {
      id: 'fiqh-browser',
      title: 'Fiqh Knowledge Base',
      subtitle: 'Islamic Jurisprudence',
      icon: <BookOpen className="w-5 h-5" />,
      description: 'Comprehensive Islamic legal rulings and scholarly opinions (Download Required)'
    },
    {
      id: 'quran-content',
      title: 'Complete Quran',
      subtitle: 'With Tafsir & Audio',
      icon: <BookOpen className="w-5 h-5" />,
      description: 'Complete Quran with Arabic text, translations, and commentary (Download Required)'
    },
    {
      id: 'hadith-content',
      title: 'Hadith Collections',
      subtitle: 'Authentic Narrations',
      icon: <BookOpen className="w-5 h-5" />,
      description: 'Complete Hadith collections from major authentic sources (Download Required)'
    }
  ];

  const renderContent = () => {
    switch (activeTab) {
      case 'deenbot':
        return <IslamicChatbot />;
      case 'daily-messages':
        return <DailyMessage />;
      case 'new-muslim':
        return <NewMuslim />;
      case 'prayer-guide':
        return <PrayerGuide />;
      case 'fiqh-browser':
        return <FiqhBrowser />;
      case 'quran-content':
        return <QuranContent />;
      case 'hadith-content':
        return <HadithContent />;
      default:
        return <IslamicChatbot />;
    }
  };

  const getActiveItem = () => {
    return navigationItems.find(item => item.id === activeTab) || navigationItems[0];
  };

  return (
    <div className="min-h-screen bg-calm-bg text-slate-100">
      {/* Mobile Sidebar Toggle */}
      <div className="lg:hidden fixed top-4 left-4 z-50">
        <button
          onClick={() => setSidebarOpen(!sidebarOpen)}
          className="bg-calm-card border border-calm-border p-2 rounded-lg text-teal-300 hover:text-teal-200 transition-colors"
        >
          {sidebarOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
        </button>
      </div>

      {/* Sidebar */}
      <div className={`fixed inset-y-0 left-0 z-40 w-80 bg-calm-card border-r border-calm-border transform transition-transform duration-300 ease-in-out lg:translate-x-0 ${
        sidebarOpen ? 'translate-x-0' : '-translate-x-full'
      }`}>
        {/* Logo and Header */}
        <div className="p-6 border-b border-calm-border">
          <div className="flex items-center gap-4">
            <Logo size={48} />
            <div>
              <h1 className="text-xl font-bold text-teal-300 font-islamic">Islamic Study Guide</h1>
              <p className="text-xs text-slate-400">Complete Islamic Knowledge</p>
            </div>
          </div>
        </div>

        {/* Navigation Items */}
        <nav className="flex-1 overflow-y-auto p-4">
          <div className="space-y-2">
            {navigationItems.map((item) => (
              <button
                key={item.id}
                onClick={() => {
                  setActiveTab(item.id);
                  setSidebarOpen(false);
                }}
                className={`w-full text-left p-4 rounded-lg transition-all duration-200 group ${
                  activeTab === item.id
                    ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                    : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                }`}
              >
                <div className="flex items-start gap-3">
                  <div className={`p-2 rounded-lg ${
                    activeTab === item.id
                      ? 'bg-teal-600/20 text-teal-300'
                      : 'bg-calm-bg text-slate-400 group-hover:text-teal-300'
                  }`}>
                    {item.icon}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="font-semibold text-sm mb-1">{item.title}</div>
                    <div className="text-xs text-slate-400 mb-2">{item.subtitle}</div>
                    <p className="text-xs text-slate-500 leading-relaxed">{item.description}</p>
                  </div>
                  <ChevronRight className={`w-4 h-4 text-slate-400 transition-transform ${
                    activeTab === item.id ? 'rotate-90' : 'group-hover:translate-x-1'
                  }`} />
                </div>
              </button>
            ))}
          </div>
        </nav>

        {/* Footer */}
        <div className="p-4 border-t border-calm-border">
          <div className="text-center text-xs text-slate-400">
            <p>Islamic Study Guide</p>
            <p className="mt-1">Complete Islamic Knowledge Base</p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className={`lg:ml-80 transition-all duration-300 ${sidebarOpen ? 'ml-80' : 'ml-0'}`}>
        {/* Top Bar */}
        <div className="bg-calm-card border-b border-calm-border p-4">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-semibold text-teal-200">{getActiveItem().title}</h2>
              <p className="text-sm text-slate-400">{getActiveItem().subtitle}</p>
            </div>
            <div className="flex items-center gap-4">
              <div className="hidden md:flex items-center gap-2 text-sm text-slate-400">
                <Globe className="w-4 h-4" />
                <span>Islamic Knowledge</span>
              </div>
            </div>
          </div>
        </div>

        {/* Content Area */}
        <main className="min-h-screen">
          {renderContent()}
        </main>
      </div>

      {/* Mobile Overlay */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-30 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}
    </div>
  );
};

export default App;

