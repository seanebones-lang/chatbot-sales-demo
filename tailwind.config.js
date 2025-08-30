/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        'islamic': {
          'gold': '#FFD700',
          'blue': '#1E90FF',
          'teal': '#00CED1',
          'green': '#32CD32',
          'purple': '#9370DB',
          'dark': '#0f1419',
          'darker': '#1a1f2e',
        }
      },
      backgroundImage: {
        'islamic-gradient': 'linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%)',
        'blue-gradient': 'linear-gradient(135deg, rgba(30, 144, 255, 0.1) 0%, rgba(0, 77, 97, 0.1) 100%)',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in',
        'slide-in': 'slideIn 0.3s ease-out',
        'pulse-slow': 'pulse 2s infinite',
        'float': 'float 3s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        },
        slideIn: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(0)' }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' }
        }
      },
      boxShadow: {
        'islamic': '0 20px 40px rgba(30, 144, 255, 0.2)',
        'islamic-hover': '0 25px 50px rgba(30, 144, 255, 0.3)',
      }
    },
  },
  plugins: [],
}
