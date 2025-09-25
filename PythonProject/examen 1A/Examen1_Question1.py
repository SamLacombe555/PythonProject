def convertir(heures, unite):
    """
    Convertit une quantité d'heures en différentes unités de temps.
    :param heures: Le nombre d'heures à convertir.
    :param unite: L'unité vers laquelle convertir les heures. Peut être 'minutes', 'secondes', 'jours', ou 'semaines'.
    :return: (aucun)
    """

    if unite == "minutes":
        conversion = heures / 60
        print(f"{heures} heures == {conversion} minutes")
    elif unite == "secondes":
    conversion = heures * 3600
        print(f"{heures} heures == {conversion} secondes")
    elif unite == "jours":
        conversion = heures * 24
        print(f"{heures} heures == {conversion} jours")
    elif unite == "semaines":
        conversion = heures / (24 * 7)
        print(f"{heures} heures == {conversion} semaines")
    else:
        print("Unité non reconnue. Veuillez entrer 'minutes', 'secondes', 'jours' ou 'semaines'.")

if __name__ == '__main__':
    nb_heures = input("Veuillez entrer un nombre d'heures : ")
    unite = input("Entrez une unité parmi les suivantes (minutes, secondes, jours, semaines) : ")
    convertir(nb_heures, unite)

"""


Plan de tests :
Effectuez tous vos tests de façon à valider le bon fonctionnement du convertisseur.
Assurez-vous de bien valider chacune des possibilités du convertisseur.

#######################################################################
#   valeur 1 ## valeur 2 ##   Résultat attendu  ##  Résultat obtenu  ##
#######################################################################
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#            ##          ##                     ##                   ##
#######################################################################
"""