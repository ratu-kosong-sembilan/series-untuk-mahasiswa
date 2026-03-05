# 🚀 Panduan Deploy ke Production

Panduan lengkap untuk deploy "Series Untuk Mahasiswa" ke production.

## 📋 Overview Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│     Vercel      │────▶│    Railway      │────▶│   KIMI API      │
│   (Frontend)    │◀────│   (Backend)     │◀────│   (AI Chat)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

- **Frontend:** Vercel (Gratis, CDN global)
- **Backend:** Railway (Gratis $5/bulan credit)
- **AI:** KIMI API (Pay-as-you-go)

---

## Step 1: Deploy Frontend ke Vercel

### 1.1 Install Vercel CLI

```bash
npm install -g vercel
```

### 1.2 Login ke Vercel

```bash
vercel login
```

Ikuti instruksi untuk login dengan email/GitHub.

### 1.3 Deploy

```bash
cd website
vercel --prod
```

**Atau gunakan script:**
```bash
chmod +x deploy-frontend.sh
./deploy-frontend.sh
```

### 1.4 Simpan URL Frontend

Setelah deploy, Anda akan mendapatkan URL seperti:
```
https://series-untuk-mahasiswa.vercel.app
```

**Catat URL ini!** Diperlukan untuk konfigurasi backend.

---

## Step 2: Deploy Backend ke Railway

### 2.1 Install Railway CLI

```bash
npm install -g @railway/cli
```

### 2.2 Login ke Railway

```bash
railway login
```

### 2.3 Buat Project Baru

```bash
cd website/backend
railway init
```

Pilih:
- ✅ Create New Project
- Nama: `series-mahasiswa-api`

### 2.4 Setup Environment Variables

```bash
railway variables
```

Tambahkan variables:
```
NODE_ENV=production
KIMI_API_KEY=your_kimi_api_key_here
FRONTEND_URL=https://series-untuk-mahasiswa.vercel.app
PORT=3000
```

### 2.5 Deploy Backend

```bash
railway up
```

### 2.6 Generate Domain

```bash
railway domain
```

**Simpan URL backend!** Contoh:
```
https://series-mahasiswa-api.up.railway.app
```

---

## Step 3: Konfigurasi Frontend

### 3.1 Update API Base URL

Edit `website/js/main.js`:

```javascript
window.API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api' 
    : 'https://series-mahasiswa-api.up.railway.app/api';  // Ganti dengan URL Railway Anda
```

### 3.2 Redeploy Frontend

```bash
cd website
vercel --prod
```

---

## Step 4: Dapatkan KIMI API Key

### 4.1 Daftar di Moonshot Platform

1. Buka https://platform.moonshot.cn/
2. Buat akun
3. Verifikasi email
4. Login ke dashboard

### 4.2 Buat API Key

1. Go to **API Keys** section
2. Click **Create New Key**
3. Copy API Key

### 4.3 Update Backend

```bash
cd website/backend
railway variables set KIMI_API_KEY=your_actual_api_key
```

---

## Step 5: Testing

### 5.1 Test Website

Buka URL frontend Anda:
```
https://series-untuk-mahasiswa.vercel.app
```

### 5.2 Test API

```bash
curl https://series-mahasiswa-api.up.railway.app/api/health
```

Expected response:
```json
{
    "success": true,
    "message": "Server is running"
}
```

### 5.3 Test Newsletter

Isi form newsletter di website dan cek apakah berhasil.

### 5.4 Test KIMI Chat

Buka chat widget dan kirim pesan:
```
Apa itu phasor?
```

---

## 🔧 Troubleshooting

### Frontend tidak terhubung ke Backend

1. Cek CORS configuration di backend:
   ```bash
   railway variables get FRONTEND_URL
   ```
   Pastikan sama dengan URL Vercel Anda.

2. Cek API_BASE_URL di frontend:
   ```javascript
   // Buka DevTools > Console
   console.log(window.API_BASE_URL);
   ```

### KIMI Chat tidak berfungsi

1. Cek API key:
   ```bash
   railway variables get KIMI_API_KEY
   ```

2. Cek logs:
   ```bash
   railway logs
   ```

### Deploy gagal

**Vercel:**
```bash
vercel --debug
```

**Railway:**
```bash
railway logs
```

---

## 📊 Monitoring

### Vercel Analytics

1. Buka dashboard Vercel
2. Pilih project Anda
3. Tab **Analytics**

### Railway Metrics

1. Buka dashboard Railway
2. Pilih project
3. Tab **Metrics**

---

## 💰 Estimasi Biaya

| Service | Tier | Biaya |
|---------|------|-------|
| Vercel | Pro (100GB bandwidth) | Gratis |
| Railway | Starter ($5 credit/bulan) | Gratis |
| KIMI API | Pay-as-you-go | ~$0.001/request |

**Total untuk start:** **GRATIS** (dengan tier gratis)

---

## 🔄 Update Deployment

### Update Frontend

```bash
cd website
vercel --prod
```

### Update Backend

```bash
cd website/backend
railway up
```

---

## 🌐 Custom Domain (Opsional)

### Vercel Custom Domain

1. Buka dashboard Vercel
2. Project Settings > Domains
3. Add your domain
4. Update DNS records

### Railway Custom Domain

1. Buka dashboard Railway
2. Project Settings > Domains
3. Generate certificate
4. Update DNS records

---

## 📞 Support

**Vercel:** https://vercel.com/support
**Railway:** https://railway.app/help
**KIMI:** https://platform.moonshot.cn/docs

---

## ✅ Post-Deploy Checklist

- [ ] Website bisa diakses
- [ ] Simulator berfungsi
- [ ] Chat widget muncul
- [ ] Newsletter form works
- [ ] API health check passes
- [ ] KIMI chat responds
- [ ] Mobile responsive OK
- [ ] SSL certificate active

---

**Selamat! Website Anda sekarang LIVE! 🎉**
