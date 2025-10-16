import pandas as pd
import numpy as np

# Creating a basic DataFrame
dates = pd.date_range('2024-01-01', periods=5)
data = {'Price': [100, 102, 99, 105, 104], 'Volume': [1000, 1500, 800, 2000, 1200]}
df_ex = pd.DataFrame(data, index=dates)

print("Sample DataFrame:")
print(df_ex)

# Quick review of calculating log returns and basic stats
log_returns_ex = np.log(df_ex['Price'] / df_ex['Price'].shift(1)).dropna()

print("\nLog Returns (first 4):")
print(log_returns_ex)
print(f"\nMean Return: {log_returns_ex.mean():.4f}")
print(f"Standard Deviation (Risk): {log_returns_ex.std():.4f}")