# Importing all the required modules
from game_data import data
import random
from art import logo, vs

# print the Logo and welcoming message
print(logo)
position_A = random.randint(1,len(data)) # Defining random position A for the list index
should_continue = True # A temporary variable for While loop

score = 0 # Variable to track the score

while should_continue: # While loop
    position_B = random.randint(1,len(data)) # Defining random position B for the list index
    print(f"""Compare A: {data[position_A]["name"]}, a {data[position_A]["description"]}, from {data[position_A]["country"]}""") # Printing the statements
    print(vs) # Printing the VS logo
    print(f"""Compare B: {data[position_B]["name"]}, a {data[position_B]["description"]}, from {data[position_B]["country"]}""")# Printing the statements
    guess = input("Who has more followers? Type 'A' or 'B': ").upper() # Prompt for the user input
    # Checking the condition
    if guess == "A": # Checking if A is greater than B. If yes, messages are printied and positions are updated
        if data[position_A]["follower_count"] > data[position_B]["follower_count"]: 
            score += 1
            print(f"You are right! Current score: {score}")
            position_A = position_A
        else:
            print(f"Sorry, that's wrong! Your score is {score}.")
            should_continue = False
    elif guess == "B": # Checking if B is greater than A. If yes, messages are printied and positions are updated   
        if data[position_A]["follower_count"] < data[position_B]["follower_count"]:
            score += 1
            print(f"You are right! Current score: {score}")
            position_A = position_B
        else:
            print(f"Sorry, that's wrong! Your score is {score}.")
            should_continue = False
            
# Program successfully built in the first attempt!