import datetime

import numpy as np
import pandas_datareader.data as web

start = datetime.date(2016, 11, 16)
end = datetime.date(2021, 11, 18)
df = web.DataReader(["SPY", "F", "BTC-USD"], "yahoo", start, end)["Adj Close"]
df.shape