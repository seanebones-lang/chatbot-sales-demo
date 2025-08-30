import React, { useState, useEffect } from 'react';
import { Calendar, BookOpen, Search, FileText, Bookmark, Share2, Heart, Star, Clock, Users } from 'lucide-react';

const DailyMessage = () => {
  const [currentMessage, setCurrentMessage] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  // Daily messages content - directly integrated
  const dailyMessages = [
    {
      id: 1,
      date: 'Today',
      title: 'The Power of Gratitude',
      category: 'Spiritual Growth',
      content: 'Allah says in the Quran: "If you are grateful, I will surely increase you [in favor]." (Quran 14:7) Gratitude is not just saying thank you, but living with appreciation for every blessing.',
      quranVerse: 'فَإِنَّ اللَّهَ شَاكِرٌ عَلِيمٌ',
      quranTranslation: 'Indeed, Allah is Appreciative and Knowing.',
      quranReference: 'Quran 2:158',
      hadith: 'The Prophet Muhammad sallallahu alayhi wa sallam said: "Whoever is not grateful to people is not grateful to Allah."',
      hadithReference: 'Sahih Bukhari',
      application: 'Practice gratitude by thanking Allah for three things before sleeping each night.',
      tags: ['Gratitude', 'Quran', 'Hadith', 'Daily Practice']
    },
    {
      id: 2,
      date: 'Yesterday',
      title: 'Patience in Adversity',
      category: 'Character Building',
      content: 'Patience is one of the most beautiful qualities praised in Islam. Allah loves those who are patient and promises great rewards for those who persevere through difficulties.',
      quranVerse: 'إِنَّ اللَّهَ مَعَ الصَّابِرِينَ',
      quranTranslation: 'Indeed, Allah is with the patient.',
      quranReference: 'Quran 2:153',
      hadith: 'The Prophet Muhammad sallallahu alayhi wa sallam said: "Patience is light."',
      hadithReference: 'Sahih Muslim',
      application: 'When facing a challenge today, remind yourself that Allah is with you and this too shall pass.',
      tags: ['Patience', 'Adversity', 'Faith', 'Perseverance']
    },
    {
      id: 3,
      date: 'Two Days Ago',
      title: 'The Beauty of Sadaqah',
      category: 'Charity',
      content: 'Charity in Islam is not just about money. A smile, kind words, helping others, and even removing harmful objects from the path are all forms of charity.',
      quranVerse: 'مَثَلُ الَّذِينَ يُنفِقُونَ أَمْوَالَهُمْ فِي سَبِيلِ اللَّهِ كَمَثَلِ حَبَّةٍ أَنبَتَتْ سَبْعَ سَنَابِلَ',
      quranTranslation: 'The example of those who spend their wealth in the way of Allah is like a seed which grows seven spikes.',
      quranReference: 'Quran 2:261',
      hadith: 'The Prophet Muhammad sallallahu alayhi wa sallam said: "Charity does not decrease wealth."',
      hadithReference: 'Sahih Muslim',
      application: 'Perform one act of charity today, whether it\'s giving money, helping someone, or just offering a kind word.',
      tags: ['Charity', 'Giving', 'Wealth', 'Kindness']
    },
    {
      id: 4,
      date: 'Three Days Ago',
      title: 'The Importance of Knowledge',
      category: 'Education',
      content: 'Seeking knowledge is a duty upon every Muslim. The Prophet Muhammad sallallahu alayhi wa sallam emphasized the importance of education and learning throughout his life.',
      quranVerse: 'يَرْفَعِ اللَّهُ الَّذِينَ آمَنُوا مِنكُمْ وَالَّذِينَ أُوتُوا الْعِلْمَ دَرَجَاتٍ',
      quranTranslation: 'Allah will raise those who have believed among you and those who were given knowledge, by degrees.',
      quranReference: 'Quran 58:11',
      hadith: 'The Prophet Muhammad sallallahu alayhi wa sallam said: "Seeking knowledge is obligatory upon every Muslim."',
      hadithReference: 'Ibn Majah',
      application: 'Learn something new about Islam today - read a verse, study a hadith, or learn about Islamic history.',
      tags: ['Knowledge', 'Learning', 'Education', 'Growth']
    },
    {
      id: 5,
      date: 'Four Days Ago',
      title: 'The Power of Dua',
      category: 'Worship',
      content: 'Dua (supplication) is the essence of worship. Allah loves when His servants call upon Him and has promised to answer the prayers of those who call upon Him sincerely.',
      quranVerse: 'وَقَالَ رَبُّكُمُ ادْعُونِي أَسْتَجِبْ لَكُمْ',
      quranTranslation: 'And your Lord says, "Call upon Me; I will respond to you."',
      quranReference: 'Quran 40:60',
      hadith: 'The Prophet Muhammad sallallahu alayhi wa sallam said: "Dua is worship."',
      hadithReference: 'Abu Dawud',
      application: 'Make dua for yourself, your family, and the Ummah today. Remember that Allah hears every prayer.',
      tags: ['Dua', 'Prayer', 'Worship', 'Supplication']
    }
  ];

  const categories = ['all', 'Spiritual Growth', 'Character Building', 'Charity', 'Education', 'Worship', 'Family', 'Community'];

  useEffect(() => {
    // Set today's message as current
    setCurrentMessage(dailyMessages[0]);
  }, []);

  const filteredMessages = dailyMessages.filter(message =>
    (selectedCategory === 'all' || message.category === selectedCategory) &&
    (message.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
     message.content.toLowerCase().includes(searchTerm.toLowerCase()) ||
     message.tags.some(tag => tag.toLowerCase().includes(searchTerm.toLowerCase())))
  );

  const handleMessageSelect = (message) => {
    setCurrentMessage(message);
  };

  const handleCategoryFilter = (category) => {
    setSelectedCategory(category);
    setSearchTerm('');
  };

  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <Calendar className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            Daily Islamic Messages
          </h1>
          <p className="text-slate-300 text-lg">
            Daily wisdom, Quran verses, and Hadiths for spiritual growth and inspiration
          </p>
        </div>

        {/* Today's Featured Message */}
        {currentMessage && (
          <div className="bg-calm-card border border-calm-border rounded-xl p-8 mb-6">
            <div className="text-center mb-6">
              <div className="text-sm text-teal-400 mb-2">{currentMessage.date}</div>
              <h2 className="text-2xl font-semibold text-teal-200 mb-4">{currentMessage.title}</h2>
              <div className="inline-block bg-teal-600/20 text-teal-300 px-3 py-1 rounded-full text-sm mb-4">
                {currentMessage.category}
              </div>
            </div>
            
            <div className="text-slate-300 text-lg leading-relaxed mb-6 text-center">
              {currentMessage.content}
            </div>

            {/* Quran Verse */}
            <div className="bg-calm-surface border border-calm-border rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-teal-200 mb-3 text-center">Quran Verse</h3>
              <div className="text-right text-2xl text-teal-200 mb-3 font-arabic leading-relaxed">
                {currentMessage.quranVerse}
              </div>
              <div className="text-slate-300 text-center mb-2 italic">
                {currentMessage.quranTranslation}
              </div>
              <div className="text-teal-400 text-sm text-center">{currentMessage.quranReference}</div>
            </div>

            {/* Hadith */}
            <div className="bg-calm-surface border border-calm-border rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-teal-200 mb-3 text-center">Hadith</h3>
              <div className="text-slate-300 text-center mb-3 italic">
                {currentMessage.hadith}
              </div>
              <div className="text-teal-400 text-sm text-center">{currentMessage.hadithReference}</div>
            </div>

            {/* Practical Application */}
            <div className="bg-gradient-to-r from-teal-600/20 to-green-600/20 border border-teal-500/30 rounded-lg p-6 mb-6">
              <h3 className="text-lg font-semibold text-teal-200 mb-3 text-center">Today's Application</h3>
              <div className="text-slate-300 text-center">
                {currentMessage.application}
              </div>
            </div>

            {/* Tags */}
            <div className="flex flex-wrap justify-center gap-2">
              {currentMessage.tags.map((tag, index) => (
                <span key={index} className="bg-calm-surface border border-calm-border px-3 py-1 rounded-full text-xs text-teal-300">
                  {tag}
                </span>
              ))}
            </div>

            {/* Quick Actions */}
            <div className="flex justify-center gap-4 mt-6">
              <button className="flex items-center gap-2 bg-calm-surface border border-calm-border px-4 py-2 rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200">
                <Bookmark className="w-4 h-4" />
                Bookmark
              </button>
              <button className="flex items-center gap-2 bg-calm-surface border border-calm-border px-4 py-2 rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200">
                <Share2 className="w-4 h-4" />
                Share
              </button>
              <button className="flex items-center gap-2 bg-calm-surface border border-calm-border px-4 py-2 rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200">
                <Heart className="w-4 h-4" />
                Like
              </button>
            </div>
          </div>
        )}

        {/* Search and Filter */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search Messages</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="Search for topics, verses, or keywords..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
            />
            <div className="flex flex-wrap gap-2">
              {categories.map((category) => (
                <button
                  key={category}
                  onClick={() => handleCategoryFilter(category)}
                  className={`px-3 py-2 rounded-lg text-sm transition-all duration-200 ${
                    selectedCategory === category
                      ? 'bg-teal-600 text-white'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  {category === 'all' ? 'All Categories' : category}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Message Archive */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6">
          <h3 className="text-lg font-semibold text-teal-200 mb-4">Message Archive</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filteredMessages.map((message) => (
              <div
                key={message.id}
                onClick={() => handleMessageSelect(message)}
                className="bg-calm-surface border border-calm-border rounded-lg p-4 cursor-pointer transition-all duration-200 hover:border-teal-500/30 hover:bg-calm-surface/80"
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="text-xs text-slate-400">{message.date}</div>
                  <div className="text-xs text-teal-400 bg-teal-600/20 px-2 py-1 rounded">
                    {message.category}
                  </div>
                </div>
                <h4 className="font-medium text-teal-200 mb-2">{message.title}</h4>
                <p className="text-slate-300 text-sm mb-3 line-clamp-3">
                  {message.content}
                </p>
                <div className="flex flex-wrap gap-1">
                  {message.tags.slice(0, 3).map((tag, index) => (
                    <span key={index} className="text-xs text-slate-400 bg-calm-bg px-2 py-1 rounded">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quick Stats */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-4 gap-4">
          <div className="bg-calm-card border border-calm-border rounded-xl p-4 text-center">
            <div className="text-2xl font-bold text-teal-400">{dailyMessages.length}</div>
            <div className="text-sm text-slate-400">Total Messages</div>
          </div>
          <div className="bg-calm-card border border-calm-border rounded-xl p-4 text-center">
            <div className="text-2xl font-bold text-teal-400">{categories.length - 1}</div>
            <div className="text-sm text-slate-400">Categories</div>
          </div>
          <div className="bg-calm-card border border-calm-border rounded-xl p-4 text-center">
            <div className="text-2xl font-bold text-teal-400">Daily</div>
            <div className="text-sm text-slate-400">Updates</div>
          </div>
          <div className="bg-calm-card border border-calm-border rounded-xl p-4 text-center">
            <div className="text-2xl font-bold text-teal-400">24/7</div>
            <div className="text-sm text-slate-400">Available</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DailyMessage;
