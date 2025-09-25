import turtle

t = turtle.Turtle()

t.speed(25)
t.color("orange")
t.left(90)

def star():
    for i in range(5):
        t.forward(50)
        t.right(144)

def go_next():
    t.penup()
    t.forward(150)
    t.pendown()
    t.right(120)

for i in range(3):
    star()
    go_next()

t.color("black")
t.left(90)
t.penup()
t.forward(100)
t.pendown()


def circle():
    for i in range(360):
        t.forward(50)
        t.backward(50)
        t.right(1)

circle()

t.color("white")
t.right(120)
t.forward(20)

circle()

turtle.done()