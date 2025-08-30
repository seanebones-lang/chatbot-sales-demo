import React from 'react';

const Logo = ({ size = 48, className = '' }) => {
  return (
    <div className={`${className}`} style={{ width: size, height: size }}>
      <svg
        viewBox="0 0 100 100"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="w-full h-full"
      >
        {/* Background Circle */}
        <circle cx="50" cy="50" r="48" fill="url(#greenGradient)" stroke="#1a2a2a" strokeWidth="2"/>
        
        {/* Mosque Dome */}
        <path
          d="M25 45 Q50 20 75 45 L75 55 Q50 30 25 55 Z"
          fill="url(#goldGradient)"
          stroke="#d4af37"
          strokeWidth="1"
        />
        
        {/* Crescent Moon */}
        <path
          d="M45 18 Q50 15 55 18 Q58 22 55 26 Q50 29 45 26 Q42 22 45 18"
          fill="url(#goldGradient)"
          stroke="#d4af37"
          strokeWidth="0.5"
        />
        
        {/* Open Book */}
        <rect x="30" y="50" width="40" height="25" rx="2" fill="url(#bookGradient)" stroke="#d4af37" strokeWidth="1"/>
        <rect x="32" y="52" width="36" height="21" rx="1" fill="#f5f5dc"/>
        
        {/* Book Pages */}
        <line x1="35" y1="58" x2="65" y2="58" stroke="#d4af37" strokeWidth="0.5"/>
        <line x1="35" y1="62" x2="65" y2="62" stroke="#d4af37" strokeWidth="0.5"/>
        <line x1="35" y1="66" x2="65" y2="66" stroke="#d4af37" strokeWidth="0.5"/>
        
        {/* Gradients */}
        <defs>
          <linearGradient id="greenGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#0f1a1a"/>
            <stop offset="50%" stopColor="#142020"/>
            <stop offset="100%" stopColor="#0a0f0f"/>
          </linearGradient>
          
          <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#ffd700"/>
            <stop offset="50%" stopColor="#ffed4e"/>
            <stop offset="100%" stopColor="#d4af37"/>
          </linearGradient>
          
          <linearGradient id="bookGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#d4af37"/>
            <stop offset="100%" stopColor="#b8860b"/>
          </linearGradient>
        </defs>
      </svg>
    </div>
  );
};

export default Logo;
