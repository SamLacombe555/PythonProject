import turtle

ninja = turtle.Turtle()

def dessiner_etoile():
    for i in range(5):
        ninja.forward(50)
        ninja.right(144)

def se_deplacer():
    ninja.penup()
    ninja.forward(150)
    ninja.right(90)
    ninja.pendown()

# Début du programme principal
for i in range(4):
    dessiner_etoile()
    se_deplacer()

turtle.done()