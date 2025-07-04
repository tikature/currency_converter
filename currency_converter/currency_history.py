import json
import os
import datetime

HISTORY_FILE_PATH = os.path.join(os.path.dirname(__file__), "currency_history.json")

def save_history_to_file(data):
    """
    Menyimpan data konversi ke file JSON dengan timestamp.
    """
    history = {}
    if os.path.exists(HISTORY_FILE_PATH):
        try:
            with open(HISTORY_FILE_PATH, "r") as f:
                history = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load existing history: {e}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history[timestamp] = data

    try:
        with open(HISTORY_FILE_PATH, "w") as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"[ERROR] Failed to save history: {e}")

def load_history_from_file():
    if os.path.exists(HISTORY_FILE_PATH):
        try:
            with open(HISTORY_FILE_PATH, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load history file: {e}")
    return {}
