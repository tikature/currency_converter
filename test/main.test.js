/**
 * @jest-environment node
 */

// Fungsi tiruan dari getConversionRate untuk keperluan tes
async function getConversionRate(from, to) {
    const mockRates = {
        "USD_EUR": 0.9,
        "USD_IDR": 15000,
        "IDR_USD": 0.000066,
        "USD_USD": 1,
    };

    if (from === to) return 1;

    const key = `${from}_${to}`;
    if (mockRates[key]) return mockRates[key];
    throw new Error("Unsupported currency pair");
}

// Fungsi konversi
async function convertCurrency(amount, from, to) {
    if (amount <= 0) throw new Error("Amount must be greater than 0");
    const rate = await getConversionRate(from, to);
    return amount * rate;
}

// TEST CASES
test("Convert 100 USD to EUR", async () => {
    const result = await convertCurrency(100, "USD", "EUR");
    expect(result).toBeCloseTo(90);
});

test("Convert 100 USD to IDR", async () => {
    const result = await convertCurrency(100, "USD", "IDR");
    expect(result).toBe(1500000);
});

test("Convert 0 should throw error", async () => {
    await expect(convertCurrency(0, "USD", "IDR")).rejects.toThrow("Amount must be greater than 0");
});

test("Convert with same currency should return same amount", async () => {
    const result = await convertCurrency(100, "USD", "USD");
    expect(result).toBe(100);
});

test("Unsupported currency pair should throw error", async () => {
    await expect(convertCurrency(100, "EUR", "BTC")).rejects.toThrow("Unsupported currency pair");
});
