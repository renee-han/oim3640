import requests

# POST: send a message (1-140 characters)
#First, send data back to API server and that specific API key i.e. reneerenee lets me send it back 
requests.post('https://oim.108122.xyz/message',
              json={'message': 'Hello from Renee!'}, #puts in dict form
              headers={'X-Token': 'reneerenee'})

# GET: read ALL messages = not just the message I sent back 
#Leaderboard technically is a visual open view of the data the API server currently holds

data = requests.get('https://oim.108122.xyz/messages').json() #data holds all the messages from everyone i.e. 'message': 'Hello from Renee!' 

#Bcz you're trying to get back multiple items, it's a list of dicts 
for msg in data:
    print(msg) #This prints out the entire dict i.e. {'author': 'Renee', 'message': 'Hello from Renee!', 'timestamp': '2026-04-07T01:44:21'}





