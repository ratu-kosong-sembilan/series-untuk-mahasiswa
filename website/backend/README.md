# Series Untuk Mahasiswa - Backend API

Backend Node.js/Express untuk website Series Untuk Mahasiswa dengan fitur newsletter dan KIMI AI integration.

## 🚀 Fitur

- **Newsletter API** - Subscribe/unsubscribe dengan rate limiting
- **KIMI AI Proxy** - Secure API proxy untuk chat AI
- **Calculation API** - Endpoint untuk perhitungan phasor, impedansi, daya
- **Contact Form** - Handler untuk form kontak
- **Security** - Helmet, CORS, Rate Limiting

## 📋 Prerequisites

- Node.js >= 14.0.0
- npm atau yarn

## 🛠️ Setup

### 1. Install Dependencies

```bash
cd website/backend
npm install
```

### 2. Environment Variables

```bash
cp .env.example .env
```

Edit `.env` dan isi konfigurasi:

```env
PORT=3000
KIMI_API_KEY=your_actual_kimi_api_key
FRONTEND_URL=http://localhost:5500
```

### 3. Run Server

**Development mode (with auto-reload):**
```bash
npm run dev
```

**Production mode:**
```bash
npm start
```

Server akan berjalan di `http://localhost:3000`

## 📡 API Endpoints

### Health Check
```http
GET /api/health
```

Response:
```json
{
    "success": true,
    "message": "Server is running",
    "timestamp": "2026-03-05T10:00:00.000Z",
    "version": "1.0.0"
}
```

### Newsletter

#### Subscribe
```http
POST /api/newsletter/subscribe
Content-Type: application/json

{
    "email": "user@example.com",
    "name": "Nama User"
}
```

#### Unsubscribe
```http
POST /api/newsletter/unsubscribe
Content-Type: application/json

{
    "email": "user@example.com"
}
```

### KIMI AI Chat

```http
POST /api/kimi/chat
Content-Type: application/json

{
    "messages": [
        {
            "role": "system",
            "content": "Anda adalah tutor Teknik Elektro."
        },
        {
            "role": "user",
            "content": "Apa itu phasor?"
        }
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}
```

Response:
```json
{
    "success": true,
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Phasor adalah representasi vektor..."
            }
        }
    ]
}
```

### Calculation APIs

#### Phasor Calculation
```http
POST /api/calculate/phasor
Content-Type: application/json

{
    "amplitude": 100,
    "frequency": 50,
    "phase": 30
}
```

#### Impedance Calculation
```http
POST /api/calculate/impedance
Content-Type: application/json

{
    "R": 10,
    "L": 100,
    "C": 100,
    "frequency": 50
}
```

#### Power Calculation
```http
POST /api/calculate/power
Content-Type: application/json

{
    "apparentPower": 1000,
    "powerFactor": 0.8
}
```

### Contact Form

```http
POST /api/contact
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Pertanyaan",
    "message": "Isi pesan..."
}
```

## 🔒 Security

- **Helmet** - Security headers
- **CORS** - Cross-origin request protection
- **Rate Limiting** - Prevent abuse:
  - General API: 100 requests per 15 minutes
  - KIMI Chat: 10 requests per minute
  - Newsletter: 5 subscriptions per hour
- **Input Validation** - Using validator.js

## 📁 Project Structure

```
backend/
├── server.js           # Main server file
├── package.json        # Dependencies
├── .env.example        # Environment template
├── .env               # Environment variables (not in git)
└── README.md          # This file
```

## 🚢 Deployment

### Deploy ke Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

### Deploy ke Heroku

1. Create Heroku app:
```bash
heroku create series-mahasiswa-api
```

2. Set environment variables:
```bash
heroku config:set KIMI_API_KEY=your_key
heroku config:set NODE_ENV=production
```

3. Deploy:
```bash
git push heroku main
```

### Deploy ke VPS (Ubuntu)

1. Clone repository
2. Install dependencies: `npm install --production`
3. Setup PM2: `pm2 start server.js`
4. Setup Nginx reverse proxy

## 🔧 Development

### Run Tests
```bash
npm test
```

### Code Style
- ESLint untuk linting
- Prettier untuk formatting

## 📊 Monitoring

Server logs menggunakan Morgan. Untuk production, pertimbangkan:
- Winston untuk logging advanced
- Sentry untuk error tracking
- New Relic untuk performance monitoring

## 🤝 Contributing

1. Fork repository
2. Buat branch fitur
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## 📝 License

MIT License

---

**Series Untuk Mahasiswa** - Paham Sistem, Bukan Hafal Rumus
