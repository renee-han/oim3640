for i in range(1,5,2):
    print(i) #Start at 1 --> go till 5, but count by increments of 2 = so 1, 3

name = 'Alejandro' #name is a string 
type(name)
name[0] #Returns the first character = A 
name[0:4] #Returns 0, 1, 2, 3 = A, l, e, j 
#Start at 0 go to 6, go up by increments of 2 
#A = 0, E = 2, A = 4
name[0:6:2] 
#Starting at 1 = 0 (a), 1(l)
#l, j, n
name[1:6:2] 


name = "Python"
print(name * 3) #return Python 3 times 
print(name + "3") #concatenate = Python3

#I'm fine
#If you try to print I'm fine but in single quotes, error = ned to use double quotes
print("'I'm fine'") 
print('Finn says "I am fine"') #If you put double quotes in single, double quotes will appear
#Escape Character
#The \ tells Python to interpret the character after it i.e. " or ' as a literal " or "
print("Finn says \"i\'m fine\"") 

#Integers are inmutuable
a = 5
b = a
a = 10 
print(b), print(a) #b is 5, a = 10 

#A list is mutuable bcz you can add more #'s to it @ the end 
a = [1,2,3] #square bracket is a list = list is mutable
a.append(4) #a and b are pointing to same position
print(a)

x = 10

def f():
    message = 'hello'
    x = 5
    return x
print(f())
print(x)
print(message)
