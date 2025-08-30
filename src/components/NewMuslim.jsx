import React, { useState } from 'react';
import { Star, BookOpen, Search, FileText, Bookmark, Share2, Heart, Users, Clock, MapPin } from 'lucide-react';

const NewMuslim = () => {
  const [selectedSection, setSelectedSection] = useState('five-pillars');
  const [searchTerm, setSearchTerm] = useState('');

  // New Muslim content - directly integrated
  const newMuslimContent = {
    'five-pillars': {
      title: 'The Five Pillars of Islam',
      arabicTitle: 'أركان الإسلام الخمسة',
      description: 'The foundation of Islamic faith and practice',
      content: [
        {
          id: 'shahada',
          title: 'Shahada (Declaration of Faith)',
          arabic: 'أشهد أن لا إله إلا الله وأشهد أن محمداً رسول الله',
          translation: 'I bear witness that there is no god but Allah, and I bear witness that Muhammad is the Messenger of Allah',
          explanation: 'The Shahada is the first and most important pillar. It is the declaration that establishes one as a Muslim. This testimony must be recited with sincerity and understanding.',
          evidence: 'Quran 3:18, Hadith from Sahih Bukhari and Muslim',
          steps: [
            'Understand the meaning of the declaration',
            'Recite with sincerity and conviction',
            'Believe in the oneness of Allah',
            'Accept Prophet Muhammad as the final messenger'
          ]
        },
        {
          id: 'salah',
          title: 'Salah (Prayer)',
          arabic: 'الصلاة',
          translation: 'The five daily prayers',
          explanation: 'Salah is the second pillar and the most visible act of worship. Muslims pray five times daily to maintain their connection with Allah and seek His guidance.',
          evidence: 'Quran 4:103, Hadith from Sahih Bukhari and Muslim',
          steps: [
            'Learn the prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha)',
            'Learn how to perform wudu (ablution)',
            'Learn the prayer movements and recitations',
            'Establish regular prayer habits'
          ]
        },
        {
          id: 'zakat',
          title: 'Zakat (Charity)',
          arabic: 'الزكاة',
          translation: 'Obligatory charity',
          explanation: 'Zakat is the third pillar and means "purification." It is a mandatory charity that purifies wealth and helps those in need.',
          evidence: 'Quran 2:277, Hadith from Sahih Bukhari and Muslim',
          steps: [
            'Calculate 2.5% of your wealth annually',
            'Give to eligible recipients (poor, needy, etc.)',
            'Understand the conditions and timing',
            'Make it a regular practice'
          ]
        },
        {
          id: 'sawm',
          title: 'Sawm (Fasting)',
          arabic: 'الصوم',
          translation: 'Fasting during Ramadan',
          explanation: 'Sawm is the fourth pillar and involves fasting from dawn to sunset during the month of Ramadan.',
          evidence: 'Quran 2:183, Hadith from Sahih Bukhari and Muslim',
          steps: [
            'Fast from dawn (Fajr) to sunset (Maghrib)',
            'Abstain from food, drink, and marital relations',
            'Maintain good behavior and avoid negative actions',
            'Break fast with dates and water'
          ]
        },
        {
          id: 'hajj',
          title: 'Hajj (Pilgrimage)',
          arabic: 'الحج',
          translation: 'Pilgrimage to Makkah',
          explanation: 'Hajj is the fifth pillar and is a once-in-a-lifetime obligation for those who are physically and financially able.',
          evidence: 'Quran 3:97, Hadith from Sahih Bukhari and Muslim',
          steps: [
            'Plan and save for the journey',
            'Learn the rituals and requirements',
            'Perform the pilgrimage with proper intention',
            'Complete all required rituals'
          ]
        }
      ]
    },
    'basic-practices': {
      title: 'Basic Islamic Practices',
      arabicTitle: 'الممارسات الإسلامية الأساسية',
      description: 'Essential practices for daily Islamic life',
      content: [
        {
          id: 'wudu',
          title: 'Wudu (Ablution)',
          explanation: 'Wudu is the ritual washing performed before prayer to achieve spiritual and physical cleanliness.',
          steps: [
            'Make intention (niyyah)',
            'Say "Bismillah"',
            'Wash hands three times',
            'Rinse mouth three times',
            'Sniff water into nostrils three times',
            'Wash face three times',
            'Wash arms up to elbows three times',
            'Wipe head once',
            'Wash feet up to ankles three times'
          ]
        },
        {
          id: 'adab',
          title: 'Islamic Etiquette (Adab)',
          explanation: 'Islamic etiquette covers proper behavior, manners, and conduct in various situations.',
          practices: [
            'Greet with "Assalamu alaikum"',
            'Say "Bismillah" before eating',
            'Use the right hand for eating and drinking',
            'Show respect to elders',
            'Be kind to parents and family',
            'Maintain good hygiene',
            'Dress modestly'
          ]
        }
      ]
    },
    'prayer-basics': {
      title: 'Prayer Basics',
      arabicTitle: 'أساسيات الصلاة',
      description: 'Learn the fundamentals of Islamic prayer',
      content: [
        {
          id: 'prayer-times',
          title: 'Prayer Times',
          explanation: 'The five daily prayers have specific times based on the position of the sun.',
          times: [
            'Fajr: Before sunrise (dawn prayer)',
            'Dhuhr: After the sun passes its zenith (noon prayer)',
            'Asr: Mid-afternoon prayer',
            'Maghrib: After sunset (evening prayer)',
            'Isha: Night prayer'
          ]
        },
        {
          id: 'prayer-positions',
          title: 'Prayer Positions',
          explanation: 'Islamic prayer involves specific physical positions that have spiritual significance.',
          positions: [
            'Qiyam: Standing position',
            'Ruku: Bowing position',
            'Sujood: Prostration position',
            'Jalsa: Sitting position between prostrations',
            'Tashahhud: Final sitting position'
          ]
        }
      ]
    },
    'quran-reading': {
      title: 'Quran Reading',
      arabicTitle: 'قراءة القرآن',
      description: 'Guidance for reading and understanding the Quran',
      content: [
        {
          id: 'basics',
          title: 'Getting Started with Quran',
          explanation: 'The Quran is the holy book of Islam, containing Allah\'s guidance for humanity.',
          steps: [
            'Learn to read Arabic (start with basic letters)',
            'Practice proper pronunciation (Tajweed)',
            'Begin with short surahs (Al-Fatiha, Al-Ikhlas)',
            'Read with understanding and reflection',
            'Set daily reading goals',
            'Seek guidance from knowledgeable teachers'
          ]
        },
        {
          id: 'memorization',
          title: 'Quran Memorization',
          explanation: 'Memorizing the Quran is a highly rewarded act in Islam.',
          tips: [
            'Start with short surahs',
            'Use audio recitations for proper pronunciation',
            'Review regularly to maintain memorization',
            'Understand the meaning of what you memorize',
            'Practice with others in study groups'
          ]
        }
      ]
    },
    'islamic-calendar': {
      title: 'Islamic Calendar',
      arabicTitle: 'التقويم الإسلامي',
      description: 'Understanding the Islamic lunar calendar and important dates',
      content: [
        {
          id: 'months',
          title: 'Islamic Months',
          explanation: 'The Islamic calendar is lunar-based and has 12 months.',
          months: [
            'Muharram (Sacred month)',
            'Safar',
            'Rabi al-Awwal (Birth of Prophet Muhammad)',
            'Rabi al-Thani',
            'Jumada al-Awwal',
            'Jumada al-Thani',
            'Rajab (Sacred month)',
            'Sha\'ban',
            'Ramadan (Month of fasting)',
            'Shawwal (Eid al-Fitr)',
            'Dhu al-Qadah (Sacred month)',
            'Dhu al-Hijjah (Hajj and Eid al-Adha)'
          ]
        },
        {
          id: 'important-dates',
          title: 'Important Islamic Dates',
          explanation: 'Key dates in the Islamic calendar that hold special significance.',
          dates: [
            '1st Muharram: Islamic New Year',
            '10th Muharram: Day of Ashura',
            '12th Rabi al-Awwal: Mawlid al-Nabi',
            '27th Rajab: Laylat al-Miraj',
            '15th Sha\'ban: Laylat al-Bara\'ah',
            '1st Ramadan: Beginning of fasting month',
            '27th Ramadan: Laylat al-Qadr',
            '1st Shawwal: Eid al-Fitr',
            '10th Dhu al-Hijjah: Eid al-Adha'
          ]
        }
      ]
    },
    'community': {
      title: 'Islamic Community',
      arabicTitle: 'المجتمع الإسلامي',
      description: 'Connecting with the Muslim community and finding support',
      content: [
        {
          id: 'finding-community',
          title: 'Finding Your Islamic Community',
          explanation: 'Building connections with other Muslims is essential for spiritual growth and support.',
          steps: [
            'Visit local mosques and Islamic centers',
            'Attend Friday prayers (Jumu\'ah)',
            'Join Islamic study groups and classes',
            'Participate in community events and activities',
            'Connect with other new Muslims',
            'Seek guidance from local scholars and imams'
          ]
        },
        {
          id: 'support-networks',
          title: 'Support Networks for New Muslims',
          explanation: 'Various resources and networks exist to support new Muslims in their journey.',
          resources: [
            'Local mosque communities',
            'Online Islamic forums and groups',
            'New Muslim support organizations',
            'Islamic books and educational materials',
            'Mentorship programs',
            'Family and friends who are Muslim'
          ]
        }
      ]
    }
  };

  const sections = Object.keys(newMuslimContent);
  const filteredContent = newMuslimContent[selectedSection]?.content?.filter(item =>
    item.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    (item.explanation && item.explanation.toLowerCase().includes(searchTerm.toLowerCase()))
  ) || [];

  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <Star className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            New Muslim Guide
          </h1>
          <p className="text-slate-300 text-lg">
            Essential guidance for new Muslims: Shahada, prayer, wudu, Quran, and essential Islamic knowledge
          </p>
        </div>

        {/* Search Bar */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search New Muslim Topics</h2>
          </div>
          <input
            type="text"
            placeholder="Search for topics, practices, or guidance..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
          />
        </div>

        {/* Content Display */}
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          {/* Navigation Sidebar */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Guide Sections</h3>
            <div className="space-y-2">
              {sections.map((section) => (
                <button
                  key={section}
                  onClick={() => setSelectedSection(section)}
                  className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                    selectedSection === section
                      ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-teal-600/20 rounded-full flex items-center justify-center text-sm font-medium text-teal-300">
                      {newMuslimContent[section].content.length}
                    </div>
                    <div>
                      <div className="font-medium text-sm">{newMuslimContent[section].title}</div>
                      <div className="text-xs text-slate-400">{newMuslimContent[section].arabicTitle}</div>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            {selectedSection && (
              <div className="bg-calm-card border border-calm-border rounded-xl p-6">
                <div className="text-center mb-6">
                  <h2 className="text-2xl font-semibold text-teal-200 mb-2">
                    {newMuslimContent[selectedSection].title}
                  </h2>
                  <div className="text-lg text-slate-300 mb-2">
                    {newMuslimContent[selectedSection].arabicTitle}
                  </div>
                  <p className="text-slate-400">
                    {newMuslimContent[selectedSection].description}
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

                      <div className="text-slate-300 leading-relaxed mb-4">
                        {item.explanation}
                      </div>

                      {item.evidence && (
                        <div className="bg-teal-600/20 border border-teal-500/30 rounded-lg p-4 mb-4">
                          <h4 className="font-semibold text-teal-200 mb-2">Evidence & Sources</h4>
                          <p className="text-slate-300 text-sm">{item.evidence}</p>
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

                      {item.practices && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Islamic Practices</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.practices.map((practice, index) => (
                              <li key={index} className="text-slate-300 text-sm">{practice}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.times && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Prayer Times</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.times.map((time, index) => (
                              <li key={index} className="text-slate-300 text-sm">{time}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.positions && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Prayer Positions</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.positions.map((position, index) => (
                              <li key={index} className="text-slate-300 text-sm">{position}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.tips && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Helpful Tips</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.tips.map((tip, index) => (
                              <li key={index} className="text-slate-300 text-sm">{tip}</li>
                            ))}
                          </ul>
                        </div>
                      )}

                      {item.months && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Islamic Months</h4>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                            {item.months.map((month, index) => (
                              <div key={index} className="bg-calm-bg p-2 rounded text-slate-300 text-sm">
                                {month}
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {item.dates && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Important Dates</h4>
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                            {item.dates.map((date, index) => (
                              <div key={index} className="bg-calm-bg p-2 rounded text-slate-300 text-sm">
                                {date}
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {item.resources && (
                        <div className="mb-4">
                          <h4 className="font-semibold text-teal-200 mb-3">Resources & Support</h4>
                          <ul className="list-disc list-inside space-y-2">
                            {item.resources.map((resource, index) => (
                              <li key={index} className="text-slate-300 text-sm">{resource}</li>
                            ))}
                          </ul>
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

        {/* Quick Start Guide */}
        <div className="mt-8 bg-calm-card border border-calm-border rounded-xl p-6">
          <h3 className="text-lg font-semibold text-teal-200 mb-4">Quick Start Guide for New Muslims</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-calm-surface border border-calm-border rounded-lg p-4">
              <h4 className="font-semibold text-teal-200 mb-2">Week 1</h4>
              <ul className="text-slate-300 text-sm space-y-1">
                <li>• Learn the Shahada</li>
                <li>• Find a local mosque</li>
                <li>• Start learning basic prayers</li>
                <li>• Read about the Five Pillars</li>
              </ul>
            </div>
            <div className="bg-calm-surface border border-calm-border rounded-lg p-4">
              <h4 className="font-semibold text-teal-200 mb-2">Week 2-4</h4>
              <ul className="text-slate-300 text-sm space-y-1">
                <li>• Learn to perform wudu</li>
                <li>• Practice basic prayer movements</li>
                <li>• Start reading Quran</li>
                <li>• Connect with Muslim community</li>
              </ul>
            </div>
            <div className="bg-calm-surface border border-calm-border rounded-lg p-4">
              <h4 className="font-semibold text-teal-200 mb-2">Month 2+</h4>
              <ul className="text-slate-300 text-sm space-y-1">
                <li>• Establish regular prayer habits</li>
                <li>• Join Islamic study groups</li>
                <li>• Learn more about Islamic history</li>
                <li>• Consider fasting during Ramadan</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NewMuslim;
