import turtle  # on importe la librairie

t = turtle.Turtle()  # on crée une tortue

t.speed(10) #vitesse

t.color("orange")
for i in range(3):
    for i in range (5):
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

t.speed(10)

for i in range(360):
    t.forward(50)
    t.backward(50)
    t.right(1)

t.penup()
t.forward(20)
t.pendown()
t.color("white")


for i in range (360):
    t.forward(50)
    t.backward(50)
    t.right(1)

turtle.done()