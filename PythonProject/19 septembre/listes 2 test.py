ls_nombre = [5, 6, 1, 3, 5]
ls_mots = ["pomme", "poire", "fraise"]
ls_prix = [5.42, 9.55, 4.66, 4.55, 1.20, 2.00]
liste_legos = ["bleu", "jaune", "rouge", "vert", "bleu", "jaune"]

for lego in liste_legos: # pour chaque item dans la liste
    print(lego)

for i in range(len(ls_prix)): # i: indices de ma liste
    print(ls_prix[i])

for i in range(len(ls_prix)):
    print(f"Le lego {liste_legos[i]} coûte {ls_prix[i]:.2f}$")

couleur = input("Quelle couleur tu veux?")
if couleur in liste_legos: # vérifier si un item existe dans une liste
    print("Il y a un lego", couleur)
else:
    print("Il n'y a pas de lego", couleur)

liste_legos.extend(["rose", "vert"]) # ajouter une liste à la fin d'une liste
print(liste_legos)

liste_nombre_2 = ls_nombre + ls_prix # fusionner 2 liste dans une 3e
print(liste_nombre_2)

phrase = input("Entre une phrase:") # séparer les mots d'une phrase dans une liste
ls_mots_2 = phrase.split(" ")
print(ls_mots_2)

print(", ".join(liste_legos)) # transforme la liste en str avec ", " entre les items

