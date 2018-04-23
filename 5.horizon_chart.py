#!/usr/bin/env python3

import pandas as pd
from bokeh.charts import Horizon, output_file, show

# read in some stock data from the Yahoo Finance API
AAPL = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=AAPL&a=0&b=1&c=2000&d=0&e=1&f=2016",
    parse_dates=['Date'])

MSFT = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=MSFT&a=0&b=1&c=2000&d=0&e=1&f=2016",
    parse_dates=['Date'])

IBM = pd.read_csv(
    "http://ichart.yahoo.com/table.csv?s=IBM&a=0&b=1&c=2000&d=0&e=1&f=2016",
    parse_dates=['Date'])

#the data and the labels in a dictionary
data = {
    'AAPL': AAPL['Adj Close'],
    'Date': AAPL['Date'],
    'MSFT': MSFT['Adj Close'],
    'IBM': IBM['Adj Close']
}

p = Horizon(data, x='Date',
             title="Horizon plot using stock inputs")

output_file("5.horizon_chart.html")

show(p)