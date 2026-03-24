s = ['Hello world', 'Python is great', 'I love programming', 'a very long sentence that exceeds the limit']

for sentence in s:
    words = sentence.split()
    print(words)

tel = '123-456-7890'
a, b, c = tel.split('-') #Unpacking i.e. putting values into variables 
print(c)

*_, ext = tel.split('-') #*_ means getting everything before the last value and ext is getting the very last value 

phonebook = ['123-456-3652', '1-235-567-3425']
for p in phonebook:
    *_, last_four = p.split('-')
    print(last_four)

