# def fizz_buzz(n):
#     for num in range(1, n + 1):
#         if num % 15 == 0:
#             print("FizzBuzz")
#         elif num % 5 == 0:
#             print("Buzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         else:
#             print(num)
#
# fizz_buzz(99)

# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
#
# print(digit_sum(1234))

# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result += s[i].upper()
#         else:
#             result += s[i].lower()
#     return result
#
# print(alternate_case("Görkem Mehmet Kaya"))

import turtle

# def draw_polygon(t, side, lenght):
#     for i in range(side):
#         t.forward(lenght)
#         t.left(360 / side)
#
# t = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t.pensize(3)
# colors = ["red", "black", "blue"]
#
# for i in range(3):
#     t.penup()
#     t.goto(-150 + i * 120, -30)
#     t.pendown()
#     t.color(colors[i])
#     draw_polygon(t, i + 3, 60)
#
# wn.exitonclick()

# def filled_square(t, size, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("lightgreen")
#
# for i in range(5):
#     t.penup()
#     t.goto(-165 + i * 70, -25)
#     t.pendown()
#     if i % 2 == 0:
#         color = "blue"
#     else:
#         color = "red"
#     filled_square(t, 50, color)
# wn.exitonclick()

# def draw_square(t, size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("lightgreen")
# t.pensize(2)
#
# for i in range(12):
#     draw_square(t, 80)
#     t.left(30)
# wn.exitonclick()

def draw_square(t, size, filled):
    if filled:
        t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    if filled:
        t.end_fill()

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")
t.speed(20)
size = 40
for row in range(6):
    for col in range(6):
        t.penup()
        t.goto(-120 + col * size, -120 + row * size)
        t.pendown()
        draw_square(t, size, (row + col) % 2 == 0)
wn.exitonclick()