# Data fetch using yfinance
import yfinance as yf
import pandas as pd

tickers = ['SPY', 'AAPL', 'MSFT', 'GLD', 'TLT']
start = '2015-01-01'
end = None

# Fetch adjusted close prices
data = yf.download(tickers, start=start, end=end, progress=False)
data = data.dropna()
data.head(10)
print(data.head(10))