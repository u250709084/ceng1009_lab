import turtle

# -- setup --
gmk = turtle.Screen()
gmk.bgcolor("lightgreen")
t = turtle.Turtle()

# -- function --

def drawPoly(someturtle, somesides, soomesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.fd(soomesize)
        someturtle.lt(angle)


def drawSpirel(someturtle, angle):
    size = 1
    for i in range(100):
        someturtle.fd(size)
        someturtle.rt(angle)
        size = size + 2


def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)


def drawStar(someturtle, somesize):
    for i in range(5):
        someturtle.fd(somesize)
        someturtle.rt(144)


def drawSprite(someturtle, legs, lenght):
    angle = 360 / legs
    for i in range(legs):
        someturtle.fd(lenght)
        someturtle.backward(lenght)
        someturtle.lt(angle)


# -- exercise --
# Exercise 1
# t.pencolor("hotpink")
# t.pensize(3)
# drawPoly(t, 8, 50)

# Exercise 2
# t.pencolor("blue")
# t.pensize(2)
# for i in range(20):
#     drawPoly(t, 4, 100)
#     t.left(18)

# Exercise 3
# t.pencolor("blue")
# t.penup()
# t.goto(-150, 0)
# t.pendown()
# drawSpirel(t, 90)
#
# t.penup()
# t.goto(150, 0)
# t.pendown()
# drawSpirel(t, 89)

# Exercise 4
# t.pencolor("hotpink")
# drawEquitriangle(t, 100)

# Exercise 5
# t.pencolor("red")
# for i in range(5):
#     drawStar(t, 50)
#     t.penup()
#     t.forward(200)
#     t.right(144)
#     t.pendown()

# Exercise 6
drawSprite(t, 15, 100)
# -- finish --

gmk.exitonclick()