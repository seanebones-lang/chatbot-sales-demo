# Islamic AI Assistant - React App

A comprehensive Islamic AI chatbot built with React, providing knowledge about Quran, Hadith, Fiqh, and Islamic guidance.

## Features

- **AI-Powered Chat**: Intelligent responses to Islamic questions
- **Comprehensive Knowledge Base**: Quran, Hadith, Fiqh, and more
- **Beautiful UI**: Modern, responsive design with Islamic theme
- **Search Functionality**: Find specific Islamic topics quickly
- **Mobile Responsive**: Works perfectly on all devices

## Tech Stack

- **Frontend**: React 18, Tailwind CSS
- **Backend**: Python Flask (DeenBot)
- **Icons**: Lucide React
- **Styling**: Custom CSS with Islamic theme

## Quick Start

### Prerequisites
- Node.js 16+ 
- Python 3.8+
- npm or yarn

### Installation

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start the React App**
   ```bash
   npm start
   ```
   The app will open at `http://localhost:3000`

3. **Start the Backend** (in another terminal)
   ```bash
   source deenbot_env/bin/activate
   python3 comprehensive_deenbot_backend.py
   ```
   Backend runs on `http://localhost:8080`

### Build for Production

```bash
npm run build
```

## Project Structure

```
src/
├── components/
│   └── IslamicChatbot.jsx    # Main chatbot component
├── App.js                     # Main app component
├── App.css                    # App-specific styles
├── index.js                   # React entry point
└── index.css                  # Global styles + Tailwind

public/
└── index.html                 # HTML template

Backend/
├── comprehensive_deenbot_backend.py  # AI backend
├── deenbot_env/                     # Python environment
└── requirements.txt                  # Python dependencies
```

## Available Scripts

- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App

## Islamic Knowledge Areas

- **Quran Study**: Verses, translations, tafsir
- **Hadith Collections**: Authentic narrations
- **Fiqh (Islamic Law)**: Rulings and guidance
- **Islamic History**: Prophets, scholars, civilization
- **Daily Life**: Family, business, health, education
- **Modern Issues**: Technology, environment, finance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ for the Islamic community**
