# A product would cost $100, how much tax would we pay? 
product = 100 # in dollars
tax_rate = 0.0625
tax = product * tax_rate
print(tax) 
#Or you could also print:
#F strings are used when you want to insert a variable value into a string 
print(f'The tax for a product which costs ${product} is ${tax}')

#If you have multiple products:
#Because you don't have a parameter inside (), the variables inside the body should've been defined before
def calc_tax(price, tax_rate):
    """Calculate product tax based on given price and tax rate, and return the tax amount.""" #Doc String: a string that describes what the chunk of code will do
    tax = price * tax_rate
    return(tax)
calc_tax(20,0.0625)
#Because the function you defined has parameters, have to define the values when you call function
#Once called, price = 20, tax rate = 0.0625
#It multiples both then returns that value back to Python but doesn't print anything out
def calc_tax(price, tax_rate):
    """Calculate product tax based on given price and tax rate, and return the tax amount.""" #Doc String: a string that describes what the chunk of code will do
    tax = price * tax_rate
    return(tax)
#Don't put print after return bcz the value of tax is returned and function ended
#If you want to see results, print here:
print(calc_tax(20,0.0625))
#Could also do value = calc_tax(20,0.0625) then print(value)


computer_price = float(input('Enter the product price: ')) #Asks the user for input, you type in a value, the value is a string at first, then is converted to a decimal
iphone_price = 1100
mass_rate = 0.0625
ny_rate = 8.875 / 100
#Tax computer takes the value you inputted * 0.0625 bcz it uses calc tax function format
tax_computer = calc_tax(computer_price, mass_rate)
#Tax iphone does the same thing
tax_iphone = calc_tax(iphone_price, ny_rate)
total_tax = tax_computer + tax_iphone
print(total_tax)




