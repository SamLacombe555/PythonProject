# faut que vitesse supérieur à 120 et temps restant est plus que 5min
# faut au moins 50 pièces
# si niveau bonus dessus 2, il passe

vitesse = float(input("Quelle est la vitesse de la voiture en km/h?"))
temps = float(input("Quelle est le temps restant? en minutes"))
piece = int(input("Combien de pièce possède-t-il?"))
bonus = int(input("Quelle est son niveau bonus?"))


vitesse2 =bool(vitesse >= 120)
temps2 =bool(temps >= 5)
piece2 = bool(piece>=50)
bonus2 = bool(bonus>=2)

if (vitesse2 and temps2 and piece2) or bonus2 == True:
    print("Le pilote peut participer à la course")
else:
    print("Le pilote ne peut pas participer à la course")

