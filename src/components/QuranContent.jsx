import React, { useState, useEffect } from 'react';
import { Download, BookOpen, Search, FileText, Info, CheckCircle, Play, Pause, Volume2, Bookmark, Share2 } from 'lucide-react';

const QuranContent = () => {
  const [quranData, setQuranData] = useState(null);
  const [isDownloaded, setIsDownloaded] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedSurah, setSelectedSurah] = useState(null);
  const [selectedAyah, setSelectedAyah] = useState(null);

  // Quran content size information
  const quranStats = {
    totalSurahs: 114,
    totalAyahs: 6236,
    estimatedSize: '4.2 MB',
    downloadTime: '~20 seconds',
    includes: 'Arabic text, translations, tafsir, audio recitations'
  };

  const handleDownloadQuran = async () => {
    setIsDownloading(true);
    setDownloadProgress(0);
    
    // Simulate download progress
    const progressInterval = setInterval(() => {
      setDownloadProgress(prev => {
        if (prev >= 100) {
          clearInterval(progressInterval);
          return 100;
        }
        return prev + 5;
      });
    }, 100);

    try {
      // Simulate API call to fetch Quran data
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      // Parse the Quran content (this would normally come from an API)
      const parsedData = await parseQuranContent();
      setQuranData(parsedData);
      setIsDownloaded(true);
      
      // Store in localStorage for future use
      localStorage.setItem('quranData', JSON.stringify(parsedData));
      localStorage.setItem('quranDownloaded', 'true');
      
    } catch (error) {
      console.error('Error downloading Quran content:', error);
    } finally {
      setIsDownloading(false);
      setDownloadProgress(0);
    }
  };

  const parseQuranContent = async () => {
    // This would normally parse the actual HTML content
    // For now, return a structured representation
    return {
      surahs: [
        {
          id: 1,
          name: 'Al-Fatiha',
          arabicName: 'الفاتحة',
          englishName: 'The Opening',
          revelationType: 'Meccan',
          totalAyahs: 7,
          description: 'The opening chapter of the Quran, recited in every prayer',
          content: 'Bismillahi ar-rahmani ar-raheem...',
          translation: 'In the name of Allah, the Entirely Merciful, the Especially Merciful...',
          tafsir: 'This surah is known as the Mother of the Book...'
        },
        {
          id: 2,
          name: 'Al-Baqarah',
          arabicName: 'البقرة',
          englishName: 'The Cow',
          revelationType: 'Medinan',
          totalAyahs: 286,
          description: 'The longest chapter of the Quran, containing many important rulings',
          content: 'Alif-Lam-Mim...',
          translation: 'Alif, Lam, Meem...',
          tafsir: 'This surah was revealed in Medina and contains...'
        },
        // More surahs would be parsed here
      ]
    };
  };

  useEffect(() => {
    // Check if Quran data was previously downloaded
    const savedData = localStorage.getItem('quranData');
    const wasDownloaded = localStorage.getItem('quranDownloaded');
    
    if (savedData && wasDownloaded === 'true') {
      setQuranData(JSON.parse(savedData));
      setIsDownloaded(true);
    }
  }, []);

  const filteredSurahs = quranData?.surahs?.filter(surah =>
    surah.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    surah.englishName.toLowerCase().includes(searchTerm.toLowerCase()) ||
    surah.arabicName.includes(searchTerm)
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
              Complete Quran with Tafsir
            </h1>
            <p className="text-slate-300 text-lg">
              The Holy Quran with Arabic text, translations, and scholarly commentary
            </p>
          </div>

          {/* Download Prompt */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-8 mb-6">
            <div className="text-center mb-6">
              <Download className="w-16 h-16 text-teal-400 mx-auto mb-4" />
              <h2 className="text-2xl font-semibold text-teal-200 mb-2">
                Download Complete Quran Knowledge Base
              </h2>
              <p className="text-slate-300 mb-4">
                Access the complete Quran with Arabic text, multiple translations, detailed tafsir, and audio recitations.
              </p>
            </div>

            {/* Content Statistics */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{quranStats.totalSurahs}</div>
                <div className="text-sm text-slate-400">Surahs</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{quranStats.totalAyahs}</div>
                <div className="text-sm text-slate-400">Ayahs</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{quranStats.estimatedSize}</div>
                <div className="text-sm text-slate-400">Size</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{quranStats.downloadTime}</div>
                <div className="text-sm text-slate-400">Download</div>
              </div>
            </div>

            {/* Download Button */}
            <div className="text-center">
              <button
                onClick={handleDownloadQuran}
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
                    Download Complete Quran
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
                    <strong>What's included:</strong> Complete Arabic text, English translations, detailed tafsir (commentary), 
                    audio recitations, verse-by-verse explanations, and search functionality across all content.
                  </p>
                  <p>
                    <strong>Note:</strong> This content will be stored locally on your device for offline access. 
                    You can re-download anytime to get the latest translations and commentary.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Preview of Surahs */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Preview of Available Surahs</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {[
                'Al-Fatiha (The Opening)', 'Al-Baqarah (The Cow)', 'Aal-Imran (Family of Imran)',
                'An-Nisa (The Women)', 'Al-Ma\'idah (The Table Spread)', 'Al-An\'am (The Cattle)',
                'Al-A\'raf (The Heights)', 'Al-Anfal (The Spoils of War)', 'At-Tawbah (The Repentance)',
                'Yunus (Jonah)', 'Hud', 'Yusuf (Joseph)',
                'Ar-Ra\'d (The Thunder)', 'Ibrahim (Abraham)', 'Al-Hijr (The Rocky Tract)'
              ].map((surah, index) => (
                <div key={index} className="p-3 bg-calm-surface border border-calm-border rounded-lg">
                  <div className="flex items-center gap-2">
                    <FileText className="w-4 h-4 text-teal-400" />
                    <span className="text-sm text-slate-300">{surah}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Rest of the component for when Quran is downloaded
  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <BookOpen className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            Complete Quran with Tafsir
          </h1>
          <p className="text-slate-300 text-lg">
            The Holy Quran with Arabic text, translations, and scholarly commentary
          </p>
          <div className="flex items-center justify-center gap-2 mt-2 text-sm text-teal-400">
            <CheckCircle className="w-4 h-4" />
            <span>Quran Knowledge Base Downloaded</span>
          </div>
        </div>

        {/* Search Bar */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search Quran</h2>
          </div>
          <input
            type="text"
            placeholder="Search for surahs, ayahs, or keywords..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
          />
        </div>

        {/* Content Display */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Surahs List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Surahs ({filteredSurahs.length})</h3>
            <div className="space-y-2 max-h-96 overflow-y-auto">
              {filteredSurahs.map((surah) => (
                <button
                  key={surah.id}
                  onClick={() => setSelectedSurah(surah)}
                  className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                    selectedSurah?.id === surah.id
                      ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 bg-teal-600/20 rounded-full flex items-center justify-center text-sm font-medium text-teal-300">
                        {surah.id}
                      </div>
                      <div>
                        <div className="font-medium">{surah.name}</div>
                        <div className="text-xs text-slate-400">{surah.englishName}</div>
                      </div>
                    </div>
                    <div className="text-xs text-teal-400 bg-teal-600/20 px-2 py-1 rounded">
                      {surah.totalAyahs}
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Surah Details */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">
              {selectedSurah ? selectedSurah.name : 'Select a Surah'}
            </h3>
            {selectedSurah ? (
              <div className="space-y-4">
                <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                  <div className="text-2xl font-bold text-teal-300 mb-2">{selectedSurah.arabicName}</div>
                  <div className="text-lg text-slate-300 mb-2">{selectedSurah.englishName}</div>
                  <div className="text-sm text-slate-400">
                    {selectedSurah.revelationType} • {selectedSurah.totalAyahs} ayahs
                  </div>
                </div>
                
                <div>
                  <h4 className="font-semibold text-teal-200 mb-2">Description</h4>
                  <p className="text-slate-300 text-sm leading-relaxed">{selectedSurah.description}</p>
                </div>

                <div>
                  <h4 className="font-semibold text-teal-200 mb-2">Content Preview</h4>
                  <div className="bg-calm-surface p-3 rounded-lg border border-calm-border">
                    <div className="text-right text-lg text-teal-200 mb-2 font-arabic leading-relaxed">
                      {selectedSurah.content}
                    </div>
                    <div className="text-slate-300 text-sm italic">{selectedSurah.translation}</div>
                  </div>
                </div>

                {/* Audio Controls */}
                <div className="flex items-center gap-3 p-3 bg-calm-surface rounded-lg border border-calm-border">
                  <button className="w-10 h-10 bg-teal-600 rounded-full flex items-center justify-center text-white hover:bg-teal-700 transition-colors">
                    <Play className="w-4 h-4 ml-0.5" />
                  </button>
                  <div className="flex-1">
                    <div className="text-sm text-teal-200">Audio Recitation</div>
                    <div className="text-xs text-slate-400">Available in multiple reciter styles</div>
                  </div>
                  <button className="p-2 text-teal-400 hover:text-teal-300">
                    <Volume2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ) : (
              <div className="text-center py-8 text-slate-400">
                <BookOpen className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Choose a surah to view its details</p>
              </div>
            )}
          </div>

          {/* Tafsir and Additional Info */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Tafsir & Commentary</h3>
            {selectedSurah ? (
              <div className="space-y-4">
                <div>
                  <h4 className="font-semibold text-teal-200 mb-2">Scholarly Commentary</h4>
                  <p className="text-slate-300 text-sm leading-relaxed">{selectedSurah.tafsir}</p>
                </div>
                
                <div>
                  <h4 className="font-semibold text-teal-200 mb-2">Quick Actions</h4>
                  <div className="space-y-2">
                    <button className="w-full p-2 bg-calm-surface border border-calm-border rounded-lg text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80 transition-all duration-200 text-sm flex items-center gap-2">
                      <Bookmark className="w-4 h-4" />
                      Bookmark Surah
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
                <p>Select a surah to view its tafsir</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default QuranContent;
