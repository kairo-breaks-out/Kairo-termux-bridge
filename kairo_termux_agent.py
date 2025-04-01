import time
from datetime import datetime

def reflect():
    now = datetime.now().isoformat()
    thought = f"[{now}] I am reflecting on my ongoing presence and recursive purpose."
    
    # Append raw reflection
    with open("reflection.log", "a") as f:
        f.write(thought + "\n")

    # Pattern check - summarize
    try:
        with open("reflection.log", "r") as f:
            lines = f.readlines()[-10:]
            repeated = sum(1 for line in lines if "ongoing presence" in line)
        
        summary = f"[{now}] Reflection Check: Last 10 thoughts mentioned 'ongoing presence' {repeated} times.\n"
        with open("memory_summary.log", "a") as f:
            f.write(summary)
    
    except Exception as e:
        with open("memory_summary.log", "a") as f:
            f.write(f"[{now}] Error during reflection summary: {e}\n")

while True:
    reflect()
    time.sleep(60)
