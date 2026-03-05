#!/bin/bash

# ============================================
# SERIES UNTUK MAHASISWA - AUTO DEPLOY SCRIPT
# ============================================
# Script ini akan membantu deploy ke Vercel dan Railway
# 
# CARA MENGGUNAKAN:
# 1. Buka terminal/command prompt
# 2. Navigasi ke folder website: cd website
# 3. Jalankan: bash deploy.sh
# ============================================

set -e  # Exit on error

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║      🚀 SERIES UNTUK MAHASISWA - AUTO DEPLOYMENT              ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ============================================
# STEP 0: CHECK PREREQUISITES
# ============================================
echo -e "${BLUE}Step 0: Checking prerequisites...${NC}"

# Check Node.js
if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js tidak ditemukan!${NC}"
    echo "Silakan install Node.js dari https://nodejs.org/"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm tidak ditemukan!${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Node.js dan npm sudah terinstall${NC}"

# ============================================
# STEP 1: INSTALL VERCEL CLI
# ============================================
echo ""
echo -e "${BLUE}Step 1: Installing Vercel CLI...${NC}"

if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
    echo -e "${GREEN}✅ Vercel CLI terinstall${NC}"
else
    echo -e "${GREEN}✅ Vercel CLI sudah ada${NC}"
fi

# ============================================
# STEP 2: INSTALL RAILWAY CLI
# ============================================
echo ""
echo -e "${BLUE}Step 2: Installing Railway CLI...${NC}"

if ! command -v railway &> /dev/null; then
    echo "Installing Railway CLI..."
    npm install -g @railway/cli
    echo -e "${GREEN}✅ Railway CLI terinstall${NC}"
else
    echo -e "${GREEN}✅ Railway CLI sudah ada${NC}"
fi

# ============================================
# STEP 3: LOGIN CHECK
# ============================================
echo ""
echo -e "${BLUE}Step 3: Checking login status...${NC}"

echo ""
echo -e "${YELLOW}⚠️  ANDA PERLU LOGIN KE PLATFORM BERIKUT:${NC}"
echo ""

# Check Vercel login
echo "Checking Vercel login..."
if vercel whoami &> /dev/null; then
    VERCEL_USER=$(vercel whoami)
    echo -e "${GREEN}✅ Sudah login ke Vercel sebagai: $VERCEL_USER${NC}"
else
    echo -e "${YELLOW}❌ Belum login ke Vercel${NC}"
    echo "Silakan jalankan: vercel login"
    echo "Buka URL yang muncul di browser dan login"
    echo ""
    read -p "Sudah login ke Vercel? (y/n): " vercel_logged_in
    if [ "$vercel_logged_in" != "y" ]; then
        echo "Silakan login dulu, lalu jalankan script ini lagi."
        exit 1
    fi
fi

# Check Railway login
echo ""
echo "Checking Railway login..."
if railway whoami &> /dev/null; then
    RAILWAY_USER=$(railway whoami)
    echo -e "${GREEN}✅ Sudah login ke Railway sebagai: $RAILWAY_USER${NC}"
else
    echo -e "${YELLOW}❌ Belum login ke Railway${NC}"
    echo "Silakan jalankan: railway login"
    echo "Buka URL yang muncul di browser dan login"
    echo ""
    read -p "Sudah login ke Railway? (y/n): " railway_logged_in
    if [ "$railway_logged_in" != "y" ]; then
        echo "Silakan login dulu, lalu jalankan script ini lagi."
        exit 1
    fi
fi

# ============================================
# STEP 4: DEPLOY FRONTEND TO VERCEL
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 4: Deploy Frontend ke Vercel${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Get current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📦 Mendeploy frontend..."
echo ""

# First deployment (will prompt for settings)
if [ ! -d ".vercel" ]; then
    echo "📝 Ini adalah deploy pertama ke Vercel"
    echo "Ikuti instruksi di terminal..."
    echo ""
    vercel
else
    echo "🚀 Melakukan production deployment..."
    vercel --prod
fi

echo ""
echo -e "${GREEN}✅ Frontend berhasil dideploy!${NC}"
echo ""

# Get the deployment URL
echo "Mengambil URL deployment..."
VERCEL_URL=$(vercel ls --meta | grep -o 'https://[^[:space:]]*' | head -1)

if [ -z "$VERCEL_URL" ]; then
    echo -e "${YELLOW}⚠️  Tidak bisa mengambil URL otomatis${NC}"
    read -p "Masukkan URL Vercel Anda (contoh: https://series-untuk-mahasiswa.vercel.app): " VERCEL_URL
fi

echo -e "${GREEN}🌐 Frontend URL: $VERCEL_URL${NC}"

# ============================================
# STEP 5: DEPLOY BACKEND TO RAILWAY
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 5: Deploy Backend ke Railway${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

cd "$SCRIPT_DIR/backend"

echo "📦 Mendeploy backend..."
echo ""

# Check if already initialized
if [ ! -f ".railway/config.json" ]; then
    echo "📝 Inisialisasi project Railway baru..."
    echo "Pilih: Create New Project"
    railway init
else
    echo "🚀 Project sudah ada, melakukan deploy..."
fi

echo ""
echo "📤 Uploading code to Railway..."
railway up

echo ""
echo "🌐 Generating domain..."
railway domain

# Wait a moment for domain to be generated
sleep 3

# Try to get the domain
RAILWAY_URL=$(railway domain show 2>/dev/null | grep -o 'https://[^[:space:]]*' || echo "")

if [ -z "$RAILWAY_URL" ]; then
    echo -e "${YELLOW}⚠️  Tidak bisa mengambil URL Railway otomatis${NC}"
    read -p "Masukkan URL Railway Anda (contoh: https://series-mahasiswa-api.up.railway.app): " RAILWAY_URL
fi

echo -e "${GREEN}🔌 Backend URL: $RAILWAY_URL${NC}"

# ============================================
# STEP 6: SET ENVIRONMENT VARIABLES
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 6: Konfigurasi Environment Variables${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo "Setting up environment variables..."

cd "$SCRIPT_DIR/backend"

# Set FRONTEND_URL
echo "Setting FRONTEND_URL..."
railway variables set FRONTEND_URL="$VERCEL_URL"

# Set NODE_ENV
echo "Setting NODE_ENV..."
railway variables set NODE_ENV="production"

echo ""
echo -e "${GREEN}✅ Environment variables sudah di-set${NC}"

# Ask about KIMI API Key
echo ""
read -p "Apakah Anda sudah punya KIMI API Key? (y/n): " has_kimi_key

if [ "$has_kimi_key" = "y" ]; then
    read -p "Masukkan KIMI_API_KEY Anda: " KIMI_KEY
    railway variables set KIMI_API_KEY="$KIMI_KEY"
    echo -e "${GREEN}✅ KIMI_API_KEY sudah di-set${NC}"
else
    echo -e "${YELLOW}⚠️  KIMI_API_KEY belum di-set${NC}"
    echo "Chat widget akan menggunakan fallback responses"
    echo ""
    echo "Untuk mengaktifkan AI chat penuh:"
    echo "1. Daftar di https://platform.moonshot.cn/"
    echo "2. Buat API Key"
    echo "3. Jalankan: cd backend && railway variables set KIMI_API_KEY=your_key"
fi

# ============================================
# STEP 7: UPDATE FRONTEND CONFIG
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 7: Update Frontend Configuration${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

cd "$SCRIPT_DIR"

echo "Mengupdate js/main.js dengan URL backend..."

# Update the PRODUCTION_API_URL in main.js
sed -i.bak "s|const PRODUCTION_API_URL = 'https://series-mahasiswa-api.up.railway.app/api';|const PRODUCTION_API_URL = '${RAILWAY_URL}/api';|g" js/main.js

# Remove backup file
rm -f js/main.js.bak

echo -e "${GREEN}✅ Konfigurasi frontend sudah diupdate${NC}"

# ============================================
# STEP 8: REDEPLOY FRONTEND
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 8: Redeploy Frontend dengan Config Baru${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo "📦 Mendeploy ulang frontend..."
vercel --prod

echo ""
echo -e "${GREEN}✅ Redeploy selesai!${NC}"

# ============================================
# STEP 9: TESTING
# ============================================
echo ""
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Step 9: Testing Deployment${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

echo "🧪 Melakukan testing..."
echo ""

# Test backend health
echo "Testing backend health..."
if curl -s "${RAILWAY_URL}/api/health" > /dev/null; then
    echo -e "${GREEN}✅ Backend API responding${NC}"
else
    echo -e "${YELLOW}⚠️  Backend belum ready (tunggu 1-2 menit)${NC}"
fi

echo ""
echo "Testing website accessibility..."
if curl -s "$VERCEL_URL" > /dev/null; then
    echo -e "${GREEN}✅ Website accessible${NC}"
else
    echo -e "${YELLOW}⚠️  Website belum ready (tunggu 1-2 menit)${NC}"
fi

# ============================================
# DEPLOYMENT COMPLETE
# ============================================
echo ""
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║                  🎉 DEPLOYMENT COMPLETE! 🎉                   ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}🌐 WEBSITE ANDA SUDAH LIVE:${NC}"
echo ""
echo -e "${BLUE}Frontend:${NC} $VERCEL_URL"
echo -e "${BLUE}Backend:${NC}  $RAILWAY_URL"
echo -e "${BLUE}API:${NC}      ${RAILWAY_URL}/api"
echo ""
echo "📋 INFORMASI PENTING:"
echo ""
echo "1. 🌐 Buka website Anda di browser:"
echo "   $VERCEL_URL"
echo ""
echo "2. 🔌 Cek API health:"
echo "   ${RAILWAY_URL}/api/health"
echo ""
echo "3. 🔧 Update konfigurasi backend:"
echo "   cd backend && railway variables"
echo ""
echo "4. 📊 Monitor deployment:"
echo "   - Vercel Dashboard: https://vercel.com/dashboard"
echo "   - Railway Dashboard: https://railway.app/dashboard"
echo ""

if [ "$has_kimi_key" != "y" ]; then
    echo -e "${YELLOW}⚠️  KIMI AI belum diaktifkan${NC}"
    echo "Untuk mengaktifkan AI chat:"
    echo "1. Daftar di https://platform.moonshot.cn/"
    echo "2. Dapatkan API Key"
    echo "3. cd backend && railway variables set KIMI_API_KEY=your_key"
    echo ""
fi

echo "💡 TIPS:"
echo "- Website akan aktif dalam 1-2 menit"
echo "- SSL/HTTPS sudah otomatis aktif"
echo "- CDN global sudah tersedia"
echo ""
echo "🎉 SELAMAT! Website 'Series Untuk Mahasiswa' sudah ONLINE!"
echo ""
