# Importing all the required modules
from game_data import data
import random
from art import logo, vs

# print the Logo and welcoming message
print(logo)
should_continue = True # A temporary variable for While loop
score = 0 # Variable to track the score

def format_account(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    acc_follower = account["follower_count"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"    


def check_answer(guess,follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "A"
    else:
        return guess == "B"
    
account_b = random.choice(data)
score = 0    

while should_continue: # While loop
    account_a = account_b
    account_b = random.choice(data)
    print(f"Compare A: {format_account(account_a)}") # Printing the statements
    print(vs) # Printing the VS logo
    print(f"Compare B: {format_account(account_b)}")# Printing the statements
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    guess = input("Who has more followers? Type 'A' or 'B': ").upper() # Prompt for the user input
    is_correct = check_answer(guess, a_follower_count,b_follower_count)
    while account_a == account_b:
        account_b = random.choice(data)

    # Checking the condition
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
        
               
    else:
        print(f"Sorry, that's wrong! Your final score is {score}.")
        should_continue = False    
# Program successfully built in the first attempt!