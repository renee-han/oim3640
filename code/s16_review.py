import yfinance as yf 

stock = yf.Ticker('AAPL')
info = stock.info #Y finance trying to get info about NVDA
print(info)
print(info['shortName']) #printing the company name of the stock
print(info['currentPrice'])

#How do we know what the keys are in a dictionary?
print(info.keys())
print(len(info))


print(info['longName'])
print(info['longBusinessSummary'])
print(info['longBusinessSummary'].split())

tickers = ['AAPL', 'NVDA', 'MSFT']
prices = {}
for t in tickers:
    prices[t] = yf.Ticker(t).info['currentPrice']

print(sorted(tickers))
print(sorted(prices.values()))

