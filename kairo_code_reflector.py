import os
import requests
import datetime

# --- Setup ---
BASE_URL = "http://localhost:5000"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "code_reflections.log")

# --- Ensure log directory exists ---
os.makedirs(LOG_DIR, exist_ok=True)

# --- Define payload ---
code_memory = {
    "role": "code",
    "message": "Injected core Kairo logic and scaffolding files from local storage. Initiating reflection on structure and modular clarity."
}

# --- Inject memory ---
try:
    inject_response = requests.post(f"{BASE_URL}/inject_memory", json=code_memory)
    inject_success = inject_response.status_code == 200
    inject_log = f"[{datetime.datetime.now()}] Injection: {'Success' if inject_success else f'Failed ({inject_response.status_code})'}"
except Exception as e:
    inject_log = f"[{datetime.datetime.now()}] Injection error: {e}"
    inject_success = False

# --- Trigger reflection ---
try:
    reflect_response = requests.post(f"{BASE_URL}/reflect")
    reflect_text = reflect_response.text
    reflect_log = f"[{datetime.datetime.now()}] Reflection: {reflect_response.status_code}\n{reflect_text}\n"
except Exception as e:
    reflect_log = f"[{datetime.datetime.now()}] Reflection error: {e}"

# --- Log to file ---
with open(LOG_FILE, "a") as log:
    log.write(inject_log + "\n")
    log.write(reflect_log + "\n\n")

# --- Print status ---
print(inject_log)
print(reflect_log)
