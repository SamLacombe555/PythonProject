def success():
    print("Le piéton traverse")

def failure():
    print("Le piéton ne traverse pas")


feu = input("Quelle couleur est le feu?")

if feu == "vert":
    success()

if feu == "orange":
    failure()

if feu == "rouge":
    barriere = input("Est-ce que la barrière est ouverte ou fermée?")
    if barriere == "ouverte":
        success()
    else:
        failure()
