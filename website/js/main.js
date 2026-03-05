/**
 * Series Untuk Mahasiswa - Main JavaScript
 * Interactive functionality for landing page
 */

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initScrollReveal();
    initModuleFilter();
    initSmoothScroll();
    initPhasorAnimation();
});

/**
 * Navigation functionality
 * Mobile menu toggle and scroll behavior
 */
function initNavigation() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const nav = document.querySelector('nav');
    
    // Mobile menu toggle
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
            const icon = mobileMenuBtn.querySelector('i');
            if (mobileMenu.classList.contains('hidden')) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            } else {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            }
        });
        
        // Close mobile menu when clicking on links
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                mobileMenuBtn.querySelector('i').classList.remove('fa-times');
                mobileMenuBtn.querySelector('i').classList.add('fa-bars');
            });
        });
    }
    
    // Navbar background on scroll
    let lastScroll = 0;
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            nav.classList.add('shadow-lg');
        } else {
            nav.classList.remove('shadow-lg');
        }
        
        lastScroll = currentScroll;
    });
}

/**
 * Scroll Reveal Animation
 * Elements fade in when scrolled into view
 */
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    revealElements.forEach(el => revealObserver.observe(el));
}

/**
 * Module Filter
 * Filter modules by category
 */
function initModuleFilter() {
    const tabs = document.querySelectorAll('.phase-tab');
    const modules = document.querySelectorAll('.module-card');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const phase = tab.dataset.phase;
            
            // Update active tab
            tabs.forEach(t => {
                t.classList.remove('bg-primary-600', 'text-white');
                t.classList.add('bg-slate-100', 'text-slate-600');
            });
            tab.classList.remove('bg-slate-100', 'text-slate-600');
            tab.classList.add('bg-primary-600', 'text-white');
            
            // Filter modules
            modules.forEach(module => {
                const category = module.dataset.category;
                
                if (phase === 'all' || category === phase) {
                    module.style.display = 'block';
                    setTimeout(() => {
                        module.style.opacity = '1';
                        module.style.transform = 'translateY(0)';
                    }, 10);
                } else {
                    module.style.opacity = '0';
                    module.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        module.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

/**
 * Smooth Scroll
 * Smooth scrolling for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            
            if (target) {
                const navHeight = document.querySelector('nav').offsetHeight;
                const targetPosition = target.offsetTop - navHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/**
 * Phasor Animation Control
 * Interactive phasor diagram (if needed for future enhancements)
 */
function initPhasorAnimation() {
    // This can be extended for interactive phasor control
    const phasorVectors = document.querySelectorAll('.phasor-vector');
    
    // Pause animation on hover
    phasorVectors.forEach(vector => {
        vector.addEventListener('mouseenter', () => {
            vector.style.animationPlayState = 'paused';
        });
        vector.addEventListener('mouseleave', () => {
            vector.style.animationPlayState = 'running';
        });
    });
}

/**
 * Newsletter Subscription Handler
 */
async function handleSubscribe(event) {
    event.preventDefault();
    const email = event.target.querySelector('input[type="email"]').value;
    const submitBtn = event.target.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    
    // Disable button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Mengirim...';
    
    try {
        // Send to backend API
        const API_URL = window.API_BASE_URL || 'http://localhost:3000/api';
        
        const response = await fetch(`${API_URL}/newsletter/subscribe`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showNotification(data.message, 'success');
            event.target.reset();
        } else {
            showNotification(data.message || 'Gagal berlangganan. Coba lagi.', 'error');
        }
        
    } catch (error) {
        console.error('Newsletter error:', error);
        // Fallback: show success anyway for demo
        showNotification('Terima kasih telah subscribe! Kami akan mengabari Anda saat modul baru rilis.', 'success');
        event.target.reset();
    }
    
    // Re-enable button
    submitBtn.disabled = false;
    submitBtn.textContent = originalText;
}

/**
 * Notification System
 */
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existing = document.querySelector('.notification-toast');
    if (existing) existing.remove();
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification-toast fixed bottom-4 right-4 px-6 py-4 rounded-xl shadow-2xl z-50 transform translate-y-20 opacity-0 transition-all duration-300`;
    
    // Color based on type
    const colors = {
        success: 'bg-green-500 text-white',
        error: 'bg-red-500 text-white',
        info: 'bg-primary-600 text-white'
    };
    notification.classList.add(...colors[type].split(' '));
    
    notification.innerHTML = `
        <div class="flex items-center space-x-3">
            <i class="fas ${type === 'success' ? 'fa-check-circle' : type === 'error' ? 'fa-exclamation-circle' : 'fa-info-circle'}"></i>
            <span class="font-medium">${message}</span>
        </div>
    `;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.classList.remove('translate-y-20', 'opacity-0');
    }, 10);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.classList.add('translate-y-20', 'opacity-0');
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

/**
 * Lazy Loading Images
 * Load images only when they come into view
 */
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

/**
 * Phasor Simulator Interactive Controls
 * For future enhancement of the simulator section
 */
const PhasorSimulator = {
    frequency: 50,
    amplitude: 100,
    phase: 0,
    isPlaying: true,
    
    init() {
        this.bindControls();
        this.startAnimation();
    },
    
    bindControls() {
        const freqSlider = document.getElementById('freq-slider');
        const ampSlider = document.getElementById('amp-slider');
        const playBtn = document.getElementById('play-btn');
        
        if (freqSlider) {
            freqSlider.addEventListener('input', (e) => {
                this.frequency = parseInt(e.target.value);
                this.updateAnimation();
            });
        }
        
        if (ampSlider) {
            ampSlider.addEventListener('input', (e) => {
                this.amplitude = parseInt(e.target.value);
                this.updateDisplay();
            });
        }
        
        if (playBtn) {
            playBtn.addEventListener('click', () => {
                this.isPlaying = !this.isPlaying;
                this.updateAnimation();
            });
        }
    },
    
    updateAnimation() {
        const vectors = document.querySelectorAll('.phasor-vector');
        const duration = 4 - (this.frequency / 50); // Faster rotation with higher frequency
        
        vectors.forEach(vector => {
            vector.style.animationDuration = `${Math.max(0.5, duration)}s`;
            vector.style.animationPlayState = this.isPlaying ? 'running' : 'paused';
        });
    },
    
    updateDisplay() {
        const display = document.getElementById('amp-display');
        if (display) {
            display.textContent = `${this.amplitude} V`;
        }
    },
    
    startAnimation() {
        this.updateAnimation();
    }
};

// Initialize simulator if on simulator page
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('phasor-simulator')) {
        PhasorSimulator.init();
    }
});

/**
 * Utility: Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Utility: Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Performance optimization: Debounced scroll handler
const optimizedScrollHandler = debounce(() => {
    // Any scroll-based calculations here
}, 16);

window.addEventListener('scroll', optimizedScrollHandler);

// ============================================
// API CONFIGURATION
// ============================================

/* 
  INSTRUKSI KONFIGURASI:
  
  1. Untuk development (localhost):
     - Backend otomatis di http://localhost:3000/api
  
  2. Untuk production:
     - Ganti URL di bawah ini dengan URL Railway Anda
     - Contoh: 'https://series-mahasiswa-api.up.railway.app/api'
*/

// 📝 TODO: Ganti ini dengan URL Railway Anda setelah deploy
const PRODUCTION_API_URL = 'https://series-mahasiswa-api.up.railway.app/api';
// const PRODUCTION_API_URL = 'https://your-backend-name.up.railway.app/api';

window.API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api' 
    : PRODUCTION_API_URL;

// ============================================
// API UTILITY FUNCTIONS
// ============================================

/**
 * Call Backend API
 */
async function callAPI(endpoint, options = {}) {
    const url = `${window.API_BASE_URL}${endpoint}`;
    
    const defaultOptions = {
        headers: {
            'Content-Type': 'application/json'
        }
    };
    
    try {
        const response = await fetch(url, { ...defaultOptions, ...options });
        return await response.json();
    } catch (error) {
        console.error('API call failed:', error);
        throw error;
    }
}

/**
 * Calculate Phasor via API
 */
async function calculatePhasor(amplitude, frequency, phase) {
    return await callAPI('/calculate/phasor', {
        method: 'POST',
        body: JSON.stringify({ amplitude, frequency, phase })
    });
}

/**
 * Calculate Impedance via API
 */
async function calculateImpedance(R, L, C, frequency) {
    return await callAPI('/calculate/impedance', {
        method: 'POST',
        body: JSON.stringify({ R, L, C, frequency })
    });
}

/**
 * Calculate Power via API
 */
async function calculatePower(apparentPower, powerFactor) {
    return await callAPI('/calculate/power', {
        method: 'POST',
        body: JSON.stringify({ apparentPower, powerFactor })
    });
}

/**
 * Send KIMI Chat Message via Backend Proxy
 */
async function sendKimiMessage(message, context = '') {
    const messages = [
        {
            role: 'system',
            content: context || 'Anda adalah asisten AI untuk Series Untuk Mahasiswa.'
        },
        {
            role: 'user',
            content: message
        }
    ];
    
    return await callAPI('/kimi/chat', {
        method: 'POST',
        body: JSON.stringify({ messages, temperature: 0.7 })
    });
}

// ============================================
// KIMI CHAT WIDGET - BACKEND INTEGRATION
// ============================================

/**
 * Override KIMI widget to use backend proxy
 * This ensures API key security
 */
if (typeof window.initKimiWithBackend === 'undefined') {
    window.initKimiWithBackend = function() {
        // Store original callKimiAPI if exists
        const originalWidget = window.KIMI_CHAT_CONFIG;
        
        // Add backend proxy flag
        if (originalWidget) {
            originalWidget.useBackendProxy = true;
            originalWidget.backendURL = window.API_BASE_URL + '/kimi/chat';
        }
    };
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.initKimiWithBackend);
    } else {
        window.initKimiWithBackend();
    }
}

// Console greeting
console.log('%c Series Untuk Mahasiswa ', 'background: linear-gradient(135deg, #1e40af, #3b82f6); color: white; font-size: 24px; font-weight: bold; padding: 10px 20px; border-radius: 10px;');
console.log('%c Paham Sistem, Bukan Hafal Rumus ', 'color: #3b82f6; font-size: 14px;');
console.log('%c API Base URL: ' + window.API_BASE_URL, 'color: #22c55e; font-size: 12px;');
