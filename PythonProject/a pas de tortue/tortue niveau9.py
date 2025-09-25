import turtle

t = turtle.Turtle()

t.speed(0) #vitesse

t.color("orange")

for i in range(3):
    for i in range(5):
        t.forward(50)
        t.right(144)

    t.penup()
    t.forward(150)
    t.pendown()
    t.right(120)


t.color("black")
t.penup()
t.left(90)
t.forward(100)
t.pendown()

for i in range (360): #cercle de la lune
    t.forward(50)
    t.backward(50)
    t.right(1)


t.color("white")
t.right(120)
t.forward(20)
for i in range (360): #cercle cachant la lune
    t.forward(50)
    t.backward(50)
    t.right(1)


turtle.done()