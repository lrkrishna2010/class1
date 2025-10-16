import yfinance as yf
import pandas as pd

# Define your tickers
tickers = ["AAPL", "MSFT", "GLD", "SPY", "TLT"]

# Download data
data = yf.download(tickers, start="2010-01-01", progress=False)

# Keep only 'Close' prices to simplify everything
data = data['Close']

# Flatten columns if it's a MultiIndex (e.g., if only 1 ticker it won't be)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [col for col in data.columns.get_level_values(0)]

# Ensure no missing data (optional: forward fill)
data = data.ffill().dropna()

print(data)

