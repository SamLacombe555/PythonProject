#Gestion d'erreurs
#nombre = -1
while True:
    try:
        nombre = int(input("Entrez un nombre:"))
        if nombre > 0 and nombre <= 100: # valider la plage de données
            break # terminer la boucle si le nombre est entier et positif
        else:
            print("Le nombre doit être entre 0 et 100")
    except: # gestion d'exception, s'assurer que c'est bien un nombre
        print("Ça doit être un nombre entier")

print(nombre)

