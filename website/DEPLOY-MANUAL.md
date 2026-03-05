# 📋 Panduan Deploy Manual (Step-by-Step)

Jika script otomatis tidak berfungsi, ikuti langkah manual ini.

---

## 🎯 Target

Setelah selesai, Anda akan punya:
- 🌐 **Frontend:** https://series-untuk-mahasiswa.vercel.app
- 🔌 **Backend:** https://series-mahasiswa-api.up.railway.app

---

## Step 1: Install Tools

### Install Node.js
1. Buka https://nodejs.org/
2. Download versi LTS (Long Term Support)
3. Install dengan default settings
4. Verifikasi:
   ```bash
   node --version
   npm --version
   ```

### Install Vercel CLI
```bash
npm install -g vercel
```

### Install Railway CLI
```bash
npm install -g @railway/cli
```

---

## Step 2: Login ke Platform

### Login Vercel
```bash
vercel login
```
- Buka URL yang muncul di browser
- Login dengan GitHub/Google/Email
- Kembali ke terminal

### Login Railway
```bash
railway login
```
- Buka URL yang muncul di browser
- Login dengan GitHub/Email
- Kembali ke terminal

---

## Step 3: Deploy Frontend (Vercel)

### 3.1 Masuk ke folder website
```bash
cd website
```

### 3.2 Deploy pertama kali
```bash
vercel
```

Pengaturan yang akan ditanya:
- **Set up "~/website"?** → `Y`
- **Which scope?** → Pilih akun Anda
- **Link to existing project?** → `N`
- **What's your project name?** → `series-untuk-mahasiswa`

Tunggu sampai selesai.

### 3.3 Simpan URL Frontend
Setelah deploy selesai, Anda akan melihat:
```
🔍  Inspect: https://vercel.com/xxx/series-untuk-mahasiswa/xxx
✅  Production: https://series-untuk-mahasiswa.vercel.app
```

**Catat URL Production ini!** (contoh: `https://series-untuk-mahasiswa.vercel.app`)

---

## Step 4: Deploy Backend (Railway)

### 4.1 Masuk ke folder backend
```bash
cd website/backend
```

### 4.2 Inisialisasi project
```bash
railway init
```

Pilih:
- **Create New Project**
- Nama: `series-mahasiswa-api`

### 4.3 Deploy
```bash
railway up
```

Tunggu sampai selesai.

### 4.4 Generate Domain
```bash
railway domain
```

### 4.5 Simpan URL Backend
Lihat URL di dashboard Railway atau output command.

Contoh: `https://series-mahasiswa-api.up.railway.app`

**Catat URL ini!**

---

## Step 5: Set Environment Variables

### 5.1 Set FRONTEND_URL
```bash
railway variables set FRONTEND_URL="https://series-untuk-mahasiswa.vercel.app"
```

**Ganti URL dengan URL Vercel Anda!**

### 5.2 Set NODE_ENV
```bash
railway variables set NODE_ENV="production"
```

### 5.3 Set KIMI_API_KEY (Opsional)
Jika sudah punya API key dari https://platform.moonshot.cn/:

```bash
railway variables set KIMI_API_KEY="your_actual_api_key_here"
```

---

## Step 6: Update Frontend Configuration

### 6.1 Buka file js/main.js
Gunakan text editor (VS Code, Notepad++, dll)

### 6.2 Cari baris ini:
```javascript
const PRODUCTION_API_URL = 'https://series-mahasiswa-api.up.railway.app/api';
```

### 6.3 Ganti dengan URL Railway Anda:
```javascript
const PRODUCTION_API_URL = 'https://your-backend-name.up.railway.app/api';
```

**Ganti `your-backend-name` dengan nama project Railway Anda!**

### 6.4 Save file

---

## Step 7: Redeploy Frontend

### 7.1 Kembali ke folder website
```bash
cd ..
```

### 7.2 Deploy ulang
```bash
vercel --prod
```

Tunggu sampai selesai.

---

## Step 8: Testing

### 8.1 Test Website
Buka browser, masukkan URL Vercel Anda:
```
https://series-untuk-mahasiswa.vercel.app
```

### 8.2 Test API Health
Buka browser/tab baru:
```
https://series-mahasiswa-api.up.railway.app/api/health
```

Harus muncul:
```json
{
    "success": true,
    "message": "Server is running"
}
```

### 8.3 Test Simulator
Di website, klik menu "Simulator" dan coba slider.

### 8.4 Test Chat Widget
Klik tombol chat di pojok kanan bawah, kirim pesan:
```
Apa itu phasor?
```

### 8.5 Test Newsletter
Isi form newsletter dengan email test.

---

## ✅ Deployment Selesai!

Website Anda sekarang LIVE di:
- 🌐 **Website:** https://series-untuk-mahasiswa.vercel.app
- 🔌 **API:** https://series-mahasiswa-api.up.railway.app

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

## 🆘 Troubleshooting

### Error: "command not found: vercel"
```bash
npm install -g vercel
```

### Error: "command not found: railway"
```bash
npm install -g @railway/cli
```

### Error: "Not logged in"
Jalankan:
```bash
vercel login
railway login
```

### Error: "CORS error" di browser
Pastikan `FRONTEND_URL` di Railway variables sudah benar (sama dengan URL Vercel).

### Website tidak loading
Tunggu 2-3 menit setelah deploy, kemudian refresh.

### Chat tidak merespons
- Cek apakah `KIMI_API_KEY` sudah di-set
- Cek Railway logs: `railway logs`

---

## 📞 Butuh Bantuan?

Lihat dokumentasi platform:
- Vercel: https://vercel.com/docs
- Railway: https://docs.railway.app/
- KIMI API: https://platform.moonshot.cn/docs

---

**Selamat! Website Anda sudah ONLINE! 🎉**
