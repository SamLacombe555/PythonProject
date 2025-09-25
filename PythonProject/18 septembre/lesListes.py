ls_nombre = [5, 1, 6, 3, 4, 5]
ls_mots = ["pomme", "poire", "fraise"]
ls_prix = [2.22, 3.22, 4.55, 2.99, 8,88, 9.30]

print(ls_nombre)
print(ls_mots)
print(ls_prix)

#nb = int(input("Entrez un nombre : "))
#mot = int(input("Entrez un mot : "))
#prix = int(input("Entrez un prix : "))

ls_nombre.append(10) # Ajouter un item à la fin de la liste
ls_mots.append("Prune")
ls_prix.append(2.20)

ls_nombre.pop(2) # supprimer l'item à l'indice 2 (3e)
ls_mots.remove("poire") # supprimer un item
ls_prix.insert(2, 4.50) # ajouter un item à l'indice choisi

ls_nombre.sort()
ls_mots.sort()
ls_prix.sort(reverse=True)

print(ls_nombre)
print(ls_mots)
print(ls_prix)

print(ls_prix[3]) # accéder à un item avec son indice
print(ls_mots.index("pomme"))

print("Somme des nombres: ", sum(ls_nombre)) #sum : additionner tous les items
moyenne = sum(ls_prix)/len(ls_prix) # len: nombre d'items
print(f"Moyenne des prix {moyenne:.2f}")
print("Prix min", min(ls_prix))
print("Prix max", max(ls_prix))



