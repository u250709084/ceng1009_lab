# for i in range (100):
#     print("We like Python's turtles")

# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#
# for month in months:
#     print("One of the months of the year is",month)

# numbers = (12, 10, 32, 3, 66, 17, 42, 99, 20)
#
# for number in numbers:
#     print(number, "squared is", number * number)

# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
#
# t.penup()
# t.goto(-200,0)
# t.pendown()
#
# for i in range(3):
#     t.forward(80)
#     t.left(120)
#
# t.penup()
# t.goto(-100,0)
# t.pendown()
#
# for i in range(4):
#     t.forward(80)
#     t.left(90)
#
# t.penup()
# t.goto(30,0)
# t.pendown()
#
# for i in range(6):
#     t.forward(60)
#     t.left(60)
#
# t.penup()
# t.goto(180,0)
# t.pendown()
#
# for i in range(8):
#     t.forward(40)
#     t.left(45)
#
# screen.exitonclick()

# import turtle
#
# t = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightblue")
# t.shape("turtle")
# t.color("purple")
# t.pensize(3)
# t.stamp()
#
# t.penup()
#
# for i in range(12):
#     t.forward(125)
#     t.pendown()
#     t.forward(15)
#
#     t.penup()
#     t.forward(25)
#     t.stamp()
#     t.backward(165)
#     t.left(30)
#
# screen.exitonclick()

import turtle

pirate = turtle.Turtle()
screen = turtle.Screen()

turns = (160, -43, 270, -97, -43, 200, -940, 17, -86)

for angle in turns:
    pirate.left(angle)
    pirate.forward(100)

print("Pirate final heading:", pirate.heading())


screen.exitonclick()