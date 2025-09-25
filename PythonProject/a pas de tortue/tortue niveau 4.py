import turtle

t = turtle.Turtle()

t.color("orange")
t.left(90)

for i in range (5):
    t.forward(50)
    t.right(144)

t.penup()
t.forward(150)
t.pendown()
t.forward(20)

turtle.done()