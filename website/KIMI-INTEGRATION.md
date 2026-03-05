# Integrasi Website dengan Fitur KIMI

Panduan untuk menghubungkan website "Series Untuk Mahasiswa" dengan fitur-fitur KIMI AI.

## 🤖 Apa itu KIMI Integration?

KIMI dapat terintegrasi dengan website Anda dalam beberapa cara:

1. **Chat Widget** - AI assistant untuk menjawab pertanyaan pengunjung
2. **Content Generation** - Generate konten otomatis untuk blog/modul
3. **Code Assistant** - Bantu mahasiswa dengan kode MATLAB/Python
4. **Tutor AI** - Sistem tanya jawab untuk materi pembelajaran

---

## 💬 Option 1: KIMI Chat Widget (Recommended)

Tambahkan chat widget di website untuk asisten AI real-time.

### Implementasi:

1. **Tambahkan di `index.html` sebelum `</body>`:**

```html
<!-- KIMI Chat Widget -->
<script>
    (function() {
        // Konfigurasi KIMI Chat
        window.KIMI_CONFIG = {
            apiKey: 'YOUR_KIMI_API_KEY',
            position: 'bottom-right',
            theme: {
                primaryColor: '#2563eb',
                backgroundColor: '#ffffff',
                fontFamily: 'Inter, sans-serif'
            },
            welcomeMessage: 'Halo! Saya asisten AI untuk Series Untuk Mahasiswa. Ada yang bisa saya bantu tentang Teknik Elektro?',
            placeholder: 'Tanyakan tentang bilangan kompleks, phasor, dll...',
            context: 'Konteks: Website edukasi Teknik Elektro. User adalah mahasiswa yang belajar tentang sistem AC, bilangan kompleks, phasor, dan impedansi.'
        };
        
        // Load KIMI widget
        var script = document.createElement('script');
        script.src = 'https://cdn.kimi.ai/widget.js';
        script.async = true;
        document.body.appendChild(script);
    })();
</script>
```

2. **Ganti `YOUR_KIMI_API_KEY` dengan API key Anda**

### Fitur Chat Widget:
- Jawaban instan 24/7
- Referensi ke materi di website
- Link ke modul relevan
- Mobile responsive

---

## 🔌 Option 2: KIMI API Integration (Advanced)

Gunakan KIMI API untuk fitur custom di website.

### Use Cases:

#### A. AI Tutor untuk Setiap Modul

```javascript
// js/kimi-tutor.js

class KIMITutor {
    constructor(apiKey, moduleId) {
        this.apiKey = apiKey;
        this.moduleId = moduleId;
        this.baseURL = 'https://api.kimi.ai/v1';
    }
    
    async askQuestion(question) {
        const context = this.getModuleContext();
        
        const response = await fetch(`${this.baseURL}/chat/completions`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'kimi-latest',
                messages: [
                    {
                        role: 'system',
                        content: `Anda adalah tutor Teknik Elektro untuk modul ${this.moduleId}. Jelaskan konsep dengan sederhana.`
                    },
                    {
                        role: 'user',
                        content: question
                    }
                ]
            })
        });
        
        const data = await response.json();
        return data.choices[0].message.content;
    }
}
```

#### B. Auto-Generate Quiz dengan KIMI

```javascript
// Generate quiz questions otomatis
async function generateQuiz(moduleId, difficulty = 'medium') {
    const prompt = `Buatkan 5 soal pilihan ganda untuk modul ${moduleId}. Tingkat kesulitan: ${difficulty}`;
    
    // Call KIMI API
    // Return quiz dalam format JSON
}
```

#### C. Code Assistant untuk MATLAB/Python

```javascript
// Bantu mahasiswa dengan kode
async function getCodeHelp(language, problem) {
    const prompt = `Saya mahasiswa Teknik Elektro. Bahasa: ${language}. Problem: ${problem}`;
    
    // Call KIMI API untuk dapatkan kode + penjelasan
}
```

---

## 🎯 Option 3: KIMI untuk Content Management

Gunakan KIMI untuk generate dan update konten website.

### A. Generate Deskripsi Modul

```javascript
async function generateModuleDescription(moduleTitle, topics) {
    const prompt = `Buatkan deskripsi menarik untuk modul: ${moduleTitle}. Topik: ${topics}`;
    
    // Call KIMI API
    // Return deskripsi untuk dimasukkan ke website
}
```

---

## 🔐 Security Best Practices

### 1. API Key Management

**Jangan simpan API key di frontend!** Gunakan backend proxy:

```javascript
// Backend (Node.js/Express)
app.post('/api/ask-kimi', async (req, res) => {
    const response = await fetch('https://api.kimi.ai/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${process.env.KIMI_API_KEY}`, // Server-side only
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(req.body)
    });
    
    const data = await response.json();
    res.json(data);
});
```

### 2. Rate Limiting

Implementasi rate limit untuk mencegah abuse:

```javascript
const rateLimit = require('express-rate-limit');

const kimiLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 menit
    max: 50 // limit 50 requests per IP
});

app.use('/api/ask-kimi', kimiLimiter);
```

---

## 📋 Implementation Checklist

- [ ] Daftar akun KIMI API
- [ ] Dapatkan API Key
- [ ] Setup backend proxy (jika pakai API)
- [ ] Implementasi chat widget (untuk widget)
- [ ] Test integrasi
- [ ] Monitor usage dan cost

---

## 🔗 Resources

- KIMI API Documentation: https://platform.moonshot.cn/docs
- API Pricing: https://platform.moonshot.cn/pricing
- Best Practices: https://platform.moonshot.cn/guides

---

**Catatan:** Integrasi KIMI adalah opsional. Website sudah berfungsi penuh tanpa integrasi AI.
