# ⚡ Quick Deploy (5 Menit)

Deploy cepat "Series Untuk Mahasiswa" ke production.

## 🎯 Overview

**Stack:**
- Frontend: **Vercel** (Gratis)
- Backend: **Railway** (Gratis $5/bulan)
- AI: **KIMI** (Pay-as-you-go)

**Time:** ~5 menit
**Cost:** GRATIS untuk start

---

## Step 1: Deploy Frontend (2 menit)

```bash
# Install Vercel CLI (kalau belum)
npm install -g vercel

# Login
vercel login

# Deploy
cd website
vercel --prod
```

**✅ Simpan URL yang muncul!** (contoh: `https://series-untuk-mahasiswa.vercel.app`)

---

## Step 2: Deploy Backend (2 menit)

```bash
# Install Railway CLI (kalau belum)
npm install -g @railway/cli

# Login
railway login

# Init project
cd website/backend
railway init
# Pilih: Create New Project

# Deploy
railway up

# Generate domain
railway domain
```

**✅ Simpan URL backend!** (contoh: `https://series-mahasiswa-api.up.railway.app`)

---

## Step 3: Konfigurasi (1 menit)

### 3.1 Update Frontend URL di Backend

```bash
cd website/backend
railway variables set FRONTEND_URL=https://series-untuk-mahasiswa.vercel.app
```

### 3.2 Update API URL di Frontend

Edit `website/js/main.js`:

```javascript
// Ganti baris ini:
window.API_BASE_URL = window.location.hostname === 'localhost' 
    ? 'http://localhost:3000/api' 
    : 'https://series-mahasiswa-api.up.railway.app/api';  // <-- Ganti ini
```

### 3.3 Redeploy Frontend

```bash
cd website
vercel --prod
```

---

## Step 4: Dapatkan KIMI API Key (Opsional)

Kalau mau chat AI berfungsi:

1. Buka https://platform.moonshot.cn/
2. Buat akun & login
3. Create API Key
4. Copy key
5. Set ke backend:

```bash
cd website/backend
railway variables set KIMI_API_KEY=your_actual_api_key_here
```

---

## ✅ Done!

Website Anda sekarang LIVE di:
- 🌐 **Frontend:** https://series-untuk-mahasiswa.vercel.app
- 🔌 **Backend:** https://series-mahasiswa-api.up.railway.app

---

## 🧪 Test

1. Buka website
2. Cek simulator berfungsi
3. Coba chat widget (kalau sudah set KIMI_API_KEY)
4. Isi newsletter form

---

## 🔄 Update

**Update Frontend:**
```bash
cd website
vercel --prod
```

**Update Backend:**
```bash
cd website/backend
railway up
```

---

**Butuh bantuan?** Lihat `DEPLOY-GUIDE.md` untuk panduan lengkap.
