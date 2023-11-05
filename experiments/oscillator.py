import numpy as np
import pandas as pd
from tinycta.signal import osc

if __name__ == "__main__":
    # simulate prices
    prices_diff = np.random.normal(0, 1, 100000)
    prices = pd.Series(data=np.cumsum(prices_diff))
    # prices can be negative, no problem...
    print(prices.min())

    for p in [2, 4, 8, 16, 32, 64]:
        o = osc(prices, fast=p, slow=3 * p, scaling=True)
        print(o.std())
