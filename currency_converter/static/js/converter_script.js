const API_KEY = "99af1e52e8b504f480478eda";
const BASE_URL = `https://v6.exchangerate-api.com/v6/${API_KEY}`;

const DEFAULT_AMOUNT = 500000;

const QUICK_CONVERSIONS = {
    "1": { desc: "USD to EUR", from: "USD", to: "EUR" },
    "2": { desc: "USD to IDR", from: "USD", to: "IDR" },
    "3": { desc: "USD to JPY", from: "USD", to: "JPY" },
    "4": { desc: "IDR to USD", from: "IDR", to: "USD" },
    "5": { desc: "EUR to USD", from: "EUR", to: "USD" },
    "6": { desc: "Show all from IDR", from: "IDR", to: null },
};


async function populateCurrencyOptions() {
    try {
        const response = await fetch(`${BASE_URL}/codes`);
        const data = await response.json();
        if (data.result !== "success") throw new Error("API failed");

        const options = data.supported_codes.map(
            ([code, name]) => `<option value="${code}">${code} - ${name}</option>`
        ).join("");

        document.getElementById('from-currency').innerHTML = options;
        document.getElementById('to-currency').innerHTML = options;

        populateQuickMenu(data.supported_codes.slice(0, 6)); // First 6 pairs
    } catch (error) {
        showError("Failed to load currency list.");
        console.error(error);
    }
}

function populateQuickMenu() {
    const menu = document.getElementById("quick-menu");
    let html = "";

    Object.entries(QUICK_CONVERSIONS).forEach(([id, { desc, from, to }]) => {
        html += `
            <div class="quick-option" onclick="${to ? `quickConvert('${from}', '${to}')` : `showAllFromIDR()`}">
                <h4>${desc}</h4>
                <p>${from}${to ? ` to ${to}` : ' to all currencies'}</p>
            </div>
            `;
    });

    menu.innerHTML = html;
}


async function convertCurrency() {
    const amount = parseFloat(document.getElementById("amount").value);
    const from = document.getElementById("from-currency").value;
    const to = document.getElementById("to-currency").value;
    const showAll = document.getElementById("show-all").checked;

    if (!amount || amount <= 0) return showError("Enter valid amount");

    showLoading();

    try {
        if (showAll) {
            await showAllConversionsAPI(amount, from);
        } else {
            const result = await getConversionRate(from, to);
            showSingleResult(amount, from, to, amount * result);
        }
    } catch (e) {
        showError(e.message);
    }

    hideLoading();
}

async function quickConvert(from, to) {
    const amount = parseFloat(document.getElementById("quick-amount").value || DEFAULT_AMOUNT);
    showLoading();

    try {
        const rate = await getConversionRate(from, to);
        showSingleResult(amount, from, to, amount * rate);
    } catch (e) {
        showError(e.message);
    }

    hideLoading();
}

function showAllFromIDR() {
    const amount = parseFloat(document.getElementById("quick-amount").value || DEFAULT_AMOUNT);
    showLoading();

    showAllConversionsAPI(amount, "IDR", ["USD", "EUR", "JPY"])
        .then(() => hideLoading())
        .catch(error => {
            showError("Conversion failed: " + error.message);
            hideLoading();
        });
}


async function showAllConversionsAPI(amount, from, targetCurrencies = null) {
    const response = await fetch(`${BASE_URL}/latest/${from}`);
    const data = await response.json();

    if (data.result !== "success") {
        throw new Error("Failed to fetch conversion data.");
    }

    const rates = data.conversion_rates;

    const html = Object.entries(rates)
        .filter(([code]) => {
            if (code === from) return false;
            return targetCurrencies ? targetCurrencies.includes(code) : true;
        })
        .map(([code, rate]) => `
            <div class="result-item">
                <span class="currency-code">${code}</span>
                <span class="currency-value">${(rate * amount).toLocaleString(undefined, { maximumFractionDigits: 2 })}</span>
            </div>
            `).join("");

    document.getElementById("result-title").textContent =
        targetCurrencies ? `${amount} ${from} to selected currencies` : `${amount} ${from} to all currencies`;

    document.getElementById("result-content").innerHTML = html;
    showResults();
    hideError();

    // Tambahkan di akhir showAllConversionsAPI
    fetch("/save-history", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: "multiple",
            amount: amount,
            from: from,
            to: targetCurrencies || "ALL",
            result: "multiple"
        })
    }).catch(err => console.error("Failed to save history:", err));

}


async function getConversionRate(from, to) {
    if (from === to) return 1;
    const response = await fetch(`${BASE_URL}/pair/${from}/${to}`);
    const data = await response.json();
    if (data.result !== "success") throw new Error(`Cannot convert ${from} to ${to}`);
    return data.conversion_rate;
}


function showSingleResult(amount, from, to, result) {
    document.getElementById("result-title").textContent = "Conversion Result";
    document.getElementById("result-content").innerHTML = `
    <div class="result-item">
        <span class="currency-code">${amount} ${from}</span>
        <span class="currency-value">${result.toLocaleString(undefined, { maximumFractionDigits: 2 })} ${to}</span>
    </div>`;
    showResults();


    fetch("/save-history", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            type: "single",
            amount: amount,
            from: from,
            to: to,
            result: result
        })
    }).catch(err => console.error("Failed to save history:", err));
}

function switchMode(mode) {
    document.querySelectorAll('.mode-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    document.querySelectorAll('.mode-content').forEach(content => content.classList.remove('active'));
    document.getElementById(mode + "-mode").classList.add("active");

    hideResults();
}

function showError(message) {
    const el = document.getElementById("error-message");
    el.textContent = message;
    el.classList.add("show");
    hideResults();
}

function showLoading() {
    document.getElementById("loading").classList.add("show");
    hideError();
}

function hideLoading() {
    document.getElementById("loading").classList.remove("show");
}

function hideError() {
    document.getElementById("error-message").classList.remove("show");
}

function showResults() {
    document.getElementById("result-section").classList.add("show");
}

function hideResults() {
    document.getElementById("result-section").classList.remove("show");
}


document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("amount").value = DEFAULT_AMOUNT;
    populateCurrencyOptions(); // Memuat <select>
    populateQuickMenu();       // Memuat Quick Menu khusus
});
