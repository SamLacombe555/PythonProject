cle = bool(int(input("Est-ce que Nova possède la clé?")))
carte = bool(int(input("Est-ce que Nova possède la carte magnétique?")))
cape = bool(int(input("Est-ce que Nova possède la cape d'invisibilit?")))
alarme = bool(int(input("Est-ce que l'alarme est désactivée?")))

def attempt_passage(porte,nom):
    if porte == True:
        print(f"Nova peut traverser la porte de {nom}")
    else:
        print(f"Nova ne peut pas traverser la porte de {nom}")


print()

bronze = bool(cle and carte)
attempt_passage(bronze,"bronze")

vent = bool(cle or cape)
attempt_passage(vent,"vent")

feu = bool(alarme)
attempt_passage(feu,"feu")

jugement = bool((cle or carte) and alarme)
attempt_passage(jugement,"jugement")


if bronze and vent and feu and jugement == True:
    print(" \nNova peut atteindre le crystal")
else:
    print(" \nNova ne peut pas atteindre le crystal")
