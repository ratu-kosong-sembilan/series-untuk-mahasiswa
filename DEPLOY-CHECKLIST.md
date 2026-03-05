# ✅ Deployment Checklist

Gunakan checklist ini untuk memastikan deployment berhasil.

---

## Pre-Deployment

### ☑️ Akun & Tools
- [ ] Install Node.js (https://nodejs.org/)
- [ ] Install Vercel CLI: `npm install -g vercel`
- [ ] Install Railway CLI: `npm install -g @railway/cli`
- [ ] Buat akun Vercel (https://vercel.com/signup)
- [ ] Buat akun Railway (https://railway.app/)
- [ ] Buat akun KIMI (opsional, https://platform.moonshot.cn/)

### ☑️ Login
- [ ] Login Vercel: `vercel login`
- [ ] Login Railway: `railway login`

---

## Deployment Steps

### Step 1: Deploy Frontend
```bash
cd website
vercel --prod
```
- [ ] Deploy berhasil
- [ ] Catat URL: `___________________________`

### Step 2: Deploy Backend
```bash
cd website/backend
railway init  # Create New Project
railway up
railway domain
```
- [ ] Deploy berhasil
- [ ] Catat URL: `___________________________`

### Step 3: Set Environment Variables
```bash
cd website/backend
railway variables set FRONTEND_URL="[URL_Vercel_Anda]"
railway variables set NODE_ENV="production"
```
- [ ] FRONTEND_URL di-set
- [ ] NODE_ENV di-set

### Step 4: KIMI API (Opsional)
```bash
railway variables set KIMI_API_KEY="[API_Key_Anda]"
```
- [ ] KIMI_API_KEY di-set (opsional)

### Step 5: Update Frontend Config
Edit `website/js/main.js`:
```javascript
const PRODUCTION_API_URL = '[URL_Railway_Anda]/api';
```
- [ ] File diupdate
- [ ] URL sudah benar

### Step 6: Redeploy Frontend
```bash
cd website
vercel --prod
```
- [ ] Redeploy berhasil

---

## Post-Deployment Testing

### ☑️ Website Accessible
- [ ] Buka URL Vercel di browser
- [ ] Halaman muncul tanpa error
- [ ] Navigasi berfungsi
- [ ] Mobile responsive OK

### ☑️ API Health Check
Buka: `[URL_Railway]/api/health`
- [ ] Response: `{"success": true}`

### ☑️ Simulator Page
- [ ] Buka `/simulator.html`
- [ ] Phasor Simulator berfungsi
- [ ] Impedance Calculator berfungsi
- [ ] Power Triangle berfungsi

### ☑️ KIMI Chat Widget
- [ ] Chat button muncul di pojok kanan bawah
- [ ] Bisa membuka chat window
- [ ] Kirim pesan: "Apa itu phasor?"
- [ ] Mendapat response (fallback atau AI)

### ☑️ Newsletter Form
- [ ] Isi form dengan email test
- [ ] Submit form
- [ ] Muncul notifikasi sukses

### ☑️ SSL/HTTPS
- [ ] URL menggunakan `https://`
- [ ] Tidak ada warning security

---

## URLs Penting

| Komponen | URL |
|----------|-----|
| **Website** | `________________________________` |
| **Backend** | `________________________________` |
| **API** | `________________________________/api` |
| **Health** | `________________________________/api/health` |

---

## Dashboard Links

- [ ] Vercel Dashboard: https://vercel.com/dashboard
- [ ] Railway Dashboard: https://railway.app/dashboard

---

## Troubleshooting Notes

Jika ada error, catat di sini:

```
Error: ________________________________________________
Solusi: ________________________________________________

Error: ________________________________________________
Solusi: ________________________________________________
```

---

## 🎉 Deployment Status

- [ ] Semua steps selesai
- [ ] Semua testing passed
- [ ] Website LIVE dan berfungsi

**Status: _________________**

**Tanggal Deploy: _________________**

**Deployed by: _________________**

---

## 📝 Catatan Tambahan

```
_________________________________________________
_________________________________________________
_________________________________________________
```

---

**Selamat! Website Anda sudah ONLINE! 🚀**
