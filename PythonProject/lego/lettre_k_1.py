# Constantes pour déclarer le code de la couleur verte
VERT = "\033[32m"

print("Construction de la lettre K :")

# Itérer (boucler) sur 5 lignes pour écrire à chaque ligne et aux bonnes
# positions les étoiles qui permettent d'écrire la lettre K
for ligne in range(3):  # 5 lignes
    if ligne == 1:
        print(VERT + "█   █")
    elif ligne == 2:
        print(VERT + "█  █ ")
    elif ligne == 3:
        print(VERT + "██   ")
    elif ligne == 4:
        print(VERT + "██")
    elif ligne == 5:
        print(VERT +"██")
    elif ligne > 5:
        print("Oups, ligne de trop!")