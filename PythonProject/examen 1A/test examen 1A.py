

def convertir(heures,unite):


        if unite == "minutes":
            convertir = heures * 60
            print(f"Dans {heures} heures, il y a {convertir} {unite}")

        elif unite == "secondes":
            convertir = heures * 3600
            print(f"Dans {heures} heures, il y a {convertir} {unite}")

        elif unite == "jours":
            convertir = heures / 24
            print(f"Dans {heures} heures, il y a {convertir} {unite}")

        elif unite == "semaines":
            convertir = heures /(24*7)
            print(f"Dans {heures} heures, il y a {convertir} {unite}")
        else:
            print("Unité non reconnue. Veuillez entrer 'minutes', 'secondes', 'jours' ou 'semaines'.")


nb_heures = float(input("Veuillez entrer un nombre d'heures : "))
unite = str(input("Entrez une unité parmi les suivantes (minutes, secondes, jours, semaines) : "))
convertir(nb_heures, unite)


