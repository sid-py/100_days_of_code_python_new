from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red", "green")
for i in range(1,3):
    timmy.forward(80)
    timmy.right(70)
    for j in range(1,5):
        timmy.forward(100)
        timmy.right(90)

    # timmy.forward(100)
    # timmy.right(90)
    # timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()