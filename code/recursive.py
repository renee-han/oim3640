import time


def groundhog_day():
    """A function that prints 'groundhog day' every second indefinitely."""
    print('Did you mean: groundhog day?')
    time.sleep(1)
    groundhog_day() #What makes this recursive is that the function call is INSIDE the body of the function  


groundhog_day() #When you call the function, it prints the word then calls itself again