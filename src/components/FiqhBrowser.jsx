import React, { useState, useEffect } from 'react';
import { Download, BookOpen, Search, FileText, Info, CheckCircle, AlertCircle } from 'lucide-react';

const FiqhBrowser = () => {
  const [fiqhData, setFiqhData] = useState(null);
  const [isDownloaded, setIsDownloaded] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedRuling, setSelectedRuling] = useState(null);

  // Fiqh content size information
  const fiqhStats = {
    totalCategories: 15,
    totalRulings: 247,
    estimatedSize: '2.8 MB',
    downloadTime: '~15 seconds'
  };

  const handleDownloadFiqh = async () => {
    setIsDownloading(true);
    setDownloadProgress(0);
    
    // Simulate download progress
    const progressInterval = setInterval(() => {
      setDownloadProgress(prev => {
        if (prev >= 100) {
          clearInterval(progressInterval);
          return 100;
        }
        return prev + 10;
      });
    }, 150);

    try {
      // Simulate API call to fetch fiqh data
      await new Promise(resolve => setTimeout(resolve, 1500));
      
      // Parse the fiqh content (this would normally come from an API)
      const parsedData = await parseFiqhContent();
      setFiqhData(parsedData);
      setIsDownloaded(true);
      
      // Store in localStorage for future use
      localStorage.setItem('fiqhData', JSON.stringify(parsedData));
      localStorage.setItem('fiqhDownloaded', 'true');
      
    } catch (error) {
      console.error('Error downloading fiqh content:', error);
    } finally {
      setIsDownloading(false);
      setDownloadProgress(0);
    }
  };

  const parseFiqhContent = async () => {
    // This would normally parse the actual HTML content
    // For now, return a structured representation
    return {
      categories: [
        {
          id: 'worship',
          name: 'Worship (Ibadah)',
          rulings: [
            {
              id: 'prayer-times',
              title: 'Prayer Times',
              content: 'Detailed rulings on prayer times, including Fajr, Dhuhr, Asr, Maghrib, and Isha...',
              evidence: 'Quran 4:103, Hadith from Sahih Bukhari and Muslim'
            },
            // More rulings would be parsed here
          ]
        },
        // More categories would be parsed here
      ]
    };
  };

  useEffect(() => {
    // Check if fiqh data was previously downloaded
    const savedData = localStorage.getItem('fiqhData');
    const wasDownloaded = localStorage.getItem('fiqhDownloaded');
    
    if (savedData && wasDownloaded === 'true') {
      setFiqhData(JSON.parse(savedData));
      setIsDownloaded(true);
    }
  }, []);

  const filteredCategories = fiqhData?.categories?.filter(cat =>
    cat.name.toLowerCase().includes(searchTerm.toLowerCase())
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
              Fiqh Knowledge Base
            </h1>
            <p className="text-slate-300 text-lg">
              Comprehensive Islamic jurisprudence and legal rulings
            </p>
          </div>

          {/* Download Prompt */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-8 mb-6">
            <div className="text-center mb-6">
              <Download className="w-16 h-16 text-teal-400 mx-auto mb-4" />
              <h2 className="text-2xl font-semibold text-teal-200 mb-2">
                Download Fiqh Knowledge Base
              </h2>
              <p className="text-slate-300 mb-4">
                This comprehensive collection contains detailed Islamic rulings, evidence, and scholarly opinions.
              </p>
            </div>

            {/* Content Statistics */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{fiqhStats.totalCategories}</div>
                <div className="text-sm text-slate-400">Categories</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{fiqhStats.totalRulings}</div>
                <div className="text-sm text-slate-400">Rulings</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{fiqhStats.estimatedSize}</div>
                <div className="text-sm text-slate-400">Size</div>
              </div>
              <div className="text-center p-4 bg-calm-surface rounded-lg border border-calm-border">
                <div className="text-2xl font-bold text-teal-400">{fiqhStats.downloadTime}</div>
                <div className="text-sm text-slate-400">Download</div>
              </div>
            </div>

            {/* Download Button */}
            <div className="text-center">
              <button
                onClick={handleDownloadFiqh}
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
                    Download Fiqh Knowledge Base
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
                    <strong>What's included:</strong> Prayer rulings, business ethics, family law, dietary laws, 
                    inheritance, marriage, divorce, and comprehensive Islamic jurisprudence from authentic sources.
                  </p>
                  <p>
                    <strong>Note:</strong> This content will be stored locally on your device for offline access. 
                    You can re-download anytime to get the latest updates.
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Preview of Categories */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Preview of Available Categories</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {[
                'Worship (Ibadah)', 'Business & Trade', 'Family & Marriage', 
                'Dietary Laws', 'Inheritance', 'Social Relations',
                'Education', 'Health & Medicine', 'Travel & Journey',
                'Financial Transactions', 'Criminal Law', 'Environmental Ethics',
                'Technology & Modern Issues', 'Interfaith Relations', 'Political Affairs'
              ].map((category, index) => (
                <div key={index} className="p-3 bg-calm-surface border border-calm-border rounded-lg">
                  <div className="flex items-center gap-2">
                    <FileText className="w-4 h-4 text-teal-400" />
                    <span className="text-sm text-slate-300">{category}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  }

  // Rest of the component for when fiqh is downloaded
  return (
    <div className="min-h-screen bg-calm-bg p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-20 h-20 bg-gradient-to-br from-teal-500 to-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
            <BookOpen className="w-10 h-10 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-teal-300 mb-2 font-islamic">
            Fiqh Knowledge Base
          </h1>
          <p className="text-slate-300 text-lg">
            Comprehensive Islamic jurisprudence and legal rulings
          </p>
          <div className="flex items-center justify-center gap-2 mt-2 text-sm text-teal-400">
            <CheckCircle className="w-4 h-4" />
            <span>Knowledge Base Downloaded</span>
          </div>
        </div>

        {/* Search Bar */}
        <div className="bg-calm-card border border-calm-border rounded-xl p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <Search className="w-5 h-5 text-teal-400" />
            <h2 className="text-lg font-semibold text-teal-200">Search Fiqh Rulings</h2>
          </div>
          <input
            type="text"
            placeholder="Search for specific rulings, topics, or keywords..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-calm-surface border border-calm-border rounded-lg px-4 py-3 text-slate-200 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-teal-500/50 focus:border-teal-500 transition-all duration-200"
          />
        </div>

        {/* Content Display */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Categories List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Categories</h3>
            <div className="space-y-2">
              {filteredCategories.map((category) => (
                <button
                  key={category.id}
                  onClick={() => setSelectedCategory(category)}
                  className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                    selectedCategory?.id === category.id
                      ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                      : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                  }`}
                >
                  <div className="flex items-center gap-2">
                    <FileText className="w-4 h-4" />
                    <span>{category.name}</span>
                  </div>
                </button>
              ))}
            </div>
          </div>

          {/* Rulings List */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">
              {selectedCategory ? `${selectedCategory.name} Rulings` : 'Select a Category'}
            </h3>
            {selectedCategory ? (
              <div className="space-y-2">
                {selectedCategory.rulings?.map((ruling) => (
                  <button
                    key={ruling.id}
                    onClick={() => setSelectedRuling(ruling)}
                    className={`w-full text-left p-3 rounded-lg transition-all duration-200 ${
                      selectedRuling?.id === ruling.id
                        ? 'bg-teal-600/20 text-teal-300 border border-teal-500/30'
                        : 'bg-calm-surface border border-calm-border text-slate-300 hover:text-teal-200 hover:bg-calm-surface/80'
                    }`}
                  >
                    <div className="text-sm font-medium">{ruling.title}</div>
                  </button>
                ))}
              </div>
            ) : (
              <div className="text-center py-8 text-slate-400">
                <BookOpen className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Choose a category to view its rulings</p>
              </div>
            )}
          </div>

          {/* Ruling Details */}
          <div className="bg-calm-card border border-calm-border rounded-xl p-6">
            <h3 className="text-lg font-semibold text-teal-200 mb-4">Ruling Details</h3>
            {selectedRuling ? (
              <div className="space-y-4">
                <div>
                  <h4 className="font-semibold text-teal-300 mb-2">{selectedRuling.title}</h4>
                  <p className="text-slate-300 text-sm leading-relaxed">{selectedRuling.content}</p>
                </div>
                <div>
                  <h5 className="font-medium text-teal-200 mb-2">Evidence & Sources</h5>
                  <p className="text-slate-300 text-sm">{selectedRuling.evidence}</p>
                </div>
              </div>
            ) : (
              <div className="text-center py-8 text-slate-400">
                <FileText className="w-12 h-12 mx-auto mb-3 text-slate-500" />
                <p>Select a ruling to view its details</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default FiqhBrowser;
