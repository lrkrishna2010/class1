import statsmodels.api as sm
from Log_returns import returns
import matplotlib.pyplot as plt
from yfin import data
import numpy as np
import seaborn as sns
from scipy.stats import norm

betas = {}
for col in returns.columns:
    X = returns['SPY']  # market returns
    y = returns[col]    # asset returns
    X = sm.add_constant(X)
    res = sm.OLS(y, X).fit()   # THIS defines `res`
    betas[col] = res.params.iloc[1]  # slope = beta

print(betas)
# --- 4. CAPM Expected Returns ---
Rf_annual = 0.01      # 1% annual risk-free rate
Rf_daily = Rf_annual / 252
Rm_daily = returns['SPY'].mean()
capm_returns = {col: Rf_daily + beta * (Rm_daily - Rf_daily) for col, beta in betas.items()}


def plot_betas_and_returns(betas, capm_returns):
    tickers = list(betas.keys())
    beta_vals = [betas[t] for t in tickers]
    capm_vals = [capm_returns[t] for t in tickers]
    
    x = np.arange(len(tickers))
    width = 0.35
    
    plt.figure(figsize=(10,6))
    plt.bar(x - width/2, beta_vals, width, label='Beta', color='skyblue')
    plt.bar(x + width/2, capm_vals, width, label='CAPM Return', color='orange')
    plt.xticks(x, tickers)
    plt.ylabel('Value')
    plt.title('CAPM Betas and Expected Returns')
    plt.legend()
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.show()

# --- 6. Run All Visuals ---

plot_betas_and_returns(betas, capm_returns)