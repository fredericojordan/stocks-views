import datetime

import seaborn
from matplotlib.pyplot import show
from pandas_datareader.data import get_data_yahoo

now = datetime.datetime.now()
start = now - datetime.timedelta(days=365)

price = get_data_yahoo(["PETR4.SA", "VALE3.SA", "WEGE3.SA", "LREN3.SA"], start, now)[
    "Adj Close"
]
returns = price.pct_change().dropna()
corr = returns.corr()

plot = seaborn.heatmap(corr, annot=True, fmt=".2f", linewidths=0.6)
show()
