from art import logo
import random
import os

print(logo)

# Step 1: Print the welcome line
print("Welcome to the Number Guessing Game!")

# Step2: Print intro line
print("I am thinking of a number between 1 and 100.\n")
target_number = random.randint(1,100)

#Step3:  Print the answer
print(f"Pssst....the correct number is {target_number}")

# Step4: Give option for difficulty level 
    # step 5: Print condition for the difficulty level
    # Step 6: Make a guess
    # Step 7: If the guess is greater than target number, print too high! Else print too less.
    # Step 8: Check if the guess is equal to target number. If yes. Print winning message. If not continue step 6.
    
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def play_game():
    difficulty = input("Choose a difficulty level 'H' for hard and 'E' for easy: ").upper()
    should_continue = True

    if difficulty == "E":
        attempt = 10
    if difficulty == "H":
        attempt = 5
    while should_continue:
        guess = int(input("Make a guess: "))
        attempt -= 1
        print(f"You have {attempt} attempts left.")
        if attempt == 0:
            should_continue = False
        if guess > target_number:
            print("Too high!")
        elif guess < target_number:
            print("Too low!")
        elif guess == target_number:
            print("Your guess is correct! You win!")
            should_continue = False

while input("Do you wan to play the game again? ") == "y":
    cls()
    play_game()  
    

    
        
    




