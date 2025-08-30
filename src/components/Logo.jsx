import React, { useState, useEffect } from 'react';

const Logo = ({ size = 48, className = '' }) => {
  const [logoSrc, setLogoSrc] = useState('');
  const [fallbackDisplay, setFallbackDisplay] = useState(false);

  useEffect(() => {
    // Force the logo to load from the correct path with cache busting
    const timestamp = Date.now();
    const logoPath = `./logo.svg?v=${timestamp}`;
    console.log('Logo component mounted, trying path:', logoPath);
    setLogoSrc(logoPath);
  }, []);

  const handleLogoError = (e) => {
    console.log('Logo failed to load from:', e.target.src);
    
    // Try alternative paths with cache busting
    const timestamp = Date.now();
    if (e.target.src.includes('logo.svg')) {
      console.log('Trying relative path with cache busting');
      e.target.src = `./logo.svg?v=${timestamp}`;
    } else if (e.target.src.includes('./logo.svg')) {
      console.log('Trying root path with cache busting');
      e.target.src = `logo.svg?v=${timestamp}`;
    } else {
      console.log('All paths failed, showing fallback');
      setFallbackDisplay(true);
    }
  };

  const handleLogoLoad = () => {
    console.log('Logo loaded successfully from:', logoSrc);
    setFallbackDisplay(false);
  };

  // If fallback is needed, show the SVG directly embedded
  if (fallbackDisplay) {
    return (
      <div className={`${className}`} style={{ width: size, height: size }}>
        <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style={{ width: '100%', height: '100%' }}>
          {/* Background Circle with enhanced depth */}
          <circle cx="100" cy="100" r="95" fill="url(#greenGradient)" stroke="#1a2a2a" strokeWidth="4"/>
          
          {/* Mosque Dome with enhanced 3D effect */}
          <path
            d="M50 90 Q100 40 150 90 L150 110 Q100 60 50 110 Z"
            fill="url(#domeGradient)"
            stroke="#d4af37"
            strokeWidth="2"
          />
          
          {/* Dome highlight for 3D effect */}
          <path
            d="M60 95 Q100 45 140 95 L140 105 Q100 55 60 105 Z"
            fill="url(#domeHighlight)"
            opacity="0.3"
          />
          
          {/* Crescent Moon with enhanced detail */}
          <path
            d="M90 36 Q100 30 110 36 Q116 44 110 52 Q100 58 90 52 Q84 44 90 36"
            fill="url(#moonGradient)"
            stroke="#d4af37"
            strokeWidth="1"
          />
          
          {/* Moon highlight */}
          <path
            d="M92 38 Q100 32 108 38 Q112 42 108 48 Q100 54 92 48 Q88 42 92 38"
            fill="url(#moonHighlight)"
            opacity="0.4"
          />
          
          {/* Open Book with enhanced 3D effect */}
          <rect x="60" y="100" width="80" height="50" rx="4" fill="url(#bookGradient)" stroke="#d4af37" strokeWidth="2"/>
          <rect x="64" y="104" width="72" height="42" rx="2" fill="url(#pageGradient)"/>
          
          {/* Book spine shadow */}
          <rect x="60" y="100" width="8" height="50" rx="4" fill="url(#spineGradient)"/>
          
          {/* Book Pages with enhanced detail */}
          <line x1="70" y1="116" x2="130" y2="116" stroke="#d4af37" strokeWidth="1" opacity="0.8"/>
          <line x1="70" y1="124" x2="130" y2="124" stroke="#d4af37" strokeWidth="1" opacity="0.8"/>
          <line x1="70" y1="132" x2="130" y2="132" stroke="#d4af37" strokeWidth="1" opacity="0.8"/>
          
          {/* Page curl effect */}
          <path
            d="M130 104 L140 104 L140 146 L130 146 Z"
            fill="url(#pageCurlGradient)"
            opacity="0.6"
          />
          
          {/* Enhanced Gradients */}
          <defs>
            <linearGradient id="greenGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#0f1a1a"/>
              <stop offset="30%" stopColor="#142020"/>
              <stop offset="70%" stopColor="#1a2a2a"/>
              <stop offset="100%" stopColor="#0a0f0f"/>
            </linearGradient>
            
            <linearGradient id="domeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#ffd700"/>
              <stop offset="30%" stopColor="#ffed4e"/>
              <stop offset="70%" stopColor="#d4af37"/>
              <stop offset="100%" stopColor="#b8860b"/>
            </linearGradient>
            
            <linearGradient id="domeHighlight" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#ffffff"/>
              <stop offset="100%" stopColor="#ffed4e"/>
            </linearGradient>
            
            <linearGradient id="moonGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#ffd700"/>
              <stop offset="50%" stopColor="#ffed4e"/>
              <stop offset="100%" stopColor="#d4af37"/>
            </linearGradient>
            
            <linearGradient id="moonHighlight" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#ffffff"/>
              <stop offset="100%" stopColor="#ffed4e"/>
            </linearGradient>
            
            <linearGradient id="bookGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#d4af37"/>
              <stop offset="50%" stopColor="#b8860b"/>
              <stop offset="100%" stopColor="#8b6914"/>
            </linearGradient>
            
            <linearGradient id="spineGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#b8860b"/>
              <stop offset="100%" stopColor="#8b6914"/>
            </linearGradient>
            
            <linearGradient id="pageGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#f5f5dc"/>
              <stop offset="50%" stopColor="#f0f0e0"/>
              <stop offset="100%" stopColor="#e8e8d0"/>
            </linearGradient>
            
            <linearGradient id="pageCurlGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#e8e8d0"/>
              <stop offset="100%" stopColor="#d0d0c0"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
    );
  }

  return (
    <div className={`${className}`} style={{ width: size, height: size }}>
      <img 
        src={logoSrc}
        alt="Islamic Study Guide Logo" 
        style={{ width: '100%', height: '100%', objectFit: 'contain' }}
        onLoad={handleLogoLoad}
        onError={handleLogoError}
      />
    </div>
  );
};

export default Logo;
