import turtle

t = turtle.Turtle()

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
    t.right(90)

for i in range(4):
    star()
    go_next()

turtle.done()