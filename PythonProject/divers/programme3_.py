
somme = 0

while True:
    nombre = float(input("Entrez un nombre (0 pour arrêter) : "))

    if nombre == 0:
        break

    somme += nombre

print(f"La somme des nombres entrés est {somme}.")

input("Appuyez sur Entrée pour quitter...")
