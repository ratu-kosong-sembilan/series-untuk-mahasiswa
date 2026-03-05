# Series Untuk Mahasiswa - Website

Landing page modern + Simulator Interaktif + KIMI AI Chat untuk project edukasi Teknik Elektro.

## 🚀 Fitur

### Frontend
- **Landing Page** - 10 section lengkap dengan animasi smooth
- **Interactive Simulator** - Phasor, Impedance, Power Triangle
- **KIMI AI Chat Widget** - Asisten AI 24/7 untuk mahasiswa
- **Responsive Design** - Optimal di desktop, tablet, dan mobile
- **SEO Ready** - Meta tags, Open Graph, semantic HTML

### Backend
- **Newsletter API** - Subscribe/unsubscribe dengan rate limiting
- **KIMI AI Proxy** - Secure API proxy untuk chat AI
- **Calculation API** - Endpoint untuk perhitungan Teknik Elektro
- **Security** - Helmet, CORS, Rate Limiting

## 📁 Struktur Folder

```
website/
├── index.html                 # Landing page utama
├── simulator.html             # Halaman simulator interaktif
├── js/
│   ├── main.js               # JavaScript utama & API integration
│   ├── kimi-chat-widget.js   # KIMI AI chat widget
│   └── simulator.js          # Simulator logic & visualization
├── assets/
│   ├── images/               # Gambar
│   └── videos/               # Video
├── backend/                   # Node.js Backend API
│   ├── server.js             # Main server
│   ├── package.json          # Dependencies
│   ├── .env                  # Environment variables
│   └── README.md             # Backend documentation
├── README.md                  # Dokumentasi utama
├── INTEGRATION.md            # Panduan integrasi lengkap
└── DEPLOY.md                 # Panduan deployment
```

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS** (CDN) - Utility-first CSS framework
- **JavaScript (Vanilla)** - Interactivity
- **Chart.js** - Grafik dan visualisasi
- **Font Awesome** - Icons
- **Google Fonts** - Inter & Sora typography

### Backend
- **Node.js** - Runtime
- **Express.js** - Web framework
- **Helmet** - Security headers
- **CORS** - Cross-origin handling
- **Rate Limit** - API protection
- **Validator** - Input validation

## 📱 Section Website

### Landing Page (index.html)
1. **Navigation** - Fixed navbar dengan smooth scroll
2. **Hero** - Value proposition dengan phasor animation
3. **Problem** - Pain points mahasiswa Teknik Elektro
4. **Solution** - Metodologi Fenomena-First Learning
5. **Trailer** - Video preview (YouTube embed)
6. **Modules** - Filterable module cards
7. **Simulator Preview** - Interactive phasor demo
8. **About** - Tentang project
9. **Newsletter** - Email subscription (connected to backend)
10. **Footer** - Links dan kontak

### Simulator Page (simulator.html)
1. **Phasor Simulator** - Real-time phasor animation
2. **Impedance Calculator** - RLC circuit calculator
3. **Power Triangle** - Power analysis visualization

### KIMI AI Chat Widget
- Available on all pages
- 24/7 AI assistant for students
- Backend proxy for security

## 🚀 Quick Start

### 1. Frontend Only (Static)

```bash
# Serve dengan Python
cd website
python -m http.server 5500

# Atau dengan Node.js
npx serve
```

Buka: `http://localhost:5500`

### 2. Full Stack (Frontend + Backend)

Terminal 1 (Backend):
```bash
cd website/backend
npm install
npm run dev
```

Terminal 2 (Frontend):
```bash
cd website
python -m http.server 5500
```

Buka: `http://localhost:5500`
Backend: `http://localhost:3000`

## 🚢 Deployment

### Option 1: Vercel (Frontend) + Heroku (Backend)

**Frontend:**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
cd website
vercel
```

**Backend:**
```bash
# Setup Heroku
cd website/backend
heroku create series-mahasiswa-api
heroku config:set KIMI_API_KEY=your_key

# Deploy
git subtree push --prefix website/backend heroku main
```

### Option 2: Vercel Full Stack (Serverless)

```bash
cd website
vercel
# Backend functions otomatis terdeploy dari api/ folder
```

### Option 2: Netlify

1. Drag & drop folder `website` ke Netlify
2. Atau connect ke GitHub

### Option 3: GitHub Pages

1. Push folder `website` ke branch `gh-pages`
2. Atau gunakan GitHub Actions

### Option 4: Static Hosting (cPanel, dll)

1. Upload semua file via FTP
2. Akses melalui domain Anda

## ⚙️ Konfigurasi

### Ganti Video Trailer

Edit bagian ini di `index.html`:

```html
<iframe 
    src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
    title="Series Untuk Mahasiswa - Trailer"
    ...
></iframe>
```

### Update Informasi Kontak

Edit section **Footer** di `index.html`:

```html
<li><i class="far fa-envelope mr-2"></i>email@anda.com</li>
```

### Tambah Modul Baru

Tambahkan card baru di section **Modules**:

```html
<div class="module-card ..." data-category="kategori">
    ...
</div>
```

## 🎨 Customization

### Warna

Edit di `tailwind.config` dalam `index.html`:

```javascript
colors: {
    primary: {
        600: '#2563eb',  // Ganti dengan warna Anda
    }
}
```

### Font

Ganti di Google Fonts link dan Tailwind config:

```javascript
fontFamily: {
    sans: ['NamaFont', 'sans-serif'],
}
```

## 📊 Analytics

Tambahkan Google Analytics atau lainnya sebelum closing `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_ID');
</script>
```

## 🔧 Development

Untuk development lokal:

```bash
# Serve dengan Python 3
cd website
python -m http.server 8000

# Atau dengan Node.js npx
cd website
npx serve

# Atau dengan PHP
cd website
php -S localhost:8000
```

Akses di browser: `http://localhost:8000`

## 📝 Changelog

### v1.0.0 (2026-03-05)
- Initial release
- Landing page lengkap dengan 10 section
- Responsive design
- Module filtering
- Newsletter form

## 🤝 Kontribusi

1. Fork repository
2. Buat branch feature (`git checkout -b feature/nama-fitur`)
3. Commit changes (`git commit -am 'Add fitur'`)
4. Push ke branch (`git push origin feature/nama-fitur`)
5. Buat Pull Request

## 📄 License

MIT License - feel free to use and modify!

---

**Series Untuk Mahasiswa** - Paham Sistem, Bukan Hafal Rumus
