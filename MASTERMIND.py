import time, random

def afficher_jeu(board_j1):
    for ligne in board_j1:
        print(ligne)
board_j1 = [

    ["_", "_", "_", "_"], # + liste[0][1]append.str("1 pion et 1 pio")
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"],
    ["_", "_", "_", "_"]

]

board_j2 = [

    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""],
    [""]

]

liste_solution = ["_", "_", "_", "_"]

def assign_couleurs(board, round):
    for i in range(4):
        choix = input(f"Décidez quelle sera la {i+1}e couleur :")
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

        board[round-1][i] = choix_c
    return board

def j2_verifie(board_j1:list, liste_solution:list):
    count_rouge = 0
    count_blanc = 0
    for i in range(4):
        if board_j1[round-1][i] in liste_solution:
            if i == liste_solution.index(board_j1[round-1][i]):
                count_rouge += 1
            else:
                count_blanc += 1
    nouveau_board = board_j1[round-1].append(f"{count_rouge} rouges, {count_blanc} blancs")
    return nouveau_board

def intro_menu_choix_joueurs():
    """
    Cette fonction fait apparaître le menu du jeu.
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

def comment_jouer():
    """
    Cette fonction fait apparaître le tutoriel du jeu.
    :return:
    """
    print("Le but de ce jeu est de deviner correctement une combinaison de 4 couleurs.\nUn joueur (le codificateur) decide quelle sera la combinaison gagnante, et un deuxième joueur (le décodeur) tente de la trouver par essai-erreur.\nS'il devine correctement une couleur, un pion blanc est placé.\nS'il devine une couleur et qu'en plus elle est placée a la bonne position, un pion rouge est placé. Il a 12 essais en tout.")
    input(print("Veuillez taper Entrée pour retourner au menu."))

def joueur_versus_joueur():
    """
    Cette fonction introduit la section joueur versus joueur.
    :return:
    """
    print(nom_decodeur + ", veuillez vous retourner et ne pas regarder l'écran.")
    time.sleep(5)
    print(nom_codificateur,", en vous servant du menu suivant, veuillez choisir une solution composée du combinaison de 4 couleurs.")

def choisir_solution(liste_solution):
    """
    Cette fonction permet de choisir la combinaison de 4 couleurs avec l'aide de la liste en menu_couleurs().
    :param liste_solution:
    :return:
    """
    for i in range(4):
        choix = input(f"Décidez quelle sera la {i+1}e couleur :")
        if choix == '1':
            choix_c = "J"
        elif choix == '2':
            choix_c = "B"
        elif choix == '3':
            choix_c = "R"
        elif choix == '4':
            choix_c = "V"
        elif choix == '5':
            choix_c = "O"
        elif choix == '6':
            choix_c = "N"
        elif choix == '7':
            choix_c = "M"
        elif choix == '8':
            choix_c = "T"
        elif choix == '9':
            choix_c = "G"
        else:
            break

        liste_solution[i] = choix_c
    return liste_solution

def menu_couleurs():
    """
    Cette fonction fait apparaître le choix de combinaison de couleurs.
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

def ordinateur_solution():
    """
    Cette fonction génère une solution au hazard.
    :return:
    """
    liste_solution = []
    for i in range(4):
        i = random.choice(liste_couleurs)
        liste_solution.append(i)
    return liste_solution

def verification_liste(liste_solution):
    """
    Cette fonction vérifie si l'utilisateur a inséré des entrées valides pour la liste.
    :param liste_solution:
    :return:
    """
    if '_' in liste_solution:
        print("Votre liste est invalide. Veuillez redémarrer le programme et réessayer.")
        return False


if __name__ == "__main__":

    round = 1
    liste_solution = ["_", "_", "_", "_"]
    liste_couleurs = ['J', 'B', 'R', 'V', 'O', 'N', 'M', 'T', 'G']

    while True:
        intro_menu_choix_joueurs()
        choix = input()
        if choix == "1":
            liste_solution = ordinateur_solution()
            break
        elif choix == "2":
            nom_codificateur = str(input("Qui sera le joueur codificateur? Veuillez taper son nom, et ensuite Entrée."))
            nom_decodeur = str(input("Qui sera le joueur décodeur? Veuillez taper son nom, et ensuite Entrée."))
            joueur_versus_joueur()
            menu_couleurs()
            choisir_solution(liste_solution)
            print(liste_solution)
            if verification_liste(liste_solution) == False:
                break
            print("Cette liste est-elle correcte? Répondez avec O ou N.")
            input_verification = input()
            if input_verification == 'N':
                print(r"Tant pis ¯\_(ツ)_/¯")
                time.sleep(3)
            elif input_verification == 'O':
                break
            else:
                print("Mauvaise entrée.")
        elif choix == "3":
            comment_jouer()

    afficher_jeu(board_j1)
    assign_couleurs(board, round)
