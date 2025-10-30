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

def choisir_solution(liste_solution2):
    for i in range(4):
        choix = int(input(f"Sélectionne la couleur n-{i}"))
        if choix == 1:
            choix_c = "J"
        elif choix == 2:
            choix_c = "B"
        elif choix == 3:
            choix_c = "R"
        elif choix == 4:
            choix_c = "V"
        elif choix == 5:
            choix_c = "O"
        elif choix == 6:
            choix_c = "N"
        elif choix == 7:
            choix_c = "M"
        elif choix == 8:
            choix_c = "T"
        elif choix == 9:
            choix_c = "G"

        liste_solution[i] = choix_c
    return liste_solution

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

    round = 1

    liste_solution = ["_", "_", "_", "_"]

    intro_menu_choix_joueurs()
    choix = input()
    if choix == "1":
        print("")
    elif choix == "2":
        nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
        nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
        joueur_versus_joueur()
        menu_couleurs()
        choisir_solution(liste_solution)
        print(liste_solution)
        input("Cette liste est-elle correcte?2")

    liste_solution = 1
    liste_solution_longeur = 4
    while liste_solution <= liste_solution_longeur:
        #couleur = input(nom_codificateur + ", décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une. Entrez la %se couleur." % liste_solution)
        couleur = input(nom_codificateur + f", décidez quelle sera la combinaison de 4 couleurs gagnante. Entrez les couleurs une par une. Entrez la {liste_solution}e couleur.")
        liste_solution = liste_solution + 1
        #liste_solution.append(couleur)
        #print(liste_solution)

