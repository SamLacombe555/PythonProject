def acces_vitesse():
    return vitesse > 120

def acces_temps():
    return temps > 5

def acces_piece():
    return piece >= 50

def acces_niveau():
    return niveau >= 2


accepter_car = "Tu peux passer à la prochaine étape car"
refus = "Tu ne peux pas passer à la prochaine étape car "
accepter = "Tu peux passer à la prochaine étape"


r_vitesse ="ta vitesse ne dépasse pas 120 km/h"
r_temps ="le temps restant ne dépasse pas 5 minutes"
r_piece ="tu possèdes en dessous de 50 pièce bonus"
a_niveau ="ton niveau bonus franchis le minimun de 2"

while True:
    print("")
    vitesse = int(input("Quelle est la vitesse de la voiture en km/h?"))
    temps = int(input("C'est quoi le temps restant en minutes?"))
    piece = int(input("Combien de pièce bonus possèdes-tu?"))
    niveau = int(input("Quelle est ton niveau bonus?"))

    print("")

    if acces_niveau() == True:
        print(accepter_car,a_niveau)
        if acces_vitesse()or acces_temps() or acces_piece() == False:
            print("Même si :")
            if acces_vitesse() == False:
                print(r_vitesse)
            if acces_temps() == False:
                print(r_temps)
            if acces_piece() == False:
                print(r_piece)
        break
    else:
        if acces_vitesse() == False or acces_temps() == False or acces_piece() == False:
            print(refus)
            if acces_vitesse() == False:
                print(r_vitesse)
            if acces_temps() == False:
                print(r_temps)
            if acces_piece() == False:
                print(r_piece)
        else:
            print(accepter)
            break


