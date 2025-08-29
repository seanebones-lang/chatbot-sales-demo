import React, { useState, useRef, useEffect } from 'react';
import { Send, Calendar, FileText, DollarSign, Phone, Info, User } from 'lucide-react';

const TattooAssistantBot = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! Thanks for calling - I'm currently with a client but my AI assistant is here to help! I can schedule appointments, show you my portfolio, process deposits, provide aftercare info, and answer any questions. What can I help you with?",
      sender: 'bot',
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [showScheduler, setShowScheduler] = useState(false);
  const [showDeposit, setShowDeposit] = useState(false);
  const [showPortfolio, setShowPortfolio] = useState(false);
  const [showAftercareInfo, setShowAftercareInfo] = useState(false);
  const messagesEndRef = useRef(null);

  // Sample artist data - you can customize this
  const artistInfo = {
    name: "Artist Name",
    specialties: ["Traditional", "Neo-Traditional", "Black & Grey", "Color Realism"],
    hourlyRate: "$150-200",
    minDeposit: "$100",
    contact: {
      phone: "(555) 123-4567",
      email: "artist@studio.com",
      instagram: "@artisthandle"
    },
    availability: ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  };

  const faqs = [
    {
      question: "What's your booking process?",
      answer: "I require a consultation first, either in-person or virtual. After we discuss your design and placement, I'll provide a quote and we can schedule your session with a deposit."
    },
    {
      question: "How much do you charge?",
      answer: `My rate is ${artistInfo.hourlyRate} per hour depending on the complexity. Minimum session is 2 hours. Small pieces may have a shop minimum of $200.`
    },
    {
      question: "Do you require a deposit?",
      answer: `Yes, I require a minimum deposit of ${artistInfo.minDeposit} to secure your appointment. This goes toward your final total and is non-refundable if you cancel within 48 hours.`
    },
    {
      question: "What styles do you specialize in?",
      answer: `I specialize in ${artistInfo.specialties.join(", ")}. Check out my portfolio to see examples of my work.`
    },
    {
      question: "How do I prepare for my appointment?",
      answer: "Eat a good meal, stay hydrated, avoid alcohol 24 hours prior, wear comfortable clothing that allows access to the tattoo area, and get a good night's sleep."
    },
    {
      question: "How long does healing take?",
      answer: "Surface healing takes 2-3 weeks, but complete healing takes 3-4 months. Follow the aftercare instructions I provide for best results."
    }
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const addMessage = (text: string, sender: 'user' | 'bot' = 'user') => {
    const newMessage = {
      id: messages.length + 1,
      text,
      sender,
      timestamp: new Date()
    };
    setMessages(prev => [...prev, newMessage]);
  };

  const handleSendMessage = () => {
    if (input.trim()) {
      addMessage(input);
      processUserMessage(input.toLowerCase());
      setInput('');
    }
  };

  const processUserMessage = (message: string) => {
    setTimeout(() => {
      if (message.includes('appointment') || message.includes('schedule') || message.includes('book')) {
        addMessage("I'd be happy to help you schedule an appointment. Let me open the scheduling interface for you.", 'bot');
        setShowScheduler(true);
      } else if (message.includes('deposit') || message.includes('payment')) {
        addMessage("I can help you with deposit information and processing. Let me show you the options.", 'bot');
        setShowDeposit(true);
      } else if (message.includes('portfolio') || message.includes('work') || message.includes('examples')) {
        addMessage("I'll show you the artist's portfolio. Here are some recent works:", 'bot');
        setShowPortfolio(true);
      } else if (message.includes('aftercare') || message.includes('healing') || message.includes('care')) {
        addMessage("Here's the comprehensive aftercare information:", 'bot');
        setShowAftercareInfo(true);
      } else if (message.includes('price') || message.includes('cost') || message.includes('rate')) {
        addMessage(`Current rates are ${artistInfo.hourlyRate} per hour. Pricing depends on size, complexity, and placement. Would you like to schedule a consultation for an accurate quote?`, 'bot');
      } else if (message.includes('contact') || message.includes('phone') || message.includes('call')) {
        addMessage(`You can reach the artist at ${artistInfo.contact.phone} or ${artistInfo.contact.email}. Instagram: ${artistInfo.contact.instagram}. Would you like me to schedule a callback?`, 'bot');
      } else if (message.includes('availability') || message.includes('available') || message.includes('open')) {
        addMessage(`Current availability is ${artistInfo.availability.join(", ")}. Would you like to check specific dates or book a consultation?`, 'bot');
      } else {
        // Check if message matches any FAQ
        const matchingFaq = faqs.find(faq =>
          faq.question.toLowerCase().includes(message) ||
          message.includes(faq.question.toLowerCase().split(' ').slice(0, 2).join(' '))
        );

        if (matchingFaq) {
          addMessage(matchingFaq.answer, 'bot');
        } else {
          addMessage("I can help you with scheduling appointments, viewing portfolios, processing deposits, aftercare information, pricing, and general questions about the artist. What would you like to know more about?", 'bot');
        }
      }
    }, 500);
  };

  const handleQuickAction = (action: string) => {
    switch (action) {
      case 'schedule':
        addMessage("I'd like to schedule an appointment");
        setShowScheduler(true);
        break;
      case 'portfolio':
        addMessage("Can I see the portfolio?");
        setShowPortfolio(true);
        break;
      case 'deposit':
        addMessage("I'd like to make a deposit");
        setShowDeposit(true);
        break;
      case 'aftercare':
        addMessage("Can I get aftercare information?");
        setShowAftercareInfo(true);
        break;
      case 'contact':
        addMessage("How can I contact the artist?");
        processUserMessage('contact');
        break;
      case 'pricing':
        addMessage("What are your rates?");
        processUserMessage('price');
        break;
    }
  };

  const SchedulingInterface = () => (
    <div className="bg-gray-800 p-4 rounded-lg mb-4 border border-teal-400">
      <h3 className="text-teal-400 font-bold mb-3">Schedule Appointment</h3>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-blue-200 text-sm mb-1">Service Type</label>
          <select className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600">
            <option>Consultation</option>
            <option>Small Tattoo (2-3 hrs)</option>
            <option>Medium Tattoo (4-6 hrs)</option>
            <option>Large Tattoo (Full Day)</option>
            <option>Touch-up</option>
          </select>
        </div>
        <div>
          <label className="block text-blue-200 text-sm mb-1">Preferred Date</label>
          <input type="date" className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600" />
        </div>
        <div>
          <label className="block text-blue-200 text-sm mb-1">Name</label>
          <input type="text" className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600" placeholder="Your name" />
        </div>
        <div>
          <label className="block text-blue-200 text-sm mb-1">Phone</label>
          <input type="tel" className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600" placeholder="(555) 123-4567" />
        </div>
        <div className="col-span-2">
          <label className="block text-blue-200 text-sm mb-1">Design Description</label>
          <textarea className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600" rows={3} placeholder="Describe your tattoo idea..."></textarea>
        </div>
      </div>
      <button className="bg-teal-500 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded mt-3">
        Submit Request
      </button>
      <button
        onClick={() => setShowScheduler(false)}
        className="bg-gray-600 hover:bg-gray-700 text-white py-2 px-4 rounded mt-3 ml-2"
      >
        Close
      </button>
    </div>
  );

  const DepositInterface = () => (
    <div className="bg-gray-800 p-4 rounded-lg mb-4 border border-teal-400">
      <h3 className="text-teal-400 font-bold mb-3">Deposit Information</h3>
      <div className="text-blue-200 mb-4">
        <p>• Minimum deposit: {artistInfo.minDeposit}</p>
        <p>• Deposits are applied to your final total</p>
        <p>• Non-refundable if cancelled within 48 hours</p>
        <p>• Accepted methods: Cash, Card, Venmo, PayPal</p>
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-blue-200 text-sm mb-1">Deposit Amount</label>
          <select className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600">
            <option>{artistInfo.minDeposit} (Minimum)</option>
            <option>$150</option>
            <option>$200</option>
            <option>$250</option>
            <option>Custom Amount</option>
          </select>
        </div>
        <div>
          <label className="block text-blue-200 text-sm mb-1">Payment Method</label>
          <select className="w-full bg-gray-900 text-white p-2 rounded border border-gray-600">
            <option>Credit/Debit Card</option>
            <option>PayPal</option>
            <option>Venmo</option>
            <option>Cash (In Person)</option>
          </select>
        </div>
      </div>
      <button className="bg-teal-500 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded mt-3">
        Process Deposit
      </button>
      <button
        onClick={() => setShowDeposit(false)}
        className="bg-gray-600 hover:bg-gray-700 text-white py-2 px-4 rounded mt-3 ml-2"
      >
        Close
      </button>
    </div>
  );

  const PortfolioInterface = () => (
    <div className="bg-gray-800 p-4 rounded-lg mb-4 border border-teal-400">
      <h3 className="text-teal-400 font-bold mb-3">{artistInfo.name}'s Portfolio</h3>
      <div className="grid grid-cols-2 gap-4 mb-4">
        {artistInfo.specialties.map((style, index) => (
          <div key={index} className="bg-gray-900 p-3 rounded border">
            <div className="h-32 bg-gray-700 rounded mb-2 flex items-center justify-center">
              <span className="text-gray-400">{style} Examples</span>
            </div>
            <p className="text-blue-200 text-sm text-center">{style}</p>
          </div>
        ))}
      </div>
      <div className="text-blue-200 text-sm">
        <p>• Full portfolio available on Instagram: {artistInfo.contact.instagram}</p>
        <p>• High-resolution images available upon consultation</p>
        <p>• Custom design process includes sketches and revisions</p>
        <p>• Rate: {artistInfo.hourlyRate}/hour</p>
      </div>
      <button className="bg-teal-500 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded mt-3">
        Download Portfolio PDF
      </button>
      <button
        onClick={() => setShowPortfolio(false)}
        className="bg-gray-600 hover:bg-gray-700 text-white py-2 px-4 rounded mt-3 ml-2"
      >
        Close
      </button>
    </div>
  );

  const AftercareInterface = () => (
    <div className="bg-gray-800 p-4 rounded-lg mb-4 border border-teal-400">
      <h3 className="text-teal-400 font-bold mb-3">Tattoo Aftercare Instructions</h3>
      <div className="text-blue-200 space-y-3 text-sm">
        <div>
          <h4 className="text-white font-semibold">First 24 Hours:</h4>
          <p>• Keep bandage on for 2-4 hours</p>
          <p>• Gently wash with antibacterial soap and lukewarm water</p>
          <p>• Pat dry with clean paper towel</p>
          <p>• Apply thin layer of recommended ointment</p>
        </div>
        <div>
          <h4 className="text-white font-semibold">Days 2-14:</h4>
          <p>• Wash 2-3 times daily with mild soap</p>
          <p>• Apply fragrance-free moisturizer when dry</p>
          <p>• Do not pick, scratch, or rub the tattoo</p>
          <p>• Avoid soaking in water (pools, baths, hot tubs)</p>
        </div>
        <div>
          <h4 className="text-white font-semibold">Ongoing Care:</h4>
          <p>• Use SPF 30+ sunscreen once healed</p>
          <p>• Keep moisturized to prevent fading</p>
          <p>• Contact {artistInfo.name} with any concerns</p>
        </div>
      </div>
      <button className="bg-teal-500 hover:bg-teal-600 text-black font-bold py-2 px-4 rounded mt-3">
        Download Aftercare PDF
      </button>
      <button
        onClick={() => setShowAftercareInfo(false)}
        className="bg-gray-600 hover:bg-gray-700 text-white py-2 px-4 rounded mt-3 ml-2"
      >
        Close
      </button>
    </div>
  );

  return (
    <div className="min-h-screen bg-black text-white flex flex-col max-w-4xl mx-auto">
      <header className="bg-gray-900 p-4 border-b border-teal-400">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-xl font-bold text-teal-400">Tattoo Artist Assistant</h1>
            <p className="text-xs text-blue-200">Available 24/7 for bookings & info</p>
          </div>
          <div className="text-right">
            <div className="text-sm text-blue-200">{artistInfo.name}</div>
            <div className="text-xs text-teal-400">📞 {artistInfo.contact.phone}</div>
            <div className="text-xs text-gray-400">Currently: With Client</div>
          </div>
        </div>
      </header>

      <div className="flex-1 flex flex-col">
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                  message.sender === 'user'
                    ? 'bg-teal-600 text-black'
                    : 'bg-gray-800 text-blue-200 border border-gray-700'
                }`}
              >
                <p>{message.text}</p>
                <p className="text-xs opacity-70 mt-1">
                  {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                </p>
              </div>
            </div>
          ))}

          {showScheduler && <SchedulingInterface />}
          {showDeposit && <DepositInterface />}
          {showPortfolio && <PortfolioInterface />}
          {showAftercareInfo && <AftercareInterface />}

          <div ref={messagesEndRef} />
        </div>

        <div className="p-4 border-t border-gray-800">
          <div className="grid grid-cols-3 gap-2 mb-4">
            <button
              onClick={() => handleQuickAction('schedule')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <Calendar size={16} />
              Schedule
            </button>
            <button
              onClick={() => handleQuickAction('portfolio')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <User size={16} />
              Portfolio
            </button>
            <button
              onClick={() => handleQuickAction('deposit')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <DollarSign size={16} />
              Deposit
            </button>
            <button
              onClick={() => handleQuickAction('aftercare')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <FileText size={16} />
              Aftercare
            </button>
            <button
              onClick={() => handleQuickAction('contact')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <Phone size={16} />
              Contact
            </button>
            <button
              onClick={() => handleQuickAction('pricing')}
              className="flex items-center justify-center gap-2 bg-gray-800 hover:bg-gray-700 text-blue-200 py-2 px-3 rounded text-sm border border-gray-600"
            >
              <Info size={16} />
              Pricing
            </button>
          </div>

          <div className="flex gap-2">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder="Ask about scheduling, pricing, portfolio, or aftercare..."
              className="flex-1 bg-gray-900 text-white p-3 rounded-lg border border-gray-600 focus:border-teal-400 focus:outline-none"
            />
            <button
              onClick={handleSendMessage}
              className="bg-teal-500 hover:bg-teal-600 text-black p-3 rounded-lg font-medium"
            >
              <Send size={20} />
            </button>
          </div>
          
          <div className="mt-2 text-center">
            <p className="text-xs text-gray-400">
              💬 Share this assistant: <span className="text-teal-400">yourstudio.com/assistant</span>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TattooAssistantBot;

