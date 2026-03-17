prices = {}
 
prices['AAPL'] = 178.50
prices['GOOG'] = 141.80
prices['MSFT'] = 415.20
print(prices)
prices['AAPL'] = 182.30
del prices['GOOG']
print(prices)

prices = {'AAPL': 182.30, 'MSFT': 415.20, 'GOOG': 141.80}
for key in prices:             
    print(key, prices[key])


for value in prices.values():    
    print(value)

for key, value in prices.items(): 
    print(f'{key}: ${value}')

for key, value in prices.items():
    print(key, value)

expensive = []  # empty list to store results

for key, value in prices.items(): 
    if value > 200:
        expensive.append(key) 
print(expensive)