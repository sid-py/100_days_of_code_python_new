import random
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cross_road = input("You are at a crossroad. Which turn would you take? (Left/Right/Straight) :\n ").lower()

lake = ""
cave = ""

if cross_road == random.choice("lrs"):
    lake = input(" You reached a lake. Would you like to take a Boat or Swim?:\n").lower()

    if lake == random.choice("bs"):
        cave = input("You reached a cave with 3 doors. Which door do you choose (1/2/3)?: \n")

        if cave == "1":
            print("Its a room full of fire. Game Over!!")

        elif cave == "2":
            print("Congratulations! You found the treasure!")
        elif cave == "3":
            print("Its a room full of snakes. Game Over!!")
        else:
            print("You chose a door that doesnt exist! Game Over!!")  

    else:
        print("You got attacked by Pirannhas! Game Over!!")
else:
        print("You fell into a hole! Game Over!!")        


