import React, { useState, useEffect } from 'react';
import { Clock, MapPin, BookOpen, Search, FileText, Bookmark, Share2, Play, Volume2, Users, Calendar } from 'lucide-react';

const PrayerGuide = () => {
  const [currentTime, setCurrentTime] = useState(new Date());
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTopic, setSelectedTopic] = useState('prayer-times');
  const [selectedContent, setSelectedContent] = useState(null);

  // Prayer content - directly integrated
  const prayerContent = {
    'prayer-times': {
      title: 'Prayer Times',
      arabicTitle: 'أوقات الصلاة',
      description: 'Daily prayer schedule and timing calculations',
      content: [
        {
          id: 'fajr',
          title: 'Fajr (Dawn Prayer)',
          time: 'Before sunrise',
          arabic: 'الفجر',
          description: 'The first prayer of the day, performed at dawn before the sun rises',
          evidence: 'Quran 17:78, Hadith from Sahih Bukhari',
          benefits: 'Blessed time for dua, spiritual awakening, and starting the day with Allah\'s remembrance'
        },
        {
          id: 'dhuhr',
          title: 'Dhuhr (Noon Prayer)',
          time: 'After sun passes zenith',
          arabic: 'الظهر',
          description: 'The second prayer, performed when the sun has passed its highest point',
          evidence: 'Quran 4:103, Hadith from Sahih Muslim',
          benefits: 'Break from daily activities, spiritual refreshment, and seeking Allah\'s guidance'
        },
        {
          id: 'asr',
          title: 'Asr (Afternoon Prayer)',
          time: 'Mid-afternoon',
          arabic: 'العصر',
          description: 'The third prayer, performed in the afternoon',
          evidence: 'Quran 2:238, Hadith from Sahih Bukhari',
          benefits: 'Maintaining spiritual connection throughout the day'
        },
        {
          id: 'maghrib',
          title: 'Maghrib (Sunset Prayer)',
          time: 'After sunset',
          arabic: 'المغرب',
          description: 'The fourth prayer, performed immediately after the sun sets',
          evidence: 'Quran 11:114, Hadith from Sahih Muslim',
          benefits: 'Gratitude for the day, seeking forgiveness, and preparing for evening'
        },
        {
          id: 'isha',
          title: 'Isha (Night Prayer)',
          time: 'Night time',
          arabic: 'العشاء',
          description: 'The fifth and final prayer of the day, performed at night',
          evidence: 'Quran 24:58, Hadith from Sahih Bukhari',
          benefits: 'Ending the day with Allah\'s remembrance and seeking His protection'
        }
      ]
    },
    'how-to-pray': {
      title: 'How to Pray',
      arabicTitle: 'كيفية الصلاة',
      description: 'Step-by-step prayer guide with proper movements and recitations',
      content: [
        {
          id: 'prayer-steps',
          title: 'Complete Prayer Steps',
          explanation: 'Islamic prayer involves specific physical positions and spiritual states',
          steps: [
            'Make intention (niyyah) for the specific prayer',
            'Stand facing the Qibla (direction of Kaaba)',
            'Raise hands to ears and say "Allahu Akbar"',
            'Place right hand over left on chest',
            'Recite Al-Fatiha and additional surah',
            'Say "Allahu Akbar" and bow (Ruku)',
            'Stand up saying "Sami Allahu liman hamidah"',
            'Prostrate (Sujood) saying "Allahu Akbar"',
            'Sit between prostrations (Jalsa)',
            'Complete the required number of units (Rak\'ah)',
            'End with Tashahhud and Salam'
          ],
          evidence: 'Hadith from Sahih Bukhari and Muslim'
        }
      ]
    },
    'wudu': {
      title: 'Wudu (Ablution)',
      arabicTitle: 'الوضوء',
      description: 'Complete wudu procedure and requirements for prayer',
      content: [
        {
          id: 'wudu-steps',
          title: 'Steps of Wudu',
          explanation: 'Wudu is the ritual washing performed before prayer to achieve spiritual and physical cleanliness',
          steps: [
            'Make intention (niyyah) for wudu',
            'Say "Bismillah" (In the name of Allah)',
            'Wash hands three times up to wrists',
            'Rinse mouth three times with water',
            'Sniff water into nostrils three times',
            'Wash face three times from hairline to chin',
            'Wash arms up to elbows three times',
            'Wipe head once with wet hands',
            'Wash feet up to ankles three times',
            'Recite the dua after completing wudu'
          ],
          evidence: 'Quran 5:6, Hadith from Sahih Bukhari and Muslim',
          nullifiers: [
            'Using the bathroom',
            'Passing gas',
            'Sleeping',
            'Losing consciousness',
            'Touching private parts',
            'Direct contact with opposite gender'
          ]
        }
      ]
    },
    'prayer-rules': {
      title: 'Prayer Rules',
      arabicTitle: 'أحكام الصلاة',
      description: 'Important rules and conditions for valid prayer',
      content: [
        {
          id: 'conditions',
          title: 'Conditions for Valid Prayer',
          explanation: 'Certain conditions must be met for prayer to be valid',
          conditions: [
            'Being Muslim',
            'Reaching the age of puberty',
            'Being mentally sound',
            'Being in a state of ritual purity (wudu)',
            'Praying at the correct time',
            'Facing the Qibla direction',
            'Covering the awrah (private parts)',
            'Having the intention to pray'
          ]
        },
        {
          id: 'nullifiers',
          title: 'Prayer Nullifiers',
          explanation: 'Actions that invalidate the prayer and require it to be repeated',
          nullifiers: [
            'Speaking intentionally during prayer',
            'Eating or drinking during prayer',
            'Laughing out loud during prayer',
            'Turning away from Qibla without valid reason',
            'Breaking wudu during prayer',
            'Missing essential prayer elements',
            'Performing prayer movements out of order'
          ]
        }
      ]
    },
    'duas': {
      title: 'Prayer Duas',
      arabicTitle: 'أدعية الصلاة',
      description: 'Essential duas for prayer and daily life',
      content: [
        {
          id: 'prayer-duas',
          title: 'Essential Prayer Duas',
          explanation: 'Important supplications to recite during and after prayer',
          duas: [
            {
              arabic: 'اللَّهُمَّ اغْفِرْ لِي وَارْحَمْنِي',
              translation: 'O Allah, forgive me and have mercy on me',
              usage: 'Recited during prostration'
            },
            {
              arabic: 'سُبْحَانَ رَبِّيَ الْأَعْلَى',
              translation: 'Glory be to my Lord, the Most High',
              usage: 'Recited during prostration'
            },
            {
              arabic: 'سُبْحَانَ رَبِّيَ الْعَظِيمِ',
              translation: 'Glory be to my Lord, the Most Great',
              usage: 'Recited during bowing'
            },
            {
              arabic: 'رَبَّنَا لَكَ الْحَمْدُ',
              translation: 'Our Lord, to You is all praise',
              usage: 'Recited when standing up from bowing'
            }
          ]
        }
      ]
    },
    'qibla': {
      title: 'Qibla Direction',
      arabicTitle: 'اتجاه القبلة',
      description: 'Find the direction of the Kaaba for prayer',
      content: [
        {
          id: 'finding-qibla',
          title: 'How to Find Qibla Direction',
          explanation: 'The Qibla is the direction Muslims face during prayer, towards the Kaaba in Makkah',
          methods: [
            'Use a Qibla compass or app',
            'Face the direction of the sun at noon',
            'Use landmarks and maps',
            'Ask local Muslims or mosque officials',
            'Use online Qibla finder tools'
          ],
          evidence: 'Quran 2:144, Hadith from Sahih Bukhari',
          importance: 'Facing the Qibla is a requirement for valid prayer and symbolizes unity of the Muslim Ummah'
        }
      ]
    }
  };

  const topics = Object.keys(prayerContent);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const getNextPrayer = () => {
    // Simplified prayer times - in a real app, this would use actual prayer time calculations
    const currentHour = currentTime.getHours();
    if (currentHour < 6) return { name: 'Fajr', time: '05:30', next: 'Dhuhr' };
    if (currentHour < 12) return { name: 'Dhuhr', time: '12:30', next: 'Asr' };
    if (currentHour < 15) return { name: 'Asr', time: '15:45', next: 'Maghrib' };
    if (currentHour < 18) return { name: 'Maghrib', time: '18:15', next: 'Isha' };
    if (currentHour < 20) return { name: 'Isha', time: '19:45', next: 'Fajr' };
    return { name: 'Fajr', time: '05:30', next: 'Dhuhr' };
  };

  const filteredContent = prayerContent[selectedTopic]?.content?.filter(item =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    (item.description && item.description.toLowerCase().includes(searchTerm.toLowerCase())) ||
    (item.explanation && item.explanation.toLowerCase().includes(searchTerm.toLowerCase()))
  ) || [];

  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <BookOpen className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            Complete Prayer Guide
          </h1>
          <p className="text-slate-300 text-lg">
            Comprehensive guide to Islamic prayer, wudu, and spiritual practices
          </p>
        </div>

        {/* Current Time and Next Prayer */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center">
              <Clock className="w-8 h-8 text-teal-400 mx-auto mb-2" />
              <div className="text-2xl font-bold text-teal-300">
                {currentTime.toLocaleTimeString('en-US', { 
                  hour: '2-digit', 
                  minute: '2-digit',
                  hour12: true 
                })}
              </div>
              <div className="text-sm text-slate-400">Current Time</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-300">{getNextPrayer().name}</div>
              <div className="text-sm text-slate-400">Next Prayer</div>
              <div className="text-xs text-teal-400">{getNextPrayer().time}</div>
            </div>
            <div className="text-center">
              <MapPin className="w-8 h-8 text-teal-400 mx-auto mb-2" />
              <div className="text-sm text-slate-400">Qibla Direction</div>
              <div className="text-xs text-teal-400">Northeast</div>
            </div>
          </div>
        </div>

        {/* Search Bar */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search Prayer Topics</h2>
          </div>
          <input
            type="text"
            placeholder="Search for prayer topics, wudu steps, or duas..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
          />
        </div>

        {/* Content Display */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Topics List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Prayer Topics</h3>
            <div className="space-y-2">
              {topics.map((topic) => (
                <button
                  key={topic}
                  onClick={() => setSelectedTopic(topic)}
                  className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                    selectedTopic === topic
                      ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-teal-600/20 rounded-full flex items-center justify-center text-sm font-medium text-teal-300">
                      {prayerContent[topic].content.length}
                    </div>
                    <div>
                      <div className="font-medium text-sm">{prayerContent[topic].title}</div>
                      <div className="text-xs text-slate-400">{prayerContent[topic].arabicTitle}</div>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            {selectedTopic && (
              <div className="bg-calm-card border border-calm-border rounded-xl p-6">
                <div className="text-center mb-6">
                  <h2 className="text-2xl font-semibold text-teal-200 mb-2">
                    {prayerContent[selectedTopic].title}
                  </h2>
                  <div className="text-lg text-slate-300 mb-2">
                    {prayerContent[selectedTopic].arabicTitle}
                  </div>
                  <p className="text-slate-400">
                    {prayerContent[selectedTopic].description}
                  </p>
                </div>

                <div className="space-y-6">
                  {filteredContent.map((item) => (
                    <div key={item.id} className="bg-calm-surface border border-calm-border rounded-lg p-6">
                      <h3 className="text-xl font-semibold text-teal-200 mb-3">{item.title}</h3>
                      
                      {item.arabic && (
                        <div className="bg-calm-bg p-4 rounded-lg mb-4">
                          <div className="text-right text-xl text-teal-200 font-arabic leading-relaxed mb-2">
                            {item.arabic}
                          </div>
                          <div className="text-slate-300 italic text-center">
                            {item.translation}
                          </div>
                        </div>
                      )}

                      {item.time && (
                        <div className="bg-teal-600/20 border border-teal-500/30 rounded-lg p-4 mb-4">
                          <h4 className="font-semibold text-teal-200 mb-2">Prayer Time</h4>
                          <div className="text-slate-300 text-center">
                            <div className="text-lg font-medium">{item.time}</div>
                            <div className="text-sm">{item.description}</div>
                          </div>
                        </div>
                      )}

                      <div className="text-slate-300 leading-relaxed mb-4">
                        {item.explanation}
                      </div>

                      {item.evidence && (
                        <div className="bg-teal-600/20 border border-teal-500/30 rounded-lg p-4 mb-4">
                          <h4 className="font-semibold text-teal-200 mb-2">Evidence & Sources</h4>
                          <p className="text-slate-300 text-sm">{item.evidence}</p>
                        </div>
                      )}

                      {item.benefits && (
                        <div className="bg-green-600/20 border border-green-500/30 rounded-lg p-4 mb-4">
                          <h4 className="font-semibold text-green-200 mb-2">Benefits</h4>
                          <p className="text-slate-300 text-sm">{item.benefits}</p>
                        </div>
                      )}

                      {item.steps && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Steps to Follow</h4>
                          <ol className="list-decimal list-inside space-y-2">
                            {item.steps.map((step, index) => (
                              <li key={index} className="text-slate-300 text-sm">{step}</li>
                            ))}
                          </ol>
                        </div>
                      )}

                      {item.conditions && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Conditions</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.conditions.map((condition, index) => (
                              <li key={index} className="text-slate-300 text-sm">{condition}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.nullifiers && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-red-200 mb-3">Nullifiers</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.nullifiers.map((nullifier, index) => (
                              <li key={index} className="text-slate-300 text-sm">{nullifier}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.methods && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Methods</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.methods.map((method, index) => (
                              <li key={index} className="text-slate-300 text-sm">{method}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.duas && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Essential Duas</h4>
                          <div className="space-y-4">
                            {item.duas.map((dua, index) => (
                              <div key={index} className="bg-calm-bg p-4 rounded-lg border border-calm-border">
                                <div className="text-right text-lg text-teal-200 font-arabic leading-relaxed mb-2">
                                  {dua.arabic}
                                </div>
                                <div className="text-slate-300 italic text-center mb-2">
                                  {dua.translation}
                                </div>
                                <div className="text-teal-400 text-sm text-center">
                                  {dua.usage}
                                </div>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {item.importance && (
                        <div className="bg-blue-600/20 border border-blue-500/30 rounded-lg p-4 mb-4">
                          <h4 className="font-semibold text-blue-200 mb-2">Importance</h4>
                          <p className="text-slate-300 text-sm">{item.importance}</p>
                        </div>
                      )}

                      {/* Quick Actions */}
                      <div className="flex gap-2 mt-4">
                        <button className="flex items-center gap-2 bg-calm-surface border border-calm-border px-3 py-2 rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm">
                          <Bookmark className="w-4 h-4" />
                          Bookmark
                        </button>
                        <button className="flex items-center gap-2 bg-calm-surface border border-calm-border px-3 py-2 rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm">
                          <Share2 className="w-4 h-4" />
                          Share
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Quick Actions */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <Calendar className="w-12 h-12 text-teal-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Prayer Calendar</h3>
            <p className="text-slate-300 text-sm">
              Monthly prayer times and special prayer dates
            </p>
          </div>
          
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <Volume2 className="w-12 h-12 text-green-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Audio Adhan</h3>
            <p className="text-slate-300 text-sm">
              Listen to beautiful Adhan calls from around the world
            </p>
          </div>
          
          <div className="bg-calm-card border border-calm-border rounded-xl p-6 text-center">
            <Users className="w-12 h-12 text-teal-400 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-teal-200 mb-2">Prayer in Congregation</h3>
            <p className="text-slate-300 text-sm">
              Learn the rules and benefits of praying together
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PrayerGuide;
