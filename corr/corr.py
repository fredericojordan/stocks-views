import datetime as dt

import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr

now = dt.datetime.now()
start = now - dt.timedelta(days=365)

price = pdr.get_data_yahoo(
    ["PETR4.SA", "VALE3.SA", "WEGE3.SA", "LREN3.SA"], start, now
)["Adj Close"]
returns = price.pct_change().dropna()
corr = returns.corr()

plot = sns.heatmap(corr, annot=True, fmt=".2f", linewidths=0.6)
plt.show()
