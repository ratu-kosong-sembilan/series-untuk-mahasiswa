# Panduan Deployment Website

Panduan lengkap untuk deploy website "Series Untuk Mahasiswa" ke berbagai platform hosting.

## 📋 Pre-Deployment Checklist

Sebelum deploy, pastikan:

- [ ] Ganti video YouTube placeholder dengan video Anda
- [ ] Update informasi kontak (email, sosial media)
- [ ] Cek semua links berfungsi
- [ ] Test responsive di mobile
- [ ] Optimasi gambar (compress)
- [ ] Tambah analytics (opsional)

---

## 🚀 Option 1: Vercel (Recommended)

**Gratis, mudah, dengan CDN global**

### Step-by-Step:

1. **Push ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial website commit"
   git branch -M main
   git remote add origin https://github.com/username/series-untuk-mahasiswa.git
   git push -u origin main
   ```

2. **Setup Vercel**
   - Buka [vercel.com](https://vercel.com)
   - Sign up/login dengan GitHub
   - Click "New Project"
   - Import repository Anda
   - Framework Preset: "Other"
   - Root Directory: `website`
   - Click "Deploy"

3. **Custom Domain** (opsional)
   - Di dashboard Vercel, pilih project
   - Settings → Domains
   - Add your domain
   - Follow DNS configuration

### Keuntungan Vercel:
- ✅ Deploy otomatis saat push ke GitHub
- ✅ SSL certificate gratis
- ✅ CDN global (load cepat di Indonesia)
- ✅ Analytics gratis

---

## 🌐 Option 2: Netlify

**Alternatif Vercel, juga gratis**

### Step-by-Step:

1. **Buka Netlify**
   - [netlify.com](https://netlify.com)
   - Sign up/login

2. **Deploy**
   - Pilih "Add new site" → "Import an existing project"
   - Connect GitHub
   - Pilih repository
   - Build command: (kosongkan - static site)
   - Publish directory: `website`
   - Click "Deploy site"

3. **Atau Drag & Drop**
   - Build website (zip folder `website`)
   - Drag ke Netlify dashboard
   - Instant deploy

---

## 📄 Option 3: GitHub Pages

**Gratis untuk repository public**

### Step-by-Step:

1. **Enable GitHub Pages**
   - Go to repository Settings
   - Pages (sidebar)
   - Source: Deploy from a branch
   - Branch: `main` / `root`
   - Click "Save"

2. **Jika pakai custom domain:**
   - Buat file `CNAME` di root website
   - Isi dengan domain Anda: `seriesuntukmahasiswa.com`

3. **Akses website:**
   - `https://username.github.io/repository-name`

---

## 🖥️ Option 4: cPanel Hosting (Indonesia)

**Untuk domain .id atau hosting lokal**

### Provider Indonesia yang recommended:
- Niagahoster
- DomaiNesia
- Qwords
- Rumahweb

### Step-by-Step:

1. **Beli Hosting & Domain**
   - Pilih paket shared hosting
   - Register domain (atau transfer)

2. **Upload Files**
   - Login cPanel
   - File Manager → public_html
   - Upload semua file dari folder `website`
   - Atau pakai FTP (FileZilla)

3. **FTP Settings:**
   ```
   Host: ftp.yourdomain.com
   Username: your_cpanel_username
   Password: your_cpanel_password
   Port: 21
   ```

4. **Verifikasi**
   - Buka domain Anda di browser
   - Website should be live

---

## ☁️ Option 5: AWS S3 + CloudFront

**Untuk scale besar, butuh setup lebih**

### Step-by-Step:

1. **Create S3 Bucket**
   - AWS Console → S3
   - Create bucket: `seriesuntukmahasiswa.com`
   - Enable "Static website hosting"
   - Upload files

2. **Set Permissions**
   - Bucket Policy → Allow public read

3. **CloudFront (CDN)**
   - Create distribution
   - Origin: S3 bucket
   - Enable HTTPS

4. **Route 53 (DNS)**
   - Point domain ke CloudFront

---

## 🔧 Custom Domain Setup

### DNS Configuration (umum):

**A Record:**
```
Host: @
Points to: [IP dari hosting]
```

**CNAME Record:**
```
Host: www
Points to: yourdomain.com
```

**Untuk Vercel/Netlify:**
```
Type: CNAME
Host: @
Value: cname.vercel-dns.com
```

---

## 🔒 SSL/HTTPS Setup

### Vercel/Netlify:
- ✅ SSL otomatis (Let's Encrypt)

### cPanel:
1. Login cPanel
2. SSL/TLS → Let's Encrypt
3. Issue certificate untuk domain

### CloudFlare (alternatif):
1. Daftar di cloudflare.com
2. Add site
3. Change nameservers
4. Enable "Always Use HTTPS"

---

## 📊 Post-Deployment

### 1. Google Search Console
- Daftar di [search.google.com](https://search.google.com)
- Add property (domain)
- Submit sitemap.xml
- Request indexing

### 2. Google Analytics
- Daftar di [analytics.google.com](https://analytics.google.com)
- Create property
- Get tracking ID (GA4)
- Add ke website

### 3. Performance Test
- [PageSpeed Insights](https://pagespeed.web.dev)
- [GTmetrix](https://gtmetrix.com)
- Target: Score > 90

---

## 🆘 Troubleshooting

### Website tidak muncul?
```
- Cek DNS propagation (bisa 24-48 jam)
- Clear browser cache
- Cek file di root directory
```

### Gambar tidak load?
```
- Cek path relatif (./assets/ vs /assets/)
- Cek case sensitivity (Assets vs assets)
- Cek file permissions (644 untuk files)
```

### Custom domain error?
```
- Pastikan A record/CNAME benar
- Cek SSL certificate
- Tunggu DNS propagation
```

---

## 📞 Support

Jika ada masalah deployment:
1. Cek dokumentasi platform hosting
2. Cek community forum
3. Contact support hosting

---

**Selamat! Website Anda sekarang online! 🎉**
