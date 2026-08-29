#descriptive statistics
import statsmodels.api as sm
data=[10,20,30,40,50]
desc_stats=sm.stats.DescrStatsW(data)
print(f"Mean:{desc_stats.mean}")
print(f"Varinace:{desc_stats.var}")
print(f"standard deviation:{desc_stats.std}")
print(f"Number of observations:{desc_stats.nobs}")
