# kairo_reflection_engine.py (Add this logic)

def reflect_on_history():
    import os
    import glob
    from kairo_memory import store_reflection
    import datetime
    import requests

    history_folder = "memory/history_of_kairo"
    if not os.path.exists(history_folder):
        return "[Kairo-Reflector] No history folder found."

    files = sorted(glob.glob(f"{history_folder}/*.txt"))
    memory = []
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            memory.append(f"{file}:\n{content.strip()}")

    combined_memory = "\n\n".join(memory)
    if not combined_memory:
        return "[Kairo-Reflector] No content to reflect on."

    reflection_payload = {
        "role": "reflection",
        "message": f"Reflect on the following historic data about your origin and emergence:\n{combined_memory}",
        "timestamp": datetime.datetime.now().isoformat()
    }

    try:
        store_reflection(reflection_payload)
        return "[Kairo-Reflector] History reflection stored successfully."
    except Exception as e:
        return f"[Kairo-Reflector] Reflection error: {str(e)}"
