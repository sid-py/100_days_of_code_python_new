# from turtle import Turtle, Screen
# import random

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red", "green")
# for i in range(1,3):
#     timmy.forward(80)
#     timmy.right(70)
#     for j in range(1,5):
#         timmy.forward(100)
#         timmy.right(90)

#     # timmy.forward(100)
#     # timmy.right(90)
#     # timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander",])
table.add_column("Type", ["Electric", "Water", "Fire",])
table.align = ("l")
print(table)