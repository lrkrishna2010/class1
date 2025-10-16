import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
from yfin import data


returns = data.pct_change().dropna()
log_returns = np.log(data).diff().dropna()

# Summary statistics
stats = returns.describe().T
stats['skew'] = returns.apply(skew)
stats['kurtosis'] = returns.apply(kurtosis)
stats['annualized_vol'] = returns.std() * (252**0.5)
stats[['mean','annualized_vol','skew','kurtosis']].round(4)
print(stats)
print("\n=== PRICE DATA HEAD ===")
print(data.head())

print("\n=== LOG RETURNS HEAD ===")
print(log_returns.head())