function showTab(tabName) {
    // Hide all tab contents
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(content => content.classList.remove('active'));

    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));

    // Show selected tab content
    document.getElementById(tabName).classList.add('active');

    // Add active class to clicked button
    event.target.classList.add('active');
}

function clearHistory() {
    if (confirm('Are you sure you want to clear all conversion history? This action cannot be undone.')) {
        fetch('/clear-history', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Failed to clear history. Please try again.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while clearing history.');
            });
    }
}

function showRateDetails(index, timestamp, rate, convertedAmount, change, changePercent, trend, fromCurrency, toCurrency, amount) {
    // Format timestamp for display
    let formattedTimestamp;
    try {
        const date = new Date(timestamp);
        formattedTimestamp = date.toLocaleString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    } catch (e) {
        formattedTimestamp = timestamp;
    }

    // Update modal content
    document.getElementById('detail-timestamp').textContent = formattedTimestamp;
    document.getElementById('detail-rate').textContent = `1 ${fromCurrency} = ${rate.toFixed(6)} ${toCurrency}`;
    document.getElementById('detail-conversion').textContent = `${amount} ${fromCurrency} = ${convertedAmount.toFixed(2)} ${toCurrency}`;

    // Update change information with color
    const changeElement = document.getElementById('detail-change');
    const trendIcon = document.getElementById('detail-trend-icon');

    if (trend === 'up') {
        changeElement.innerHTML = `<span style="color: #4CAF50;">+${change.toFixed(6)} (+${changePercent.toFixed(2)}%)</span>`;
        trendIcon.textContent = '📈';
    } else if (trend === 'down') {
        changeElement.innerHTML = `<span style="color: #f44336;">${change.toFixed(6)} (${changePercent.toFixed(2)}%)</span>`;
        trendIcon.textContent = '📉';
    } else {
        changeElement.innerHTML = `<span style="color: #ccc;">No change (0.00%)</span>`;
        trendIcon.textContent = '➡️';
    }

    // Generate rate analysis
    const rateAnalysis = generateRateAnalysis(rate, change, changePercent, trend);
    document.getElementById('rate-analysis').textContent = rateAnalysis;

    // Generate market insights
    const marketInsights = generateMarketInsights(fromCurrency, toCurrency, trend, changePercent);
    document.getElementById('market-insights').textContent = marketInsights;

    // Show modal
    document.getElementById('rateModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('rateModal').style.display = 'none';
}

function generateRateAnalysis(rate, change, changePercent, trend) {
    if (trend === 'up') {
        if (Math.abs(changePercent) > 2) {
            return `Strong upward movement detected. The exchange rate has increased significantly by ${Math.abs(changePercent).toFixed(2)}%, indicating positive market momentum.`;
        } else if (Math.abs(changePercent) > 0.5) {
            return `Moderate upward trend observed. The rate shows steady growth of ${Math.abs(changePercent).toFixed(2)}%, suggesting stable market conditions.`;
        } else {
            return `Slight upward movement. The rate has increased marginally by ${Math.abs(changePercent).toFixed(2)}%, indicating minor market fluctuations.`;
        }
    } else if (trend === 'down') {
        if (Math.abs(changePercent) > 2) {
            return `Significant downward movement detected. The exchange rate has decreased by ${Math.abs(changePercent).toFixed(2)}%, suggesting market volatility or negative sentiment.`;
        } else if (Math.abs(changePercent) > 0.5) {
            return `Moderate downward trend observed. The rate shows a decline of ${Math.abs(changePercent).toFixed(2)}%, indicating some market pressure.`;
        } else {
            return `Slight downward movement. The rate has decreased marginally by ${Math.abs(changePercent).toFixed(2)}%, showing minor market adjustments.`;
        }
    } else {
        return `Stable exchange rate with no significant movement. This indicates a balanced market with minimal volatility during this period.`;
    }
}

function generateMarketInsights(fromCurrency, toCurrency, trend, changePercent) {
    const insights = [
        `Exchange rates between ${fromCurrency} and ${toCurrency} are influenced by various economic factors including interest rates, inflation, and political stability.`,
        `Currency fluctuations are normal and reflect the dynamic nature of global financial markets and economic conditions.`,
        `For international transactions, consider the timing of your exchanges to optimize value based on current market trends.`,
        `Historical rate data can help identify patterns, but past performance doesn't guarantee future movements.`,
        `Economic events, central bank policies, and geopolitical developments can significantly impact exchange rates.`
    ];

    // Add trend-specific insight
    if (Math.abs(changePercent) > 1) {
        if (trend === 'up') {
            insights.unshift(`The current upward trend suggests ${fromCurrency} is strengthening against ${toCurrency}. This could be favorable for ${fromCurrency} holders looking to exchange.`);
        } else if (trend === 'down') {
            insights.unshift(`The current downward trend indicates ${fromCurrency} is weakening against ${toCurrency}. Consider market timing for optimal exchange rates.`);
        }
    }

    // Return a random insight
    return insights[Math.floor(Math.random() * insights.length)];
}

// Close modal when clicking outside of it
window.onclick = function (event) {
    const modal = document.getElementById('rateModal');
    if (event.target === modal) {
        closeModal();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});