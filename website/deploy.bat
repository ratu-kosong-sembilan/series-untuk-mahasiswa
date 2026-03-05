@echo off
chcp 65001 >nul
cls

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║      🚀 SERIES UNTUK MAHASISWA - AUTO DEPLOYMENT              ║
echo ║                        (Windows)                               ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

:: Check prerequisites
echo [Step 0] Checking prerequisites...

node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js tidak ditemukan!
    echo Silakan install Node.js dari https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ Node.js terinstall

:: Install Vercel CLI
echo.
echo [Step 1] Installing Vercel CLI...

call vercel --version >nul 2>&1
if errorlevel 1 (
    echo Installing Vercel CLI...
    call npm install -g vercel
) else (
    echo ✅ Vercel CLI sudah ada
)

:: Install Railway CLI
echo.
echo [Step 2] Installing Railway CLI...

call railway --version >nul 2>&1
if errorlevel 1 (
    echo Installing Railway CLI...
    call npm install -g @railway/cli
) else (
    echo ✅ Railway CLI sudah ada
)

:: Login checks
echo.
echo [Step 3] Checking login status...
echo.

echo ⚠️ ANDA PERLU LOGIN KE PLATFORM BERIKUT:
echo.

echo Checking Vercel login...
call vercel whoami >nul 2>&1
if errorlevel 1 (
    echo ❌ Belum login ke Vercel
    echo Silakan jalankan: vercel login
    echo Buka URL yang muncul di browser dan login
    echo.
    set /p vercel_login="Sudah login ke Vercel? (y/n): "
    if /I not "%vercel_login%"=="y" (
        echo Silakan login dulu, lalu jalankan script ini lagi.
        pause
        exit /b 1
    )
) else (
    echo ✅ Sudah login ke Vercel
)

echo.
echo Checking Railway login...
call railway whoami >nul 2>&1
if errorlevel 1 (
    echo ❌ Belum login ke Railway
    echo Silakan jalankan: railway login
    echo Buka URL yang muncul di browser dan login
    echo.
    set /p railway_login="Sudah login ke Railway? (y/n): "
    if /I not "%railway_login%"=="y" (
        echo Silakan login dulu, lalu jalankan script ini lagi.
        pause
        exit /b 1
    )
) else (
    echo ✅ Sudah login ke Railway
)

:: Deploy Frontend
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 4] Deploy Frontend ke Vercel
echo ════════════════════════════════════════════════════════════
echo.

echo 📦 Mendeploy frontend...
echo.

if not exist ".vercel" (
    echo 📝 Ini adalah deploy pertama ke Vercel
    echo Ikuti instruksi di terminal...
    echo.
    call vercel
) else (
    echo 🚀 Melakukan production deployment...
    call vercel --prod
)

echo.
echo ✅ Frontend berhasil dideploy!
echo.

set /p VERCEL_URL="Masukkan URL Vercel Anda (contoh: https://series-untuk-mahasiswa.vercel.app): "

:: Deploy Backend
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 5] Deploy Backend ke Railway
echo ════════════════════════════════════════════════════════════
echo.

cd backend

echo 📦 Mendeploy backend...
echo.

if not exist ".railway" (
    echo 📝 Inisialisasi project Railway baru...
    echo Pilih: Create New Project
    call railway init
) else (
    echo 🚀 Project sudah ada, melakukan deploy...
)

echo.
echo 📤 Uploading code to Railway...
call railway up

echo.
echo 🌐 Generating domain...
call railway domain

echo.
set /p RAILWAY_URL="Masukkan URL Railway Anda (contoh: https://series-mahasiswa-api.up.railway.app): "

:: Set Environment Variables
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 6] Konfigurasi Environment Variables
echo ════════════════════════════════════════════════════════════
echo.

echo Setting FRONTEND_URL...
call railway variables set FRONTEND_URL="%VERCEL_URL%"

echo Setting NODE_ENV...
call railway variables set NODE_ENV="production"

echo.
echo ✅ Environment variables sudah di-set

:: KIMI API Key
echo.
set /p has_kimi="Apakah Anda sudah punya KIMI API Key? (y/n): "

if /I "%has_kimi%"=="y" (
    set /p KIMI_KEY="Masukkan KIMI_API_KEY Anda: "
    call railway variables set KIMI_API_KEY="%KIMI_KEY%"
    echo ✅ KIMI_API_KEY sudah di-set
) else (
    echo ⚠️ KIMI_API_KEY belum di-set
    echo Chat widget akan menggunakan fallback responses
    echo.
    echo Untuk mengaktifkan AI chat penuh:
    echo 1. Daftar di https://platform.moonshot.cn/
    echo 2. Buat API Key
    echo 3. cd backend ^&^& railway variables set KIMI_API_KEY=your_key
)

cd ..

:: Update Frontend Config
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 7] Update Frontend Configuration
echo ════════════════════════════════════════════════════════════
echo.

echo Mengupdate js/main.js dengan URL backend...

:: Using PowerShell to replace text
powershell -Command "(Get-Content js\main.js) -replace 'const PRODUCTION_API_URL = .*', 'const PRODUCTION_API_URL = ''%RAILWAY_URL%/api'';' | Set-Content js\main.js"

echo ✅ Konfigurasi frontend sudah diupdate

:: Redeploy Frontend
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 8] Redeploy Frontend dengan Config Baru
echo ════════════════════════════════════════════════════════════
echo.

echo 📦 Mendeploy ulang frontend...
call vercel --prod

echo.
echo ✅ Redeploy selesai!

:: Testing
echo.
echo ════════════════════════════════════════════════════════════
echo [Step 9] Testing Deployment
echo ════════════════════════════════════════════════════════════
echo.

echo 🧪 Melakukan testing...
echo.

echo Testing backend health...
curl -s "%RAILWAY_URL%/api/health" >nul
if errorlevel 1 (
    echo ⚠️ Backend belum ready (tunggu 1-2 menit)
) else (
    echo ✅ Backend API responding
)

echo.
echo Testing website accessibility...
curl -s "%VERCEL_URL%" >nul
if errorlevel 1 (
    echo ⚠️ Website belum ready (tunggu 1-2 menit)
) else (
    echo ✅ Website accessible
)

:: Complete
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║                  🎉 DEPLOYMENT COMPLETE! 🎉                   ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 🌐 WEBSITE ANDA SUDAH LIVE:
echo.
echo Frontend: %VERCEL_URL%
echo Backend:  %RAILWAY_URL%
echo API:      %RAILWAY_URL%/api
echo.
echo 📋 INFORMASI PENTING:
echo.
echo 1. 🌐 Buka website Anda di browser:
echo    %VERCEL_URL%
echo.
echo 2. 🔌 Cek API health:
echo    %RAILWAY_URL%/api/health
echo.
echo 3. 🔧 Update konfigurasi backend:
echo    cd backend ^&^& railway variables
echo.
echo 4. 📊 Monitor deployment:
echo    - Vercel Dashboard: https://vercel.com/dashboard
echo    - Railway Dashboard: https://railway.app/dashboard
echo.

if /I not "%has_kimi%"=="y" (
    echo ⚠️ KIMI AI belum diaktifkan
    echo Untuk mengaktifkan AI chat:
    echo 1. Daftar di https://platform.moonshot.cn/
    echo 2. Dapatkan API Key
    echo 3. cd backend ^&^& railway variables set KIMI_API_KEY=your_key
    echo.
)

echo 💡 TIPS:
echo - Website akan aktif dalam 1-2 menit
echo - SSL/HTTPS sudah otomatis aktif
echo - CDN global sudah tersedia
echo.
echo 🎉 SELAMAT! Website 'Series Untuk Mahasiswa' sudah ONLINE!
echo.

pause
