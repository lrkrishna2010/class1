# volatility.py
import numpy as np
import matplotlib.pyplot as plt
from Log_returns import returns
from yfin import tickers

# Equal weights
weights = np.repeat(1 / len(tickers), len(tickers))

# Portfolio return
portfolio_returns = returns.dot(weights)

# Annualized stats
annualized_return = (1 + portfolio_returns.mean()) ** 252 - 1
annualized_vol = portfolio_returns.std() * np.sqrt(252)
sharpe = (annualized_return - 0.01) / annualized_vol

# Drawdown
cum_returns = (1 + portfolio_returns).cumprod()
running_max = cum_returns.cummax()
drawdown = (cum_returns - running_max) / running_max

print(f"Annualized Return: {annualized_return:.2%}")
print(f"Annualized Volatility: {annualized_vol:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {drawdown.min():.2%}")

# Plots
cum_returns.plot(figsize=(12, 5), title="Portfolio Cumulative Return")
plt.grid()
plt.tight_layout()


drawdown.plot(figsize=(12, 4), title="Portfolio Drawdown", color='red')
plt.grid()
plt.tight_layout()
plt.show()
