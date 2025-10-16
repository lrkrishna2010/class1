import numpy as np
from statsmodels.graphics.gofplots import qqplot
from volatility import portfolio_returns
import matplotlib.pyplot as plt
from volatility import returns
# QQ-plot for portfolio returns
qqplot(portfolio_returns, line='s')
plt.title('QQ-plot: Portfolio Returns vs Normal')
plt.show()

# Empirical tail index (Hill-ish) simple diagnostic for SPY
sorted_losses = np.sort(-returns['SPY'])[::-1]  # descending losses
k = 500
hill_est = np.mean(np.log(sorted_losses[:k]) - np.log(sorted_losses[k]))
print(f"Rough Hill estimate (k={k}): {1/hill_est if hill_est>0 else np.nan:.3f}")