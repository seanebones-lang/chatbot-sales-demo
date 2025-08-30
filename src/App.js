import React, { useState } from 'react';
import IslamicChatbot from './components/IslamicChatbot';
import FiqhBrowser from './components/FiqhBrowser';
import './App.css';

function App() {
  const [activeTab, setActiveTab] = useState('chatbot');

  const tabs = [
    { id: 'chatbot', name: 'AI Assistant', icon: '🤖' },
    { id: 'fiqh', name: 'Fiqh Knowledge', icon: '📚' },
    { id: 'quran', name: 'Quran & Tafsir', icon: '🕋' },
    { id: 'hadith', name: 'Hadith Collection', icon: '📖' },
    { id: 'prayer', name: 'Prayer Guide', icon: '🕌' },
    { id: 'daily', name: 'Daily Message', icon: '💬' },
    { id: 'new-muslim', name: 'New Muslim', icon: '❤️' },
    { id: 'islam-basics', name: 'Islam Basics', icon: '⭐' }
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
        return <PrayerContent />;
      case 'daily':
        return <DailyContent />;
      case 'new-muslim':
        return <NewMuslimContent />;
      case 'islam-basics':
        return <IslamBasicsContent />;
      default:
        return <IslamicChatbot />;
    }
  };

  return (
    <div className="App">
      {/* App Header */}
      <header className="bg-slate-800/90 backdrop-blur-sm border-b border-slate-700/30 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-br from-teal-400 to-teal-600 rounded-lg flex items-center justify-center">
                <span className="text-white text-lg">☪️</span>
              </div>
              <span className="text-xl font-bold text-teal-300">Islamic Guide App</span>
            </div>
            <div className="text-slate-400 text-sm">
              Complete Islamic Knowledge & AI Assistant
            </div>
          </div>
        </div>
      </header>

      {/* Tab Navigation */}
      <div className="bg-slate-800/50 border-b border-slate-700/30">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-1 overflow-x-auto pb-2">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center space-x-2 px-4 py-3 rounded-lg text-sm font-medium whitespace-nowrap transition-all duration-200 ${
                  activeTab === tab.id
                    ? 'bg-teal-700/50 text-teal-300 border border-teal-600/50'
                    : 'text-slate-400 hover:bg-slate-700/50 hover:text-slate-200'
                }`}
              >
                <span className="text-lg">{tab.icon}</span>
                <span>{tab.name}</span>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="min-h-screen bg-slate-900">
        {renderContent()}
      </main>
    </div>
  );
}

// Content Components
const QuranContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Quran & Tafsir</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Complete Quran with translations, tafsir, and memorization tools
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Complete Quran</h3>
          <p className="text-slate-300">Full Quran text with multiple translations</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Tafsir</h3>
          <p className="text-slate-300">Detailed explanations and interpretations</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Memorization</h3>
          <p className="text-slate-300">Tools and techniques for Quran memorization</p>
        </div>
      </div>
    </div>
  </div>
);

const HadithContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Hadith Collection</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Authentic Hadith collections with detailed explanations
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Sahih Bukhari</h3>
          <p className="text-slate-300">Most authentic Hadith collection</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Sahih Muslim</h3>
          <p className="text-slate-300">Second most authentic collection</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Other Collections</h3>
          <p className="text-slate-300">Abu Dawud, Tirmidhi, and more</p>
        </div>
      </div>
    </div>
  </div>
);

const PrayerContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Prayer Guide</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Complete guide to Islamic prayer, times, and procedures
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Prayer Times</h3>
          <p className="text-slate-300">Daily prayer schedules and calculations</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Prayer Procedures</h3>
          <p className="text-slate-300">Step-by-step prayer instructions</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Wudu Guide</h3>
          <p className="text-slate-300">Ablution procedures and requirements</p>
        </div>
      </div>
    </div>
  </div>
);

const DailyContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Daily Islamic Message</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Daily wisdom, reminders, and Islamic teachings
      </p>
      <div className="bg-slate-700/30 p-8 rounded-lg border border-slate-600/30">
        <h3 className="text-2xl font-semibold text-teal-300 mb-4">Today's Message</h3>
        <p className="text-slate-300 text-lg leading-relaxed">
          "The best of you are those who are best to their families, and I am the best of you to my family."
        </p>
        <p className="text-teal-400 mt-4 text-sm">- Prophet Muhammad (ﷺ)</p>
      </div>
    </div>
  </div>
);

const NewMuslimContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Guide for New Muslims</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Essential knowledge and guidance for those new to Islam
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Getting Started</h3>
          <p className="text-slate-300">Basic steps and first prayers</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Essential Knowledge</h3>
          <p className="text-slate-300">Core beliefs and practices</p>
        </div>
      </div>
    </div>
  </div>
);

const IslamBasicsContent = () => (
  <div className="max-w-6xl mx-auto p-6">
    <div className="bg-slate-800/30 border border-slate-700/30 rounded-xl p-8">
      <h1 className="text-4xl font-bold text-teal-300 mb-6 text-center">Islam Basics</h1>
      <p className="text-slate-300 text-lg text-center mb-8">
        Fundamental concepts and introduction to Islam
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">What is Islam</h3>
          <p className="text-slate-300">Introduction and core concepts</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Five Pillars</h3>
          <p className="text-slate-300">Core Islamic practices</p>
        </div>
        <div className="bg-slate-700/30 p-6 rounded-lg border border-slate-600/30">
          <h3 className="text-xl font-semibold text-teal-300 mb-3">Islamic Values</h3>
          <p className="text-slate-300">Moral and ethical principles</p>
        </div>
      </div>
    </div>
  </div>
);

export default App;
