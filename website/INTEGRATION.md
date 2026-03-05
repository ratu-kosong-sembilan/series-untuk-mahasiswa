# Panduan Integrasi Lengkap

Dokumen ini menjelaskan cara mengintegrasikan semua komponen website "Series Untuk Mahasiswa".

## 📋 Daftar Isi

1. [Struktur Project](#struktur-project)
2. [KIMI Chat Widget](#kimi-chat-widget)
3. [Simulator Interaktif](#simulator-interaktif)
4. [Backend API](#backend-api)
5. [Deployment](#deployment)

---

## 📁 Struktur Project

```
website/
├── index.html                 # Landing page utama
├── simulator.html             # Halaman simulator interaktif
├── css/                       # Stylesheets
├── js/
│   ├── main.js               # JavaScript utama
│   ├── kimi-chat-widget.js   # KIMI chat widget
│   └── simulator.js          # Simulator logic
├── assets/
│   ├── images/               # Gambar
│   └── videos/               # Video
├── backend/                   # Node.js Backend
│   ├── server.js             # Main server
│   ├── package.json          # Dependencies
│   ├── .env                  # Environment variables
│   └── README.md             # Backend docs
├── README.md                  # Dokumentasi utama
├── DEPLOY.md                  # Panduan deployment
└── INTEGRATION.md            # Dokumen ini
```

---

## 🤖 KIMI Chat Widget

### Fitur
- Chat AI 24/7 untuk menjawab pertanyaan mahasiswa
- Fallback responses jika API tidak tersedia
- Suggested questions untuk memudahkan pengguna
- Mobile responsive

### Konfigurasi

Edit konfigurasi di `index.html`:

```javascript
window.KIMI_CHAT_CONFIG = {
    apiKey: 'YOUR_KIMI_API_KEY',  // Dari platform.moonshot.cn
    position: 'bottom-right',
    primaryColor: '#2563eb',
    welcomeMessage: 'Halo! Saya asisten AI...',
    placeholder: 'Tanyakan tentang...',
    suggestedQuestions: [
        'Apa itu phasor?',
        'Kenapa bilangan kompleks dipakai di AC?',
        'Bagaimana cara menghitung impedansi?'
    ]
};
```

### Mode Operasi

#### Mode 1: Direct API (Development)
- API key langsung di frontend
- ⚠️ **Tidak aman untuk production!**
- Cocok untuk testing lokal

#### Mode 2: Backend Proxy (Production) ✅ **Recommended**
- API key disimpan di backend
- Frontend hanya komunikasi ke backend
- Aman untuk production

Untuk mengaktifkan mode proxy, pastikan:
1. Backend sudah running
2. `API_BASE_URL` di `main.js` sudah benar
3. Konfigurasi CORS di backend sudah sesuai

---

## 🎮 Simulator Interaktif

### Fitur

#### 1. Phasor Simulator
- Visualisasi vektor berputar real-time
- Gelombang sinus dengan parameter adjustable
- Equation display (time domain & phasor domain)
- Play/Pause dan speed control

#### 2. Impedance Calculator
- Input: R, L, C, Frequency
- Output: XL, XC, Z (rectangular & polar)
- Visual diagram impedansi
- Real-time calculation

#### 3. Power Triangle
- Input: Daya Semu (S), Faktor Daya
- Output: Daya Aktif (P), Daya Reaktif (Q)
- Visualisasi segitiga daya
- Interpretasi faktor daya

### Cara Menggunakan

1. Buka `simulator.html`
2. Pilih tab simulator yang diinginkan
3. Geser slider untuk mengubah parameter
4. Lihat hasil secara real-time

### Integrasi dengan Backend

Simulator juga bisa menggunakan API backend untuk kalkulasi:

```javascript
// Contoh penggunaan API
const result = await calculateImpedance(10, 100, 100, 50);
console.log(result.data.Z);  // Impedansi total
```

---

## 🔌 Backend API

### Fitur

| Endpoint | Method | Deskripsi |
|----------|--------|-----------|
| `/api/health` | GET | Health check |
| `/api/newsletter/subscribe` | POST | Subscribe newsletter |
| `/api/newsletter/unsubscribe` | POST | Unsubscribe newsletter |
| `/api/kimi/chat` | POST | KIMI AI chat proxy |
| `/api/calculate/phasor` | POST | Kalkulasi phasor |
| `/api/calculate/impedance` | POST | Kalkulasi impedansi |
| `/api/calculate/power` | POST | Kalkulasi daya |
| `/api/contact` | POST | Contact form |

### Setup Backend

```bash
cd website/backend

# 1. Install dependencies
npm install

# 2. Setup environment
cp .env.example .env
# Edit .env dan isi KIMI_API_KEY

# 3. Run development
npm run dev

# 4. Run production
npm start
```

### Environment Variables

| Variable | Deskripsi | Default |
|----------|-----------|---------|
| `PORT` | Port server | 3000 |
| `NODE_ENV` | Environment | development |
| `FRONTEND_URL` | URL frontend | http://localhost:5500 |
| `KIMI_API_KEY` | API key KIMI | - |

### Rate Limiting

| Endpoint | Limit |
|----------|-------|
| General API | 100 requests / 15 min |
| KIMI Chat | 10 requests / 1 min |
| Newsletter | 5 requests / 1 hour |

---

## 🚀 Deployment

### Deploy Frontend (Vercel)

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Deploy
vercel

# 3. Set environment variables di Vercel dashboard
```

### Deploy Backend (Heroku)

```bash
# 1. Login Heroku
heroku login

# 2. Create app
heroku create series-mahasiswa-api

# 3. Set config
heroku config:set KIMI_API_KEY=your_key
heroku config:set NODE_ENV=production
heroku config:set FRONTEND_URL=https://your-frontend.vercel.app

# 4. Deploy
git subtree push --prefix website/backend heroku main
```

### Deploy Full Stack (Vercel + Serverless Functions)

Vercel juga support serverless functions:

```bash
# 1. Pindah backend ke api/ folder
mkdir -p api
mv website/backend/server.js api/index.js

# 2. Update package.json
{
  "scripts": {
    "dev": "vercel dev"
  }
}

# 3. Deploy
vercel
```

---

## 🔗 Integrasi Frontend-Backend

### Alur Data

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Browser   │────▶│   Backend   │────▶│  KIMI API   │
│  (Website)  │◀────│   (Proxy)   │◀────│             │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Konfigurasi API URL

Edit di `js/main.js`:

```javascript
window.API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api' 
    : 'https://your-production-api.com/api';
```

### Testing Integrasi

1. **Test Backend:**
   ```bash
   curl http://localhost:3000/api/health
   ```

2. **Test Newsletter:**
   ```bash
   curl -X POST http://localhost:3000/api/newsletter/subscribe \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com"}'
   ```

3. **Test KIMI Chat:**
   ```bash
   curl -X POST http://localhost:3000/api/kimi/chat \
     -H "Content-Type: application/json" \
     -d '{"messages":[{"role":"user","content":"Apa itu phasor?"}]}'
   ```

---

## 📝 Checklist Pre-Launch

### Frontend
- [ ] Ganti video YouTube placeholder
- [ ] Update email & sosial media
- [ ] Cek semua links
- [ ] Test responsive di mobile
- [ ] Optimasi gambar

### Backend
- [ ] Setup production database
- [ ] Konfigurasi email service
- [ ] Setup monitoring/logging
- [ ] Configure CORS untuk production
- [ ] Setup SSL/HTTPS

### KIMI Integration
- [ ] Dapatkan API key dari Moonshot
- [ ] Test chat widget
- [ ] Konfigurasi rate limiting
- [ ] Setup fallback responses

### Deployment
- [ ] Deploy frontend
- [ ] Deploy backend
- [ ] Configure custom domain
- [ ] Setup SSL certificate
- [ ] Test end-to-end

---

## 🆘 Troubleshooting

### Chat Widget tidak muncul
```
- Cek console browser untuk error
- Pastikan Font Awesome loaded
- Cek apakah KIMI_CHAT_CONFIG sudah di-set
```

### Simulator tidak berfungsi
```
- Cek apakah Chart.js loaded
- Cek console untuk JavaScript error
- Refresh halaman
```

### Backend tidak terhubung
```
- Cek apakah backend running
- Cek CORS configuration
- Cek API_BASE_URL di frontend
- Cek network tab di DevTools
```

### KIMI API error
```
- Cek API key valid
- Cek rate limit
- Cek KIMI API status
- Gunakan mock response untuk testing
```

---

## 📚 Resources

- [KIMI API Docs](https://platform.moonshot.cn/docs)
- [Express.js Docs](https://expressjs.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/)
- [Chart.js Docs](https://www.chartjs.org/)

---

**Butuh bantuan?** Silakan buat issue di repository atau hubungi tim developer.
