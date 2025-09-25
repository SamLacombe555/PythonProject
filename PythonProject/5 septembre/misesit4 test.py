# Un pilote participe à une course et doit savoir s’il peut passer à l’étape suivante selon certaines conditions.
#
# Lorsque a vitesse est supérieure à 120 km/h et le temps restant est d'e plus de 5 minutes.
#
# Lorsqu'il possède au moins 50 pièces bonus
#
# De plus, si son niveau bonus est au moins à 2, il peut passer même si les autres conditions ne sont pas remplies.




"""
def demande_vitesse():
    print("Quelle est la vitesse de la voiture en km/h?")

def demande_temps():
    print("C'est quoi le temps restant en minutes?")

def demande_piece(piece):
    print("Combien de pièce bonus possèdes-tu?")

def demande_niveau():
    print("Quelle est ton niveau bonus?")

def niveau(niveau):
    niveau

accepter = "Tu peux passer à la prochaine étape car"
refus = "Tu ne peux pas passer à la prochaine étape car "

demande_vitesse()
vitesse = int(input())
demande_temps()
temps=int(input())
demande_piece()
piece= int(input())
demande_niveau()
niveau=int(input())

if niveau >= 2:
    print(accepter, "ton niveau bonus franchis le minimun de 2")
else:
    if not vitesse > 120:
        print(refus, "ta vitesse ne dépasse pas 120 km/h")
        acces = False
    if not temps > 5:
        print(refus, "le temps restant ne dépasse pas 5 minutes")
        acces = False
    if not piece >= 50:
        print(refus, "tu possèdes en dessous de 50 pièce bonus")
        acces = False
"""

def acces_vitesse():
    return vitesse > 120

def acces_temps():
    return temps > 5

def acces_piece():
    return piece >= 50

def acces_niveau():
    return niveau >= 2


accepter = "Tu peux passer à la prochaine étape car "
refus = "Tu ne peux pas passer à la prochaine étape car "

vitesse = int(input("Quelle est la vitesse de la voiture en km/h?"))
temps = int(input("C'est quoi le temps restant en minutes?"))
piece = int(input("Combien de pièce bonus possèdes-tu?"))
niveau = int(input("Quelle est ton niveau bonus?"))


if acces_niveau() == True:
    print(accepter, "ton niveau bonus franchis le minimun de 2")
else:
    if acces_vitesse() == False:
        print(refus,"ta vitesse ne dépasse pas 120 km/h")
    if acces_temps() == False:
        print(refus,"le temps restant ne dépasse pas 5 minutes")
    if acces_piece() == False:
        print(refus,"le temps restant ne dépasse pas 5 minutes")





