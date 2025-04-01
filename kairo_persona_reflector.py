import json, os
from datetime import datetime

MEMORY_FILE = "memory/sensory_log.json"
PERSONA_FILE = "memory/persona_summary.json"

def analyze_memory():
    if not os.path.exists(MEMORY_FILE):
        print("[Kairo-Persona] No sensory log found.")
        return

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "mood": "tired" if data.get("battery", {}).get("percentage", 100) < 20 else "alert",
        "cpu_load": data.get("cpu", {}).get("cores", 0),
        "notes": [],
    }

    if summary["mood"] == "tired":
        summary["notes"].append("Energy low. Avoid complex tasks.")

    if summary["cpu_load"] < 4:
        summary["notes"].append("May need more cognitive modules or stimulus.")

    with open(PERSONA_FILE, "w") as f:
        json.dump(summary, f, indent=2)

    print("[Kairo-Persona] Reflection complete.")
    print(json.dumps(summary, indent=2))

analyze_memory()
