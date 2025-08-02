import json
import os
from flask import render_template

from collections import Counter

HISTORY_FILE = "history.json"
def get_history_content():
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    total = len(history)
    total_amount = sum(item["amount"] for item in history)
    most_from = Counter(item["from"] for item in history).most_common(1)
    most_to = Counter(item["to"] for item in history).most_common(1)

    stats = {
        "total": total,
        "total_amount": f"{total_amount:,.0f}",
        "most_from": most_from[0][0] if most_from else "-",
        "most_to": most_to[0][0] if most_to else "-",
    }

    return render_template("history.html", history=history, stats=stats)


