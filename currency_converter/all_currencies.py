from datetime import datetime
import random

# Import dari existing modules
try:
    from config import SUPPORTED_CURRENCIES
    from converter import get_exchange_rate
except ImportError:
    # Complete list of supported currencies
    SUPPORTED_CURRENCIES = [
        ("AED", "UAE Dirham"),
        ("AFN", "Afghan Afghani"),
        ("ALL", "Albanian Lek"),
        ("AMD", "Armenian Dram"),
        ("ANG", "Netherlands Antillian Guilder"),
        ("AOA", "Angolan Kwanza"),
        ("ARS", "Argentine Peso"),
        ("AUD", "Australian Dollar"),
        ("AWG", "Aruban Florin"),
        ("AZN", "Azerbaijani Manat"),
        ("BAM", "Bosnia and Herzegovina Convertible Mark"),
        ("BBD", "Barbados Dollar"),
        ("BDT", "Bangladeshi Taka"),
        ("BGN", "Bulgarian Lev"),
        ("BHD", "Bahraini Dinar"),
        ("BIF", "Burundian Franc"),
        ("BMD", "Bermudian Dollar"),
        ("BND", "Brunei Dollar"),
        ("BOB", "Bolivian Boliviano"),
        ("BRL", "Brazilian Real"),
        ("BSD", "Bahamian Dollar"),
        ("BTN", "Bhutanese Ngultrum"),
        ("BWP", "Botswana Pula"),
        ("BYN", "Belarusian Ruble"),
        ("BZD", "Belize Dollar"),
        ("CAD", "Canadian Dollar"),
        ("CDF", "Congolese Franc"),
        ("CHF", "Swiss Franc"),
        ("CLP", "Chilean Peso"),
        ("CNY", "Chinese Renminbi"),
        ("COP", "Colombian Peso"),
        ("CRC", "Costa Rican Colon"),
        ("CUP", "Cuban Peso"),
        ("CVE", "Cape Verdean Escudo"),
        ("CZK", "Czech Koruna"),
        ("DJF", "Djiboutian Franc"),
        ("DKK", "Danish Krone"),
        ("DOP", "Dominican Peso"),
        ("DZD", "Algerian Dinar"),
        ("EGP", "Egyptian Pound"),
        ("ERN", "Eritrean Nakfa"),
        ("ETB", "Ethiopian Birr"),
        ("EUR", "Euro"),
        ("FJD", "Fiji Dollar"),
        ("FKP", "Falkland Islands Pound"),
        ("FOK", "Faroese Króna"),
        ("GBP", "Pound Sterling"),
        ("GEL", "Georgian Lari"),
        ("GGP", "Guernsey Pound"),
        ("GHS", "Ghanaian Cedi"),
        ("GIP", "Gibraltar Pound"),
        ("GMD", "Gambian Dalasi"),
        ("GNF", "Guinean Franc"),
        ("GTQ", "Guatemalan Quetzal"),
        ("GYD", "Guyanese Dollar"),
        ("HKD", "Hong Kong Dollar"),
        ("HNL", "Honduran Lempira"),
        ("HRK", "Croatian Kuna"),
        ("HTG", "Haitian Gourde"),
        ("HUF", "Hungarian Forint"),
        ("IDR", "Indonesian Rupiah"),
        ("ILS", "Israeli New Shekel"),
        ("IMP", "Manx Pound"),
        ("INR", "Indian Rupee"),
        ("IQD", "Iraqi Dinar"),
        ("IRR", "Iranian Rial"),
        ("ISK", "Icelandic Króna"),
        ("JEP", "Jersey Pound"),
        ("JMD", "Jamaican Dollar"),
        ("JOD", "Jordanian Dinar"),
        ("JPY", "Japanese Yen"),
        ("KES", "Kenyan Shilling"),
        ("KGS", "Kyrgyzstani Som"),
        ("KHR", "Cambodian Riel"),
        ("KID", "Kiribati Dollar"),
        ("KMF", "Comorian Franc"),
        ("KRW", "South Korean Won"),
        ("KWD", "Kuwaiti Dinar"),
        ("KYD", "Cayman Islands Dollar"),
        ("KZT", "Kazakhstani Tenge"),
        ("LAK", "Lao Kip"),
        ("LBP", "Lebanese Pound"),
        ("LKR", "Sri Lanka Rupee"),
        ("LRD", "Liberian Dollar"),
        ("LSL", "Lesotho Loti"),
        ("LYD", "Libyan Dinar"),
        ("MAD", "Moroccan Dirham"),
        ("MDL", "Moldovan Leu"),
        ("MGA", "Malagasy Ariary"),
        ("MKD", "Macedonian Denar"),
        ("MMK", "Burmese Kyat"),
        ("MNT", "Mongolian Tögrög"),
        ("MOP", "Macanese Pataca"),
        ("MRU", "Mauritanian Ouguiya"),
        ("MUR", "Mauritian Rupee"),
        ("MVR", "Maldivian Rufiyaa"),
        ("MWK", "Malawian Kwacha"),
        ("MXN", "Mexican Peso"),
        ("MYR", "Malaysian Ringgit"),
        ("MZN", "Mozambican Metical"),
        ("NAD", "Namibian Dollar"),
        ("NGN", "Nigerian Naira"),
        ("NIO", "Nicaraguan Córdoba"),
        ("NOK", "Norwegian Krone"),
        ("NPR", "Nepalese Rupee"),
        ("NZD", "New Zealand Dollar"),
        ("OMR", "Omani Rial"),
        ("PAB", "Panamanian Balboa"),
        ("PEN", "Peruvian Sol"),
        ("PGK", "Papua New Guinean Kina"),
        ("PHP", "Philippine Peso"),
        ("PKR", "Pakistani Rupee"),
        ("PLN", "Polish Złoty"),
        ("PYG", "Paraguayan Guaraní"),
        ("QAR", "Qatari Riyal"),
        ("RON", "Romanian Leu"),
        ("RSD", "Serbian Dinar"),
        ("RUB", "Russian Ruble"),
        ("RWF", "Rwandan Franc"),
        ("SAR", "Saudi Riyal"),
        ("SBD", "Solomon Islands Dollar"),
        ("SCR", "Seychellois Rupee"),
        ("SDG", "Sudanese Pound"),
        ("SEK", "Swedish Krona"),
        ("SGD", "Singapore Dollar"),
        ("SHP", "Saint Helena Pound"),
        ("SLE", "Sierra Leonean Leone"),
        ("SLL", "Sierra Leonean Leone"),
        ("SOS", "Somali Shilling"),
        ("SRD", "Surinamese Dollar"),
        ("SSP", "South Sudanese Pound"),
        ("STN", "São Tomé and Príncipe Dobra"),
        ("SYP", "Syrian Pound"),
        ("SZL", "Eswatini Lilangeni"),
        ("THB", "Thai Baht"),
        ("TJS", "Tajikistani Somoni"),
        ("TMT", "Turkmenistan Manat"),
        ("TND", "Tunisian Dinar"),
        ("TOP", "Tongan Paʻanga"),
        ("TRY", "Turkish Lira"),
        ("TTD", "Trinidad and Tobago Dollar"),
        ("TVD", "Tuvaluan Dollar"),
        ("TWD", "New Taiwan Dollar"),
        ("TZS", "Tanzanian Shilling"),
        ("UAH", "Ukrainian Hryvnia"),
        ("UGX", "Ugandan Shilling"),
        ("USD", "United States Dollar"),
        ("UYU", "Uruguayan Peso"),
        ("UZS", "Uzbekistani So'm"),
        ("VES", "Venezuelan Bolívar Soberano"),
        ("VND", "Vietnamese Đồng"),
        ("VUV", "Vanuatu Vatu"),
        ("WST", "Samoan Tālā"),
        ("XAF", "Central African CFA Franc"),
        ("XCD", "East Caribbean Dollar"),
        ("XCG", "Caribbean Guilder"),
        ("XDR", "Special Drawing Rights"),
        ("XOF", "West African CFA franc"),
        ("XPF", "CFP Franc"),
        ("YER", "Yemeni Rial"),
        ("ZAR", "South African Rand"),
        ("ZMW", "Zambian Kwacha"),
        ("ZWL", "Zimbabwean Dollar")
    ]

# Store previous rates for trend calculation
previous_rates = {}

def get_mock_exchange_rate(currency_code):
    """
    Generate mock exchange rates for demo purposes
    In real implementation, this would fetch from your converter module
    """
    # Jika USD, return 1.0 sebagai base
    if currency_code == "USD":
        return 1.0
    
    # Mock rates relative to USD - comprehensive list
    base_rates = {
        "AED": 3.67, "AFN": 88.5, "ALL": 92.4, "AMD": 387.2, "ANG": 1.79,
        "AOA": 827.5, "ARS": 350.8, "AUD": 1.35, "AWG": 1.79, "AZN": 1.70,
        "BAM": 1.66, "BBD": 2.0, "BDT": 110.5, "BGN": 1.66, "BHD": 0.376,
        "BIF": 2850.0, "BMD": 1.0, "BND": 1.35, "BOB": 6.91, "BRL": 5.3,
        "BSD": 1.0, "BTN": 83.2, "BWP": 13.6, "BYN": 3.26, "BZD": 2.0,
        "CAD": 1.25, "CDF": 2680.0, "CHF": 0.92, "CLP": 950.0, "CNY": 6.5,
        "COP": 4180.0, "CRC": 530.0, "CUP": 24.0, "CVE": 93.5, "CZK": 21.8,
        "DJF": 177.7, "DKK": 6.32, "DOP": 58.4, "DZD": 134.5, "EGP": 30.9,
        "ERN": 15.0, "ETB": 56.8, "EUR": 0.85, "FJD": 2.21, "FKP": 0.75,
        "FOK": 6.32, "GBP": 0.75, "GEL": 2.67, "GGP": 0.75, "GHS": 12.1,
        "GIP": 0.75, "GMD": 67.0, "GNF": 8600.0, "GTQ": 7.83, "GYD": 209.0,
        "HKD": 7.8, "HNL": 24.7, "HRK": 6.4, "HTG": 132.0, "HUF": 345.0,
        "IDR": 15400.0, "ILS": 3.25, "IMP": 0.75, "INR": 83.2, "IQD": 1310.0,
        "IRR": 42000.0, "ISK": 138.0, "JEP": 0.75, "JMD": 155.0, "JOD": 0.709,
        "JPY": 110.0, "KES": 128.0, "KGS": 89.5, "KHR": 4100.0, "KID": 1.35,
        "KMF": 417.0, "KRW": 1280.0, "KWD": 0.303, "KYD": 0.833, "KZT": 450.0,
        "LAK": 20500.0, "LBP": 15000.0, "LKR": 325.0, "LRD": 190.0, "LSL": 18.5,
        "LYD": 4.8, "MAD": 9.8, "MDL": 17.8, "MGA": 4500.0, "MKD": 52.3,
        "MMK": 2100.0, "MNT": 3450.0, "MOP": 8.05, "MRU": 40.0, "MUR": 45.2,
        "MVR": 15.4, "MWK": 1680.0, "MXN": 17.8, "MYR": 4.2, "MZN": 63.9,
        "NAD": 18.5, "NGN": 775.0, "NIO": 36.7, "NOK": 10.8, "NPR": 133.0,
        "NZD": 1.41, "OMR": 0.385, "PAB": 1.0, "PEN": 3.77, "PGK": 3.95,
        "PHP": 56.8, "PKR": 287.0, "PLN": 3.92, "PYG": 7350.0, "QAR": 3.64,
        "RON": 4.21, "RSD": 99.5, "RUB": 92.0, "RWF": 1280.0, "SAR": 3.75,
        "SBD": 8.5, "SCR": 13.6, "SDG": 601.0, "SEK": 10.6, "SGD": 1.35,
        "SHP": 0.75, "SLE": 22800.0, "SLL": 22800.0, "SOS": 570.0, "SRD": 37.2,
        "SSP": 130.0, "STN": 22.0, "SYP": 2512.0, "SZL": 18.5, "THB": 35.8,
        "TJS": 10.9, "TMT": 3.5, "TND": 3.1, "TOP": 2.35, "TRY": 32.2,
        "TTD": 6.78, "TVD": 1.35, "TWD": 31.5, "TZS": 2520.0, "UAH": 40.5,
        "UGX": 3750.0, "UYU": 39.8, "UZS": 12800.0, "VES": 36.2,
        "VND": 24500.0, "VUV": 119.0, "WST": 2.7, "XAF": 557.0, "XCD": 2.7,
        "XCG": 1.79, "XDR": 0.75, "XOF": 557.0, "XPF": 101.0, "YER": 250.0,
        "ZAR": 18.9, "ZMW": 27.0, "ZWL": 322.0
    }
    
    # Dapatkan base rate
    base_rate = base_rates.get(currency_code, random.uniform(0.5, 100.0))
    
    # Tambahkan variasi kecil untuk simulasi fluktuasi
    variation = random.uniform(0.98, 1.02)  # Variasi ±2%
    final_rate = base_rate * variation
    
    # Format sesuai dengan karakteristik mata uang
    if final_rate >= 1000:
        return round(final_rate, 0)
    elif final_rate >= 100:
        return round(final_rate, 2)
    elif final_rate >= 10:
        return round(final_rate, 3)
    else:
        return round(final_rate, 4)

def get_currency_flag(currency_code):
    """
    Return flag emoji for currency - comprehensive mapping
    """
    flags = {
        "AED": "🇦🇪", "AFN": "🇦🇫", "ALL": "🇦🇱", "AMD": "🇦🇲", "ANG": "🇳🇱",
        "AOA": "🇦🇴", "ARS": "🇦🇷", "AUD": "🇦🇺", "AWG": "🇦🇼", "AZN": "🇦🇿",
        "BAM": "🇧🇦", "BBD": "🇧🇧", "BDT": "🇧🇩", "BGN": "🇧🇬", "BHD": "🇧🇭",
        "BIF": "🇧🇮", "BMD": "🇧🇲", "BND": "🇧🇳", "BOB": "🇧🇴", "BRL": "🇧🇷",
        "BSD": "🇧🇸", "BTN": "🇧🇹", "BWP": "🇧🇼", "BYN": "🇧🇾", "BZD": "🇧🇿",
        "CAD": "🇨🇦", "CDF": "🇨🇩", "CHF": "🇨🇭", "CLP": "🇨🇱", "CNY": "🇨🇳",
        "COP": "🇨🇴", "CRC": "🇨🇷", "CUP": "🇨🇺", "CVE": "🇨🇻", "CZK": "🇨🇿",
        "DJF": "🇩🇯", "DKK": "🇩🇰", "DOP": "🇩🇴", "DZD": "🇩🇿", "EGP": "🇪🇬",
        "ERN": "🇪🇷", "ETB": "🇪🇹", "EUR": "🇪🇺", "FJD": "🇫🇯", "FKP": "🇫🇰",
        "FOK": "🇫🇴", "GBP": "🇬🇧", "GEL": "🇬🇪", "GGP": "🇬🇬", "GHS": "🇬🇭",
        "GIP": "🇬🇮", "GMD": "🇬🇲", "GNF": "🇬🇳", "GTQ": "🇬🇹", "GYD": "🇬🇾",
        "HKD": "🇭🇰", "HNL": "🇭🇳", "HRK": "🇭🇷", "HTG": "🇭🇹", "HUF": "🇭🇺",
        "IDR": "🇮🇩", "ILS": "🇮🇱", "IMP": "🇮🇲", "INR": "🇮🇳", "IQD": "🇮🇶",
        "IRR": "🇮🇷", "ISK": "🇮🇸", "JEP": "🇯🇪", "JMD": "🇯🇲", "JOD": "🇯🇴",
        "JPY": "🇯🇵", "KES": "🇰🇪", "KGS": "🇰🇬", "KHR": "🇰🇭", "KID": "🇰🇮",
        "KMF": "🇰🇲", "KRW": "🇰🇷", "KWD": "🇰🇼", "KYD": "🇰🇾", "KZT": "🇰🇿",
        "LAK": "🇱🇦", "LBP": "🇱🇧", "LKR": "🇱🇰", "LRD": "🇱🇷", "LSL": "🇱🇸",
        "LYD": "🇱🇾", "MAD": "🇲🇦", "MDL": "🇲🇩", "MGA": "🇲🇬", "MKD": "🇲🇰",
        "MMK": "🇲🇲", "MNT": "🇲🇳", "MOP": "🇲🇴", "MRU": "🇲🇷", "MUR": "🇲🇺",
        "MVR": "🇲🇻", "MWK": "🇲🇼", "MXN": "🇲🇽", "MYR": "🇲🇾", "MZN": "🇲🇿",
        "NAD": "🇳🇦", "NGN": "🇳🇬", "NIO": "🇳🇮", "NOK": "🇳🇴", "NPR": "🇳🇵",
        "NZD": "🇳🇿", "OMR": "🇴🇲", "PAB": "🇵🇦", "PEN": "🇵🇪", "PGK": "🇵🇬",
        "PHP": "🇵🇭", "PKR": "🇵🇰", "PLN": "🇵🇱", "PYG": "🇵🇾", "QAR": "🇶🇦",
        "RON": "🇷🇴", "RSD": "🇷🇸", "RUB": "🇷🇺", "RWF": "🇷🇼", "SAR": "🇸🇦",
        "SBD": "🇸🇧", "SCR": "🇸🇨", "SDG": "🇸🇩", "SEK": "🇸🇪", "SGD": "🇸🇬",
        "SHP": "🇸🇭", "SLE": "🇸🇱", "SLL": "🇸🇱", "SOS": "🇸🇴", "SRD": "🇸🇷",
        "SSP": "🇸🇸", "STN": "🇸🇹", "SYP": "🇸🇾", "SZL": "🇸🇿", "THB": "🇹🇭",
        "TJS": "🇹🇯", "TMT": "🇹🇲", "TND": "🇹🇳", "TOP": "🇹🇴", "TRY": "🇹🇷",
        "TTD": "🇹🇹", "TVD": "🇹🇻", "TWD": "🇹🇼", "TZS": "🇹🇿", "UAH": "🇺🇦",
        "UGX": "🇺🇬", "USD": "🇺🇸", "UYU": "🇺🇾", "UZS": "🇺🇿", "VES": "🇻🇪",
        "VND": "🇻🇳", "VUV": "🇻🇺", "WST": "🇼🇸", "XAF": "🌍", "XCD": "🏝️",
        "XCG": "🏝️", "XDR": "🏛️", "XOF": "🌍", "XPF": "🏝️", "YER": "🇾🇪",
        "ZAR": "🇿🇦", "ZMW": "🇿🇲", "ZWL": "🇿🇼"
    }
    return flags.get(currency_code, "💱")

def get_currency_trend(currency_code, current_rate):
    """
    Generate trend based on previous rate comparison
    """
    global previous_rates
    
    # Jika USD, selalu stable
    if currency_code == "USD":
        return "➡️"
    
    # Jika tidak ada data sebelumnya, generate berdasarkan karakteristik mata uang
    if currency_code not in previous_rates:
        # Mata uang volatile cenderung berfluktuasi lebih banyak
        volatile_currencies = ["TRY", "ARS", "VES", "IRR", "LBP", "SYP", "ZWL", "SSP"]
        stable_currencies = ["EUR", "GBP", "CHF", "JPY", "SGD", "HKD", "SAR", "AED"]
        
        if currency_code in volatile_currencies:
            # Mata uang volatile: 60% turun, 30% naik, 10% stabil
            trend = random.choices(["📉", "📈", "➡️"], weights=[0.6, 0.3, 0.1])[0]
        elif currency_code in stable_currencies:
            # Mata uang stabil: 30% turun, 30% naik, 40% stabil
            trend = random.choices(["📉", "📈", "➡️"], weights=[0.3, 0.3, 0.4])[0]
        else:
            # Mata uang normal: 40% turun, 40% naik, 20% stabil
            trend = random.choices(["📉", "📈", "➡️"], weights=[0.4, 0.4, 0.2])[0]
        
        # Simpan rate untuk perbandingan berikutnya
        previous_rates[currency_code] = current_rate
        return trend
    
    # Bandingkan dengan rate sebelumnya
    previous_rate = previous_rates[currency_code]
    change_percent = ((current_rate - previous_rate) / previous_rate) * 100
    
    # Update rate
    previous_rates[currency_code] = current_rate
    
    # Tentukan trend berdasarkan perubahan
    if change_percent > 0.5:  # Naik > 0.5%
        return "📈"
    elif change_percent < -0.5:  # Turun > 0.5%
        return "📉"
    else:  # Perubahan kecil atau stabil
        return "➡️"

def format_rate_display(rate, currency_code):
    """
    Format rate untuk display yang lebih baik
    """
    if currency_code == 'USD':
        return "1.0000 (Base)"
    
    if rate >= 1000:
        return f"{rate:,.0f}"
    elif rate >= 100:
        return f"{rate:.2f}"
    elif rate >= 10:
        return f"{rate:.3f}"
    else:
        return f"{rate:.4f}"

def get_all_currencies_content():
    """
    Generate content for all currencies page
    """
    current_time = datetime.now().strftime("%B %d, %Y at %H:%M")
    
    # Generate currency data untuk SEMUA mata uang yang didukung
    currency_data = []
    for code, name in SUPPORTED_CURRENCIES:
        rate = get_mock_exchange_rate(code)
        flag = get_currency_flag(code)
        trend = get_currency_trend(code, rate)
        
        currency_data.append({
            'code': code,
            'name': name,
            'rate': rate,
            'flag': flag,
            'trend': trend
        })
    
    # Sort by currency code
    currency_data.sort(key=lambda x: x['code'])
    
    # Generate currency cards HTML untuk SEMUA mata uang
    currency_cards = ""
    for currency in currency_data:
        rate_display = format_rate_display(currency['rate'], currency['code'])
        trend_text = "Base Currency" if currency['code'] == 'USD' else "vs USD"
        
        # Tambahkan kelas khusus untuk USD
        card_class = "currency-card"
        if currency['code'] == 'USD':
            card_class += " base-currency"
        
        # Tambahkan kelas untuk trend
        trend_class = ""
        if currency['trend'] == "📈":
            trend_class = "trend-up"
        elif currency['trend'] == "📉":
            trend_class = "trend-down"
        else:
            trend_class = "trend-stable"
        
        currency_cards += f'''
        <div class="{card_class} {trend_class}" data-currency="{currency['code']}">
            <div class="currency-header">
                <div class="currency-flag">{currency['flag']}</div>
                <div class="currency-info">
                    <div class="currency-code">{currency['code']}</div>
                    <div class="currency-name">{currency['name']}</div>
                </div>
                <div class="currency-trend">{currency['trend']}</div>
            </div>
            <div class="currency-rate">
                <div class="rate-value">{rate_display}</div>
                <div class="rate-label">{trend_text}</div>
            </div>
        </div>
        '''
    
    content = f'''
    <div class="currencies-container">
        <style>
            .currencies-container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }}
            
            .currencies-header {{
                text-align: center;
                padding: 30px 0;
                background: linear-gradient(135deg, rgba(233, 69, 96, 0.1) 0%, rgba(15, 52, 96, 0.2) 100%);
                border-radius: 15px;
                margin-bottom: 30px;
                position: relative;
                overflow: hidden;
            }}
            
            .currencies-header::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: radial-gradient(circle, rgba(233, 69, 96, 0.03) 0%, transparent 70%);
                animation: pulse 4s ease-in-out infinite;
            }}
            
            @keyframes pulse {{
                0%, 100% {{ transform: scale(1); }}
                50% {{ transform: scale(1.05); }}
            }}
            
            .currencies-title {{
                font-size: 32px;
                color: #e94560;
                font-weight: bold;
                margin-bottom: 10px;
                position: relative;
                z-index: 1;
            }}
            
            .currencies-subtitle {{
                color: #ccc;
                font-size: 16px;
                position: relative;
                z-index: 1;
            }}
            
            .search-container {{
                margin-bottom: 30px;
                text-align: center;
            }}
            
            .search-box {{
                background: rgba(22, 33, 62, 0.8);
                border: 2px solid rgba(233, 69, 96, 0.3);
                border-radius: 25px;
                padding: 12px 20px;
                color: white;
                font-size: 16px;
                width: 100%;
                max-width: 400px;
                outline: none;
                transition: all 0.3s ease;
            }}
            
            .search-box:focus {{
                border-color: #e94560;
                box-shadow: 0 0 20px rgba(233, 69, 96, 0.3);
            }}
            
            .search-box::placeholder {{
                color: #888;
            }}
            
            .stats-bar {{
                display: flex;
                justify-content: space-around;
                background: rgba(15, 52, 96, 0.3);
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 30px;
                text-align: center;
            }}
            
            .stat-item {{
                color: #ccc;
            }}
            
            .stat-number {{
                font-size: 24px;
                font-weight: bold;
                color: #e94560;
                display: block;
            }}
            
            .stat-label {{
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-top: 5px;
            }}
            
            .currencies-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 40px;
            }}
            
            .currency-card {{
                background: linear-gradient(145deg, rgba(22, 33, 62, 0.6) 0%, rgba(15, 52, 96, 0.4) 100%);
                border: 1px solid rgba(233, 69, 96, 0.2);
                border-radius: 15px;
                padding: 20px;
                transition: all 0.3s ease;
                cursor: pointer;
                position: relative;
                overflow: hidden;
            }}
            
            .currency-card.base-currency {{
                background: linear-gradient(145deg, rgba(233, 69, 96, 0.2) 0%, rgba(15, 52, 96, 0.4) 100%);
                border: 2px solid rgba(233, 69, 96, 0.5);
            }}
            
            .currency-card.trend-up {{
                border-left: 4px solid #00ff88;
            }}
            
            .currency-card.trend-down {{
                border-left: 4px solid #ff4757;
            }}
            
            .currency-card.trend-stable {{
                border-left: 4px solid #ffa502;
            }}
            
            .currency-card::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(233, 69, 96, 0.1), transparent);
                transition: left 0.6s;
            }}
            
            .currency-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 15px 35px rgba(233, 69, 96, 0.2);
                border-color: #e94560;
            }}
            
            .currency-card:hover::before {{
                left: 100%;
            }}
            
            .currency-header {{
                display: flex;
                align-items: center;
                margin-bottom: 15px;
                position: relative;
                z-index: 1;
            }}
            
            .currency-flag {{
                font-size: 32px;
                margin-right: 15px;
            }}
            
            .currency-info {{
                flex: 1;
            }}
            
            .currency-code {{
                font-size: 18px;
                font-weight: bold;
                color: #e94560;
                margin-bottom: 2px;
            }}
            
            .currency-name {{
                font-size: 14px;
                color: #ccc;
                line-height: 1.3;
            }}
            
            .currency-trend {{
                font-size: 24px;
                animation: pulse-trend 2s ease-in-out infinite;
            }}
            
            @keyframes pulse-trend {{
                0%, 100% {{ transform: scale(1); }}
                50% {{ transform: scale(1.1); }}
            }}
            
            .currency-rate {{
                text-align: center;
                padding-top: 15px;
                border-top: 1px solid rgba(233, 69, 96, 0.2);
                position: relative;
                z-index: 1;
            }}
            
            .rate-value {{
                font-size: 20px;
                font-weight: bold;
                color: white;
                margin-bottom: 5px;
            }}
            
            .rate-label {{
                font-size: 12px;
                color: #888;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            
            .last-updated {{
                text-align: center;
                color: #888;
                font-size: 14px;
                padding: 20px;
                background: rgba(15, 52, 96, 0.2);
                border-radius: 10px;
                border-left: 4px solid #e94560;
            }}
            
            .no-results {{
                text-align: center;
                padding: 40px;
                color: #888;
                font-size: 16px;
                display: none;
            }}
            
            .trend-legend {{
                display: flex;
                justify-content: center;
                gap: 30px;
                margin-bottom: 20px;
                padding: 15px;
                background: rgba(15, 52, 96, 0.2);
                border-radius: 10px;
                font-size: 14px;
            }}
            
            .trend-item {{
                display: flex;
                align-items: center;
                gap: 8px;
                color: #ccc;
            }}
            
            .trend-emoji {{
                font-size: 18px;
            }}
            
            @media (max-width: 768px) {{
                .currencies-container {{ padding: 10px; }}
                .currencies-title {{ font-size: 24px; }}
                .currencies-grid {{ 
                    grid-template-columns: 1fr; 
                    gap: 15px;
                }}
                .stats-bar {{ 
                    flex-direction: column; 
                    gap: 15px; 
                }}
                .trend-legend {{
                    flex-direction: column;
                    gap: 10px;
                }}
                .search-box {{ width: 90%; }}
                .currency-card {{ padding: 15px; }}
            }}
        </style>
        
        <!-- Header Section -->
        <div class="currencies-header">
            <h1 class="currencies-title">🌍 All Currencies</h1>
            <p class="currencies-subtitle">Real-time exchange rates for all {len(SUPPORTED_CURRENCIES)} supported currencies</p>
        </div>
        
        <!-- Search Box -->
        <div class="search-container">
            <input type="text" class="search-box" placeholder="🔍 Search currencies by code or name..." id="currencySearch">
        </div>
        
        <!-- Trend Legend -->
        <div class="trend-legend">
            <div class="trend-item">
                <span class="trend-emoji">📈</span>
                <span>Rising</span>
            </div>
            <div class="trend-item">
                <span class="trend-emoji">📉</span>
                <span>Falling</span>
            </div>
            <div class="trend-item">
                <span class="trend-emoji">➡️</span>
                <span>Stable</span>
            </div>
        </div>
        
        <!-- Stats Bar -->
        <div class="stats-bar">
            <div class="stat-item">
                <span class="stat-number">{len(SUPPORTED_CURRENCIES)}</span>
                <div class="stat-label">Total Currencies</div>
            </div>
            <div class="stat-item">
                <span class="stat-number" id="visibleCount">{len(SUPPORTED_CURRENCIES)}</span>
                <div class="stat-label">Showing</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">Live</span>
                <div class="stat-label">Updates</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">24/7</span>
                <div class="stat-label">Available</div>
            </div>
        </div>
        
        <!-- Currencies Grid -->
        <div class="currencies-grid" id="currenciesGrid">
            {currency_cards}
        </div>
        
        <!-- No Results Message -->
        <div class="no-results" id="noResults">
            <h3>🔍 No currencies found</h3>
            <p>Try adjusting your search terms or clear the search box to see all currencies</p>
            <button onclick="clearSearch()" style="
                background: #e94560; 
                color: white; 
                border: none; 
                padding: 8px 16px; 
                border-radius: 5px; 
                cursor: pointer; 
                margin-top: 10px;
            ">Clear Search</button>
        </div>
        
        <!-- Last Updated -->
        <div class="last-updated">
            📅 Last updated: {current_time} • Rates refresh automatically • Total currencies: {len(SUPPORTED_CURRENCIES)}
        </div>
    </div>
    
    <script>
        // Search functionality
        document.getElementById('currencySearch').addEventListener('input', function(e) {{
            const searchTerm = e.target.value.toLowerCase();
            const currencyCards = document.querySelectorAll('.currency-card');
            const noResults = document.getElementById('noResults');
            const visibleCount = document.getElementById('visibleCount');
            let visible = 0;
            
            currencyCards.forEach(card => {{
                const currencyCode = card.dataset.currency.toLowerCase();
                const currencyName = card.querySelector('.currency-name').textContent.toLowerCase();
                
                if (currencyCode.includes(searchTerm) || currencyName.includes(searchTerm)) {{
                    card.style.display = 'block';
                    visible++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});
            
            // Update visible count
            visibleCount.textContent = visible;
            
            // Show/hide no results message
            if (visible === 0 && searchTerm !== '') {{
                noResults.style.display = 'block';
            }} else {{
                noResults.style.display = 'none';
            }}
        }});
        
        // Clear search function
        function clearSearch() {{
            document.getElementById('currencySearch').value = '';
            document.getElementById('currencySearch').dispatchEvent(new Event('input'));
        }}
        
        // Filter by trend
        function filterByTrend(trendType) {{
            const currencyCards = document.querySelectorAll('.currency-card');
            const visibleCount = document.getElementById('visibleCount');
            let visible = 0;
            
            currencyCards.forEach(card => {{
                const trend = card.querySelector('.currency-trend').textContent;
                let shouldShow = false;
                
                switch(trendType) {{
                    case 'up':
                        shouldShow = trend === '📈';
                        break;
                    case 'down':
                        shouldShow = trend === '📉';
                        break;
                    case 'stable':
                        shouldShow = trend === '➡️';
                        break;
                    case 'all':
                    default:
                        shouldShow = true;
                        break;
                }}
                
                if (shouldShow) {{
                    card.style.display = 'block';
                    visible++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});
            
            visibleCount.textContent = visible;
        }}
        
        // Add click functionality to currency cards
        document.querySelectorAll('.currency-card').forEach(card => {{
            card.addEventListener('click', function() {{
                const currencyCode = this.dataset.currency;
                const currencyName = this.querySelector('.currency-name').textContent;
                const trend = this.querySelector('.currency-trend').textContent;
                
                // Highlight clicked card temporarily
                this.style.transform = 'scale(0.95)';
                setTimeout(() => {{
                    this.style.transform = '';
                }}, 150);
                
                console.log('Selected currency:', currencyCode, '-', currencyName, 'Trend:', trend);
            }});
        }});
        
        // Add keyboard navigation
        document.getElementById('currencySearch').addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                clearSearch();
            }}
        }});
        
        // Add trend legend click handlers
        document.querySelectorAll('.trend-item').forEach(item => {{
            item.style.cursor = 'pointer';
            item.addEventListener('click', function() {{
                const emoji = this.querySelector('.trend-emoji').textContent;
                let trendType = 'all';
                
                switch(emoji) {{
                    case '📈':
                        trendType = 'up';
                        break;
                    case '📉':
                        trendType = 'down';
                        break;
                    case '➡️':
                        trendType = 'stable';
                        break;
                }}
                
                filterByTrend(trendType);
                
                // Visual feedback
                document.querySelectorAll('.trend-item').forEach(t => t.style.opacity = '0.6');
                this.style.opacity = '1';
                
                setTimeout(() => {{
                    document.querySelectorAll('.trend-item').forEach(t => t.style.opacity = '1');
                }}, 2000);
            }});
        }});
        
        console.log('All currencies loaded: {len(SUPPORTED_CURRENCIES)} currencies displayed');
    </script>
    '''
    
    return content

def get_supported_currencies_list():
    """
    Return list of supported currencies for other modules
    """
    return SUPPORTED_CURRENCIES