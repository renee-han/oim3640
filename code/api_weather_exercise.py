import requests
#The API company determines which style they use for API link syntax and in the link syntax, how to access the link+data you want
#Before w/ the leaderboard one, the way to access data/API link was w/ /, but now in the weather one, it uses the ? and q

API_KEY = 'abc123...'  # Don't hardcode this bcz if you committ/push code to GitHub, everyone can see your API key+use it

url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')
#? = start of the parameters i.e. what data I want
#q = city name (set bcz of the API company)
#& = connects parameters 
#appid={API_KEY} = proves you can access the data
#units = imperial (gets temp in °F = again set by API company)

data = requests.get(url).json() #gets the data from the url request i.e. the Boston weather in F and then gets converted into dict
print(f"Boston: {data['main']['temp']}F°")



