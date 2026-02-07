a = 5 #First sets variable a w/ a value of 5
a = input("Enter an integer: ") #Now, the value of a is overwritten, now input() asks user for input = asks user to type in a value
a = int(a) # Once you type in a number, let's say 10, it'll return '10' as a string because the number you enter is still part of the string: 'Enter an integer:'. Then right after, converts it into an integer 
# Check odd or even
#If the number that I put in was 10, the value of a is now 10, no longer 5. Because it's even/divides cleanly, no remainder, so prints even.
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exprssion (returns a value)
a = 2
1 + a #an expression, which evaluates to 3, but doesn't do anything w/ it 
#Statement
print(1+a) # a statement, which prints the result (actually performs an action) 



