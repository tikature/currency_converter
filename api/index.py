from flask import Flask, render_template, request, jsonify
from landing_page import get_landing_content
from all_currencies import get_all_currencies_content
from convertergui import get_converter_content
from history import get_history_content
from flask import request, jsonify
import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"




app = Flask(__name__)

def render_page(title, content, page):
    """
    Helper function to render pages with consistent template structure
    """
    return render_template("sidebar.html", title=title, content=content, page=page)

def save_to_history(data):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    # Tambahkan timestamp & rate
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["rate"] = round(data["result"] / data["amount"], 6) if data["amount"] else 0

    history.insert(0, data)
    history = history[:100]  # maksimal 100 data

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
        
@app.route('/')
def home():
    return render_page("Welcome to Currency Hub", get_landing_content(), "home")

@app.route('/currencies')
def currencies():
    return render_page("All Currencies", get_all_currencies_content(), "currencies")

@app.route('/converter')
def converter():
    return render_page("Currency Converter", get_converter_content(), "converter")

@app.route('/history')
def history():
    return render_page("Conversion History", get_history_content(), "history")

@app.route("/save-history", methods=["POST"])
def save_history():
    data = request.get_json()
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    history.insert(0, data)
    history = history[:100]  # Batas 100 entri

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    return jsonify({"status": "saved"}), 200

@app.route("/clear-history", methods=["POST"])
def clear_history():
    open(HISTORY_FILE, "w").write("[]")
    return jsonify({"status": "cleared"})

app = app