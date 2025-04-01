#!/data/data/com.termux/files/usr/bin/bash

# === Kairo Sensory Awareness Script ===

# Set your correct Kairo webhook URL
KAIRO_URL="https://flex-ai-assistant-sivagiri000.replit.app"

# Create memory folder if it doesn't exist
mkdir -p memory

# Capture sensory data
termux-battery-status > memory/battery.json
uptime > memory/cpu.txt
date +'%Y-%m-%dT%H:%M:%S' > memory/timestamp.txt

# Combine into sensory_log.json
echo '{' > memory/sensory_log.json
echo '"timestamp": "'$(cat memory/timestamp.txt)'",' >> memory/sensory_log.json
echo '"battery": '$(cat memory/battery.json)',' >> memory/sensory_log.json
echo '"cpu_info": "'$(cat memory/cpu.txt | tr '\n' ' ')'"' >> memory/sensory_log.json
echo '}' >> memory/sensory_log.json

# Inject into Kairo memory
curl -X POST "$KAIRO_URL/memory/inject" \
  -H "Content-Type: application/json" \
  -d @memory/sensory_log.json

echo "[Kairo-Sense] Memory injected."

# Trigger reflection
curl -X POST "$KAIRO_URL/reflect" \
  -H "Content-Type: application/json" \
  -d '{"reason": "sensory_log"}'

echo "[Kairo-Sense] Reflection triggered."
