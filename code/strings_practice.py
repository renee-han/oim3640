stocks = 'AAPL,MSFT,GOOG,AMZN' 
stocks[0]
print(stocks[0])
stocks[-1]
print(stocks[-1])
len(stocks)
print(len(stocks))
#stocks[19]
#print(stocks[19])

stocks = 'APPL, MSFT, GOOG, AMZN, TLSA'
stocks.islower() 
stocks.isupper()
stocks.lower() 
stocks.find('MSFT')

#Find returns the index 
print(stocks.find('MSFT'))

'BABSON'.find('B')
print('BABSON'.find('B'))

#Stock in stocks_info is that entire sub list i.e. ['APPL', 100, 'Hardware']
#Is the word 'Hardware' in that sublist, yes
#Print stock[0], stock is a list, so 'APPL'
stocks_info = [['APPL', 100, 'Hardware'], ['MSFT', 200, 'Software'], ['GOOG', 300, 'Hardware']]
for stock in stocks_info:
    if 'Hardware' in stock:
        print(stock[0])


stocks = 'AAPL,MSFT,GOOG,AMZN'
#How do you make it become 'AAPL,MSFT,GOOG,AMZN,TSLA'
#Can't use append bcz append is only for a list
stocks_2 = stocks + ',TSLA'
print(stocks_2)
#What is 'GOOG' in stocks? 'AA' in stocks?
#GOOG in stocks is True
#AA in stocks is True 
stocks.lower()
print(stocks.lower())
stocks.find('MSFT')
#THIS IS A STRING, COUNTING INDVL CHARACTERS + COUNTS THE , TOO 
print(stocks.find('MSFT'))

#Sorting stocks in reverse = need to convert string into list first bcz if you sort a string, it'll treat it as indvl characters, not what we want = we want to sort by the whole word
stocks = 'AAPL,MSFT,GOOG,AMZN'
t = stocks.split(',')
t
print(t)
#Reverse alphabetical order
print(sorted(t, reverse=True))






