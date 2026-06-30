import yfinance as yf

data = yf.download("RELIANCE.NS", start="2023-01-01", end="2024-01-01")
print(data.head())
print(data['Close'].mean())