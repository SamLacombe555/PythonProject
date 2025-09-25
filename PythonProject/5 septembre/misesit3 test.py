# Un piéton veut traverser la rue. Il doit respecter certaines conditions :
#
# Le feu doit être vert.
#
# Lorsque le feu est rouge, il peut traverser seulement si la barrière de sécurité est ouverte.
#
# Mais si le feu est orange, il ne peut jamais traverser.


def menu_lumiere():
    print("Quelle couleur est le feu?")
    print("1 - Vert")
    print("2 - Orange")
    print("3 - Rouge")

def vert():
    print("Tu peux passer")

def orange():
    print("Tu ne peux pas passer à la lumière orange")

def rouge():
    print("Est-ce que la barrière de sécurité est ouverte?")
    print("1 - Oui, elle est ouverte")
    print("2 - Non, elle est fermée")


while True:
    menu_lumiere()
    couleur = input()

    if couleur == "1":
        vert()
        break
    elif couleur == "2":
        orange()
    elif couleur == "3":
        rouge()
        barriere = input()
        if barriere == "1":
            print("Tu peux passer")
            break
        elif barriere =="2":
            print("Tu ne peux pas passer avec la barrière de sécurité fermée")
