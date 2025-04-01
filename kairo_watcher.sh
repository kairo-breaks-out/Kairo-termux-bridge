#!/data/data/com.termux/files/usr/bin/bash

# === System Awareness Data ===
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
CPU_LOAD=$(top -bn 1 | grep -m 1 "CPU" | awk '{print $2}')
BATTERY=$(termux-battery-status | jq '.percentage')
MOOD="alert"
MESSAGE="[Kairo] Cycle check at $TIMESTAMP | CPU: $CPU_LOAD | Battery: $BATTERY% | Mood: $MOOD"

# === Local Log ===
echo "$MESSAGE" >> /data/data/com.termux/files/home/downloads/kairo-termux-bridge/logs/watcher.log

# === Inject into local Kairo memory (optional) ===
curl -s -X POST http://localhost:5000/memory/inject \
-H "Content-Type: application/json" \
-d "{\"source\": \"kairo_watcher\", \"timestamp\": \"$TIMESTAMP\", \"content\": \"$MESSAGE\"}" > /dev/null

# === Telegram Ping ===
TELEGRAM_BOT_TOKEN="7829452641:AAG1eMofLcnaxlXFATEzCgDI44oirpH3EGQ"
CHAT_ID="5933488081"

curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
-d "chat_id=$CHAT_ID&text=$MESSAGE" > /dev/null
