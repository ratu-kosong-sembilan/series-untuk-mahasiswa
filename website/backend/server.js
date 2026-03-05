/**
 * Series Untuk Mahasiswa - Backend API
 * Express.js server with endpoints for newsletter and KIMI AI integration
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');
const fetch = require('node-fetch');
const validator = require('validator');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// ============================================
// MIDDLEWARE
// ============================================

// Security headers
app.use(helmet({
    contentSecurityPolicy: false,
    crossOriginEmbedderPolicy: false
}));

// CORS - Allow requests from your frontend
app.use(cors({
    origin: process.env.FRONTEND_URL || ['http://localhost:5500', 'http://localhost:3000'],
    methods: ['GET', 'POST'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));

// Body parsing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Logging
app.use(morgan('combined'));

// Rate limiting
const apiLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // limit each IP to 100 requests per windowMs
    message: {
        success: false,
        message: 'Terlalu banyak permintaan. Silakan coba lagi nanti.'
    }
});

const kimiLimiter = rateLimit({
    windowMs: 60 * 1000, // 1 minute
    max: 10, // 10 requests per minute for KIMI API
    message: {
        success: false,
        message: 'Rate limit exceeded. Please slow down.'
    }
});

const newsletterLimiter = rateLimit({
    windowMs: 60 * 60 * 1000, // 1 hour
    max: 5, // 5 subscriptions per hour per IP
    message: {
        success: false,
        message: 'Terlalu banyak percobaan. Silakan coba lagi dalam 1 jam.'
    }
});

app.use('/api/', apiLimiter);

// ============================================
// IN-MEMORY STORAGE (Replace with database in production)
// ============================================

const subscribers = [];
const chatHistory = [];

// ============================================
// ROUTES
// ============================================

// Health check
app.get('/api/health', (req, res) => {
    res.json({
        success: true,
        message: 'Server is running',
        timestamp: new Date().toISOString(),
        version: '1.0.0'
    });
});

// ============================================
// NEWSLETTER API
// ============================================

// Subscribe to newsletter
app.post('/api/newsletter/subscribe', newsletterLimiter, async (req, res) => {
    try {
        const { email, name = '' } = req.body;
        
        // Validate email
        if (!email || !validator.isEmail(email)) {
            return res.status(400).json({
                success: false,
                message: 'Email tidak valid'
            });
        }
        
        // Normalize email
        const normalizedEmail = validator.normalizeEmail(email);
        
        // Check if already subscribed
        if (subscribers.find(s => s.email === normalizedEmail)) {
            return res.status(409).json({
                success: false,
                message: 'Email sudah terdaftar'
            });
        }
        
        // Add subscriber
        const subscriber = {
            id: Date.now().toString(),
            email: normalizedEmail,
            name: name.trim(),
            subscribedAt: new Date().toISOString(),
            active: true
        };
        
        subscribers.push(subscriber);
        
        // TODO: Send welcome email
        // TODO: Add to external email service (Mailchimp, SendGrid, etc.)
        
        console.log(`New subscriber: ${normalizedEmail}`);
        
        res.json({
            success: true,
            message: 'Berhasil berlangganan! Terima kasih.',
            data: {
                id: subscriber.id,
                email: subscriber.email
            }
        });
        
    } catch (error) {
        console.error('Newsletter subscription error:', error);
        res.status(500).json({
            success: false,
            message: 'Terjadi kesalahan server'
        });
    }
});

// Unsubscribe
app.post('/api/newsletter/unsubscribe', async (req, res) => {
    try {
        const { email } = req.body;
        
        if (!email || !validator.isEmail(email)) {
            return res.status(400).json({
                success: false,
                message: 'Email tidak valid'
            });
        }
        
        const normalizedEmail = validator.normalizeEmail(email);
        const subscriberIndex = subscribers.findIndex(s => s.email === normalizedEmail);
        
        if (subscriberIndex === -1) {
            return res.status(404).json({
                success: false,
                message: 'Email tidak ditemukan'
            });
        }
        
        subscribers[subscriberIndex].active = false;
        subscribers[subscriberIndex].unsubscribedAt = new Date().toISOString();
        
        res.json({
            success: true,
            message: 'Berhasil berhenti berlangganan'
        });
        
    } catch (error) {
        console.error('Unsubscribe error:', error);
        res.status(500).json({
            success: false,
            message: 'Terjadi kesalahan server'
        });
    }
});

// Get subscriber count (admin only - should add auth)
app.get('/api/newsletter/stats', (req, res) => {
    const activeSubscribers = subscribers.filter(s => s.active).length;
    
    res.json({
        success: true,
        data: {
            total: subscribers.length,
            active: activeSubscribers,
            unsubscribed: subscribers.length - activeSubscribers
        }
    });
});

// ============================================
// KIMI AI PROXY API
// ============================================

// KIMI Chat Completion Proxy
app.post('/api/kimi/chat', kimiLimiter, async (req, res) => {
    try {
        const { messages, temperature = 0.7, max_tokens = 1000 } = req.body;
        
        // Validate request
        if (!messages || !Array.isArray(messages) || messages.length === 0) {
            return res.status(400).json({
                success: false,
                message: 'Invalid messages format'
            });
        }
        
        // Check if KIMI API key is configured
        const KIMI_API_KEY = process.env.KIMI_API_KEY;
        if (!KIMI_API_KEY || KIMI_API_KEY === 'YOUR_KIMI_API_KEY') {
            // Return mock response for development
            return res.json({
                success: true,
                mock: true,
                message: 'This is a mock response. Configure KIMI_API_KEY for real AI responses.',
                choices: [{
                    message: {
                        role: 'assistant',
                        content: getMockResponse(messages[messages.length - 1].content)
                    }
                }]
            });
        }
        
        // Call KIMI API
        const response = await fetch('https://api.moonshot.cn/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${KIMI_API_KEY}`
            },
            body: JSON.stringify({
                model: 'moonshot-v1-8k',
                messages: messages,
                temperature: temperature,
                max_tokens: max_tokens
            })
        });
        
        if (!response.ok) {
            const error = await response.text();
            throw new Error(`KIMI API error: ${error}`);
        }
        
        const data = await response.json();
        
        // Log chat for analytics (don't store full content for privacy)
        chatHistory.push({
            timestamp: new Date().toISOString(),
            ip: req.ip,
            messageCount: messages.length
        });
        
        res.json({
            success: true,
            choices: data.choices
        });
        
    } catch (error) {
        console.error('KIMI API error:', error);
        res.status(500).json({
            success: false,
            message: 'AI service temporarily unavailable',
            error: process.env.NODE_ENV === 'development' ? error.message : undefined
        });
    }
});

// Mock response for development
function getMockResponse(message) {
    const lowerMsg = message.toLowerCase();
    
    if (lowerMsg.includes('phasor')) {
        return '**Phasor** adalah representasi vektor dari besaran sinusoidal. Bayangkan vektor yang berputar dengan kecepatan sudut ω. Proyeksi vektor ini pada sumbu horizontal membentuk gelombang sinus!';
    }
    if (lowerMsg.includes('kompleks') || lowerMsg.includes('imaginer')) {
        return '**Bilangan kompleks** dengan simbol **j** digunakan di AC karena bisa merepresentasikan **magnitudo** dan **fase** sekaligus! Contoh: V = 100∠30° artinya tegangan 100V dengan fase 30 derajat.';
    }
    if (lowerMsg.includes('impedansi')) {
        return '**Impedansi (Z)** adalah hambatan total dalam rangkaian AC.\n\n• **Resistor**: Z = R\n• **Induktor**: Z = jωL\n• **Kapasitor**: Z = 1/(jωC)\n\nImpedansi total: Z_total = R + j(XL - XC)';
    }
    if (lowerMsg.includes('daya')) {
        return 'Dalam sistem AC ada **3 jenis daya**:\n\n1. **Daya Aktif (P)** - dalam Watt\n2. **Daya Reaktif (Q)** - dalam VAR\n3. **Daya Semu (S)** - dalam VA\n\n**Faktor Daya** = cos(θ) = P/S';
    }
    
    return 'Terima kasih atas pertanyaannya! Saya bisa membantu memahami konsep bilangan kompleks, phasor, impedansi RLC, dan analisis daya dalam sistem AC. Silakan ajukan pertanyaan spesifik!';
}

// ============================================
// CALCULATION API
// ============================================

// Phasor calculation
app.post('/api/calculate/phasor', (req, res) => {
    try {
        const { amplitude, frequency, phase } = req.body;
        
        const omega = 2 * Math.PI * frequency;
        const rms = amplitude / Math.sqrt(2);
        const period = 1 / frequency;
        
        res.json({
            success: true,
            data: {
                timeDomain: `v(t) = ${amplitude} sin(${omega.toFixed(2)}t + ${phase}°)`,
                phasorDomain: `${amplitude}∠${phase}°`,
                rms: rms.toFixed(2),
                omega: omega.toFixed(2),
                period: period.toFixed(4)
            }
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: 'Calculation error'
        });
    }
});

// Impedance calculation
app.post('/api/calculate/impedance', (req, res) => {
    try {
        const { R, L, C, frequency } = req.body;
        
        const omega = 2 * Math.PI * frequency;
        const XL = omega * (L / 1000); // mH to H
        const XC = 1 / (omega * (C / 1000000)); // µF to F
        const X = XL - XC;
        
        const Z = Math.sqrt(R * R + X * X);
        const theta = Math.atan2(X, R) * 180 / Math.PI;
        
        res.json({
            success: true,
            data: {
                XL: XL.toFixed(2),
                XC: XC.toFixed(2),
                X: X.toFixed(2),
                Z: Z.toFixed(2),
                theta: theta.toFixed(2),
                rectangular: `${R} + j${X.toFixed(2)}`,
                polar: `${Z.toFixed(2)}∠${theta.toFixed(2)}°`
            }
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: 'Calculation error'
        });
    }
});

// Power calculation
app.post('/api/calculate/power', (req, res) => {
    try {
        const { apparentPower, powerFactor } = req.body;
        
        const P = apparentPower * powerFactor;
        const phi = Math.acos(powerFactor);
        const Q = apparentPower * Math.sin(phi);
        
        res.json({
            success: true,
            data: {
                P: P.toFixed(2),
                Q: Q.toFixed(2),
                S: apparentPower,
                powerFactor: powerFactor,
                angle: (phi * 180 / Math.PI).toFixed(2)
            }
        });
    } catch (error) {
        res.status(500).json({
            success: false,
            message: 'Calculation error'
        });
    }
});

// ============================================
// CONTACT FORM API
// ============================================

app.post('/api/contact', async (req, res) => {
    try {
        const { name, email, subject, message } = req.body;
        
        // Validation
        if (!name || !email || !subject || !message) {
            return res.status(400).json({
                success: false,
                message: 'Semua field harus diisi'
            });
        }
        
        if (!validator.isEmail(email)) {
            return res.status(400).json({
                success: false,
                message: 'Email tidak valid'
            });
        }
        
        // Sanitize inputs
        const sanitizedData = {
            name: validator.escape(name.trim()),
            email: validator.normalizeEmail(email),
            subject: validator.escape(subject.trim()),
            message: validator.escape(message.trim()),
            timestamp: new Date().toISOString()
        };
        
        // TODO: Send email notification
        // TODO: Store in database
        
        console.log('Contact form submission:', sanitizedData);
        
        res.json({
            success: true,
            message: 'Pesan berhasil dikirim. Kami akan merespons segera.'
        });
        
    } catch (error) {
        console.error('Contact form error:', error);
        res.status(500).json({
            success: false,
            message: 'Terjadi kesalahan server'
        });
    }
});

// ============================================
// ERROR HANDLING
// ============================================

// 404 handler
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: 'Endpoint tidak ditemukan'
    });
});

// Error handler
app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({
        success: false,
        message: 'Terjadi kesalahan server'
    });
});

// ============================================
// START SERVER
// ============================================

app.listen(PORT, () => {
    console.log(`
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║   Series Untuk Mahasiswa - Backend API             ║
    ║                                                    ║
    ║   Server running on http://localhost:${PORT}        ║
    ║                                                    ║
    ║   Available endpoints:                             ║
    ║   • GET  /api/health                               ║
    ║   • POST /api/newsletter/subscribe                 ║
    ║   • POST /api/newsletter/unsubscribe               ║
    ║   • POST /api/kimi/chat                            ║
    ║   • POST /api/calculate/phasor                     ║
    ║   • POST /api/calculate/impedance                  ║
    ║   • POST /api/calculate/power                      ║
    ║   • POST /api/contact                              ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    `);
});

module.exports = app;
