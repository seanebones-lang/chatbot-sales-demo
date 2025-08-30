/**
 * DeenBot Stability System - Frontend Connection Management
 * Ensures 100% uptime and automatic reconnection for DeenBot
 */

class DeenBotStabilitySystem {
    constructor() {
        this.config = {
            serverUrl: 'http://localhost:8080',
            healthCheckInterval: 10000, // 10 seconds
            reconnectAttempts: 5,
            reconnectDelay: 2000, // 2 seconds
            maxRetries: 3,
            timeout: 15000, // 15 seconds
            fallbackMode: false
        };
        
        this.state = {
            isConnected: false,
            connectionAttempts: 0,
            lastHealthCheck: 0,
            isReconnecting: false,
            fallbackResponses: [],
            connectionHistory: []
        };
        
        this.healthCheckTimer = null;
        this.reconnectTimer = null;
        this.connectionMonitor = null;
        
        this.initializeStabilitySystem();
    }
    
    initializeStabilitySystem() {
        console.log('🔄 Initializing DeenBot Stability System...');
        
        // Start connection monitoring
        this.startConnectionMonitoring();
        
        // Setup health checks
        this.startHealthChecks();
        
        // Setup connection event listeners
        this.setupConnectionEvents();
        
        // Initialize fallback responses
        this.initializeFallbackResponses();
        
        console.log('✅ DeenBot Stability System initialized');
    }
    
    startConnectionMonitoring() {
        this.connectionMonitor = setInterval(() => {
            this.monitorConnection();
        }, 5000); // Check every 5 seconds
    }
    
    startHealthChecks() {
        this.healthCheckTimer = setInterval(() => {
            this.performHealthCheck();
        }, this.config.healthCheckInterval);
    }
    
    async performHealthCheck() {
        try {
            const response = await fetch(`${this.config.serverUrl}/health`, {
                method: 'GET',
                timeout: 5000
            });
            
            if (response.ok) {
                const data = await response.json();
                this.updateConnectionStatus(true, 'healthy');
                this.state.lastHealthCheck = Date.now();
                
                // Log connection success
                this.logConnectionEvent('health_check_success', data);
                
            } else {
                this.updateConnectionStatus(false, 'health_check_failed');
                this.logConnectionEvent('health_check_failed', { status: response.status });
            }
            
        } catch (error) {
            this.updateConnectionStatus(false, 'health_check_error');
            this.logConnectionEvent('health_check_error', { error: error.message });
            
            // Attempt reconnection if not already trying
            if (!this.state.isReconnecting) {
                this.attemptReconnection();
            }
        }
    }
    
    async monitorConnection() {
        if (this.state.isConnected) {
            // Check if connection is still responsive
            try {
                const response = await fetch(`${this.config.serverUrl}/status`, {
                    method: 'GET',
                    timeout: 3000
                });
                
                if (!response.ok) {
                    this.updateConnectionStatus(false, 'connection_lost');
                    this.attemptReconnection();
                }
                
            } catch (error) {
                this.updateConnectionStatus(false, 'connection_monitor_error');
                this.attemptReconnection();
            }
        } else {
            // Not connected, try to reconnect
            if (!this.state.isReconnecting) {
                this.attemptReconnection();
            }
        }
    }
    
    async attemptReconnection() {
        if (this.state.isReconnecting || this.state.connectionAttempts >= this.config.reconnectAttempts) {
            return;
        }
        
        this.state.isReconnecting = true;
        this.state.connectionAttempts++;
        
        console.log(`🔄 Attempting reconnection (${this.state.connectionAttempts}/${this.config.reconnectAttempts})...`);
        
        try {
            // Test connection
            const response = await fetch(`${this.config.serverUrl}/health`, {
                method: 'GET',
                timeout: 5000
            });
            
            if (response.ok) {
                this.updateConnectionStatus(true, 'reconnected');
                this.state.connectionAttempts = 0;
                this.state.isReconnecting = false;
                
                console.log('✅ Successfully reconnected to DeenBot');
                this.logConnectionEvent('reconnection_success');
                
                // Notify chat interface
                this.notifyConnectionRestored();
                
            } else {
                throw new Error(`HTTP ${response.status}`);
            }
            
        } catch (error) {
            console.log(`❌ Reconnection attempt ${this.state.connectionAttempts} failed: ${error.message}`);
            this.logConnectionEvent('reconnection_failed', { error: error.message });
            
            // Schedule next reconnection attempt
            if (this.state.connectionAttempts < this.config.reconnectAttempts) {
                this.reconnectTimer = setTimeout(() => {
                    this.state.isReconnecting = false;
                    this.attemptReconnection();
                }, this.config.reconnectDelay * this.state.connectionAttempts);
            } else {
                // Max attempts reached, enable fallback mode
                this.enableFallbackMode();
            }
        }
    }
    
    updateConnectionStatus(isConnected, status) {
        const wasConnected = this.state.isConnected;
        this.state.isConnected = isConnected;
        
        if (wasConnected !== isConnected) {
            this.logConnectionEvent(isConnected ? 'connected' : 'disconnected', { status });
            
            // Update UI indicators
            this.updateConnectionUI(isConnected, status);
            
            // Notify chat interface
            if (isConnected) {
                this.notifyConnectionRestored();
            } else {
                this.notifyConnectionLost();
            }
        }
    }
    
    updateConnectionUI(isConnected, status) {
        // Update connection status indicator
        const statusElement = document.querySelector('.chat-status');
        if (statusElement) {
            if (isConnected) {
                statusElement.textContent = '● Online';
                statusElement.className = 'chat-status online';
            } else {
                statusElement.textContent = '● Offline';
                statusElement.className = 'chat-status offline';
            }
        }
        
        // Update chat input state
        const chatInput = document.getElementById('chatInput');
        const sendButton = document.getElementById('sendButton');
        
        if (chatInput && sendButton) {
            if (isConnected) {
                chatInput.placeholder = "Ask me anything about Islam...";
                chatInput.disabled = false;
                sendButton.disabled = false;
            } else {
                chatInput.placeholder = "DeenBot is currently offline. Reconnecting...";
                chatInput.disabled = true;
                sendButton.disabled = true;
            }
        }
    }
    
    enableFallbackMode() {
        this.config.fallbackMode = true;
        console.log('🔄 Enabling fallback mode - DeenBot offline');
        
        // Update UI for fallback mode
        this.updateConnectionUI(false, 'fallback_mode');
        
        // Notify user
        this.showFallbackNotification();
    }
    
    disableFallbackMode() {
        this.config.fallbackMode = false;
        console.log('✅ Disabling fallback mode - DeenBot restored');
    }
    
    showFallbackNotification() {
        // Add fallback message to chat
        if (window.deenbotChatInstance) {
            window.deenbotChatInstance.addFallbackMessage();
        }
    }
    
    async sendMessageWithStability(message) {
        if (!this.state.isConnected && !this.config.fallbackMode) {
            throw new Error('DeenBot is offline and fallback mode is disabled');
        }
        
        if (this.config.fallbackMode) {
            return this.getFallbackResponse(message);
        }
        
        // Try to send with retry logic
        for (let attempt = 1; attempt <= this.config.maxRetries; attempt++) {
            try {
                const response = await fetch(`${this.config.serverUrl}/chat`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message }),
                    timeout: this.config.timeout
                });
                
                if (response.ok) {
                    const data = await response.json();
                    this.logConnectionEvent('message_sent_success', { attempt });
                    return data;
                } else {
                    throw new Error(`HTTP ${response.status}`);
                }
                
            } catch (error) {
                console.log(`❌ Message send attempt ${attempt} failed: ${error.message}`);
                
                if (attempt === this.config.maxRetries) {
                    // All retries failed, enable fallback mode
                    this.enableFallbackMode();
                    return this.getFallbackResponse(message);
                }
                
                // Wait before retry
                await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
            }
        }
    }
    
    getFallbackResponse(message) {
        // Provide helpful fallback responses when DeenBot is offline
        const fallbackResponses = {
            'prayer': "I'm currently offline, but I can tell you that prayer is one of the Five Pillars of Islam. Please check reliable Islamic sources for detailed guidance.",
            'fasting': "I'm currently offline, but fasting during Ramadan is obligatory for all adult Muslims. Please consult with your local imam for specific questions.",
            'halal': "I'm currently offline, but halal refers to what is permissible in Islam. Please check reliable Islamic sources for detailed guidance.",
            'default': "I'm currently offline and unable to provide detailed Islamic guidance. Please try again in a few moments, or consult with your local imam or reliable Islamic sources."
        };
        
        // Try to match question type
        const lowerMessage = message.toLowerCase();
        if (lowerMessage.includes('pray') || lowerMessage.includes('salah')) {
            return { response: fallbackResponses.prayer, source: 'Fallback Mode' };
        } else if (lowerMessage.includes('fast') || lowerMessage.includes('ramadan')) {
            return { response: fallbackResponses.fasting, source: 'Fallback Mode' };
        } else if (lowerMessage.includes('halal') || lowerMessage.includes('haram')) {
            return { response: fallbackResponses.halal, source: 'Fallback Mode' };
        } else {
            return { response: fallbackResponses.default, source: 'Fallback Mode' };
        }
    }
    
    initializeFallbackResponses() {
        this.state.fallbackResponses = [
            "I'm currently offline. Please try again in a few moments.",
            "DeenBot is temporarily unavailable. Please consult with your local imam.",
            "I'm experiencing connection issues. Please check back soon.",
            "Currently offline. For urgent questions, please contact your local mosque."
        ];
    }
    
    logConnectionEvent(eventType, data = {}) {
        const event = {
            timestamp: new Date().toISOString(),
            event: eventType,
            data: data,
            connectionState: this.state.isConnected,
            attempts: this.state.connectionAttempts
        };
        
        this.state.connectionHistory.push(event);
        
        // Keep only last 100 events
        if (this.state.connectionHistory.length > 100) {
            this.state.connectionHistory.shift();
        }
        
        console.log(`📊 Connection Event: ${eventType}`, event);
    }
    
    getConnectionStats() {
        const now = Date.now();
        const uptime = this.state.lastHealthCheck > 0 ? now - this.state.lastHealthCheck : 0;
        
        return {
            isConnected: this.state.isConnected,
            uptime: uptime,
            connectionAttempts: this.state.connectionAttempts,
            isReconnecting: this.state.isReconnecting,
            fallbackMode: this.config.fallbackMode,
            lastHealthCheck: this.state.lastHealthCheck,
            connectionHistory: this.state.connectionHistory.length
        };
    }
    
    notifyConnectionRestored() {
        // Dispatch custom event for chat interface
        const event = new CustomEvent('deenbotConnectionRestored', {
            detail: { timestamp: Date.now() }
        });
        document.dispatchEvent(event);
    }
    
    notifyConnectionLost() {
        // Dispatch custom event for chat interface
        const event = new CustomEvent('deenbotConnectionLost', {
            detail: { timestamp: Date.now() }
        });
        document.dispatchEvent(event);
    }
    
    setupConnectionEvents() {
        // Listen for page visibility changes
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden) {
                // Page became visible, check connection
                this.performHealthCheck();
            }
        });
        
        // Listen for online/offline events
        window.addEventListener('online', () => {
            console.log('🌐 Internet connection restored');
            this.attemptReconnection();
        });
        
        window.addEventListener('offline', () => {
            console.log('🌐 Internet connection lost');
            this.updateConnectionStatus(false, 'internet_offline');
        });
    }
    
    cleanup() {
        // Clear all timers
        if (this.healthCheckTimer) {
            clearInterval(this.healthCheckTimer);
        }
        if (this.reconnectTimer) {
            clearTimeout(this.reconnectTimer);
        }
        if (this.connectionMonitor) {
            clearInterval(this.connectionMonitor);
        }
        
        console.log('🧹 DeenBot Stability System cleaned up');
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = DeenBotStabilitySystem;
} else {
    // Browser environment
    window.DeenBotStabilitySystem = DeenBotStabilitySystem;
}
