# AI Chatbot Frontend

A modern React TypeScript chatbot interface that connects to an OpenAI-powered backend.

## Features

- 🎨 **Modern UI**: Clean, responsive chat interface with dark theme
- 💬 **Real-time Chat**: Instant message display with loading indicators
- 📱 **Mobile Responsive**: Works perfectly on all device sizes
- ⚡ **TypeScript**: Full type safety and better development experience
- 🔄 **Auto-scroll**: Messages automatically scroll to bottom
- ⏱️ **Timestamps**: Each message shows when it was sent
- 🚀 **Fast**: Built with React 18 and modern hooks

## Tech Stack

- **React 18** with TypeScript
- **Axios** for API communication
- **CSS3** with responsive design
- **Create React App** for development

## Prerequisites

- Node.js 16+ 
- npm or yarn
- Backend server running on `http://localhost:5000`

## Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd chatbot-frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000`

## Available Scripts

- `npm start` - Runs the app in development mode
- `npm run build` - Builds the app for production
- `npm test` - Launches the test runner
- `npm run eject` - Ejects from Create React App (irreversible)

## Project Structure

```
chatbot-frontend/
├── public/
│   └── index.html          # Main HTML file
├── src/
│   ├── App.tsx            # Main React component
│   ├── App.css            # Component styles
│   ├── index.tsx          # React entry point
│   └── index.css          # Global styles
├── package.json           # Dependencies and scripts
└── README.md              # This file
```

## Configuration

The frontend is configured to connect to the backend at `http://localhost:5000`. If you need to change this:

1. Open `src/App.tsx`
2. Find the axios POST request
3. Update the URL to match your backend

## Features in Detail

### Message Display
- User messages: Right-aligned with blue gradient
- Bot messages: Left-aligned with dark gray background
- Timestamps on every message
- Smooth auto-scroll to latest message

### Input Handling
- Text input with placeholder
- Send button with loading state
- Enter key support (Shift+Enter for new lines)
- Input disabled during API calls

### Loading States
- Animated loading spinner
- Disabled input during requests
- Visual feedback for all interactions

### Error Handling
- Graceful error messages
- User-friendly alerts
- Fallback responses

## Development

### Adding New Features
1. Create new components in `src/components/`
2. Add styles to `App.css`
3. Update types in `App.tsx` if needed

### Styling
- CSS classes follow BEM methodology
- Responsive breakpoints at 768px and 480px
- Dark theme with accent colors
- Smooth transitions and animations

### State Management
- Uses React hooks (useState, useEffect, useRef)
- Message history stored in component state
- Loading states managed locally

## Troubleshooting

### Common Issues

**"Module not found" errors:**
```bash
rm -rf node_modules package-lock.json
npm install
```

**Port already in use:**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

**Backend connection failed:**
- Ensure backend is running on port 5000
- Check CORS settings in backend
- Verify network connectivity

### Performance Tips

- Messages are stored in component state (consider Redux for large apps)
- Images and media not yet implemented
- Consider implementing message pagination for long conversations

## Deployment

### Build for Production
```bash
npm run build
```

### Deploy to Static Hosting
The `build` folder contains static files that can be deployed to:
- Netlify
- Vercel
- AWS S3
- GitHub Pages

### Environment Variables
Create `.env` file for production:
```env
REACT_APP_API_URL=https://your-backend-url.com
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
