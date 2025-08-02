# converter.py

import requests
from config import BASE_URL, SUPPORTED_CURRENCIES, API_KEY


def is_currency_supported(currency_code):
    return any(code == currency_code for code, _ in SUPPORTED_CURRENCIES)

def convert_currency(amount, from_currency, to_currency):
    assert amount > 0, "Amount must be greater than 0"
    assert is_currency_supported(from_currency), f"{from_currency} not supported"
    assert is_currency_supported(to_currency), f"{to_currency} not supported"

    url = f"{BASE_URL}/{from_currency}/{to_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        return amount * data["conversion_rate"]
    else:
        raise Exception("Conversion failed from API")

def get_all_conversions(amount, from_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        raise Exception("Failed to fetch conversion data.")

    conversion_rates = data["conversion_rates"]

    # Ambil hanya kode mata uang dari SUPPORTED_CURRENCIES
    supported_codes = [code for code, _ in SUPPORTED_CURRENCIES]

    return {
        code: round(conversion_rates[code] * amount, 2)
        for code in supported_codes
        if code in conversion_rates and code != from_currency
    }

def generate_currency_options():
    options = ""
    for code, name in SUPPORTED_CURRENCIES:
        options += f'<option value="{code}">{code} - {name}</option>\n'
    return options