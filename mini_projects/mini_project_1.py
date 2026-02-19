## Welcome to the Secret Number Guessing Game Program
## This section imports a random number generator function
#request user to enter a number
print("Enter a number between 1 and 100")

#Display the max, min, and average of a range of numbers 
numbered_list = (100,22,57,99,1,32)
min_list = min(numbered_list)
print(min_list)
max_list = max(numbered_list)
print(max_list)

#calculate the average
avg_list = sum(numbered_list) / len(numbered_list)
print(avg_list)

#round the average to 2 decimal places
avg_list = round(avg_list,2)
print(avg_list)

#input a number and print it back out
my_input = int(input("Enter a number between 1 and 100:"))
print("The number you entered is ", my_input)

#import a function to assign a random number
import random
secret_number = random.randint(1,100)
print("The secret random number is", secret_number)

#loop until variable is equal to or less than 5
current_number = 1
while current_number <= 5: 
  print(current_number)
  current_number = current_number + 1

# evaluate whether a number is positive or negative 
num = -2
if num > 0:
  print("the number is positive")
else:
  print("the number is negative")
