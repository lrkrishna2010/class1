from Log_returns import returns
import matplotlib.pyplot as plt

cov = returns.cov()
corr = returns.corr()

import seaborn as sns
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='vlag')
plt.title('Correlation Matrix')
plt.show()