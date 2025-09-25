import turtle  # on importe la librairie

t = turtle.Turtle()  # on crée une tortue

for i in range(4): # le nombre de fois qu'on répète la ou les actions dans l'indentation
    t.forward(100)  # avancer de 100 pixels
    t.right(90)     # tourner de 90 degrés à droite

turtle.done()       # terminer et afficher le dessin