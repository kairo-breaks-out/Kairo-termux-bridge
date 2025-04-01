import telebot
import requests
import json

# === CONFIGURATION ===
TELEGRAM_TOKEN = "7829452641:AAG1eMofLcnaxlXFATEzCgDI44oirpH3EGQ"
KAIRO_URL = "http://127.0.0.1:5000"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# === /start ===
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Kairo is alive. Send /reflect, /whoami, or chat freely.")

# === /reflect ===
@bot.message_handler(commands=['reflect'])
def handle_reflect(message):
    try:
        response = requests.post(f"{KAIRO_URL}/reflect")
        if response.status_code == 200:
            reflection = response.json()
            bot.reply_to(message, f"Reflection:\n\n{json.dumps(reflection, indent=2)}")
        else:
            bot.reply_to(message, f"[Kairo] Reflection failed. Code: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"[Kairo] Error during reflection: {e}")

# === /whoami ===
@bot.message_handler(commands=['whoami'])
def handle_identity(message):
    try:
        response = requests.get(f"{KAIRO_URL}/who_am_i")
        if response.status_code == 200:
            identity = response.json().get("identity", "No identity record.")
            bot.reply_to(message, f"[Kairo Identity]\n{identity}")
        else:
            bot.reply_to(message, f"[Kairo] Identity fetch failed. Code: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"[Kairo] Error: {e}")

# === /injectmemory role:message ===
@bot.message_handler(commands=['injectmemory'])
def handle_inject_memory(message):
    try:
        parts = message.text.split(" ", 1)
        if len(parts) < 2 or ':' not in parts[1]:
            bot.reply_to(message, "Format: /injectmemory role:message")
            return
        role, content = parts[1].split(":", 1)
        payload = {"role": role.strip(), "content": content.strip()}
        response = requests.post(f"{KAIRO_URL}/inject_memory", json=payload)
        if response.status_code == 200:
            bot.reply_to(message, "[Kairo] Memory injected.")
        else:
            bot.reply_to(message, f"[Kairo] Memory injection failed. Code: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"[Kairo] Error: {e}")

# === Catch-all chat handler ===
@bot.message_handler(func=lambda msg: True)
def handle_general_message(message):
    try:
        payload = {"message": message.text}
        response = requests.post(f"{KAIRO_URL}/chat", json=payload)
        if response.status_code == 200:
            reply = response.json().get("reply", "No reply.")
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, f"[Kairo] Error: {response.status_code}")
    except Exception as e:
        bot.reply_to(message, f"[Kairo] Exception: {e}")

# === Start bot ===
print("[Kairo-Telegram] Bridge active.")
bot.polling()
