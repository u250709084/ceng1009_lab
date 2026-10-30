# def sumTo(n):
#     return n * (n + 1) / 2
#
# print(sumTo(10))
#
# n = int(input("please enter a number: "))
# print("Sum is", sumTo(n))

# import turtle
#
# def drawStar(t, n, size):
#     angle = 180 - 180 / n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 11, 100)
#
# wn.exitonclick()

# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#
#     return total
#
# print(sumTo(10))
# n = int(input("please enter a number: "))
# print("Sum is", sumTo(n))

import math
import turtle


# def wySqrt(x):
#     guess = x / 2
#     for i in range(20):
#         guess = (1/2) * (guess + x / guess)
#
#     return guess
#
# w = int(input("Enter a positive integer: "))
#
# print("The result is", wySqrt(w))
# print("The result is", wySqrt(w))

# def drawSprite(someturtle, legs, lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.fd(lenght)
#         someturtle.backward(lenght)
#         someturtle.lt(angle)
#
# def fancySquare(t, size):
#     for i in range(4):
#         drawSprite(t, 8, 20)
#         t.fd(size)
#         t.left(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("black")
# t.color("pink")
# t.pensize(2)
#
# fancySquare(t, 100)
#
# wn.exitonclick()

# def drawTip(t, size):
#     t.begin_fill()
#     t.lt(90)
#     t.fd(size / 2)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size)
#     t.rt(120)
#     t.fd(size / 2)
#     t.rt(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         drawTip(someturtle, 10)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#     for i in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.fd(size)
#         t.lt(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("lightgreen")
# t.pensize(2)
#
# fancySquare(t, 100)
#
# wn.exitonclick()

# def checkSign(x):
#     if x > 0:
#         return "The number is positive"
#     elif x < 0:
#         return "The number is negative"
#     else:
#         return "The number is zero"
#
# numbers = (-7, 5, 0)
#
# for numbers in numbers:
#     print(numbers, "is", checkSign(numbers))
#
# n = int(input("Enter a number: "))
# print(checkSign(n))

def drawBar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height + gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)
    border = 10

    gap = (maxheight - num_bars) / 25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    right = 40 + num_bars + border
    top = maxheight + 4 * border

    wn.setworldcoordinates(-border, -border, right, top)
    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t, height, gap)

    wn.exitonclick()



data = [48, 117, 200, 240, 160, 260, 220]

barChart(data)