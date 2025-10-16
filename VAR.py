import numpy as np
from volatility import portfolio_returns
alpha = 0.01  # 99% VaR level as lower tail
# Historical VaR
VaR_hist = -np.quantile(portfolio_returns, alpha)
# Parametric VaR (Gaussian)
mu = portfolio_returns.mean()
sigma = portfolio_returns.std()
z = np.quantile(np.random.normal(size=1000000), alpha)
VaR_param = -(mu + z * sigma)
# CVaR (Expected Shortfall) historical
losses = -portfolio_returns
CVaR_hist = losses[losses >= VaR_hist].mean()

print(f"Historical VaR (99%): {VaR_hist:.4%}")
print(f"Parametric VaR (99%): {VaR_param:.4%}")
print(f"Historical CVaR (99%): {CVaR_hist:.4%}")