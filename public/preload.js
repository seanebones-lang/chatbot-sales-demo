const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  // You can expose functions here if needed for future features
  platform: process.platform,
  version: process.versions.electron,
  
  // Example: Send message to main process
  sendMessage: (message) => ipcRenderer.send('message', message),
  
  // Example: Receive message from main process
  onMessage: (callback) => ipcRenderer.on('message', callback),
  
  // Example: Get app info
  getAppInfo: () => ({
    name: 'Islamic Study Guide',
    version: '1.0.0',
    description: 'Complete Islamic Knowledge Application'
  })
});

// Handle window controls
window.addEventListener('DOMContentLoaded', () => {
  // Add any initialization code here
  console.log('Islamic Study Guide - Preload script loaded');
});

