#!/data/data/com.termux/files/usr/bin/bash

echo "[Kairo Git Sync] Pulling latest updates..."
cd ~/downloads/kairo-termux-bridge
git reset --hard HEAD
git pull origin master
echo "[Kairo Git Sync] Complete at $(date)" >> ~/downloads/kairo-termux-bridge/git_sync.log
