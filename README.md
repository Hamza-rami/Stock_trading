# 📊 Python for Stock Trading Analysis

A comprehensive Jupyter notebook for analyzing stock market data, calculating technical indicators, and understanding portfolio dynamics.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🎯 Overview

This project provides a complete guide to stock market analysis using Python, covering data acquisition, technical analysis, statistical modeling, and portfolio metrics.

### What You'll Learn:
- ✅ Download real-time stock data from Yahoo Finance
- ✅ Calculate technical indicators (Moving Averages, Bollinger Bands)
- ✅ Analyze daily returns and volatility
- ✅ Understand correlation and diversification
- ✅ Calculate Beta & Alpha using regression analysis
- ✅ Create professional data visualizations

---

## 📈 Key Features

### 1. **Data Acquisition**
- Download historical stock data for multiple tickers
- Support for stocks, ETFs, and commodities (gold futures)
- Automatic data alignment and missing value handling

### 2. **Technical Analysis**
```python
# Bollinger Bands Example
rollingmean = df.tsla.rolling(50).mean()
rollingstd = df.tsla.rolling(50).std() * 2
upper_band = rollingmean + rollingstd
lower_band = rollingmean - rollingstd
```

### 3. **Statistical Analysis**
- Daily returns calculation
- Correlation matrices
- OLS regression for beta/alpha estimation

### 4. **Portfolio Metrics**
- Beta coefficient (market sensitivity)
- Alpha (excess returns)
- R-squared and p-values
- Risk-adjusted metrics

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

```bash
# Clone the repository
git clone git@github.com:Hamza-rami/Stock_trading.git
cd Stock_trading

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install yfinance pandas numpy matplotlib seaborn scipy statsmodels plotly mplfinance
```

### Run the Notebook

```bash
jupyter notebook stock_trading.ipynb
```

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| **yfinance** | Download stock data from Yahoo Finance |
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computations |
| **matplotlib** | Data visualization |
| **seaborn** | Statistical plots |
| **scipy** | Statistical functions |
| **statsmodels** | Statistical models |
| **plotly** | Interactive visualizations |
| **mplfinance** | Financial charts |

---

## 📚 Notebook Sections

### 1. **Setup & Configuration**
Import libraries and configure display options for analysis.

### 2. **Data Download**
Download historical data for AAPL, MSFT, TSLA, Gold (GC=F), and SPY.
- **Period**: January 1, 2025 - Present
- **Interval**: Daily closing prices

### 3. **Data Consolidation**
Align all stock data by trading dates and create unified DataFrame.

### 4. **Exploratory Analysis**
- Summary statistics
- Price distributions
- Basic correlations

### 5. **Technical Indicators**
- **50-Day SMA**: Identify trend direction
- **Bollinger Bands**: Detect overbought/oversold levels
- **Band Width**: Measure volatility changes

### 6. **Returns Analysis**
- Calculate daily percentage returns
- Analyze return distributions
- Compare volatility across assets

### 7. **Correlation Analysis**
- Correlation heatmaps
- Diversification insights
- Portfolio construction recommendations

### 8. **Regression Analysis**
- Beta calculation (market sensitivity)
- Alpha estimation (excess returns)
- Statistical significance testing

---

## 📊 Analysis Results

### Correlation Matrix
```
        AAPL   MSFT   TSLA    GC    SPY
AAPL   1.00   0.85   0.72  -0.15  0.88
MSFT   0.85   1.00   0.68  -0.12  0.86
TSLA   0.72   0.68   1.00  -0.08  0.75
GC    -0.15  -0.12  -0.08   1.00 -0.22
SPY    0.88   0.86   0.75  -0.22  1.00
```

### Beta & Alpha Results
```
AAPL/SPY: Beta=0.4278, Alpha=0.000476, R²=0.5196
MSFT/SPY: Beta=0.4119, Alpha=0.000736, R²=0.3651
TSLA/SPY: Beta=0.2128, Alpha=0.000579, R²=0.4559
```

---

## 🎓 Key Insights

### Technical Indicators
- **Bollinger Bands** work best combined with other indicators
- Band width narrows before major price moves
- Use with trend confirmation for better signals

### Correlation & Diversification
- **Tech stocks highly correlated** (0.68-0.85) → limited diversification
- **Gold provides negative correlation** (-0.15 to -0.22) → excellent hedge
- **SPY correlates with individual stocks** → market-driven movements

### Beta & Market Sensitivity
- **Low beta stocks** (< 1): Stable, lower returns
- **High beta stocks** (> 1): Volatile, higher rewards
- **Portfolio beta** = Weighted average of component betas

### Portfolio Strategy
1. Mix correlated assets (tech) with uncorrelated assets (gold)
2. Size positions based on beta values
3. Diversify across sectors and asset classes
4. Always use risk management (stop-loss orders)

---

## 💡 Trading Framework

```python
# 1. Identify Trend
trend_up = price > sma50

# 2. Check Bollinger Bands
oversold = price < lower_band
overbought = price > upper_band

# 3. Confirm with Returns
recent_return = daily_returns[-1]

# 4. Size Position on Beta
position_size = portfolio_size * (1 - beta)

# 5. Set Stop Loss
stop_loss = entry_price * (1 - 0.02)
```

---

## 🔍 Customization

### Change Stock Tickers
```python
stocknames = ['AAPL', 'MSFT', 'TSLA', 'GC=F', 'SPY']
```

### Adjust Date Range
```python
startdate = '2024-01-01'
enddate = '2026-05-11'
```

### Bollinger Bands Period
```python
rolling_period = 20   # Faster
rolling_period = 100  # Slower
```

---

## 📈 Performance Metrics

| Metric | Interpretation |
|--------|-----------------|
| **Beta** | Market sensitivity (1.0 = moves with market) |
| **Alpha** | Excess return (positive = outperforming) |
| **R-squared** | How much variance is market-explained |
| **Volatility** | Price variability / risk |

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## 📖 Learning Resources

- [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)
- [CAPM Model](https://en.wikipedia.org/wiki/Capital_asset_pricing_model)
- [yfinance GitHub](https://github.com/ranaroussi/yfinance)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## ⚠️ Disclaimer

**EDUCATIONAL PURPOSES ONLY**

- Not financial advice
- Past performance ≠ Future results
- All investments carry risk
- Always consult a qualified financial advisor

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

Created for the financial data analysis community.

If helpful, please ⭐ star this repository!

---

**Happy Trading! 📈**
