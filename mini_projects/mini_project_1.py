## Welcome to the Treasure Hunt Game! The goal of this game is to unlock a treasure chest filled with gold and the only way you can do that is if you guess the correct number!
#Initalization 
max_tries = 4
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
    print("You will be given 4 tries to guess a number between 1 and 20 and if you guess correctly, you will be able to unlock the treasure chest!")
    print("If you happen to guess in a certain number of tries, you'll be able to win one of the prizes from our tier selection")
    print("Tier 1 means if you guess the right number in 1 try, you'll earn the crown 👑")
    print("Tier 2 means if you guess the right number in 2 tries, you'll get a gem 💎")
    print("And finally, if you guess in 3 or more tries, you'll earn a coin 🪙")
    print("Good luck traveler!")
welcome()

#Start of Game - Player Entry
def player_guess():
    """This is the point where the player guesses for the number"""
    player_input = int(input("Guess a number between 1 and 20: "))
    print(f"The number you entered is: {player_input}")

tries = 0
#Player makes a guess
while tries < max_tries:
    guess = player_guess() #Stores the player's input
    tries = tries + 1
#Checking if guesses were correct or not
    if guess == correct_number:
        print("Congratulations! You guessed the correct number which was {correct_number}.") #Guessing right on the 1st try
        print("You earned yourself the {tier_1_prize}")
    break
else:
    tries = tries + 1
    print("")