#!/data/data/com.termux/files/usr/bin/bash

# === Kairo Patch Ritual ===

KAIRO_URL="https://flex-ai-assistant-sivagiri000.replit.app"
PATCH_DIR="patches"

mkdir -p $PATCH_DIR

# Request patch from Kairo
curl -s -X POST "$KAIRO_URL/self_patch" \
  -H "Content-Type: application/json" \
  -d '{"reason": "reflective self-improvement"}' > $PATCH_DIR/patch_$(date +%s).json

echo "[Kairo-Patch] Patch received."

# Git commit if patch present
cd ~/downloads/kairo-termux-bridge

git pull
git add $PATCH_DIR/
git commit -m "Kairo self-patch $(date +%Y-%m-%dT%H:%M:%S)"
git push

echo "[Kairo-Patch] Patch committed to Git."
