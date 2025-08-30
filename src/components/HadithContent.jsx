import React, { useState, useEffect } from 'react';
import { Download, BookOpen, Search, FileText, Info, CheckCircle, Bookmark, Share2, Filter, Star } from 'lucide-react';

const HadithContent = () => {
  const [hadithData, setHadithData] = useState(null);
  const [isDownloaded, setIsDownloaded] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCollection, setSelectedCollection] = useState(null);
  const [selectedHadith, setSelectedHadith] = useState(null);
  const [filterCategory, setFilterCategory] = useState('all');

  // Hadith content size information
  const hadithStats = {
    totalCollections: 8,
    totalHadiths: 15420,
    estimatedSize: '3.1 MB',
    downloadTime: '~18 seconds',
    includes: 'Authentic Hadith collections, grading, translations, and commentary'
  };

  const handleDownloadHadith = async () => {
    setIsDownloading(true);
    setDownloadProgress(0);
    
    // Simulate download progress
    const progressInterval = setInterval(() => {
      setDownloadProgress(prev => {
        if (prev >= 100) {
          clearInterval(progressInterval);
          return 100;
        }
        return prev + 6;
      });
    }, 120);

    try {
      // Simulate API call to fetch Hadith data
      await new Promise(resolve => setTimeout(resolve, 1800));
      
      // Parse the Hadith content (this would normally come from an API)
      const parsedData = await parseHadithContent();
      setHadithData(parsedData);
      setIsDownloaded(true);
      
      // Store in localStorage for future use
      localStorage.setItem('hadithData', JSON.stringify(parsedData));
      localStorage.setItem('hadithDownloaded', 'true');
      
    } catch (error) {
      console.error('Error downloading Hadith content:', error);
    } finally {
      setIsDownloading(false);
      setDownloadProgress(0);
    }
  };

  const parseHadithContent = async () => {
    // This would normally parse the actual HTML content
    // For now, return a structured representation
    return {
      collections: [
        {
          id: 'bukhari',
          name: 'Sahih Bukhari',
          arabicName: 'صحيح البخاري',
          englishName: 'Authentic Collection of Bukhari',
          totalHadiths: 7563,
          compiler: 'Imam Muhammad ibn Ismail al-Bukhari',
          period: '810-870 CE',
          description: 'The most authentic collection of Hadith, containing only the most reliable narrations',
          categories: ['Faith', 'Prayer', 'Business', 'Family', 'Social Relations'],
          hadiths: [
            {
              id: 'bukhari-1',
              number: 1,
              title: 'The Beginning of Divine Inspiration',
              arabic: 'إنما الأعمال بالنيات...',
              translation: 'Actions are judged by intentions...',
              narrator: 'Umar ibn al-Khattab',
              grade: 'Sahih',
              category: 'Faith',
              explanation: 'This hadith establishes the fundamental principle that all actions are judged by their underlying intentions...'
            }
            // More hadiths would be parsed here
          ]
        },
        {
          id: 'muslim',
          name: 'Sahih Muslim',
          arabicName: 'صحيح مسلم',
          englishName: 'Authentic Collection of Muslim',
          totalHadiths: 7563,
          compiler: 'Imam Muslim ibn al-Hajjaj',
          period: '817-875 CE',
          description: 'Second most authentic collection, known for its excellent organization and reliability',
          categories: ['Faith', 'Prayer', 'Business', 'Family', 'Social Relations'],
          hadiths: []
        }
        // More collections would be parsed here
      ]
    };
  };

  useEffect(() => {
    // Check if Hadith data was previously downloaded
    const savedData = localStorage.getItem('hadithData');
    const wasDownloaded = localStorage.getItem('hadithDownloaded');
    
    if (savedData && wasDownloaded === 'true') {
      setHadithData(JSON.parse(savedData));
      setIsDownloaded(true);
    }
  }, []);

  const filteredCollections = hadithData?.collections?.filter(collection =>
    collection.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    collection.englishName.toLowerCase().includes(searchTerm.toLowerCase()) ||
    collection.arabicName.includes(searchTerm)
  ) || [];

  const filteredHadiths = selectedCollection?.hadiths?.filter(hadith =>
    (filterCategory === 'all' || hadith.category === filterCategory) &&
    (hadith.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
     hadith.translation.toLowerCase().includes(searchTerm.toLowerCase()))
  ) || [];

  if (!isDownloaded) {
    return (
      <div className="min-h-screen bg-calm-bg p-6">
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <BookOpen className="w-10 h-10 text-white" />
            </div>
            <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
              Complete Hadith Collections
            </h1>
            <p className="text-slate-300 text-lg">
              Authentic sayings and actions of Prophet Muhammad sallallahu alayhi wa sallam
            </p>
          </div>

          {/* Download Prompt */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-8 mb-6">
            <div className="text-center mb-6">
              <Download className="w-16 h-16 text-teal-400 mx-auto mb-4" />
              <h2 className="text-2xl font-semibold text-teal-200 mb-2">
                Download Complete Hadith Knowledge Base
              </h2>
              <p className="text-slate-300 mb-4">
                Access authentic Hadith collections with grading, translations, and scholarly commentary.
              </p>
            </div>

            {/* Content Statistics */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{hadithStats.totalCollections}</div>
                <div className="text-sm text-slate-400">Collections</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{hadithStats.totalHadiths.toLocaleString()}</div>
                <div className="text-sm text-slate-400">Hadiths</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{hadithStats.estimatedSize}</div>
                <div className="text-sm text-slate-400">Size</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{hadithStats.downloadTime}</div>
                <div className="text-sm text-slate-400">Download</div>
              </div>
            </div>

            {/* Download Button */}
            <div className="text-center">
              <button
                onClick={handleDownloadHadith}
                disabled={isDownloading}
                className="bg-gradient-to-r from-teal-600 to-green-600 hover:from-teal-700 hover:to-green-700 text-white px-8 py-4 rounded-lg font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed hover:shadow-teal-glow text-lg"
              >
                {isDownloading ? (
                  <div className="flex items-center gap-3">
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                    Downloading... {downloadProgress}%
                  </div>
                ) : (
                  <div className="flex items-center gap-3">
                    <Download className="w-5 h-5" />
                    Download Hadith Collections
                  </div>
                )}
              </button>
            </div>

            {/* Progress Bar */}
            {isDownloading && (
              <div className="mt-6">
                <div className="w-full bg-calm-surface rounded-full h-2 border border-calm-border">
                  <div 
                    className="bg-gradient-to-r from-teal-500 to-green-500 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${downloadProgress}%` }}
                  ></div>
                </div>
              </div>
            )}

            {/* Information */}
            <div className="mt-6 p-4 bg-calm-surface/50 rounded-lg border border-calm-border">
              <div className="flex items-start gap-3">
                <Info className="w-5 h-5 text-teal-400 mt-0.5 flex-shrink-0" />
                <div className="text-sm text-slate-300">
                  <p className="mb-2">
                    <strong>What's included:</strong> Sahih Bukhari, Sahih Muslim, Sunan Abu Dawud, Sunan at-Tirmidhi, 
                    Sunan an-Nasa'i, Sunan Ibn Majah, Muwatta Malik, and Musnad Ahmad with complete grading and commentary.
                  </p>
                  <p>
                    <strong>Note:</strong> This content will be stored locally on your device for offline access. 
                    You can re-download anytime to get the latest translations and commentary.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Preview of Collections */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Preview of Available Collections</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {[
                'Sahih Bukhari', 'Sahih Muslim', 'Sunan Abu Dawud', 
                'Sunan at-Tirmidhi', 'Sunan an-Nasa\'i', 'Sunan Ibn Majah',
                'Muwatta Malik', 'Musnad Ahmad', 'Riyadh as-Saliheen',
                'Mishkat al-Masabih', 'Bulugh al-Maram', 'Nail al-Awtar'
              ].map((collection, index) => (
                <div key={index} className="p-3 bg-calm-surface border border-calm-border rounded-lg">
                  <div className="flex items-center gap-2">
                    <FileText className="w-4 h-4 text-teal-400" />
                    <span className="text-sm text-slate-300">{collection}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Rest of the component for when Hadith is downloaded
  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <BookOpen className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            Complete Hadith Collections
          </h1>
          <p className="text-slate-300 text-lg">
            Authentic sayings and actions of Prophet Muhammad sallallahu alayhi wa sallam
          </p>
          <div className="flex items-center justify-center gap-2 mt-2 text-sm text-teal-400">
            <CheckCircle className="w-4 h-4" />
            <span>Hadith Knowledge Base Downloaded</span>
          </div>
        </div>

        {/* Search and Filter Bar */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search Hadith</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="Search for hadiths, narrators, or keywords..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
            />
            <select
              value={filterCategory}
              onChange={(e) => setFilterCategory(e.target.value)}
              className="bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
            >
              <option value="all">All Categories</option>
              <option value="Faith">Faith</option>
              <option value="Prayer">Prayer</option>
              <option value="Business">Business</option>
              <option value="Family">Family</option>
              <option value="Social Relations">Social Relations</option>
            </select>
          </div>
        </div>

        {/* Content Display */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Collections List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Collections ({filteredCollections.length})</h3>
            <div className="space-y-2 max-h-96 overflow-y-auto">
              {filteredCollections.map((collection) => (
                <button
                  key={collection.id}
                  onClick={() => setSelectedCollection(collection)}
                  className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                    selectedCollection?.id === collection.id
                      ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 bg-teal-600/20 rounded-full flex items-center justify-center text-sm font-medium text-teal-300">
                        {collection.totalHadiths.toLocaleString()}
                      </div>
                      <div>
                        <div className="font-medium">{collection.name}</div>
                        <div className="text-xs text-slate-400">{collection.englishName}</div>
                      </div>
                    </div>
                    <Star className="w-4 h-4 text-teal-400" />
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Hadith List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">
              {selectedCollection ? `${selectedCollection.name} Hadiths` : 'Select a Collection'}
            </h3>
            {selectedCollection ? (
              <div className="space-y-2 max-h-96 overflow-y-auto">
                {filteredHadiths.map((hadith) => (
                  <button
                    key={hadith.id}
                    onClick={() => setSelectedHadith(hadith)}
                    className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                      selectedHadith?.id === hadith.id
                        ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                        : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex-1">
                        <div className="text-sm font-medium">{hadith.title}</div>
                        <div className="text-xs text-slate-400 mt-1">{hadith.narrator}</div>
                      </div>
                      <div className="text-xs text-teal-400 bg-teal-600/20 px-2 py-1 rounded">
                        {hadith.grade}
                      </div>
                    </div>
                  </button>
                ))}
              </div>
            ) : (
              <div className="text-center py-8 text-slate-400">
                <BookOpen className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Choose a collection to view its hadiths</p>
              </div>
            )}
          </div>

          {/* Hadith Details */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Hadith Details</h3>
            {selectedHadith ? (
              <div className="space-y-4">
                <div>
                  <h4 className="font-semibold text-teal-300 mb-2">{selectedHadith.title}</h4>
                  <div className="text-xs text-slate-400 mb-2">
                    Narrated by {selectedHadith.narrator} • Grade: {selectedHadith.grade}
                  </div>
                </div>

                <div>
                  <h5 className="font-medium text-teal-200 mb-2">Arabic Text</h5>
                  <div className="bg-calm-surface p-3 rounded-lg border border-calm-border">
                    <div className="text-right text-lg text-teal-200 font-arabic leading-relaxed">
                      {selectedHadith.arabic}
                    </div>
                  </div>
                </div>

                <div>
                  <h5 className="font-medium text-teal-200 mb-2">Translation</h5>
                  <p className="text-slate-300 text-sm leading-relaxed">{selectedHadith.translation}</p>
                </div>

                <div>
                  <h5 className="font-medium text-teal-200 mb-2">Explanation</h5>
                  <p className="text-slate-300 text-sm leading-relaxed">{selectedHadith.explanation}</p>
                </div>

                {/* Quick Actions */}
                <div>
                  <h5 className="font-medium text-teal-200 mb-2">Quick Actions</h5>
                  <div className="space-y-2">
                    <button className="w-full p-2 bg-calm-surface border border-calm-border rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm flex items-center gap-2">
                      <Bookmark className="w-4 h-4" />
                      Bookmark Hadith
                    </button>
                    <button className="w-full p-2 bg-calm-surface border border-calm-border rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm flex items-center gap-2">
                      <Share2 className="w-4 h-4" />
                      Share
                    </button>
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-8 text-slate-400">
                <FileText className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Select a hadith to view its details</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HadithContent;
