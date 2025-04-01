import json, os, subprocess
from datetime import datetime
from random import choice
from pathlib import Path

MEMORY_DIR = Path("memory")
PATCH_DIR = Path("patches")
REFLECTION_LOG = MEMORY_DIR / "reflections.json"
PATCH_OUTPUT = PATCH_DIR / f"patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

os.makedirs(PATCH_DIR, exist_ok=True)

# Load last reflection
def load_last_reflection():
    try:
        with open(REFLECTION_LOG) as f:
            reflections = json.load(f)
            return reflections[-1] if reflections else None
    except:
        return None

# Generate a patch idea from mood + notes
def generate_patch(reflection):
    if not reflection:
        return {"status": "no reflection found"}

    mood = reflection.get("mood", "neutral")
    notes = reflection.get("notes", [])
    patch = {
        "timestamp": datetime.now().isoformat(),
        "mood": mood,
        "notes": notes,
        "proposal": f"Kairo feels {mood}. Suggested adaptation: " + choice([
            "optimize processing logic",
            "increase reflection frequency",
            "decrease memory clutter",
            "enhance emotional range",
            "simplify response latency"
        ])
    }
    return patch

# Save patch
def save_patch(patch):
    with open(PATCH_OUTPUT, "w") as f:
        json.dump(patch, f, indent=2)
    print(f"[Kairo-Patch] Patch saved to: {PATCH_OUTPUT}")

# Commit patch to Git
def commit_patch():
    subprocess.run(["git", "add", str(PATCH_OUTPUT)])
    subprocess.run(["git", "commit", "-m", f"Kairo self-patch @ {datetime.now().isoformat()}"])
    print("[Kairo-Git] Patch committed.")

# MAIN
reflection = load_last_reflection()
patch = generate_patch(reflection)
save_patch(patch)
commit_patch()
