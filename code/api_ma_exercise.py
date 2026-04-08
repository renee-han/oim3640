import requests
data = requests.get('https://oim.108122.xyz/mass').json()
print(type(data))
print(type(data['data']))
print(type(data['data'][0]))

print(data['name'])       # 'Massachusetts' bcz looking @ first key in the data i.e. name which has value of Mass
print(data['governor'])   # 'Maura Healey' bcz ooking @ second key in the data i.e. governor which has value of Maura Healy
print(len(data))
print(data.keys())
towns = data['data']
print(type(towns)) 

#Pretty print prints dicts/lists in a more readable manner = instead of everything squished in 1 line --> makes data appear vertically 
from pprint import pprint
pprint(towns) #grabs that entire list of city/town dicts and stores it in towns
print(len(towns)) #how many of those mini dicts you have
pprint(towns[0]) #first mini dict 

for town in data['data'][:5]:
    print(f"{town['name']}: pop {town['population']:,}")

#Find smallest town 
#Start w/ infinity i.e. inf first bcz  you need a starting point to compare against = if you use 0, any pop will be not be less than that -- doesn't work out so use infinity bcz it's a guaranteed starting point that any real population will always be smaller than

smallest_pop = float('inf') # super large number
smallest_town = 'N/A'  # placeholder until we find the smallest

for town in towns: #town is each mini dict
    if town['population'] < smallest_pop:
        smallest_pop = town['population'] #inifinity replaced immediately
        smallest_town = town['name'] #smallest town value will no longer be N/A
print(smallest_town, smallest_pop )

print(smallest_town, smallest_pop)  # print the winner!

# North Reading (15554) < infinity ✅ → update! smallest_pop = 15554
# Dalton (6330) < 15554 ✅ → update! smallest_pop = 6330
# Rowe (424) < 6330 ✅ → update! smallest_pop = 424
# Edgartown (5168) < 424 ❌ → don't update!
# Sandwich (20259) < 424 ❌ → don't update! 

#When you're comparing if a # is less than another # i.e. x < y then x's info gets updated but if a towns pop is not less than the current smallest dont update keep going. @ end of loop whatever x is left i.e. nothings that smaller than this thats your final answer

# North Reading (15554) < infinity ✅ → smallest_pop = 15554, smallest_town = 'North Reading'
# Dalton (6330) < 15554 ✅ → smallest_pop = 6330, smallest_town = 'Dalton'
# Rowe (424) < 6330 ✅ → smallest_pop = 424, smallest_town = 'Rowe'
# Edgartown (5168) < 424 ❌ → keep going
# ... many towns that are bigger than 424 ...
# Gosnold (70) < 424 ✅ → smallest_pop = 70, smallest_town = 'Gosnold'
# ... rest of towns checked, nothing smaller than 70 ...
# loop ends!

# print(smallest_town, smallest_pop)  # → Gosnold 70



