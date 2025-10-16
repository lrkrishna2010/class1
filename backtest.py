from scipy.stats import binomtest
from volatility import portfolio_returns
from VAR import VaR_hist
from VAR import alpha

# Kupiec test (unconditional coverage)
breaches = (portfolio_returns < -VaR_hist).sum()
n_obs = len(portfolio_returns)
p_hat = breaches / n_obs
p0 = alpha

print(f"Breaches: {breaches} / {n_obs} (observed rate={p_hat:.4f})")

# two-sided binomial test (exact)
result = binomtest(breaches, n_obs, p0, alternative='two-sided')
pvalue = result.pvalue  # extract the float p-value
print(f"Kupiec (binomial) p-value: {pvalue:.4f}")