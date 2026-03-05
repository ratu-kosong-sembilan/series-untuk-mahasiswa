/**
 * KIMI Chat Widget for Series Untuk Mahasiswa
 * Integrasi dengan KIMI AI API
 */

(function() {
    'use strict';
    
    // Config dari global variable
    const config = window.KIMI_CHAT_CONFIG || {};
    
    // API Configuration
    const API_BASE_URL = 'https://api.moonshot.cn/v1';
    const API_KEY = config.apiKey || '';
    
    // State
    let isOpen = false;
    let messages = [];
    let isTyping = false;
    
    // Create Widget DOM
    function createWidget() {
        const widgetContainer = document.createElement('div');
        widgetContainer.id = 'kimi-chat-widget';
        
        // Create styles
        const styles = document.createElement('style');
        styles.textContent = getWidgetStyles();
        widgetContainer.appendChild(styles);
        
        // Create HTML structure
        widgetContainer.innerHTML += getWidgetHTML();
        
        document.body.appendChild(widgetContainer);
        
        // Setup event listeners
        setupEventListeners();
        
        // Auto open jika di-enable
        if (config.autoOpen) {
            setTimeout(() => {
                openChat();
            }, config.openDelay || 3000);
        }
    }
    
    // Get Widget Styles
    function getWidgetStyles() {
        const primaryColor = config.primaryColor || '#2563eb';
        const bgColor = config.backgroundColor || '#ffffff';
        const position = config.position === 'bottom-left' ? 'left: 20px;' : 'right: 20px;';
        
        return `
            #kimi-chat-widget {
                position: fixed;
                ${position}
                bottom: 20px;
                z-index: 9999;
                font-family: ${config.fontFamily || 'Inter, sans-serif'};
            }
            
            .kimi-chat-button {
                width: 60px;
                height: 60px;
                border-radius: 50%;
                background: linear-gradient(135deg, ${primaryColor}, #1e40af);
                border: none;
                cursor: pointer;
                box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s ease;
                position: relative;
            }
            
            .kimi-chat-button:hover {
                transform: scale(1.1);
                box-shadow: 0 6px 30px rgba(37, 99, 235, 0.5);
            }
            
            .kimi-chat-button i {
                color: white;
                font-size: 24px;
            }
            
            .kimi-chat-button .notification-badge {
                position: absolute;
                top: -2px;
                right: -2px;
                width: 20px;
                height: 20px;
                background: #ef4444;
                border-radius: 50%;
                border: 2px solid white;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 10px;
                color: white;
                font-weight: bold;
            }
            
            .kimi-chat-window {
                position: absolute;
                ${position}
                bottom: 80px;
                width: ${config.width || '380px'};
                max-width: calc(100vw - 40px);
                height: ${config.maxHeight || '500px'};
                max-height: calc(100vh - 160px);
                background: ${bgColor};
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
                display: flex;
                flex-direction: column;
                overflow: hidden;
                opacity: 0;
                transform: translateY(20px) scale(0.95);
                visibility: hidden;
                transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .kimi-chat-window.open {
                opacity: 1;
                transform: translateY(0) scale(1);
                visibility: visible;
            }
            
            .kimi-chat-header {
                background: linear-gradient(135deg, ${primaryColor}, #1e40af);
                color: white;
                padding: 20px;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            
            .kimi-chat-header-info {
                display: flex;
                align-items: center;
                gap: 12px;
            }
            
            .kimi-chat-avatar {
                width: 44px;
                height: 44px;
                background: white;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
            }
            
            .kimi-chat-title h4 {
                margin: 0;
                font-size: 16px;
                font-weight: 600;
            }
            
            .kimi-chat-title span {
                font-size: 12px;
                opacity: 0.9;
                display: flex;
                align-items: center;
                gap: 4px;
            }
            
            .kimi-chat-title .online-dot {
                width: 8px;
                height: 8px;
                background: #22c55e;
                border-radius: 50%;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .kimi-chat-close {
                background: rgba(255, 255, 255, 0.2);
                border: none;
                width: 32px;
                height: 32px;
                border-radius: 8px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                transition: background 0.2s;
            }
            
            .kimi-chat-close:hover {
                background: rgba(255, 255, 255, 0.3);
            }
            
            .kimi-chat-messages {
                flex: 1;
                overflow-y: auto;
                padding: 20px;
                background: #f8fafc;
            }
            
            .kimi-chat-messages::-webkit-scrollbar {
                width: 6px;
            }
            
            .kimi-chat-messages::-webkit-scrollbar-thumb {
                background: #cbd5e1;
                border-radius: 3px;
            }
            
            .kimi-message {
                display: flex;
                gap: 12px;
                margin-bottom: 16px;
                animation: messageSlide 0.3s ease;
            }
            
            @keyframes messageSlide {
                from {
                    opacity: 0;
                    transform: translateY(10px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .kimi-message.user {
                flex-direction: row-reverse;
            }
            
            .kimi-message-avatar {
                width: 36px;
                height: 36px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 16px;
                flex-shrink: 0;
            }
            
            .kimi-message.bot .kimi-message-avatar {
                background: linear-gradient(135deg, ${primaryColor}, #1e40af);
            }
            
            .kimi-message.user .kimi-message-avatar {
                background: #e2e8f0;
            }
            
            .kimi-message-content {
                max-width: 70%;
                padding: 12px 16px;
                border-radius: 16px;
                font-size: 14px;
                line-height: 1.6;
            }
            
            .kimi-message.bot .kimi-message-content {
                background: white;
                border: 1px solid #e2e8f0;
                border-bottom-left-radius: 4px;
            }
            
            .kimi-message.user .kimi-message-content {
                background: ${primaryColor};
                color: white;
                border-bottom-right-radius: 4px;
            }
            
            .kimi-message-time {
                font-size: 11px;
                color: #94a3b8;
                margin-top: 4px;
                text-align: right;
            }
            
            .kimi-typing {
                display: flex;
                gap: 12px;
                margin-bottom: 16px;
            }
            
            .kimi-typing-indicator {
                background: white;
                border: 1px solid #e2e8f0;
                border-radius: 16px;
                border-bottom-left-radius: 4px;
                padding: 16px 20px;
                display: flex;
                align-items: center;
                gap: 4px;
            }
            
            .kimi-typing-indicator span {
                width: 8px;
                height: 8px;
                background: ${primaryColor};
                border-radius: 50%;
                animation: typingBounce 1.4s infinite ease-in-out both;
            }
            
            .kimi-typing-indicator span:nth-child(1) { animation-delay: -0.32s; }
            .kimi-typing-indicator span:nth-child(2) { animation-delay: -0.16s; }
            
            @keyframes typingBounce {
                0%, 80%, 100% { transform: scale(0); }
                40% { transform: scale(1); }
            }
            
            .kimi-suggested-questions {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-bottom: 16px;
                padding: 0 20px;
            }
            
            .kimi-suggested-question {
                background: white;
                border: 1px solid #e2e8f0;
                border-radius: 20px;
                padding: 8px 16px;
                font-size: 13px;
                color: ${primaryColor};
                cursor: pointer;
                transition: all 0.2s;
            }
            
            .kimi-suggested-question:hover {
                background: ${primaryColor};
                color: white;
                border-color: ${primaryColor};
            }
            
            .kimi-chat-input-container {
                padding: 16px 20px;
                background: white;
                border-top: 1px solid #e2e8f0;
                display: flex;
                gap: 12px;
                align-items: flex-end;
            }
            
            .kimi-chat-input {
                flex: 1;
                border: 1px solid #e2e8f0;
                border-radius: 24px;
                padding: 12px 20px;
                font-size: 14px;
                resize: none;
                max-height: 120px;
                font-family: inherit;
                outline: none;
                transition: border-color 0.2s;
            }
            
            .kimi-chat-input:focus {
                border-color: ${primaryColor};
            }
            
            .kimi-chat-send {
                width: 44px;
                height: 44px;
                border-radius: 50%;
                background: ${primaryColor};
                border: none;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                transition: all 0.2s;
                flex-shrink: 0;
            }
            
            .kimi-chat-send:hover {
                background: #1e40af;
                transform: scale(1.05);
            }
            
            .kimi-chat-send:disabled {
                background: #cbd5e1;
                cursor: not-allowed;
                transform: none;
            }
            
            @media (max-width: 480px) {
                .kimi-chat-window {
                    position: fixed;
                    left: 10px;
                    right: 10px;
                    bottom: 80px;
                    width: auto;
                    max-width: none;
                }
            }
        `;
    }
    
    // Get Widget HTML
    function getWidgetHTML() {
        const welcomeMsg = config.welcomeMessage || 'Halo! Saya asisten AI. Ada yang bisa saya bantu?';
        const placeholder = config.placeholder || 'Ketik pesan...';
        
        let suggestedHTML = '';
        if (config.suggestedQuestions && config.suggestedQuestions.length > 0) {
            suggestedHTML = `
                <div class="kimi-suggested-questions" id="kimi-suggested-questions">
                    ${config.suggestedQuestions.map(q => `
                        <button class="kimi-suggested-question" data-question="${escapeHtml(q)}">${escapeHtml(q)}</button>
                    `).join('')}
                </div>
            `;
        }
        
        return `
            <!-- Chat Button -->
            <button class="kimi-chat-button" id="kimi-chat-toggle" aria-label="Open chat">
                <i class="fas fa-robot"></i>
                <span class="notification-badge" style="display: none;">1</span>
            </button>
            
            <!-- Chat Window -->
            <div class="kimi-chat-window" id="kimi-chat-window">
                <!-- Header -->
                <div class="kimi-chat-header">
                    <div class="kimi-chat-header-info">
                        <div class="kimi-chat-avatar">🤖</div>
                        <div class="kimi-chat-title">
                            <h4>KIMI Assistant</h4>
                            <span><span class="online-dot"></span> Online</span>
                        </div>
                    </div>
                    <button class="kimi-chat-close" id="kimi-chat-close" aria-label="Close chat">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                
                <!-- Messages -->
                <div class="kimi-chat-messages" id="kimi-chat-messages">
                    <div class="kimi-message bot">
                        <div class="kimi-message-avatar">🤖</div>
                        <div>
                            <div class="kimi-message-content">${welcomeMsg}</div>
                            ${config.showTimestamp ? `<div class="kimi-message-time">${getCurrentTime()}</div>` : ''}
                        </div>
                    </div>
                </div>
                
                <!-- Suggested Questions -->
                ${suggestedHTML}
                
                <!-- Input -->
                <div class="kimi-chat-input-container">
                    <textarea 
                        class="kimi-chat-input" 
                        id="kimi-chat-input" 
                        placeholder="${placeholder}"
                        rows="1"
                    ></textarea>
                    <button class="kimi-chat-send" id="kimi-chat-send" aria-label="Send message">
                        <i class="fas fa-paper-plane"></i>
                    </button>
                </div>
            </div>
        `;
    }
    
    // Setup Event Listeners
    function setupEventListeners() {
        const toggleBtn = document.getElementById('kimi-chat-toggle');
        const closeBtn = document.getElementById('kimi-chat-close');
        const chatInput = document.getElementById('kimi-chat-input');
        const sendBtn = document.getElementById('kimi-chat-send');
        
        toggleBtn.addEventListener('click', toggleChat);
        closeBtn.addEventListener('click', closeChat);
        
        sendBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
        
        chatInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = Math.min(this.scrollHeight, 120) + 'px';
        });
        
        const suggestedContainer = document.getElementById('kimi-suggested-questions');
        if (suggestedContainer) {
            suggestedContainer.addEventListener('click', (e) => {
                if (e.target.classList.contains('kimi-suggested-question')) {
                    chatInput.value = e.target.dataset.question;
                    sendMessage();
                }
            });
        }
        
        document.addEventListener('click', (e) => {
            const chatWindow = document.getElementById('kimi-chat-window');
            if (isOpen && !chatWindow.contains(e.target) && !toggleBtn.contains(e.target)) {
                closeChat();
            }
        });
    }
    
    function toggleChat() {
        isOpen ? closeChat() : openChat();
    }
    
    function openChat() {
        document.getElementById('kimi-chat-window').classList.add('open');
        isOpen = true;
        document.querySelector('.notification-badge').style.display = 'none';
        setTimeout(() => document.getElementById('kimi-chat-input').focus(), 300);
        scrollToBottom();
    }
    
    function closeChat() {
        document.getElementById('kimi-chat-window').classList.remove('open');
        isOpen = false;
    }
    
    async function sendMessage() {
        const chatInput = document.getElementById('kimi-chat-input');
        const sendBtn = document.getElementById('kimi-chat-send');
        const message = chatInput.value.trim();
        
        if (!message || isTyping) return;
        
        addMessage(message, 'user');
        chatInput.value = '';
        chatInput.style.height = 'auto';
        
        const suggestedContainer = document.getElementById('kimi-suggested-questions');
        if (suggestedContainer) suggestedContainer.style.display = 'none';
        
        showTyping();
        sendBtn.disabled = true;
        
        try {
            const response = await callKimiAPI(message);
            hideTyping();
            addMessage(response, 'bot');
        } catch (error) {
            hideTyping();
            addMessage('Maaf, terjadi kesalahan. Silakan coba lagi.', 'bot');
            console.error('KIMI API Error:', error);
        }
        
        sendBtn.disabled = false;
    }
    
    async function callKimiAPI(message) {
        if (!API_KEY || API_KEY === 'YOUR_KIMI_API_KEY') {
            return getFallbackResponse(message);
        }
        
        try {
            const response = await fetch(`${API_BASE_URL}/chat/completions`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${API_KEY}`
                },
                body: JSON.stringify({
                    model: 'moonshot-v1-8k',
                    messages: [
                        { role: 'system', content: config.systemContext || 'Anda adalah asisten AI.' },
                        ...messages.map(m => ({ role: m.type === 'user' ? 'user' : 'assistant', content: m.content })),
                        { role: 'user', content: message }
                    ],
                    temperature: 0.7,
                    max_tokens: 1000
                })
            });
            
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            
            const data = await response.json();
            return data.choices[0].message.content;
        } catch (error) {
            console.error('API call failed:', error);
            return getFallbackResponse(message);
        }
    }
    
    function getFallbackResponse(message) {
        const lowerMsg = message.toLowerCase();
        
        if (lowerMsg.includes('phasor')) {
            return 'Phasor adalah representasi vektor dari besaran sinusoidal. Bayangkan vektor yang berputar dengan kecepatan sudut omega. Proyeksi vektor ini pada sumbu horizontal membentuk gelombang sinus!';
        }
        if (lowerMsg.includes('kompleks') || lowerMsg.includes('imaginer')) {
            return 'Bilangan kompleks dengan simbol j digunakan di AC karena bisa merepresentasikan magnitudo dan fase sekaligus! Contoh: V = 100∠30° artinya tegangan 100V dengan fase 30 derajat.';
        }
        if (lowerMsg.includes('impedansi')) {
            return 'Impedansi (Z) adalah hambatan total dalam rangkaian AC. Resistor: Z=R, Induktor: Z=jωL, Kapasitor: Z=1/(jωC). Impedansi total: Z_total = R + j(XL - XC)';
        }
        if (lowerMsg.includes('daya')) {
            return 'Dalam sistem AC ada 3 daya: Daya Aktif (P) dalam Watt, Daya Reaktif (Q) dalam VAR, dan Daya Kompleks (S) dalam VA. Faktor Daya = cos(θ) = P/S.';
        }
        
        return 'Terima kasih atas pertanyaannya! Saya bisa membantu memahami konsep bilangan kompleks, phasor, impedansi RLC, dan analisis daya dalam sistem AC. Silakan ajukan pertanyaan spesifik!';
    }
    
    function addMessage(content, type) {
        const messagesContainer = document.getElementById('kimi-chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `kimi-message ${type}`;
        
        const avatar = type === 'bot' ? '🤖' : '👤';
        const time = config.showTimestamp ? `<div class="kimi-message-time">${getCurrentTime()}</div>` : '';
        
        messageDiv.innerHTML = `
            <div class="kimi-message-avatar">${avatar}</div>
            <div>
                <div class="kimi-message-content">${formatMessage(content)}</div>
                ${time}
            </div>
        `;
        
        messagesContainer.appendChild(messageDiv);
        scrollToBottom();
        messages.push({ type, content });
        if (messages.length > 20) messages = messages.slice(-20);
    }
    
    function formatMessage(content) {
        return content
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
    }
    
    function showTyping() {
        const messagesContainer = document.getElementById('kimi-chat-messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'kimi-typing';
        typingDiv.id = 'kimi-typing-indicator';
        typingDiv.innerHTML = `
            <div class="kimi-message-avatar">🤖</div>
            <div class="kimi-typing-indicator">
                <span></span><span></span><span></span>
            </div>
        `;
        messagesContainer.appendChild(typingDiv);
        scrollToBottom();
        isTyping = true;
    }
    
    function hideTyping() {
        const indicator = document.getElementById('kimi-typing-indicator');
        if (indicator) indicator.remove();
        isTyping = false;
    }
    
    function scrollToBottom() {
        const container = document.getElementById('kimi-chat-messages');
        container.scrollTop = container.scrollHeight;
    }
    
    function getCurrentTime() {
        return new Date().toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit' });
    }
    
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createWidget);
    } else {
        createWidget();
    }
})();
