import numpy as np
from CAPM import betas
from Log_returns import returns
from Cov import corr

# Stress scenario: market crash and correlation spike
# 1) Market crash: -10% on SPY day (shock)
shock = -0.10
# approximate impact on portfolio: revalue by applying same shock proportionally to holdings via betas
approx_port_loss = sum([betas.get(ticker, 1.0) * shock * w for ticker, w in zip(returns.columns, [1/len(returns.columns)]*len(returns.columns))])
print(f"Approx portfolio loss from -10% market shock (beta-weighted): {approx_port_loss:.2%}")

# 2) Correlation shock: recompute portfolio volatility with high correlation
high_corr = corr.copy()
high_corr_values = high_corr.values
high_corr_values[high_corr_values<1] = 0.9  # set off-diagonals to 0.9 roughly
# rebuild covariance assuming same vol but high corr (simplified)
vols = returns.std().values
cov_high = np.outer(vols, vols) * 0.9
w = np.repeat(1/len(vols), len(vols))
sigma_p_high = (w @ cov_high @ w)**0.5
print(f"Portfolio vol under high-correlation scenario: {sigma_p_high* (252**0.5):.2%} annualized")