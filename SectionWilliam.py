import time

def intro_menu_choix_joueurs():
    """

    :return:
    """

    print(r"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━				    
     ███    ███  █████  ███████ ████████ ███████ ██████  ███    ███ ██ ███    ██ ██████  
     ████  ████ ██   ██ ██         ██    ██      ██   ██ ████  ████ ██ ████   ██ ██   ██ 
     ██ ████ ██ ███████ ███████    ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ██   ██ 
     ██  ██  ██ ██   ██      ██    ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ 
     ██      ██ ██   ██ ███████    ██    ███████ ██   ██ ██      ██ ██ ██   ████ ██████
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
      """)
    time.sleep(1)
    print("------------")
    print("1 - JOUEUR versus CPU")
    print("2 - JOUEUR versus JOUEUR")
    print("3 - Comment jouer")
    print("------------")
    print("Veuillez taper un chiffre entre 1 et 3, et ensuite Entrée.")

def joueur_versus_joueur():
    """

    :return:
    """
    print(nom_decodeur + ", veuillez vous retourner et ne pas regarder l'écran.")
    time.sleep(1)
    #input(nom_codificateur, ", en vous servant du menu qui apparaitra, veuillez choisir une solution composée du combinaison de 6 couleurs.")

def menu_couleurs():
    """

    :return:
    """
    print ("1 - Jaune")
    print ("2 - Bleu")
    print ("3 - Rouge")
    print ("4 - Vert")
    print ("5 - Orange")
    print ("6 - Noir")
    print ("7 - Mauve")
    print ("8 - Turquoise")
    print ("9 - Gris")

def codificateur_solution():
    """

    :return:
    """



def ordinateur_solution():
    """

    :return:
    """

if __name__ == "__main__":

    intro_menu_choix_joueurs()

    choix = input()

    if choix == "1":
        afficher_solde(solde)
    elif choix == "2":
        nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
        nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
        joueur_versus_joueur()


    liste_solution = 1
    liste_solution_longeur = 4
    while liste_solution <= liste_solution_longeur:
        couleur = input(nom_codificateur + ", décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une. Entrez la %se couleur." % liste_solution)
        liste_solution = liste_solution + 1
        #liste_solution.append(couleur)
        #print(liste_solution)
