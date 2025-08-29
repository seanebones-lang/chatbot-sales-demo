// Universal PDF Delivery System
// This script provides PDF delivery functionality across all pages

class PDFDeliverySystem {
    constructor() {
        this.initializeModals();
        this.setupEventListeners();
    }

    initializeModals() {
        // Create universal PDF delivery modal
        if (!document.getElementById('universalPdfModal')) {
            const modalHTML = `
                <div id="universalPdfModal" class="pdf-modal" style="display: none;">
                    <div class="pdf-modal-content">
                        <span class="pdf-modal-close" onclick="pdfDelivery.closeModal()">&times;</span>
                        <h2 id="pdfModalTitle" style="color: #FFD700; margin-bottom: 20px;">📄 Request PDF</h2>
                        <p id="pdfModalDescription" style="color: #E0E0E0; margin-bottom: 20px;">
                            Enter your contact information to receive this PDF via email or text message:
                        </p>
                        
                        <form id="pdfDeliveryForm" onsubmit="pdfDelivery.submitRequest(event)">
                            <div class="form-group">
                                <label for="pdfName">Full Name:</label>
                                <input type="text" id="pdfName" name="name" required 
                                       placeholder="Enter your full name">
                            </div>
                            
                            <div class="form-group">
                                <label for="pdfEmail">Email Address:</label>
                                <input type="email" id="pdfEmail" name="email" 
                                       placeholder="Enter your email address">
                            </div>
                            
                            <div class="form-group">
                                <label for="pdfPhone">Phone Number:</label>
                                <input type="tel" id="pdfPhone" name="phone" 
                                       placeholder="Enter your phone number">
                            </div>
                            
                            <div class="form-group">
                                <label for="pdfDeliveryMethod">Delivery Method:</label>
                                <select id="pdfDeliveryMethod" name="deliveryMethod" required>
                                    <option value="">Select delivery method</option>
                                    <option value="email">📧 Email PDF</option>
                                    <option value="text">📱 Text Message Link</option>
                                    <option value="both">📧📱 Both Email & Text</option>
                                </select>
                            </div>
                            
                            <div class="form-group">
                                <label for="pdfNotes">Additional Notes (Optional):</label>
                                <textarea id="pdfNotes" name="notes" rows="3" 
                                          placeholder="Any special requests or additional information..."></textarea>
                            </div>
                            
                            <div class="form-actions">
                                <button type="submit" class="submit-pdf-btn">📤 Submit Request</button>
                                <button type="button" class="cancel-pdf-btn" onclick="pdfDelivery.closeModal()">❌ Cancel</button>
                            </div>
                        </form>
                        
                        <div id="pdfSuccessMessage" class="success-message" style="display: none;">
                            <h3 style="color: #98FB98;">✅ Request Submitted Successfully!</h3>
                            <p style="color: #E0E0E0;">
                                Thank you for your request. You will receive your PDF within 24 hours via your chosen delivery method.
                            </p>
                            <p style="color: #87CEEB; font-size: 0.9rem;">
                                📧 Email: Check your inbox and spam folder<br>
                                📱 Text: You'll receive a secure download link
                            </p>
                        </div>
                    </div>
                </div>
            `;
            document.body.insertAdjacentHTML('beforeend', modalHTML);
        }

        // Add CSS styles
        if (!document.getElementById('pdfDeliveryStyles')) {
            const styles = `
                <style id="pdfDeliveryStyles">
                    .pdf-modal {
                        position: fixed;
                        z-index: 10000;
                        left: 0;
                        top: 0;
                        width: 100%;
                        height: 100%;
                        background-color: rgba(0, 0, 0, 0.8);
                        backdrop-filter: blur(5px);
                    }

                    .pdf-modal-content {
                        background: linear-gradient(135deg, #1a1f2e 0%, #0f1419 100%);
                        margin: 5% auto;
                        padding: 30px;
                        border: 2px solid rgba(255, 215, 0, 0.3);
                        border-radius: 20px;
                        width: 90%;
                        max-width: 500px;
                        position: relative;
                        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
                    }

                    .pdf-modal-close {
                        color: #aaa;
                        float: right;
                        font-size: 28px;
                        font-weight: bold;
                        cursor: pointer;
                        position: absolute;
                        right: 20px;
                        top: 15px;
                        transition: all 0.3s ease;
                    }

                    .pdf-modal-close:hover {
                        color: #FFD700;
                        transform: scale(1.1);
                    }

                    .form-group {
                        margin-bottom: 20px;
                    }

                    .form-group label {
                        display: block;
                        color: #87CEEB;
                        margin-bottom: 8px;
                        font-weight: bold;
                    }

                    .form-group input,
                    .form-group select,
                    .form-group textarea {
                        width: 100%;
                        padding: 12px;
                        border: 2px solid rgba(68, 68, 68, 0.5);
                        border-radius: 10px;
                        background: rgba(18, 18, 18, 0.8);
                        color: #E0E0E0;
                        font-size: 16px;
                        transition: all 0.3s ease;
                    }

                    .form-group input:focus,
                    .form-group select:focus,
                    .form-group textarea:focus {
                        outline: none;
                        border-color: #1E90FF;
                        box-shadow: 0 0 20px rgba(30, 144, 255, 0.3);
                        transform: scale(1.02);
                    }

                    .form-group input:hover,
                    .form-group select:hover,
                    .form-group textarea:hover {
                        border-color: rgba(30, 144, 255, 0.4);
                    }

                    .form-actions {
                        display: flex;
                        gap: 15px;
                        justify-content: center;
                        margin-top: 25px;
                    }

                    .submit-pdf-btn,
                    .cancel-pdf-btn {
                        padding: 12px 25px;
                        border: none;
                        border-radius: 10px;
                        cursor: pointer;
                        font-size: 16px;
                        font-weight: bold;
                        transition: all 0.3s ease;
                    }

                    .submit-pdf-btn {
                        background: linear-gradient(135deg, #1E90FF 0%, #004D61 100%);
                        color: white;
                    }

                    .submit-pdf-btn:hover {
                        transform: translateY(-2px);
                        box-shadow: 0 10px 25px rgba(30, 144, 255, 0.4);
                    }

                    .cancel-pdf-btn {
                        background: rgba(68, 68, 68, 0.5);
                        color: #E0E0E0;
                        border: 1px solid rgba(68, 68, 68, 0.8);
                    }

                    .cancel-pdf-btn:hover {
                        background: rgba(68, 68, 68, 0.7);
                        transform: translateY(-2px);
                    }

                    .success-message {
                        text-align: center;
                        padding: 20px;
                        background: rgba(152, 251, 152, 0.1);
                        border-radius: 15px;
                        border: 1px solid rgba(152, 251, 152, 0.3);
                    }

                    @media (max-width: 768px) {
                        .pdf-modal-content {
                            width: 95%;
                            margin: 10% auto;
                            padding: 20px;
                        }
                        
                        .form-actions {
                            flex-direction: column;
                        }
                    }
                </style>
            `;
            document.head.insertAdjacentHTML('beforeend', styles);
        }
    }

    setupEventListeners() {
        // Close modal when clicking outside
        document.addEventListener('click', (e) => {
            if (e.target.id === 'universalPdfModal') {
                this.closeModal();
            }
        });

        // Close modal with Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                this.closeModal();
            }
        });
    }

    openModal(pdfTitle, pdfDescription, pdfType = 'document') {
        const modal = document.getElementById('universalPdfModal');
        const title = document.getElementById('pdfModalTitle');
        const description = document.getElementById('pdfModalDescription');
        const form = document.getElementById('pdfDeliveryForm');
        const successMessage = document.getElementById('pdfSuccessMessage');

        // Set modal content
        title.textContent = `📄 Request ${pdfTitle}`;
        description.textContent = pdfDescription || `Enter your contact information to receive the ${pdfTitle} PDF via email or text message:`;

        // Store PDF information
        this.currentPdfRequest = {
            title: pdfTitle,
            type: pdfType,
            timestamp: new Date().toISOString()
        };

        // Show form, hide success message
        form.style.display = 'block';
        successMessage.style.display = 'none';

        // Show modal
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }

    closeModal() {
        const modal = document.getElementById('universalPdfModal');
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
        
        // Reset form
        document.getElementById('pdfDeliveryForm').reset();
    }

    async submitRequest(event) {
        event.preventDefault();
        
        const formData = new FormData(event.target);
        const requestData = {
            ...Object.fromEntries(formData),
            ...this.currentPdfRequest,
            submittedAt: new Date().toISOString()
        };

        // Validate delivery method
        if (!requestData.deliveryMethod) {
            alert('Please select a delivery method.');
            return;
        }

        // Validate contact information
        if (requestData.deliveryMethod === 'email' && !requestData.email) {
            alert('Please provide an email address for email delivery.');
            return;
        }
        if (requestData.deliveryMethod === 'text' && !requestData.phone) {
            alert('Please provide a phone number for text delivery.');
            return;
        }
        if (requestData.deliveryMethod === 'both' && (!requestData.email || !requestData.phone)) {
            alert('Please provide both email and phone number for combined delivery.');
            return;
        }

        try {
            // Show loading state
            const submitBtn = event.target.querySelector('.submit-pdf-btn');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = '📤 Processing...';
            submitBtn.disabled = true;

            // Simulate API call (replace with actual backend integration)
            await this.processPdfRequest(requestData);

            // Show success message
            document.getElementById('pdfDeliveryForm').style.display = 'none';
            document.getElementById('pdfSuccessMessage').style.display = 'block';

            // Auto-close after 5 seconds
            setTimeout(() => {
                this.closeModal();
            }, 5000);

        } catch (error) {
            console.error('PDF request failed:', error);
            alert('There was an error processing your request. Please try again.');
        } finally {
            // Reset button
            const submitBtn = event.target.querySelector('.submit-pdf-btn');
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    }

    async processPdfRequest(requestData) {
        // This is where you would integrate with your backend
        // For now, we'll simulate the process
        
        return new Promise((resolve) => {
            setTimeout(() => {
                console.log('PDF Request Processed:', requestData);
                
                // Here you would typically:
                // 1. Save the request to your database
                // 2. Generate the PDF
                // 3. Send via email/SMS
                // 4. Update request status
                
                resolve({ success: true, requestId: Date.now() });
            }, 1500);
        });
    }

    // Utility function to replace existing PDF buttons
    replacePdfButtons() {
        const pdfButtons = document.querySelectorAll('[onclick*="download"], [onclick*="generatePDF"], .download-btn, .pdf-btn');
        
        pdfButtons.forEach(button => {
            const originalOnClick = button.getAttribute('onclick');
            if (originalOnClick && !originalOnClick.includes('pdfDelivery.openModal')) {
                // Extract PDF title from button text or context
                const pdfTitle = this.extractPdfTitle(button);
                const pdfDescription = this.extractPdfDescription(button);
                
                button.onclick = (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    this.openModal(pdfTitle, pdfDescription);
                };
                
                // Update button text if it's generic
                if (button.textContent.toLowerCase().includes('download') || button.textContent.toLowerCase().includes('pdf')) {
                    button.textContent = '📄 Request PDF';
                }
            }
        });
    }

    extractPdfTitle(button) {
        // Try to extract meaningful title from button context
        const context = button.closest('.verse-item, .hadith-item, .surah-item, .menu-item') || button.parentElement;
        
        if (context) {
            const titleElement = context.querySelector('h3, h4, .title, .name');
            if (titleElement) {
                return titleElement.textContent.trim();
            }
        }
        
        // Fallback to button text or generic title
        return button.textContent.replace(/Download|PDF|Request/gi, '').trim() || 'Document';
    }

    extractPdfDescription(button) {
        const context = button.closest('.verse-item, .hadith-item, .surah-item, .menu-item') || button.parentElement;
        
        if (context) {
            const descElement = context.querySelector('p, .description, .content');
            if (descElement) {
                return `Get the complete ${this.extractPdfTitle(button)} content as a beautifully formatted PDF.`;
            }
        }
        
        return 'Get this content as a beautifully formatted PDF delivered to your email or phone.';
    }
}

// Initialize the PDF delivery system
const pdfDelivery = new PDFDeliverySystem();

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        pdfDelivery.replacePdfButtons();
    });
} else {
    pdfDelivery.replacePdfButtons();
}

// Export for use in other scripts
window.pdfDelivery = pdfDelivery;
