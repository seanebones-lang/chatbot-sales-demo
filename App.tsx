import React, { useState } from 'react';
import IslamicChatbot from './components/IslamicChatbot';
import FiqhBrowser from './components/FiqhBrowser';
import QuranContent from './components/QuranContent';
import HadithContent from './components/HadithContent';
import PrayerGuide from './components/PrayerGuide';
import DailyMessage from './components/DailyMessage';
import NewMuslim from './components/NewMuslim';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('chatbot');
  
  const tabs = [
    { id: 'chatbot', name: 'DeenBot AI', icon: '🤖' },
    { id: 'fiqh', name: 'Fiqh Knowledge', icon: '📚' },
    { id: 'quran', name: 'Quran Study', icon: '📖' },
    { id: 'hadith', name: 'Hadith Collection', icon: '💎' },
    { id: 'prayer', name: 'Prayer Guide', icon: '🕌' },
    { id: 'daily', name: 'Daily Message', icon: '📅' },
    { id: 'newmuslim', name: 'New Muslim', icon: '🌟' }
  ];

  const renderContent = () => {
    switch (activeTab) {
      case 'chatbot':
        return <IslamicChatbot />;
      case 'fiqh':
        return <FiqhBrowser />;
      case 'quran':
        return <QuranContent />;
      case 'hadith':
        return <HadithContent />;
      case 'prayer':
        return <PrayerGuide />;
      case 'daily':
        return <DailyMessage />;
      case 'newmuslim':
        return <NewMuslim />;
      default:
        return <IslamicChatbot />;
    }
  };

  return (
    <div className="App bg-calm-bg min-h-screen">
      {/* App Header */}
      <header className="bg-calm-surface/80 backdrop-blur-sm border-b border-calm-border sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-center">
            <h1 className="text-3xl font-bold text-teal-300 font-islamic">
              Islamic Study Guide
            </h1>
            <div className="ml-4 text-teal-400 text-lg">
              Complete Islamic Knowledge & DeenBot AI Assistant
            </div>
          </div>
        </div>
      </header>

      {/* Tab Navigation */}
      <div className="bg-calm-surface/60 border-b border-calm-border sticky top-20 z-40">
        <div className="max-w-7xl mx-auto px-4">
          <nav className="flex space-x-1 overflow-x-auto">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30 shadow-teal-glow'
                    : 'text-slate-300 hover:text-teal-200 hover:bg-calm-card/50'
                }`}
              >
                <span className="mr-2">{tab.icon}</span>
                {tab.name}
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <main className="min-h-screen bg-calm-bg">
        {renderContent()}
      </main>
    </div>
  );
}

export default App;

