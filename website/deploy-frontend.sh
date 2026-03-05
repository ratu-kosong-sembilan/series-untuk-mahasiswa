#!/bin/bash

# ============================================
# Deploy Frontend to Vercel
# ============================================

echo "🚀 Deploying Series Untuk Mahasiswa - Frontend"
echo "================================================"

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Check if user is logged in
echo "🔑 Checking Vercel login status..."
vercel whoami || (echo "Please login first: vercel login" && exit 1)

# Deploy to Vercel
echo ""
echo "📦 Starting deployment..."
vercel --prod

echo ""
echo "✅ Frontend deployment complete!"
echo "📝 Note: Update API_BASE_URL in js/main.js with your backend URL"
