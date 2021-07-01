import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_tools = [rock, paper, scissors]

print("Welcome to Rock Paper Scissors!")
player_selection = int(input("Please enter your selection. 1-Rock, 2-Paper and 3-Scissors: \n"))

print("Player selected: \n", game_tools[player_selection - 1])

comp_selection = random.randint(1,3)
print("Computer selected: \n", game_tools[comp_selection - 1])

if player_selection == 1 and comp_selection == 2:
    print("Computer won!")
elif player_selection == 1 and comp_selection == 3:
    print("Player won!")
elif player_selection == 2 and comp_selection == 1:
    print("Player won")
elif player_selection == 2 and comp_selection == 3:
    print("Computer won")
elif player_selection == 3 and comp_selection == 1:
    print("Computer won")
elif player_selection == 3 and comp_selection == 2:
    print("Player won")
else:
    print("Its a draw. Play again.")
 