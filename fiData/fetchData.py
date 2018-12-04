#! /usr/local/bin/python3
import pandas_datareader.data as web
from datetime import datetime

#import matplotlib.finance as mpf
import matplotlib.pyplot as plt

start = datetime(2015, 2, 9)
end = datetime(2017, 5, 24)
start_date = '2010-01-01'
end_date = '2016-12-31'

tickers = ['AAPL', 'MSFT', '^GSPC']

f = web.DataReader('F', 'yahoo', start, end)
g = web.DataReader(tickers, 'yahoo', start, end)
#panel_data = web.DataReader(tickers, 'yahoo', start_date, end_date)

#print(f.head())

#h = panel_data.to_frame()
print(g.head())
