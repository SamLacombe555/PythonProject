"""
A DOCUMENTER (SAM)

afficher_jeu()
assign_couleurs()

ligne
board_j1 (liste)
board_j2 (liste)
j2_verifie
board
nouveau_board
round
count_rouge
rouges
count_blanc
blancs

+ PSEUDOCODE

"""

# - PSEUDOCODE -

# FONCTIONS:

# intro_menu_choix_joueurs(): Fait apparaître le menu du jeu.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer le titre et les choixs du menu
# Fin

# comment_jouer(): Fait apparaître le tutoriel du jeu.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer le tutoriel
# Fin

# joueur_versus_joueur(): Introduit la section joueur versus joueur.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer l'instruction
# Fin

# ordinateur_solution(): Génère une solution au hazard.
# Entrées: liste_solution (vide)
# Sorties: liste_solution
# Début:
#   Boucle qui génère une liste à 4 couleurs.
#   Retourner la fonction
# Fin

# menu_couleurs(): Fait apparaître le choix de combinaison de couleurs.
# Entrées: Aucunes
# Sorties: Aucunes
# Début:
#   Imprimer les choixs (J, B, R, V, O, N, M, T, G)
# Fin

# verification_liste(): Vérifie si l'utilisateur a inséré des entrées valides pour la liste.
# Entrées: liste_solution
# Sorties: True ou False
# Début:
#   S'il y a autre chose que les lettres acceptées, retourner un message d'erreur et False.
# Fin



# Entrées:
# nom_codificateur (str): Nom du joueur codificateur
# nom_decodeur (str): Nom du joueur décodeur
# choix/choix_c: L'entrée pour les différents menus de sélection. S'identifie par un chiffre

# Sorties:
# liste_solution (liste simple de 4 couleurs entrée par joueur Codificateur ou générée par hazard par la fonction ordinateur_solution()

# Modules:
# Time: Purement pour petit effet esthétique
# Random: Pour générer une liste au hazard dans la fonction ordinateur_solution()

"""
Programme principal:
Définir liste_couleurs

    boucle
        intro_menu_choix_joueurs()
        choix égal input()
        si choix est égal à 1:
            liste_solution égal ordinateur_solution()
            casser la boucle
        si choix est égal à 2:
            nom_codificateur égal str(input())
            nom_decodeur égal str(input())
            joueur_versus_joueur()
            menu_couleurs()
            choisir_solution(liste_solution)
            imprimer(liste_solution)
            si verification_liste(liste_solution) égal Faux:
                casser la boucle
            imprimer("O ou N")
            si input_verification égal N:
                imprimer("Tant pis")
            sinon input_verification égal O:
                break
            sinon:
                print("Mauvaise entrée.")
        si choix est égal à 3:
            comment_jouer()

"""

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
    print("-" * 10)
    print("1 - JOUEUR versus CPU")
    print("2 - JOUEUR versus JOUEUR")
    print("3 - Comment jouer")
    print("-" * 10)
    print("Veuillez taper un chiffre entre 1 et 3, et ensuite Entrée.")

def comment_jouer():
    """
    Cette fonction fait apparaître le tutoriel du jeu.
    :return:
    """
    print("-" * 10)
    print("Le but de ce jeu est de deviner correctement une combinaison de 4 couleurs.\nUn joueur (le codificateur) decide quelle sera la combinaison gagnante, et un deuxième joueur (le décodeur) tente de la trouver par essai-erreur.\nSi une couleur est correctement devinée une couleur, un pion blanc est placé.\nSi une couleur est devinée et qu'en plus elle est placée à la bonne position, un pion rouge est placé.\n12 essais en tout sont permis.")
    print("-" * 10)
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
                print(r"Tant pis ¯\_(ツ)_/¯. Veuillez recommencer depuis le début.")
                time.sleep(3)
            elif input_verification == 'O':
                break
            else:
                print("Mauvaise entrée.")
        elif choix == "3":
            comment_jouer()

    afficher_jeu(board_j1)
    assign_couleurs(board, round)
