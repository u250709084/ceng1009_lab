# import random
#
# for i in range(10):
#     print(random.randint(25,35))

# import math
#
# a = int(input("Enter lenght"))
# b = int(input("Enter width"))
# hypotenuse = math.sqrt(a**2 + b**2)
#
# print(hypotenuse)

# import math
#
# def areaOfCircle(r):
#     return math.pi * r**2
#
# print(areaOfCircle(5))

# import turtle
#
# def drawStar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# screen = turtle.Screen()
# tess = turtle.Turtle()
#
# drawStar(tess, 100)
#
# screen.exitonclick()

# import turtle
#
# def drawSquare(t, side):
#     for i in range(4):
#         t.forward(side)
#         t.left(90)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("purple")
# tess.pensize(3)
# for i in range(5):
#     drawSquare(tess, 20)
#     tess.penup()
#     tess.forward(30)
#     tess.pendown()
#
# screen.exitonclick()

import turtle

def drawSquare(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)

screen = turtle.Screen()
t = turtle.Turtle()

screen.bgcolor("black")
t.color("white")
t.pensize(3)

for i in range(20, 120, 20):
    drawSquare(t, i)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

screen.exitonclick()