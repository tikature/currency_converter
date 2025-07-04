import os
import requests
import logging

API_KEY = os.getenv("99af1e52e8b504f480478eda")  # API Key dari environment variable
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair"
CODES_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/codes"

# Setup basic logging
logging.basicConfig(level=logging.INFO)

def get_supported_currencies():
    try:
        response = requests.get(CODES_URL, timeout=10)
        response.raise_for_status()  # raise error jika response code bukan 200
        data = response.json()
        return data.get("supported_codes", []) if data.get("result") == "success" else []
    except Exception as e:
        logging.error(f"Failed to fetch supported currencies: {e}")
        return []

SUPPORTED_CURRENCIES = get_supported_currencies()
