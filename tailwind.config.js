module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
    "./*.html"
  ],
  theme: {
    extend: {
      colors: {
        // Very calming, easy-on-the-eyes color palette
        'calm': {
          'bg': '#0a0f0f',      // Very dark teal-black background
          'surface': '#0f1a1a',  // Dark teal surface
          'card': '#142020',     // Slightly lighter card background
          'border': '#1a2a2a',   // Subtle border color
        },
        'teal': {
          '50': '#f0fdfa',      // Very light teal
          '100': '#ccfbf1',     // Light teal
          '200': '#99f6e4',     // Soft teal
          '300': '#5eead4',     // Medium teal
          '400': '#2dd4bf',     // Bright teal
          '500': '#14b8a6',     // Primary teal
          '600': '#0d9488',     // Darker teal
          '700': '#0f766e',     // Deep teal
          '800': '#115e59',     // Very deep teal
          '900': '#134e4a',     // Darkest teal
        },
        'green': {
          '50': '#f0fdf4',      // Very light green
          '100': '#dcfce7',     // Light green
          '200': '#bbf7d0',     // Soft green
          '300': '#86efac',     // Medium green
          '400': '#4ade80',     // Bright green
          '500': '#22c55e',     // Primary green
          '600': '#16a34a',     // Darker green
          '700': '#15803d',     // Deep green
          '800': '#166534',     // Very deep green
          '900': '#14532d',     // Darkest green
        },
        'slate': {
          '50': '#f8fafc',      // Very light slate
          '100': '#f1f5f9',     // Light slate
          '200': '#e2e8f0',     // Soft slate
          '300': '#cbd5e1',     // Medium slate
          '400': '#94a3b8',     // Bright slate
          '500': '#64748b',     // Primary slate
          '600': '#475569',     // Darker slate
          '700': '#334155',     // Deep slate
          '800': '#1e293b',     // Very deep slate
          '900': '#0f172a',     // Darkest slate
        }
      },
      fontFamily: {
        'arabic': ['Noto Naskh Arabic', 'serif'],
        'islamic': ['Amiri', 'serif'],
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      backgroundImage: {
        'islamic-pattern': "url('data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%231a2a2a' fill-opacity='0.1'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')",
        'calm-gradient': 'linear-gradient(135deg, #0a0f0f 0%, #0f1a1a 50%, #142020 100%)',
        'teal-gradient': 'linear-gradient(135deg, rgba(20, 184, 166, 0.05) 0%, rgba(13, 148, 136, 0.05) 100%)',
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in-out',
        'slide-up': 'slideUp 0.4s ease-out',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
        'glow': 'glow 3s ease-in-out infinite alternate',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        glow: {
          '0%': { boxShadow: '0 0 20px rgba(20, 184, 166, 0.1)' },
          '100%': { boxShadow: '0 0 30px rgba(20, 184, 166, 0.2)' },
        }
      },
      boxShadow: {
        'calm': '0 4px 6px -1px rgba(0, 0, 0, 0.3)',
        'calm-lg': '0 10px 15px -3px rgba(0, 0, 0, 0.4)',
        'teal-glow': '0 0 20px rgba(20, 184, 166, 0.15)',
        'green-glow': '0 0 20px rgba(34, 197, 94, 0.15)',
      }
    },
  },
  plugins: [],
}
