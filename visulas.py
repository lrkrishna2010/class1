# visuals.py
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import numpy as np
from scipy.stats import norm

plt.style.use('ggplot')

def plot_prices(data):
    plt.figure(figsize=(12,6))
    data.plot(title='Adjusted Close Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

def plot_rolling_volatility(returns, ticker='SPY', window=21):
    rolling_vol = returns[ticker].rolling(window=window).std() * np.sqrt(252)
    plt.figure(figsize=(12,6))
    rolling_vol.plot(title=f'{window}-day Rolling Annualized Volatility ({ticker})')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.show()

def plot_return_distribution(returns, ticker='SPY', bins=80):
    plt.figure(figsize=(12,4))

    # Histogram + Normal overlay
    plt.subplot(1,2,1)
    sns.histplot(returns[ticker], bins=bins, kde=True, stat='density', color='skyblue')
    mu, sigma = returns[ticker].mean(), returns[ticker].std()
    x = np.linspace(returns[ticker].min(), returns[ticker].max(), 100)
    plt.plot(x, norm.pdf(x, mu, sigma), 'r', lw=2)
    plt.title(f'{ticker} Daily Returns Histogram')
    plt.xlabel('Return')
    plt.ylabel('Density')

    # QQ-plot
    plt.subplot(1,2,2)
    sm.qqplot(returns[ticker], line='s', ax=plt.gca())
    plt.title(f'QQ-Plot {ticker} vs Normal')

    plt.tight_layout()
    plt.show()


# --- Run all visuals if script is executed directly ---
if __name__ == "__main__":
    import pandas as pd
    from yfin import data  # your prices dataframe
    from Log_returns import returns  # your log returns dataframe

    plot_prices(data)
    plot_rolling_volatility(returns, ticker='SPY', window=21)
    plot_return_distribution(returns, ticker='SPY', bins=80)