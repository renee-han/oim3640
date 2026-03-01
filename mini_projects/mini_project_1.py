## Welcome to the Treasure Hunt Game! The goal of this game is to unlock a treasure chest filled with gold and the only way you can do that is if you guess the correct number!
#Initalization 
max_tries = 10
def generate_secret_number():
    """This function picks the correct number guess"""
    secret_number = 88
    return secret_number
correct_number = generate_secret_number() #Don't print this because the answer will be shown to player

#Prize Tiers
tier_1_prize = "👑"
tier_2_prize = "💎"
tier_3_prize = "🪙"
#Set Up 
def welcome():
    """Intro to Game """
    print("Welcome to the Secret Number Treasure Hunt Game!")
    print("Here are the rules of this game: ")
    print("You will be given 10 tries to guess a number between 1 and 100 and if you guess correctly, you will be able to unlock the treasure chest!")
    print("If you happen to guess in a certain number of tries, you'll be able to win one of the prizes from our tier selection")
    print("Tier 1 means if you guess the right number in 1 try, you'll earn the crown 👑")
    print("Tier 2 means if you guess the right number in 2 tries, you'll get a gem 💎")
    print("And finally, if you guess in 3 or more tries, you'll earn a coin 🪙")
    print("Good luck traveler!")
welcome()

#Start of Game - Player Entry
def player_guess():
    """This is the point where the player guesses for the number"""
    while True:
        try:
            player_input = int(input("Guess a number between 1 and 100: "))
            if 1 <= player_input <= 100: #If the player inputs a number greater than 1 and less than 100
                print(f"The number you entered is: {player_input}")
                return player_input
            else:
                print("Out of range! Please enter a number between 1 and 100.")
        except ValueError:
            print("That's not a number! Please try again.")
#Playing the Game
#Logic:
#1. Starts of with tries = 0 and if I make a try i.e. tries is now 1 INSIDE the while loop, if it's right on 1st try print congrats/get crown 
#2. Start with tries = 0 and I make my 1st try i.e. tries = 1 and my 1st try isn't right, do the else
#3. Because my 1st try wasn't correct maybe I want to do it again, so tries = 1st try + 1 = 2 on my 2nd try and if I get in 2 tries, jewel
#4. If I don't get it in 2 tries, else, loops back agian = 2+1 = 3rd try
#5. If I get it in 3 tries = coin = if not go back up again and keep going until hit max tries

#Player makes a guess (this while loop will keep going until the user runs out of tries)

playing = True 
while playing:
    tries = 0 #When the player guesses, the tries goes up to 1
    while tries < max_tries:
        guess = player_guess() #Stores the player's input
        tries = tries + 1 #Player makes a guess, # of tries goes up
        if guess == correct_number: #If the player guessed correctly whether that be in 1, 2, 3, or more tries
            if tries == 1:
                print(f"Congratulations! You guessed the correct number in your first attempt. You've earned yourself the {tier_1_prize}") #Guessing right on the 1st try
            elif tries == 2: 
                print(f"Congratulations! You guessed the correct number in 2 attempts. You've earned yourself the {tier_2_prize}") #Guessing right on the 2nd try
            else:
                print(f"Congratulations! You guessed the correct number in 3 or more attempts. You've earned yourself the {tier_3_prize}") #Guessing right on the 3rd or more try
            break
        else:
            print("Not quite there, keep searching")
    if tries == max_tries and guess != correct_number:
        print(f"Sorry, you're all out of tries! Better luck next time.")
    